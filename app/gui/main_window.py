from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QScrollArea, QLabel, QInputDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QThread, Signal, QTimer, Qt , QRect
from PySide6.QtGui import QImage, QPixmap, QPainter, QPen, QColor, QBrush, QIntValidator
from app.gui.canvas_label import ClickableCanvas
from app.core.adb_manager import ADBManager
from app.core.vision import VisionSystem
from app.brain.llm_client import LLMClient
from src.utils.logger import LogLevel

from app.core.path_utils import get_root_path

import subprocess
import requests
import os
import json
import time
from datetime import datetime

root = get_root_path()
ui_path = os.path.join(root, "app", "gui", "main_window.ui")
config_path = os.path.join(root, "configs.json")


class AutoRunThread(QThread):
    log_signal = Signal(str)
    finished_signal = Signal()

    def __init__(self, active_config, parent=None):
        super().__init__(parent)
        self.active_config = active_config
        self.is_running = True

    def run(self):
        self.log_signal.emit("🚀 自动运行线程已启动...")
        if not self.active_config:
            self.log_signal.emit("❌ 错误：未选中任何有效配置！")
            self.finished_signal.emit()
            return

        self.log_signal.emit(f"📋 当前使用配置: {self.active_config.get('name')}")
        
        # =========================================================
        # 1. 初始化核心模块
        # (因为 VisionSystem 加载模型较慢，放在子线程里不会卡死主界面 UI)
        # =========================================================
        self.log_signal.emit("⏳ 正在初始化 ADB、视觉与大模型模块 (请稍候)...")
        try:
            adb = ADBManager()
            if not adb.device:
                self.log_signal.emit("❌ 错误：未检测到 ADB 设备，请检查连接！")
                self.finished_signal.emit()
                return
                
            vision = VisionSystem(use_gpu=True) # 初始化 OCR
            llm = LLMClient()                   # 初始化 LLM 客户端
            self.log_signal.emit("✅ 初始化完成，开始自动答题！\n")
        except Exception as e:
            self.log_signal.emit(f"❌ 初始化严重错误: {str(e)}")
            self.finished_signal.emit()
            return
        
        # 提取当前配置里的 ROI 区域和 Tap 点击坐标
        roi_config = self.active_config.get("roi", {})
        tap_config = self.active_config.get("tap", {})
        
        step = 1
        # =========================================================
        # 2. 核心死循环，直到点击“停止运行”
        # =========================================================
        while self.is_running:
            self.log_signal.emit(f"--- 🔄 正在处理第 {step} 题 ---")
            
            try:
                # [A] 截取手机实时画面
                self.log_signal.emit("正在采集手机画面...")
                img = adb.take_screenshot()
                if not self.is_running: break
                
                # [B] 执行 OCR 识别
                self.log_signal.emit("正在进行 OCR 文本提取...")
                q_data = vision.process_rois(img, roi_config)
                
                # 格式化输出 OCR 日志
                ocr_log = f"  [题干]: {q_data.get('topic', '未识别到内容')}\n"
                for opt in ['A', 'B', 'C', 'D']:
                    if opt in q_data:
                        ocr_log += f"  [{opt}]: {q_data[opt]}\n"
                self.log_signal.emit(ocr_log.strip())
                
                if not self.is_running: break
                
                # [C] 调用大模型进行推理
                answer = llm.get_answer(q_data)
                
                # [D] 判断并执行点击
                if answer in ['A', 'B', 'C', 'D']:
                    self.log_signal.emit(f"AI 答案: 【{answer}】")
                    
                    if answer in tap_config:
                        # 拿到标定时保存的点击坐标
                        tx, ty = tap_config[answer]
                        self.log_signal.emit(f"正在点击选项 {answer} (坐标: {tx}, {ty})")
                        
                        # 调用 ADB shell 命令执行物理点击
                        adb.device.shell(f"input tap {tx} {ty}")
                        self.log_signal.emit(f"第 {step} 题处理完毕。")
                    else:
                        self.log_signal.emit(f"⚠️ 无法点击：配置中缺少选项 {answer} 的坐标数据！")
                else:
                    self.log_signal.emit(f"❓ AI 回复内容异常或无法判断: {answer}")
                    self.log_signal.emit(f"⚠️ 第 {step} 题跳过操作。")
                    
            except Exception as e:
                self.log_signal.emit(f"❌ 本题处理异常: {str(e)}")

            # =========================================================
            # 等待下一题动画加载 (这里用细颗粒度睡眠，防止点击停止后还需要等很久)
            # =========================================================
            wait_seconds = 0.5
            self.log_signal.emit(f"⏳ 等待 {wait_seconds} 秒后进入下一题...\n")
            
            for _ in range(int(wait_seconds * 10)): 
                if not self.is_running: 
                    break
                time.sleep(0.1) # 每次只睡 0.1 秒，快速响应终止指令
            
            step += 1

        # 退出循环的扫尾工作
        if not self.is_running:
            self.log_signal.emit("🛑 任务已被手动中止。")
        else:
            self.log_signal.emit("🎉 运行结束！")
            
        self.finished_signal.emit()

    def stop(self):
        """外部调用，安全停止线程"""
        self.is_running = False

