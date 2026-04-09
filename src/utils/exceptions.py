# src/utils/exceptions.py
from src.models.error_codes import ErrorCode

class LexiLoomException(Exception):
    """项目自定义异常基类"""
    def __init__(self, error_enum: ErrorCode, detail=None):
        self.code = error_enum.code
        self.message = error_enum.message
        self.detail = detail
        full_msg = f"[{self.code}] {self.message}"
        if detail:
            full_msg += f" - {detail}"
        super().__init__(full_msg)

class ConfigError(LexiLoomException): pass
class ADBError(Exception): pass
class VisionError(LexiLoomException): pass
class LLMError(LexiLoomException): pass
class AppException(LexiLoomException): pass