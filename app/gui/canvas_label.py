from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal, Qt

class ClickableCanvas(QLabel):
    # 定义信号：传出相对于 Label 的坐标 (x, y)
    clicked_pos = Signal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True) # 开启鼠标追踪

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 获取点击时相对于 Label 左上角的坐标
            self.clicked_pos.emit(event.x(), event.y())