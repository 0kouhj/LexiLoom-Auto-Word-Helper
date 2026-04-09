from enum import Enum, auto
from PySide6.QtWidgets import QMessageBox
from src.models.error_codes import ErrorCode

class MsgType(Enum):
    INFO = auto()
    SUCCESS = auto()
    WARNING = auto()
    ERROR = auto()

class NotificationManager:
    @staticmethod
    def show_error(parent, err: ErrorCode, detail: str = ""):
        """
        基于自定义 ErrorCode 的统一错误弹窗
        """
        msg_box = QMessageBox(parent)
        # 标题显示 4 位错误码，例如 [2002]
        msg_box.setWindowTitle(f"错误 [{err.code}]")
        
        # 内容：枚举定义的标准 message + 运行时捕获的具体 detail
        main_text = f"<b>{err.message}</b>"
        if detail:
            main_text += f"<br><br><i style='color: #555;'>详情: {detail}</i>"
            
        msg_box.setText(main_text)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.exec()

    @staticmethod
    def show_hint(parent, title, content):
        """
        创建一个非阻塞的‘软提醒’窗口
        """
        from PySide6.QtWidgets import QMessageBox
        from PySide6.QtCore import Qt
        
        # 创建对象但不运行 exec()
        msg_box = QMessageBox(parent)
        msg_box.setAttribute(Qt.WA_DeleteOnClose) # 关掉后自动释放内存
        msg_box.setWindowModality(Qt.NonModal)    # 设置为非模态（关键！）
        
        msg_box.setWindowTitle(title)
        msg_box.setText(content)
        msg_box.setIcon(QMessageBox.Information)
        
        msg_box.show() # 使用 show() 立即返回，不阻塞后续代码