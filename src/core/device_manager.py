# src/core/device_manager.py
import io
import os
import subprocess
import numpy as np
from PIL import Image
from ppadb.client import Client as AdbClient

from src.utils.path_utils import get_bin_resource, get_debug_dir
from src.utils.logger import logger
from src.models.error_codes import ErrorCode
from src.utils.exceptions import ADBError

class DeviceManager:
    def __init__(self, host="127.0.0.1", port=5037):
        self.host = host
        self.port = port
        self.device = None
        
        # 1. 确保 ADB 环境就绪
        self._ensure_adb_alive()
        

    def _ensure_adb_alive(self):
        """静默检测并强制拉起 ADB 守护进程"""
        adb_exe = get_bin_resource("adb.exe")
        
        if not os.path.exists(adb_exe):
            logger.error(f"找不到 ADB 执行文件: {adb_exe}")
            raise ADBError(ErrorCode.ADB_NOT_FOUND, detail=f"路径: {adb_exe}")

        try:
            # 尝试启动服务
            subprocess.run(
                f'"{adb_exe}" start-server', 
                shell=True, 
                capture_output=True, 
                check=True
            )
            logger.info("📡 ADB 服务已确认存活")
        except subprocess.CalledProcessError as e:
            logger.error(f"无法启动 ADB 服务: {e}")
            raise ADBError(ErrorCode.ADB_CMD_FAILED, detail=str(e))

    def refresh_devices(self):
        """刷新并获取当前连接的设备"""
        try:
            client = AdbClient(host=self.host, port=self.port)
            devices = client.devices()
            
            if not devices:
                logger.warning("📴 未发现已连接的设备")
                self.device = None
                return
            
            self.device = devices[0]
            logger.info(f"📱 成功连接设备: {self.device.serial}")
        except Exception as e:
            logger.error(f"连接 ADB Client 失败: {e}")
            self.device = None

    def take_screenshot(self) -> Image.Image:
        """获取屏幕截图并返回 PIL 对象"""
        if not self.device:
            # 资深建议：在这里抛出业务异常，让 TaskRunner 知道该停下了
            raise ADBError(ErrorCode.DEVICE_NOT_FOUND)

        try:
            screenshot_data = self.device.screencap()
            if not screenshot_data:
                raise ValueError("截取数据为空")
            
            img = Image.open(io.BytesIO(screenshot_data))
            
            # 自动备份一张到 debug 目录，方便排查 OCR 问题
            debug_path = os.path.join(get_debug_dir(), "last_screenshot.png")
            img.save(debug_path)
            
            return img
        except Exception as e:
            logger.error(f"截图过程中发生异常: {e}")
            raise ADBError(ErrorCode.SCREENSHOT_FAILED, detail=str(e))

    def click(self, x: int, y: int):
        """执行带随机偏移的点击"""
        if not self.device:
            raise ADBError(ErrorCode.DEVICE_NOT_FOUND)

        # 增加防封随机偏移
        rand_x = x + np.random.randint(-5, 5)
        rand_y = y + np.random.randint(-5, 5)

        try:
            self.device.shell(f"input tap {rand_x} {rand_y}")
            logger.debug(f"🎯 模拟点击坐标: ({rand_x}, {rand_y})")
        except Exception as e:
            logger.error(f"点击指令执行失败: {e}")
            raise ADBError(ErrorCode.ADB_CMD_FAILED, detail=str(e))

    def check_connection(self) -> bool:
        """供 UI 定时调用的心跳检查"""
        try:
            if self.device:
                # 简单执行一个 shell 看看设备还在不在
                self.device.shell("echo 1")
                return True
        except:
            pass
        return False
    
    def get_screen_size(self):
        """利用 ppadb 获取当前连接设备的屏幕分辨率"""
        if not self.device:
            return "Unknown"
        try:
            # 这种写法比 subprocess 更“模块化”
            res = self.device.shell("wm size")
            # 返回通常是 "Physical size: 1080x2400"
            if "size:" in res:
                return res.split(":")[-1].strip()
        except Exception as e:
            logger.error(f"获取分辨率失败: {e}")
        return "Unknown"

    def list_devices_serials(self):
        """返回所有在线设备的序列号列表 (供 UI 下拉框使用)"""
        try:
            client = AdbClient(host=self.host, port=self.port)
            return [d.serial for d in client.devices()]
        except:
            return []