class CheckEnvThread(QThread):
    # 信号参数：target, text, success, extra
    result_ready = Signal(str, str, bool, str)

    def run(self):
        # 1. 初始化默认值
        model_val = "未知型号"
        model_val_real = "未设置名称"
        screen_val = "未知分辨率"
        
        try:
            # 2. 检查 ADB 基础连接
            res = subprocess.run("adb devices", shell=True, capture_output=True, text=True)
            if "device" in res.stdout and len(res.stdout.strip().split('\n')) > 1:
                self.result_ready.emit("adb", "🟢 已连接", True, "")
                
                # --- 获取设备详细信息 ---
                try:
                    # 获取“艺名” (用户定义的设备名)
                    name_raw = subprocess.check_output("adb shell settings get global device_name", shell=True, text=True).strip()
                    if name_raw != "null" and name_raw:
                        model_val_real = name_raw
                    
                    # 获取“真名” (硬件代号)
                    model_val = subprocess.check_output("adb shell getprop ro.product.model", shell=True, text=True).strip()
                except: 
                    pass 

                # --- 合成 HTML 字符串：两行显示 ---
                combined_info = (
                    f"<b style='color: #2196F3;'>{model_val_real}</b><br>"
                    f"<span style='color: #757575; font-size: 10px;'>型号代号: {model_val}</span>"
                )
                self.result_ready.emit("model", combined_info, True, "")

                try:
                    # 获取分辨率
                    size_str = subprocess.check_output("adb shell wm size", shell=True, text=True).strip()
                    screen_val = size_str.split(":")[-1].strip()
                except: 
                    pass
                self.result_ready.emit("screen", f"{screen_val}", True, screen_val)
                
            else:
                self.result_ready.emit("adb", "🔴 未发现设备", False, "")
                # 未连接时清空信息显示
                self.result_ready.emit("model", "等待设备连接...", False, "")
                self.result_ready.emit("screen", "未知", False, "")
        except Exception as e:
            self.result_ready.emit("adb", f"❌ 错误: {str(e)}", False, "")

        # 3. 检查 Ollama 状态及模型列表
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=3)
            if response.status_code == 200:
                data = response.json()
                models = data.get("models", [])
                model_names = [m["name"] for m in models]
                model_list_str = " | ".join(model_names) if model_names else "无可用模型"
                
                self.result_ready.emit("ollama", "🟢 运行中", True, "")
                self.result_ready.emit("ollama_list", model_list_str, True, model_list_str)
            else:
                self.result_ready.emit("ollama", "🟡 服务异常", False, "")
        except Exception:
            self.result_ready.emit("ollama", "🔴 未启动", False, "")
            self.result_ready.emit("ollama_list", "请先启动 Ollama", False, "")

