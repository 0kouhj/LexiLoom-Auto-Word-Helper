import os
import io
import sys
import subprocess
import numpy as np
from PIL import Image
from ppadb.client import Client as AdbClient
from app.core.path_utils import get_bin_path

class ADBManager:
    def __init__(self, host="127.0.0.1", port=5037):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        self.adb_path = os.path.join(os.getcwd(), "bin", "adb.exe")
        self._ensure_adb_alive()
        try:
            self.client = AdbClient(host=host, port=port)
            devices = self.client.devices()
            self.device = devices[0] if devices else None
        except Exception:
            self.device = None

    def _ensure_adb_alive(self):
        """静默检测并强制拉起 ADB 守护进程"""
        adb_exe = get_bin_path("adb.exe")
        try:
            # 检查 adb 是否在路径中并尝试启动服务
            subprocess.run(f'"{adb_exe}" start-server', shell=True, capture_output=True)
        except FileNotFoundError:
            print("❌ 错误: 系统路径中未找到 adb")

    def take_screenshot_and_save(self, save_path):
        """
        通过内存流获取截图并保存到本地 debug 文件夹
        """
        if not self.device:
            return False, "未发现连接的设备"
        
        try:
            # 确保目录存在
            directory = os.path.dirname(save_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            # 使用 ppadb 获取截图二进制流
            screenshot_data = self.device.screencap()
            
            # 使用 PIL 处理并保存
            img = Image.open(io.BytesIO(screenshot_data))
            img.save(save_path)
            
            return True, f"截图已保存: {save_path}"
        except Exception as e:
            return False, f"截图失败: {str(e)}"
    
    def take_screenshot(self):
        if not self.device:
            raise Exception("未连接 ADB 设备")
        # 获取截图二进制流
        screenshot_data = self.device.screencap()
        # 返回 PIL Image 对象
        return Image.open(io.BytesIO(screenshot_data))

    def click(self, x, y):
        """执行带随机偏移的点击（防封逻辑）"""
        if self.device:
            rand_x = x + np.random.randint(-3, 3)
            rand_y = y + np.random.randint(-3, 3)
            self.device.shell(f"input tap {rand_x} {rand_y}")
            return True
        return False