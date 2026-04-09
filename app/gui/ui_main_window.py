# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

from app.gui.canvas_label import ClickableCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 505)
        MainWindow.setMinimumSize(QSize(600, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.content_stack = QStackedWidget(self.centralwidget)
        self.content_stack.setObjectName(u"content_stack")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.verticalLayout_2 = QVBoxLayout(self.page_0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.start_env_check = QGroupBox(self.page_0)
        self.start_env_check.setObjectName(u"start_env_check")
        self.gridLayout_4 = QGridLayout(self.start_env_check)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, -1, -1, -1)
        self.label_adb_status = QLabel(self.start_env_check)
        self.label_adb_status.setObjectName(u"label_adb_status")
        self.label_adb_status.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_4.addWidget(self.label_adb_status, 0, 1, 1, 1)

        self.label_ollama_status = QLabel(self.start_env_check)
        self.label_ollama_status.setObjectName(u"label_ollama_status")
        self.label_ollama_status.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_4.addWidget(self.label_ollama_status, 1, 1, 1, 1)

        self.btn_check_env = QPushButton(self.start_env_check)
        self.btn_check_env.setObjectName(u"btn_check_env")
        self.btn_check_env.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.btn_check_env, 2, 1, 1, 1)

        self.btn_start_ollama = QPushButton(self.start_env_check)
        self.btn_start_ollama.setObjectName(u"btn_start_ollama")
        self.btn_start_ollama.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.btn_start_ollama, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.start_env_check)

        self.system_info = QGroupBox(self.page_0)
        self.system_info.setObjectName(u"system_info")
        self.gridLayout = QGridLayout(self.system_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, -1, -1, -1)
        self.label_device_screen = QLabel(self.system_info)
        self.label_device_screen.setObjectName(u"label_device_screen")

        self.gridLayout.addWidget(self.label_device_screen, 1, 0, 1, 1)

        self.label_device_model_text = QLabel(self.system_info)
        self.label_device_model_text.setObjectName(u"label_device_model_text")
        self.label_device_model_text.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_device_model_text, 0, 1, 1, 1)

        self.label_Ollama_AIs = QLabel(self.system_info)
        self.label_Ollama_AIs.setObjectName(u"label_Ollama_AIs")

        self.gridLayout.addWidget(self.label_Ollama_AIs, 2, 0, 1, 1)

        self.label_device_screen_text = QLabel(self.system_info)
        self.label_device_screen_text.setObjectName(u"label_device_screen_text")
        self.label_device_screen_text.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_device_screen_text, 1, 1, 1, 1)

        self.label_Ollama_AIs_text = QLabel(self.system_info)
        self.label_Ollama_AIs_text.setObjectName(u"label_Ollama_AIs_text")
        self.label_Ollama_AIs_text.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_Ollama_AIs_text, 2, 1, 1, 1)

        self.label_device_model = QLabel(self.system_info)
        self.label_device_model.setObjectName(u"label_device_model")

        self.gridLayout.addWidget(self.label_device_model, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.system_info)

        self.content_stack.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_preview_config = QPushButton(self.groupBox)
        self.btn_preview_config.setObjectName(u"btn_preview_config")

        self.gridLayout_2.addWidget(self.btn_preview_config, 2, 2, 1, 1)

        self.btn_delete_config = QPushButton(self.groupBox)
        self.btn_delete_config.setObjectName(u"btn_delete_config")

        self.gridLayout_2.addWidget(self.btn_delete_config, 3, 2, 1, 1)

        self.btn_load_config = QPushButton(self.groupBox)
        self.btn_load_config.setObjectName(u"btn_load_config")

        self.gridLayout_2.addWidget(self.btn_load_config, 3, 1, 1, 1)

        self.btn_create_config = QPushButton(self.groupBox)
        self.btn_create_config.setObjectName(u"btn_create_config")

        self.gridLayout_2.addWidget(self.btn_create_config, 2, 1, 1, 1)

        self.combo_configs = QComboBox(self.groupBox)
        self.combo_configs.setObjectName(u"combo_configs")
        self.combo_configs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_2.addWidget(self.combo_configs, 1, 1, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.page_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_refresh_canvas = QPushButton(self.groupBox_2)
        self.btn_refresh_canvas.setObjectName(u"btn_refresh_canvas")
        self.btn_refresh_canvas.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(11)
        self.btn_refresh_canvas.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_refresh_canvas)

        self.edit_coord_display = QLineEdit(self.groupBox_2)
        self.edit_coord_display.setObjectName(u"edit_coord_display")
        self.edit_coord_display.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_2.addWidget(self.edit_coord_display)


        self.gridLayout_3.addWidget(self.groupBox_2, 4, 0, 1, 2)

        self.label_canvas = ClickableCanvas(self.page_1)
        self.label_canvas.setObjectName(u"label_canvas")
        self.label_canvas.setMaximumSize(QSize(1, 1))

        self.gridLayout_3.addWidget(self.label_canvas, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.page_1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 14)
        self.edit_b_x2 = QLineEdit(self.groupBox_3)
        self.edit_b_x2.setObjectName(u"edit_b_x2")

        self.gridLayout_5.addWidget(self.edit_b_x2, 3, 1, 1, 1)

        self.edit_b_y1 = QLineEdit(self.groupBox_3)
        self.edit_b_y1.setObjectName(u"edit_b_y1")

        self.gridLayout_5.addWidget(self.edit_b_y1, 3, 2, 1, 1)

        self.edit_topic_x2 = QLineEdit(self.groupBox_3)
        self.edit_topic_x2.setObjectName(u"edit_topic_x2")

        self.gridLayout_5.addWidget(self.edit_topic_x2, 1, 1, 1, 1)

        self.edit_c_x1 = QLineEdit(self.groupBox_3)
        self.edit_c_x1.setObjectName(u"edit_c_x1")

        self.gridLayout_5.addWidget(self.edit_c_x1, 4, 3, 1, 1)

        self.edit_topic_y1 = QLineEdit(self.groupBox_3)
        self.edit_topic_y1.setObjectName(u"edit_topic_y1")

        self.gridLayout_5.addWidget(self.edit_topic_y1, 1, 2, 1, 1)

        self.edit_d_y2 = QLineEdit(self.groupBox_3)
        self.edit_d_y2.setObjectName(u"edit_d_y2")

        self.gridLayout_5.addWidget(self.edit_d_y2, 5, 0, 1, 1)

        self.edit_a_y2 = QLineEdit(self.groupBox_3)
        self.edit_a_y2.setObjectName(u"edit_a_y2")

        self.gridLayout_5.addWidget(self.edit_a_y2, 2, 0, 1, 1)

        self.edit_c_y2 = QLineEdit(self.groupBox_3)
        self.edit_c_y2.setObjectName(u"edit_c_y2")

        self.gridLayout_5.addWidget(self.edit_c_y2, 4, 0, 1, 1)

        self.edit_topic_y2 = QLineEdit(self.groupBox_3)
        self.edit_topic_y2.setObjectName(u"edit_topic_y2")

        self.gridLayout_5.addWidget(self.edit_topic_y2, 1, 0, 1, 1)

        self.edit_b_y2 = QLineEdit(self.groupBox_3)
        self.edit_b_y2.setObjectName(u"edit_b_y2")

        self.gridLayout_5.addWidget(self.edit_b_y2, 3, 0, 1, 1)

        self.edit_d_y1 = QLineEdit(self.groupBox_3)
        self.edit_d_y1.setObjectName(u"edit_d_y1")

        self.gridLayout_5.addWidget(self.edit_d_y1, 5, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 3, 4, 1, 1)

        self.edit_c_y1 = QLineEdit(self.groupBox_3)
        self.edit_c_y1.setObjectName(u"edit_c_y1")

        self.gridLayout_5.addWidget(self.edit_c_y1, 4, 2, 1, 1)

        self.edit_d_x2 = QLineEdit(self.groupBox_3)
        self.edit_d_x2.setObjectName(u"edit_d_x2")

        self.gridLayout_5.addWidget(self.edit_d_x2, 5, 1, 1, 1)

        self.edit_c_x2 = QLineEdit(self.groupBox_3)
        self.edit_c_x2.setObjectName(u"edit_c_x2")

        self.gridLayout_5.addWidget(self.edit_c_x2, 4, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(120, 16777215))
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_4, 4, 4, 1, 1)

        self.edit_a_x1 = QLineEdit(self.groupBox_3)
        self.edit_a_x1.setObjectName(u"edit_a_x1")

        self.gridLayout_5.addWidget(self.edit_a_x1, 2, 3, 1, 1)

        self.edit_a_y1 = QLineEdit(self.groupBox_3)
        self.edit_a_y1.setObjectName(u"edit_a_y1")

        self.gridLayout_5.addWidget(self.edit_a_y1, 2, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(120, 16777215))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_5, 5, 4, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 2, 4, 1, 1)

        self.edit_topic_x1 = QLineEdit(self.groupBox_3)
        self.edit_topic_x1.setObjectName(u"edit_topic_x1")

        self.gridLayout_5.addWidget(self.edit_topic_x1, 1, 3, 1, 1)

        self.edit_b_x1 = QLineEdit(self.groupBox_3)
        self.edit_b_x1.setObjectName(u"edit_b_x1")

        self.gridLayout_5.addWidget(self.edit_b_x1, 3, 3, 1, 1)

        self.edit_a_x2 = QLineEdit(self.groupBox_3)
        self.edit_a_x2.setObjectName(u"edit_a_x2")

        self.gridLayout_5.addWidget(self.edit_a_x2, 2, 1, 1, 1)

        self.edit_d_x1 = QLineEdit(self.groupBox_3)
        self.edit_d_x1.setObjectName(u"edit_d_x1")

        self.gridLayout_5.addWidget(self.edit_d_x1, 5, 3, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 1, 4, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 2, 2)

        self.content_stack.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.content_stack.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.content_stack)

        self.nav_list = QListWidget(self.centralwidget)
        QListWidgetItem(self.nav_list)
        QListWidgetItem(self.nav_list)
        QListWidgetItem(self.nav_list)
        self.nav_list.setObjectName(u"nav_list")
        self.nav_list.setMaximumSize(QSize(150, 16777215))
        self.nav_list.setStyleSheet(u"QListWidget {\n"
"    background-color: #2b2b2b; /* \u6df1\u7070\u8272\u80cc\u666f */\n"
"    color: #f0f0f0;            /* \u6d45\u7070\u8272\u6587\u5b57 */\n"
"    border: none;               /* \u53bb\u6389\u8fb9\u6846 */\n"
"    font-size: 14px;\n"
"    outline: none;              /* \u53bb\u6389\u70b9\u51fb\u65f6\u7684\u865a\u7ebf\u6846 */\n"
"}\n"
"QListWidget::item {\n"
"    height: 80px;               /* \u8ba9\u9009\u9879\u9ad8\u4e00\u70b9\uff0c\u66f4\u597d\u70b9 */\n"
"    padding-left: 10px;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: #0078d4; /* \u9009\u4e2d\u65f6\u53d8\u6210 Windows \u84dd\u8272 */\n"
"}")

        self.horizontalLayout.addWidget(self.nav_list)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 610, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.content_stack.setCurrentIndex(2)
        self.nav_list.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_env_check.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u73af\u5883\u68c0\u67e5", None))
        self.label_adb_status.setText(QCoreApplication.translate("MainWindow", u"ADB\u72b6\u6001: \u7b49\u5f85\u68c0\u6d4b", None))
        self.label_ollama_status.setText(QCoreApplication.translate("MainWindow", u"Ollama \u72b6\u6001: \u7b49\u5f85\u68c0\u6d4b", None))
        self.btn_check_env.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u68c0\u67e5\u73af\u5883", None))
        self.btn_start_ollama.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8Ollama", None))
        self.system_info.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u4fe1\u606f", None))
        self.label_device_screen.setText("")
        self.label_device_model_text.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u578b\u53f7", None))
        self.label_Ollama_AIs.setText("")
        self.label_device_screen_text.setText(QCoreApplication.translate("MainWindow", u"\u5c4f\u5e55\u5206\u8fa8\u7387", None))
        self.label_Ollama_AIs_text.setText(QCoreApplication.translate("MainWindow", u"Ollama\u53ef\u7528AI", None))
        self.label_device_model.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5750\u6807\u914d\u7f6e", None))
        self.btn_preview_config.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8\u914d\u7f6e", None))
        self.btn_delete_config.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u914d\u7f6e", None))
        self.btn_load_config.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u914d\u7f6e", None))
        self.btn_create_config.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u914d\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5f39\u7a97\u63a7\u5236", None))
        self.btn_refresh_canvas.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u624b\u673a\u753b\u9762", None))
        self.label_canvas.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u914d\u7f6e\u5750\u6807\uff08Read Only\uff09", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9898\u76ee", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"y1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"x2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"y2", None))

        __sortingEnabled = self.nav_list.isSortingEnabled()
        self.nav_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.nav_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u68c0\u67e5", None))
        ___qlistwidgetitem1 = self.nav_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807\u6807\u5b9a", None))
        ___qlistwidgetitem2 = self.nav_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.nav_list.setSortingEnabled(__sortingEnabled)

    # retranslateUi

