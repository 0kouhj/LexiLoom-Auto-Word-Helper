# src/gui/widgets/canvas.py
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal, Qt, QRect
from PySide6.QtGui import QPainter, QPen, QColor, QBrush

class ClickableCanvas(QLabel):
    clicked_pos = Signal(int, int) 

    def __init__(self, parent=None):
        super().__init__(parent)
        self.rects = [] 
        self._show_overlay = False

    def set_overlay_rect(self, x, y, w, h, color):
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
            pen_color.setAlpha(255) 
            painter.setPen(QPen(pen_color, 2))
            painter.setBrush(QBrush(color))
            painter.drawRect(rect)
        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked_pos.emit(int(event.position().x()), int(event.position().y()))