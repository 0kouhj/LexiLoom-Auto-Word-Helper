# src/gui/widgets/ui_effects.py
import os
import webbrowser
from PySide6.QtWidgets import QGraphicsOpacityEffect, QSizePolicy
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QFont
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QPoint

from src.utils.path_utils import get_project_root

class UIEffects:
    @staticmethod
    def apply_round_avatar(label_widget, size=64):
        """
        将头像处理为圆形并设置到指定的 QLabel 上
        """
        avatar_path = os.path.join(get_project_root(), "src", "gui", "resources", "avatar.jpg")
        
        if not os.path.exists(avatar_path):
            print(f"Error: Avatar not found at {avatar_path}")
            return

        # 1. 处理图片缩放与裁剪
        src_pixmap = QPixmap(avatar_path)
        scaled_pixmap = src_pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        dest_pixmap = QPixmap(size, size)
        dest_pixmap.fill(Qt.transparent)

        painter = QPainter(dest_pixmap)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)
        
        # 居中绘制
        x = (scaled_pixmap.width() - size) // 2
        y = (scaled_pixmap.height() - size) // 2
        painter.drawPixmap(0, 0, scaled_pixmap.copy(x, y, size, size))
        painter.end()

        # 2. 应用到控件
        label_widget.setFixedSize(size, size)
        label_widget.setPixmap(dest_pixmap)
        label_widget.setAlignment(Qt.AlignCenter)
        label_widget.setStyleSheet("background-color: transparent; border: none;")
        label_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    @staticmethod
    def play_pcl_transition(stack_widget, next_index):
        """
        PCL 风格切换：左 -> 右 + 回弹 + 淡入淡出
        """
        current_widget = stack_widget.currentWidget()
        next_widget = stack_widget.widget(next_index)

        if current_widget == next_widget:
            return

        def get_opacity_eff(w):
            eff = w.graphicsEffect()
            if not isinstance(eff, QGraphicsOpacityEffect):
                eff = QGraphicsOpacityEffect(w)
                w.setGraphicsEffect(eff)
            return eff

        eff_next = get_opacity_eff(next_widget)
        eff_curr = get_opacity_eff(current_widget)

        stack_widget.anim_group = QParallelAnimationGroup()

        # =========================
        # 1. 下一页：左 -> 右 + 回弹
        # =========================
        offset = -40  # 从左侧进入（负数）
        
        anim_pos = QPropertyAnimation(next_widget, b"pos")
        anim_pos.setDuration(500)
        anim_pos.setStartValue(QPoint(offset, 0))
        anim_pos.setEndValue(QPoint(0, 0))
        
        # 关键：回弹效果
        anim_pos.setEasingCurve(QEasingCurve.OutBack)

        # =========================
        # 2. 下一页：淡入
        # =========================
        anim_fade_in = QPropertyAnimation(eff_next, b"opacity")
        anim_fade_in.setDuration(400)
        anim_fade_in.setStartValue(0)
        anim_fade_in.setEndValue(1)

        # =========================
        # 3. 当前页：淡出
        # =========================
        anim_fade_out = QPropertyAnimation(eff_curr, b"opacity")
        anim_fade_out.setDuration(250)
        anim_fade_out.setStartValue(1)
        anim_fade_out.setEndValue(0)

        stack_widget.anim_group.addAnimation(anim_pos)
        stack_widget.anim_group.addAnimation(anim_fade_in)
        stack_widget.anim_group.addAnimation(anim_fade_out)

        # 切换并播放
        stack_widget.setCurrentIndex(next_index)
        next_widget.raise_()
        stack_widget.anim_group.start()
    @staticmethod
    def bind_link(button, url):
        """
        给按钮绑定一个简单的网页跳转
        """
        button.clicked.connect(lambda: webbrowser.open(url))

    @staticmethod
    def beautify_combobox(combo):
        """
        进一步优化 ComboBox 的显示效果
        """
        # 让下拉列表支持圆角 (需要设置窗口标志)
        view = combo.view()
        view.window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        view.window().setAttribute(Qt.WA_TranslucentBackground)
        
        # 设置下拉列表的行高（QSS 有时无效，代码最稳）
        combo.setStyleSheet(combo.styleSheet() + """
            QComboBox QAbstractItemView {
                border-radius: 6px;
                padding: 4px;
            }
        """)