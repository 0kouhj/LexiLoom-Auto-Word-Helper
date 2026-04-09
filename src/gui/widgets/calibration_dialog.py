# src/gui/widgets/calibration_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QScrollArea, QApplication
from PySide6.QtCore import Qt
from src.gui.widgets.canvas import ClickableCanvas

class CalibrationDialog(QDialog):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("坐标标定 - 适配模式")
        
        # 【修改点】强制窗口始终置顶，提升用户交互体验
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        
        screen_geo = QApplication.primaryScreen().availableGeometry()
        max_h = screen_geo.height() * 0.8
        orig_w, orig_h = pixmap.width(), pixmap.height()
        
        self.display_scale = 1.0
        if orig_h > max_h:
            self.display_scale = max_h / orig_h
            
        target_w = int(orig_w * self.display_scale)
        target_h = int(orig_h * self.display_scale)

        display_pixmap = pixmap.scaled(
            target_w, target_h, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) # 【修改点】去除白边
        
        self.scroll = QScrollArea()
        self.canvas = ClickableCanvas()
        self.canvas.setPixmap(display_pixmap)
        self.canvas.setFixedSize(target_w, target_h)
        self.canvas.setCursor(Qt.CrossCursor)
        
        self.scroll.setWidget(self.canvas)
        layout.addWidget(self.scroll)
        self.resize(target_w, target_h) # 去除原有多余的空白补偿

    def get_real_coords(self, lx, ly):
        """将 UI 点击坐标还原为手机原始绝对坐标"""
        return int(lx / self.display_scale), int(ly / self.display_scale)