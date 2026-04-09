import time
from PySide6.QtCore import QThread, Signal

# 1. 导入标准化的日志与错误体系
from src.utils.logger import logger
from src.models.error_codes import ErrorCode
from src.utils.exceptions import AppException, ADBError, VisionError, LLMError

# 2. 导入更新后的核心模块 (DeviceManager 和 VisionProcessor)
from src.utils.logger import LogLevel, logger
from src.core.vision_processor import VisionProcessor
from src.core.llm_client import LLMClientFactory
from src.models.config_schema import LLMConfig, ROIConfig

class AutoRunThread(QThread):
    log_signal = Signal(object, str)
    finished_signal = Signal()

    def __init__(self,device_manager, active_config, parent=None):
        super().__init__(parent)
        self.dm = device_manager
        self.active_config = active_config
        self.is_running = True

    # src/core/run_thread.py

    def _ui_log(self, level: LogLevel, msg: str, error: Exception = None):
        """
        标准化日志接口：支持等级、消息、以及可选的报错对象
        """
        self.log_signal.emit(level, msg)
        
        from src.utils.logger import app_logger_instance
        app_logger_instance.log(level, msg, error)

    def run(self):
        self._ui_log(LogLevel.INFO,"自动运行线程已启动...")
        
        if not self.active_config:
            self._ui_log(LogLevel.ERRO,"错误：未选中任何有效配置！", "error")
            self.finished_signal.emit()
            return

        # =========================================================
        # 1. 解析配置
        # =========================================================
        device_name = self.active_config.get("name", "Unknown Device")
        ai_model_name = self.active_config.get("ai_model", "qwen2.5:7b")
        
        # 将原始字典转为强类型的 ROIConfig 对象，供 VisionProcessor 使用
        roi_data = self.active_config.get("roi", {})
        roi_obj = ROIConfig(**roi_data) 
        
        tap_config = self.active_config.get("tap", {})

        self._ui_log(LogLevel.INFO,f"当前配置: {device_name} | AI 模型: {ai_model_name}")

        # =========================================================
        # 2. 初始化核心模块 (使用新模块名)
        # =========================================================
        self._ui_log(LogLevel.INFO,"正在初始化核心模块 (ADB/OCR/LLM)...")
        try:
            # 2.1 初始化 DeviceManager (原 ADBManager)
            if not self.dm or not self.dm.device:
                raise ADBError(ErrorCode.DEVICE_NOT_FOUND, "主程序未检测到有效设备连接")
            # 2.2 初始化 VisionProcessor (原 VisionSystem)
            # 它会自动通过 get_bin_resource 加载模型
            vision = VisionProcessor(use_gpu=True) 

            # 2.3 初始化 LLM 客户端
            llm_cfg = LLMConfig(
                mode="local", 
                model_name=ai_model_name,
                api_url="http://localhost:11434/api/generate",
                temperature=0.3,
                max_tokens=50
            )
            llm = LLMClientFactory.create(llm_cfg)

            self._ui_log(LogLevel.INFO,"初始化完成，开始自动答题！\n")

        except AppException as e:
            self._ui_log(LogLevel.ERRO, "启动失败", error=e)
            self.finished_signal.emit()
            return
        except Exception as e:
            # 修改这一行，把详细的错误信息打出来
            import traceback
            err_details = traceback.format_exc() 
            self._ui_log(LogLevel.ERRO, f"未知启动错误: {str(e)}", error=e)
            print(err_details) # 在控制台看详细堆栈
            logger.exception("AutoRunThread 初始化发生严重崩溃")
            self.finished_signal.emit()
            return
        
        # =========================================================
        # 3. 核心死循环
        # =========================================================
        step = 1
        while self.is_running:
            self._ui_log(LogLevel.INFO,f"------ 正在处理第 {step} 题 ------")
            
            try:
                # [A] 截取画面 (使用 DeviceManager)
                self._ui_log(LogLevel.INFO,"正在采集手机画面...")
                img = self.dm.take_screenshot()
                if not self.is_running: break
                
                # [B] OCR 识别 (使用 VisionProcessor)
                self._ui_log(LogLevel.INFO,"正在进行 OCR 文本提取...")
                q_data = vision.analyze(img, roi_obj)
                
                # 格式化输出 OCR 日志
                ocr_log = f"  [题干]: {q_data.get('topic', '未识别到内容')}\n"
                for opt in ['A', 'B', 'C', 'D']:
                    if opt in q_data:
                        ocr_log += f"  [{opt}]: {q_data[opt]}\n"
                self._ui_log(LogLevel.INFO,ocr_log.strip())
                
                if not self.is_running: break
                
                # [C] 调用大模型进行推理
                self._ui_log(LogLevel.INFO,f"正在请求 AI 模型 ({ai_model_name}) ...")
                answer = llm.ask(q_data) 
                
                # [D] 执行点击 (使用 DeviceManager 的 click 方法，带随机偏移)
                if answer in ['A', 'B', 'C', 'D']:
                    self._ui_log(LogLevel.INFO,f"AI 答案: 【{answer}】")
                    
                    if answer in tap_config:
                        tx, ty = tap_config[answer]
                        self._ui_log(LogLevel.INFO,f" 正在点击选项 {answer} (中心坐标: {tx}, {ty})")
                        self.dm.click(tx, ty) # 使用封装好的 click 方法，更安全且带偏移
                    else:
                        self._ui_log(LogLevel.ERRO,f"无法点击：配置中缺少选项 {answer} 的坐标数据！")
                else:
                    self._ui_log(LogLevel.ERRO,f"AI 回复无法解析: {answer}")
                    
            except ADBError as e:
                self._ui_log(LogLevel.ERRO,f"ADB 连接异常 [{e.code.name}]: {e.detail}")
                break 
            except LLMError as e:
                self._ui_log(LogLevel.ERRO,f"AI 推理异常: {e.detail}")
            except VisionError as e:
                self._ui_log(LogLevel.ERRO,f"视觉识别异常: {e.detail}")
            except Exception as e:
                self._ui_log(LogLevel.ERRO,f"运行中发生未知错误",error= e)
                logger.exception(f"第 {step} 题执行崩溃")

            # 等待下一题动画
            time.sleep(0.5)
            
            step += 1

        # =========================================================
        # 4. 扫尾工作
        # =========================================================
        if not self.is_running:
            self._ui_log(LogLevel.WARN,"任务已被手动中止。")
        self.finished_signal.emit()

    def stop(self):
        self.is_running = False