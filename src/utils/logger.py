# src/utils/logger.py
import logging
import os
import sys
import enum
from datetime import datetime
from src.utils.path_utils import get_project_root

class LogLevel(enum.Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERRO = "ERRO"
    DEBG = "DEBG"

class AppLogger:
    def __init__(self, name="LexiLoom"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        log_dir = os.path.join(get_project_root(), "debug")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 1. 文件处理器：记录 DEBUG 级别及以上所有信息
        log_file = os.path.join(log_dir, f"run_{datetime.now().strftime('%Y%m%d')}.log")
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'))

        # 2. 控制台处理器：只记录 INFO 以上
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log(self, level: LogLevel, msg: str, error: Exception = None):
        """统一后端记录接口"""
        if level == LogLevel.INFO:
            self.logger.info(msg)
        elif level == LogLevel.WARN:
            self.logger.warning(msg)
        elif level == LogLevel.ERRO:
            if error:
                # 自动记录堆栈轨迹
                self.logger.error(f"{msg} | Exception: {str(error)}", exc_info=True)
            else:
                self.logger.error(msg)
        elif level == LogLevel.DEBG:
            self.logger.debug(msg)

# 全局单例
app_logger_instance = AppLogger()
# 直接导出 logger 对象和枚举
logger = app_logger_instance.logger