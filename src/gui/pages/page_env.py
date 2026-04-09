# src/gui/pages/page_env.py
from src.models.error_codes import ErrorCode
from src.utils.exceptions import ADBError
from src.utils.logger import LogLevel
import subprocess
import requests
import os

class PageEnv:
    def on_btn_check_env_clicked(self):
        self.append_log(LogLevel.INFO,"正在调用 DeviceManager 执行标准化自检...")
        try:
            # 1. 直接使用你写好的刷新接口
            self.dm.refresh_devices()
            
            # 2. 检查 DM 状态
            if not self.dm.device:
                # 统一抛出你定义的错误码
                raise ADBError(ErrorCode.DEVICE_NOT_FOUND)

            # 3. 调用你写好的分辨率接口
            screen_size = self.dm.get_screen_size()
            
            # 4. 获取详细 HTML 名称 (补充逻辑)
            model_info_html = self._get_detailed_model_html()

            # 5. 更新 UI
            self.ui.label_adb_status.setText("ADB状态: ✅ 已连接")
            self.ui.label_adb_status.setStyleSheet("color: #4CAF50; font-weight: bold;background-color: #FFFFFF;")
            self.ui.label_device_model.setText(model_info_html)
            self.ui.label_device_screen.setText(screen_size)
            
            self.append_log(LogLevel.INFO,f"设备就绪: {self.dm.device.serial} [{screen_size}]")

        except ADBError as e:
            # 捕获你定义的业务异常
            self.show_error_dialog(ErrorCode.DEVICE_NOT_FOUND, str(e))
            self.append_log(LogLevel.ERRO,"",error = e)
        except Exception as e:
            self.show_error_dialog(ErrorCode.ADB_CMD_FAILED, str(e))
            self.append_log(LogLevel.ERRO,"",error = e)

        # 检查模型服务
        self._check_llm_service()

    def _get_detailed_model_html(self):
        try:
            name_raw = subprocess.check_output("adb shell settings get global device_name", shell=True, text=True, timeout=2).strip()
            model_code = subprocess.check_output("adb shell getprop ro.product.model", shell=True, text=True, timeout=2).strip()
            
            real_name = name_raw if (name_raw and name_raw != "null") else model_code
            return f"<b style='color: #2196F3;'>{real_name}</b><br><span style='color: #757575; font-size: 11px;'>型号: {model_code}</span>"
        except:
            return "未知设备"


    def _check_llm_service(self):
        """探测 Ollama"""
        try:
            # 增加超时处理，防止本地服务没开时卡顿
            resp = requests.get("http://localhost:11434/api/tags", timeout=1)
            if resp.status_code == 200:
                # 获取模型名称列表
                models = [m['name'] for m in resp.json().get('models', [])]
                
                if models:
                    # --- 核心改动：处理超过三个的情况 ---
                    if len(models) > 3:
                        display_text = "<br>".join(models[:3]) + "......"
                    else:
                        display_text = "<br>".join(models)
                    # -------------------------------
                    self.ui.label_Ollama_AIs.setText(display_text)
                self.ui.label_ollama_status.setText("Ollama状态: ✅ 在线")
                self.ui.label_ollama_status.setStyleSheet("color: #4CAF50; font-weight: bold;background-color: #FFFFFF;")
            else:
                raise Exception()
        except Exception as e:
            self.ui.label_ollama_status.setText("Ollama状态: ❌ 离线")
            self.ui.label_ollama_status.setStyleSheet("color: #F44336; font-weight: bold;background-color: #FFFFFF;")
            self.show_error_dialog(ErrorCode.LLM_CONN_ERROR, str(e))

