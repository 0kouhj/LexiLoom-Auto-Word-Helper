import sys
import os

# 确保项目根目录在系统路径中
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.gui.main_window import LexiLoomMainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LexiLoomMainWindow()
    window.show()
    sys.exit(app.exec())