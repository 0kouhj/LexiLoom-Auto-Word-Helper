from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QFont, QTextCursor

from src.models.error_codes import ErrorCode
from src.utils.logger import app_logger_instance, LogLevel
from src.core.device_manager import DeviceManager
from src.core.llm_client import OllamaClient

from src.gui.resources.ui_main_window import Ui_MainWindow
from src.gui.pages.page_env import PageEnv
from src.gui.pages.page_config import PageConfig
from src.gui.pages.page_task import PageTask

from src.gui.widgets.notification import NotificationManager, MsgType
from src.gui.widgets.ui_effects import UIEffects


class LexiLoomMainWindow(PageEnv, PageConfig, PageTask, QMainWindow):
    sig_notification = Signal(str, str, MsgType)

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ✅ 全局控件字体修复（关键）
        self._fix_all_fonts()

        # ✅ 日志字体（等宽）
        self._init_log_font()

        UIEffects.apply_round_avatar(self.ui.label_avatar, size=82)

        self.dm = DeviceManager()
        self.all_ai_models = OllamaClient.fetch_all_models()

        self.init_page_config()
        self.init_page_task()

        self._bind_all_signals()
        
        self.sig_notification.connect(self._on_notification_received)

        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("lexiloom.version1")

        self.ui.nav_list.currentRowChanged.connect(
            lambda index: UIEffects.play_pcl_transition(self.ui.content_stack, index)
        )
        self.ui.content_stack.setCurrentIndex(0)
        self.ui.nav_list.setCurrentRow(0)
        
        self.on_btn_check_env_clicked()


    # =========================
    # 信号处理
    # =========================
    @Slot(str, str, object)
    def _on_notification_received(self, title, content, m_type):
        NotificationManager.show_dialog(self, title, content, m_type)

    # =========================
    # 对话框接口
    # =========================
    def show_error_dialog(self, err: ErrorCode, detail: str = ""):
        NotificationManager.show_error(self, err, detail)

    def show_hint_dialog(self, title, content):
        NotificationManager.show_hint(self, title, content)

    def show_msg(self, title: str, content: str, m_type):
        NotificationManager.show_dialog(self, title, content, m_type)

    # =========================
    # 信号绑定
    # =========================
    def _bind_all_signals(self):
        

        self.ui.btn_check_env.clicked.connect(self.on_btn_check_env_clicked)

        self.ui.btn_delete_config.clicked.connect(self.on_btn_delete_clicked)
        self.ui.btn_load_config.clicked.connect(self.on_btn_load_clicked)
        self.ui.btn_create_config.clicked.connect(self.on_btn_create_clicked)
        self.ui.btn_save_config.clicked.connect(self.on_btn_save_config_clicked)
        self.ui.btn_refresh_config.clicked.connect(self.on_btn_refresh_clicked)

        self.ui.btn_start_task.clicked.connect(self.on_btn_start_task_clicked)
        self.ui.btn_stop_task.clicked.connect(self.on_btn_stop_task_clicked)

        UIEffects.bind_link(self.ui.btn_github, "https://github.com/0kouhj")
        UIEffects.bind_link(self.ui.btn_blog, "https://blog.0kouhj.cloud")

    # =========================
    # ✅ 日志输出（无锯齿）
    # =========================
    def append_log(self, level: LogLevel, msg: str, error: Exception = None):
        """
        统一 UI 与后端的日志出口
        :param level: LogLevel 枚举 (INFO, WARN, ERRO)
        :param msg: 简短描述
        :param error: 报错对象 (如果是 ERRO 级别)
        """
        # 1. 后端记录（写文件）
        app_logger_instance.log(level, msg, error)

        # 2. UI 渲染渲染
        edit = self.ui.text_log_output
        
        # 颜色映射表
        color_map = {
            LogLevel.INFO: "#0078D7", # 经典蓝
            LogLevel.WARN: "#FFA500", # 橙色
            LogLevel.ERRO: "#FF4D4D", # 红色
            LogLevel.DEBG: "#888888"  # 灰色
        }
        color = color_map.get(level, "#FFFFFF")

        # 构造 HTML
        tag = f"[{level.value}]"
        display_msg = msg
        if error:
            display_msg += f" (Reason: {str(error)})"

        html_line = f'<span style="color:{color}; font-weight:bold;">{tag}</span> {display_msg}'
        
        # 写入并滚动
        edit.append(html_line)
        edit.moveCursor(QTextCursor.End)

    # =========================
    # ✅ 日志字体（等宽优化）
    # =========================
    def _init_log_font(self):
        font = QFont("Consolas")
        font.setPointSize(11)

        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferFullHinting)

        self.ui.text_log_output.setFont(font)

    # =========================
    # ✅ 全局控件抗锯齿修复（核心）
    # =========================
    def _fix_all_fonts(self):
        font = QFont()
        font.setFamilies([
            "Microsoft YaHei UI",
            "Segoe UI",
            "Segoe UI Emoji"
        ])
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferFullHinting)

        # QLabel / QPushButton 全部修复
        for w in self.findChildren(QLabel):
            w.setFont(font)

        for w in self.findChildren(QPushButton):
            w.setFont(font)
    
