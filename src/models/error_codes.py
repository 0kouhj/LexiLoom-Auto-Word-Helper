# src/models/error_codes.py
from enum import Enum

class ErrorCode(Enum):
    # 1xxx: 基础与配置 (System)
    SUCCESS = (0, "操作成功")
    UNKNOWN_ERROR = (1000, "未知错误")
    CONFIG_LOAD_FAILED = (1001, "配置文件读取失败")
    CONFIG_SAVE_FAILED = (1002, "配置文件保存失败")
    FILE_NOT_FOUND = (1003, "找不到指定文件")

    # 2xxx: 硬件与连接 (Hardware/ADB)
    ADB_NOT_FOUND = (2001, "未找到本地 ADB 运行环境")
    DEVICE_NOT_FOUND = (2002, "未检测到已连接的安卓设备")
    ADB_CMD_FAILED = (2003, "ADB 指令执行异常")
    SCREENSHOT_FAILED = (2004, "截图失败")

    # 3xxx: 核心引擎 (AI/OCR)
    OCR_INIT_ERROR = (3001, "OCR 引擎初始化失败")
    OCR_READ_ERROR = (3002, "文字识别过程出错")
    LLM_CONN_ERROR = (4001, "无法连接到大模型服务 (Ollama)")
    LLM_EMPTY_RES = (4002, "大模型返回了空结果")
    PREVIEW_FAILED = (5001, "预览失败")

    def __init__(self, code, message):
        self.code = code
        self.message = message