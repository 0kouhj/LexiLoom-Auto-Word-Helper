# run.py
import sys
import os
from PySide6.QtGui import QIcon
from src.utils.path_utils import get_project_root
# =========================
# ✅ 1. 必须在 QApplication 前
# =========================
os.environ["QT_QPA_PLATFORM"] = "windows:fontengine=freetype"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
os.environ["QT_SCALE_FACTOR_ROUNDING_POLICY"] = "PassThrough"

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from src.gui.main_window import LexiLoomMainWindow
from src.utils.logger import logger

def get_app_icon():
        """
        利用 path_utils 提供的物理根目录，定位图标资源
        """
        # 路径：根目录/src/gui/resources/assets/icon.ico
        icon_path = os.path.join(
            get_project_root(), 
            "src", "gui", "resources", "icon.ico"
        )
            
        if os.path.exists(icon_path):
            return QIcon(icon_path)
            
        # 如果找不到图标，返回空图标或打印警告，防止程序崩溃
        print(f"警告: 未能在路径找到图标: {icon_path}")
        return QIcon()

def main():
    logger.info("🚀 程序启动中...")

    # =========================
    # ✅ 2. 创建应用
    # =========================
    app = QApplication(sys.argv)


    # =========================
    # ✅ 4. 全局字体（关键）
    # =========================
    font = QFont("Microsoft YaHei UI")  # 中文清晰

    font.setStyleStrategy(QFont.PreferAntialias)
    font.setHintingPreference(QFont.PreferFullHinting)

    app.setFont(font)

    # =========================
    # ✅ 5. UI风格
    # =========================
    app.setStyle("Fusion")

    # =========================
    # ✅ 6. 启动窗口
    # =========================
    window = LexiLoomMainWindow()
    window.setWindowIcon(get_app_icon())
    window.setWindowTitle("LexiLoom 词梭")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()