class CalibrationDialog(QDialog):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("坐标标定 - 适配模式 (点击画面获取坐标)")

        self.canvas = ClickableCanvas()
        
        # 1. 计算适配屏幕的分辨率
        # 获取电脑屏幕可用区域（扣除任务栏）
        screen_geo = QApplication.primaryScreen().availableGeometry()
        max_h = screen_geo.height() * 0.8  # 最大允许占屏幕高度的 80%
        
        # 获取手机图片原始尺寸
        orig_w = pixmap.width()
        orig_h = pixmap.height()
        
        # 计算缩放比：如果图片高度超过 max_h，则等比例缩小
        self.display_scale = 1.0
        if orig_h > max_h:
            self.display_scale = max_h / orig_h
        
        target_w = int(orig_w * self.display_scale)
        target_h = int(orig_h * self.display_scale)

        # 2. 预缩放图片以解决卡顿
        # 使用 SmoothTransformation 保证清晰度，预缩放后 QLabel 渲染压力极大减小
        self.display_pixmap = pixmap.scaled(
            target_w, target_h, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )

        # 3. 构建 UI
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) # 去除边距，让画面更紧凑
        
        self.scroll = QScrollArea()
        self.canvas = ClickableCanvas() # 你的自定义类
        self.canvas.setPixmap(self.display_pixmap)
        self.canvas.setCursor(Qt.CrossCursor)
        
        # 强制 Canvas 尺寸与缩放后的图片一致，防止点击偏移
        self.canvas.setFixedSize(target_w, target_h)
        
        self.scroll.setWidget(self.canvas)
        self.scroll.setAlignment(Qt.AlignCenter) # 居中显示
        layout.addWidget(self.scroll)
        
        # 调整窗口自身大小以适配图片
        self.resize(target_w + 20, target_h + 20)

    def get_real_coords(self, x, y):
        """将点击的 UI 坐标还原为手机原始坐标"""
        real_x = int(x / self.display_scale)
        real_y = int(y / self.display_scale)
        return real_x, real_y

class ClickableCanvas(QLabel):
    clicked_pos = Signal(int, int) 

    def __init__(self, parent=None):
        super().__init__(parent)
        # 存储多个矩形的列表，每个元素为 (QRect, QColor)
        self.rects = [] 
        self._show_overlay = False

    def set_overlay_rect(self, x, y, w, h, color):
        """接收坐标和颜色，添加到列表并触发重绘"""
        self.rects.append((QRect(x, y, w, h), color))
        self._show_overlay = True
        self.update() 

    def hide_overlay(self):
        self.rects = [] 
        self._show_overlay = False
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event) 
        if not self._show_overlay or not self.rects:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        for rect, color in self.rects:
            pen_color = QColor(color)
            pen_color.setAlpha(255) # 边框不透明
            painter.setPen(QPen(pen_color, 2))
            painter.setBrush(QBrush(color)) # 填充半透明
            painter.drawRect(rect)
        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 使用 position().x() 代替 x() 以消除警告
            self.clicked_pos.emit(int(event.position().x()), int(event.position().y()))

    
class LexiLoomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_file = QFile(ui_path)
        # --- 1. 加载 UI ---
        if ui_file.open(QFile.ReadOnly):
            loader = QUiLoader()
            loader.registerCustomWidget(ClickableCanvas)
            self.ui = loader.load(ui_file)
            ui_file.close()
        else:
            # 如果打不开，打印出绝对路径，方便排查到底是哪没对准
            print(f"❌ 无法加载 UI 文件，请检查路径是否存在: {ui_path}")

        self.setCentralWidget(self.ui) 
        
        # --- 2. 基础逻辑绑定 ---
        self.ui.nav_list.currentRowChanged.connect(self.ui.content_stack.setCurrentIndex)
        self.ui.nav_list.setCurrentRow(0)
        self.ui.btn_check_env.clicked.connect(self.start_env_check)

        # --- 3. 标定页逻辑绑定 ---
        self.adb = ADBManager()
        # 绑定点击信号（仅绑定一个合并后的处理函数）
        self.ui.label_canvas.clicked_pos.connect(self.handle_dialog_click)
        self.ui.btn_refresh_canvas.clicked.connect(self.display_snapshot)

        self.config_path = "devices.json"

        # 状态机变量
        self.calibrate_steps = ["topic", "A", "B", "C", "D"]
        self.current_step_idx = -1  # -1 表示未在标定状态
        self.temp_roi = {}          # 存放本次标定的 roi
        self.temp_tap = {}          # 存放本次标定的 tap
        self.p1_cache = None        # 存放矩形第一个点

        self.coord_widgets = {
            "topic": (self.ui.edit_topic_x1, self.ui.edit_topic_y1, self.ui.edit_topic_x2, self.ui.edit_topic_y2),
            "A": (self.ui.edit_a_x1, self.ui.edit_a_y1, self.ui.edit_a_x2, self.ui.edit_a_y2),
            "B": (self.ui.edit_b_x1, self.ui.edit_b_y1, self.ui.edit_b_x2, self.ui.edit_b_y2),
            "C": (self.ui.edit_c_x1, self.ui.edit_c_y1, self.ui.edit_c_x2, self.ui.edit_c_y2),
            "D": (self.ui.edit_d_x1, self.ui.edit_d_y1, self.ui.edit_d_x2, self.ui.edit_d_y2),
        }

        digit_validator = QIntValidator(0, 10000)

        for widgets in self.coord_widgets.values():
            for w in widgets:
                w.setValidator(digit_validator)
                # 绑定回车事件，修改后按回车立即生效
                w.returnPressed.connect(self.sync_manual_coords)

        # === 新增：下拉框切换自动加载配置 ===
        self.ui.combo_configs.currentIndexChanged.connect(
            lambda: self.load_selected_config()
        )

        # 绑定按钮 (请确保你的 UI 文件中有这些 ObjectName)
        self.ui.btn_create_config.clicked.connect(self.start_calibration)
        self.ui.btn_load_config.clicked.connect(self.load_selected_config)
        self.ui.btn_preview_config.clicked.connect(self.preview_selected_config)
        self.ui.btn_delete_config.clicked.connect(self.delete_selected_config)

        self.refresh_config_list()

        # --- 5. 开始运行页逻辑绑定 ---
        self.run_thread = None
        self.ui.btn_start_task.clicked.connect(self.toggle_auto_task)

        # --- 4. 初始化检测线程 ---
        self.check_thread = CheckEnvThread()
        self.check_thread.result_ready.connect(self.update_env_labels)
        self.auto_check_timer = QTimer()
        self.auto_check_timer.timeout.connect(self.start_env_check)
        self.auto_check_timer.start(5000)
        self.start_env_check()

    def start_env_check(self):
        # 防止线程重叠运行
        if not self.check_thread.isRunning():
            self.check_thread.start()

    def update_env_labels(self, target, text, success, extra):
        # 统一处理颜色样式
        color = "#4CAF50" if success else "#F44336"
        style = f"color: {color}; font-weight: bold;"
        
        if target == "adb":
            self.ui.label_adb_status.setText(f"ADB 状态: {text}")
            self.ui.label_adb_status.setStyleSheet(style)
        elif target == "ollama":
            self.ui.label_ollama_status.setText(f"Ollama 状态: {text}")
            self.ui.label_ollama_status.setStyleSheet(style)
        elif target == "model":
            # 自动支持 HTML 换行渲染
            self.ui.label_device_model.setText(text)
        elif target == "screen":
            self.ui.label_device_screen.setText(f"{text}")
        elif target == "ollama_list":
            self.ui.label_Ollama_AIs.setWordWrap(True) 
            self.ui.label_Ollama_AIs.setText(f"{text}")
            self.ui.label_Ollama_AIs.setStyleSheet("color: #2196F3;" if success else "color: gray;")

    def display_snapshot(self):
        """采集画面并弹出/刷新大窗口"""
        try:
            # 1. 检查并清理旧窗口，防止多开
            if hasattr(self, 'dial') and self.dial is not None:
                try:
                    self.dial.close()    # 关闭窗口
                    self.dial.deleteLater() # 彻底释放内存
                except:
                    pass

            print("正在采集画面...")
            pil_img = self.adb.take_screenshot() #
            self.raw_w, self.raw_h = pil_img.size #
            
            # 2. 转换图像格式
            if pil_img.mode != "RGB":
                pil_img = pil_img.convert("RGB")
            data = pil_img.tobytes("raw", "RGB")
            q_img = QImage(data, self.raw_w, self.raw_h, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)

            # 3. 创建并弹出新窗口
            self.dial = CalibrationDialog(pixmap, self)
            self.dial.canvas.clicked_pos.connect(self.handle_dialog_click)
            self.dial.show()
            
        except Exception as e:
            print(f"❌ 弹出失败: {e}")

    def start_calibration(self):
        """开启标定流程"""
        self.current_step_idx = 0
        self.temp_roi = {}
        self.temp_tap = {}
        self.p1_cache = None
        print(f"🚀 开始标定流: 请在大窗口点击 [{self.calibrate_steps[0]}] 的左上角")
        self.display_snapshot() # 弹出/刷新大窗口

    def handle_dialog_click(self, lx, ly):
        if self.current_step_idx == -1:
            return

        rx, ry = self.dial.get_real_coords(lx, ly)
        step_key = self.calibrate_steps[self.current_step_idx]

        colors = {
            "topic": QColor(255, 87, 34, 80),
            "A": QColor(76, 175, 80, 80),
            "B": QColor(33, 150, 243, 80),
            "C": QColor(255, 193, 7, 80),
            "D": QColor(156, 39, 176, 80)
        }
        current_color = colors.get(step_key, QColor(255, 255, 255, 80))

        # ========= 第一点 =========
        if self.p1_cache is None:
            self.p1_cache = (rx, ry, lx, ly)

            # 小点提示
            self.dial.canvas.set_overlay_rect(lx-2, ly-2, 4, 4, current_color)

            print(f"📍 [{step_key}] 起点已记录，请点击右下角")
            return

        # ========= 第二点 =========
        p1_rx, p1_ry, p1_lx, p1_ly = self.p1_cache

        x1, y1 = min(p1_rx, rx), min(p1_ry, ry)
        x2, y2 = max(p1_rx, rx), max(p1_ry, ry)

        self.temp_roi[step_key] = [x1, y1, x2, y2]

        # ✅ 同步 UI 输入框
        if step_key in self.coord_widgets:
            w_x1, w_y1, w_x2, w_y2 = self.coord_widgets[step_key]
            w_x1.setText(str(x1))
            w_y1.setText(str(y1))
            w_x2.setText(str(x2))
            w_y2.setText(str(y2))

        # ✅ 自动 tap
        if step_key != "topic":
            self.temp_tap[step_key] = [
                int((x1 + x2) / 2),
                int((y1 + y2) / 2)
            ]

        # ✅ 画矩形（关键）
        self.dial.canvas.set_overlay_rect(
            min(p1_lx, lx),
            min(p1_ly, ly),
            abs(p1_lx - lx),
            abs(p1_ly - ly),
            current_color
        )

        print(f"✅ [{step_key}] 标定完成")

        # ========= 进入下一步 =========
        self.current_step_idx += 1
        self.p1_cache = None

        if self.current_step_idx < len(self.calibrate_steps):
            print(f"💡 下一步: 请点击 [{self.calibrate_steps[self.current_step_idx]}] 的左上角")
        else:
            print("🎉 标定完成，自动保存...")
            self.save_new_config()
            self.refresh_config_list()

            if hasattr(self, 'dial') and self.dial:
                self.dial.close()

            self.current_step_idx = -1

    def save_new_config(self):
        """将数据持久化到 devices.json，支持自定义名称"""
        # 1. 弹出输入框询问名称
        # 参数：父窗口, 标题, 提示文字
        config_name, ok = QInputDialog.getText(self, "保存配置", "请输入该配置的名称 (如: 某斩_Reno14):")
        
        if not ok or not config_name:
            print("❌ 已取消保存，或未输入名称")
            return

        # 2. 确定新的 ID
        existing_ids = [int(k) for k in self.devices_data.keys()] or [0]
        new_id = str(max(existing_ids) + 1)
        
        # 3. 构造符合 devices.json 格式的字典
        new_entry = {
            "name": f"{config_name} ({self.raw_w}x{self.raw_h})",
            "size": [self.raw_w, self.raw_h],
            "roi": self.temp_roi,
            "tap": self.temp_tap
        }
        
        # 4. 更新内存并写入文件
        self.devices_data[new_id] = new_entry
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                import json # 确保已经导入
                json.dump(self.devices_data, f, indent=1, ensure_ascii=False)
            
            self.active_config = new_entry
            print(f"💾 配置 '{config_name}' 已成功保存至 devices.json！")
            
            # 可选：更新 UI 上的坐标显示区域来反馈成功
            if hasattr(self.ui, 'edit_coord_display'):
                self.ui.edit_coord_display.setText(f"已激活: {config_name}")
        
                
        except Exception as e:
            print(f"❌ 保存配置文件失败: {e}")

    def refresh_config_list(self):
        """重新读取 JSON 并更新下拉框内容（稳定版）"""
        self.devices_data = self.load_all_configs()

        self.ui.combo_configs.blockSignals(True)  # ✅ 防止触发信号

        self.ui.combo_configs.clear()

        last_index = -1
        for i, (cfg_id, cfg_data) in enumerate(self.devices_data.items()):
            display_name = f"{cfg_id}: {cfg_data.get('name', '未知设备')}"
            self.ui.combo_configs.addItem(display_name, cfg_id)
            last_index = i

        self.ui.combo_configs.blockSignals(False)

        # ✅ 自动选中最后一个配置
        if last_index != -1:
            self.ui.combo_configs.setCurrentIndex(last_index)
            self.load_selected_config()  # 手动触发一次

    def get_current_selected_id(self):
        """获取当前下拉框选中的配置 ID"""
        return self.ui.combo_configs.currentData()

    def load_selected_config(self):
        """加载选中配置并刷新 UI"""

        # ✅ 防止初始化顺序问题
        if not hasattr(self, "coord_widgets"):
            return

        cfg_id = self.get_current_selected_id()

        if not cfg_id or cfg_id not in self.devices_data:
            return

        self.active_config = self.devices_data[cfg_id]
        rois = self.active_config.get("roi", {})

        for step_key, widgets in self.coord_widgets.items():
            if step_key in rois:
                roi = rois[step_key]
                for i in range(4):
                    widgets[i].setText(str(roi[i]))
            else:
                for w in widgets:
                    w.clear()

    def load_all_configs(self):
        """读取并解析 JSON 配置文件"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if not content: 
                        return {}
                    return json.loads(content)
            except Exception as e:
                print(f"📂 读取配置失败: {e}")
                return {}
        return {}
    
    def preview_selected_config(self):
        """【预览】截图 + ROI 可视化"""
        cfg_id = self.get_current_selected_id()
        if not cfg_id or cfg_id not in self.devices_data:
            print("⚠️ 无法预览：未选中配置")
            return

        cfg = self.devices_data[cfg_id]

        try:
            print("📸 正在采集画面用于预览...")
            pil_img = self.adb.take_screenshot()
            raw_w, raw_h = pil_img.size

            # 转 QPixmap
            if pil_img.mode != "RGB":
                pil_img = pil_img.convert("RGB")
            data = pil_img.tobytes("raw", "RGB")
            q_img = QImage(data, raw_w, raw_h, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)

            # 弹出窗口
            self.dial = CalibrationDialog(pixmap, self)
            self.dial.show()

            # 清空旧 overlay
            self.dial.canvas.hide_overlay()

            # ROI 颜色配置（和你标定一致）
            colors = {
                "topic": QColor(255, 87, 34, 80),
                "A": QColor(76, 175, 80, 80),
                "B": QColor(33, 150, 243, 80),
                "C": QColor(255, 193, 7, 80),
                "D": QColor(156, 39, 176, 80)
            }

            scale = self.dial.display_scale

            # 遍历 ROI 并绘制
            for key, roi in cfg.get("roi", {}).items():
                x1, y1, x2, y2 = roi

                # 转 UI 坐标（关键）
                lx = int(x1 * scale)
                ly = int(y1 * scale)
                w = int((x2 - x1) * scale)
                h = int((y2 - y1) * scale)

                color = colors.get(key, QColor(255, 255, 255, 80))

                self.dial.canvas.set_overlay_rect(lx, ly, w, h, color)

            print(f"👁️ 已完成配置 [{cfg_id}] 可视化预览")

        except Exception as e:
            print(f"❌ 预览失败: {e}")

    def delete_selected_config(self):
        """【删除】从 JSON 中移除选中配置并刷新"""
        cfg_id = self.get_current_selected_id()
        if not cfg_id:
            return

        # 弹窗确认，防止误删
        from PySide6.QtWidgets import QMessageBox
        reply = QMessageBox.question(self, "确认删除", 
                                   f"确定要删除配置 [{cfg_id}] 吗？此操作不可撤销。",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            del self.devices_data[cfg_id]
            # 重新保存 JSON
            try:
                with open(self.config_path, 'w', encoding='utf-8') as f:
                    json.dump(self.devices_data, f, indent=2, ensure_ascii=False)
                print(f"🗑️ 配置 [{cfg_id}] 已删除")
                self.refresh_config_list() # 刷新 UI
            except Exception as e:
                print(f"❌ 删除失败: {e}")

    def sync_manual_coords(self):
        """当手动修改文本框数值时，同步到内存数据中"""
        for step_key, (w_x1, w_y1, w_x2, w_y2) in self.coord_widgets.items():
            try:
                coords = [
                    int(w_x1.text()), int(w_y1.text()),
                    int(w_x2.text()), int(w_y2.text())
                ]
                # 更新当前正在标定的临时数据
                self.temp_roi[step_key] = coords
                
                # 如果当前有激活的配置，也同步进去
                if hasattr(self, 'active_config'):
                    self.active_config['roi'][step_key] = coords
                    # 重新计算对应的 tap 点
                    if step_key != "topic":
                        self.active_config['tap'][step_key] = [
                            int((coords[0] + coords[2]) / 2),
                            int((coords[1] + coords[3]) / 2)
                        ]
            except ValueError:
                pass # 忽略非数字输入
        print("✍️ 坐标已根据手动输入同步")

    def toggle_auto_task(self):
        """开始/停止任务按钮的逻辑切换"""
        if self.run_thread is None or not self.run_thread.isRunning():
            # ---------- 准备启动 ----------
            cfg_id = self.get_current_selected_id()
            if not cfg_id or cfg_id not in self.devices_data:
                self.append_log(LogLevel.ERRO,"无法启动：请先在下拉框中选择一个有效配置！")
                # 自动跳转回第 2 页 (Index 1 是坐标标定页) 提醒用户选择
                self.ui.nav_list.setCurrentRow(1) 
                return

            self.ui.text_log_output.clear() # 清空旧日志
            self.append_log(LogLevel.INFO,"初始化运行环境...")
            
            # 初始化并启动线程
            self.run_thread = AutoRunThread(self.devices_data[cfg_id])
            self.run_thread.log_signal.connect(self.append_log)
            self.run_thread.finished_signal.connect(self.on_task_finished)
            self.run_thread.start()
            
        else:
            # ---------- 准备停止 ----------
            self.append_log(LogLevel.WARN,"正在发送停止指令，请等待当前步骤执行完毕...")
            self.ui.btn_start_task.setText("正在停止...")
            self.ui.btn_start_task.setEnabled(False) # 禁用按钮防止疯狂连点
            self.run_thread.stop()

    def on_task_finished(self):
        """任务自然结束或被强制停止后的回调"""
        self.ui.btn_start_task.setText("▶ 开始自动运行")
        self.ui.btn_start_task.setStyleSheet("font-size: 14px;") # 恢复默认样式
        self.ui.btn_start_task.setEnabled(True)
        self.run_thread = None

    def append_log(self, text):
        """将日志追加到文本框，并自动滚动到最底部"""
        now = datetime.now().strftime("%H:%M:%S")
        log_msg = f"[{now}] {text}"
        
        self.ui.text_log_output.append(log_msg)
        
        # 确保滚动条始终在最底部
        scrollbar = self.ui.text_log_output.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

if __name__ == "__main__":
    app = QApplication([])
    window = LexiLoomMainWindow()
    window.resize(610, 500) # 设置默认窗口大小
    window.setWindowTitle("LexiLoom AI 自动化控制台")
    window.show()
    app.exec()