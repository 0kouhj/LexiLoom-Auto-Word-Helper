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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

from app.gui.canvas_label import ClickableCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(673, 500)
        MainWindow.setMinimumSize(QSize(600, 500))
        MainWindow.setStyleSheet(u"QPushButton {\n"
"    /* \u683c\u5f0f\uff1a\u5bbd\u5ea6 \u5b9e\u7ebf \u989c\u8272(\u4f7f\u7528rgba\u5b9e\u73b0\u534a\u900f\u660e) */\n"
"    border: 1px solid rgba(0, 0, 0, 185); \n"
"    border-radius: 8px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"/* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u72b6\u6001 */\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(74, 144, 226, 180); \n"
"	background-color: rgba(0, 120, 215, 0.1);\n"
"    color: #2d5a89; \n"
"}\n"
"\n"
"/* \u9f20\u6807\u6309\u4e0b\u65f6\u7684\u72b6\u6001\uff08\u53ef\u9009\uff0c\u589e\u52a0\u70b9\u51fb\u53cd\u9988\uff09 */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(135, 206, 250, 255);\n"
"    border: 2px solid rgba(74, 144, 226, 255);\n"
"}\n"
"\n"
"QMainWindow{margin:0px;\n"
"	padding:0px;}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.centralwidget.setStyleSheet(u"QWidget{background-color:#d6e4f7;\n"
"	margin:0px;\n"
"	padding:0px;}\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 6, 0)
        self.content_stack = QStackedWidget(self.centralwidget)
        self.content_stack.setObjectName(u"content_stack")
        self.content_stack.setStyleSheet(u"/* \u4f7f\u7528\u901a\u914d\u7b26\u6216\u786e\u4fdd\u6ca1\u6709 ID \u9650\u5236 */\n"
"QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"    margin-top: 20px;\n"
"	margin-bottom:20px;\n"
"	margin-left:15 px;\n"
"	margin-right:15px;\n"
"    padding: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u5f3a\u5236\u8ba9 QStackedWidget \u5185\u90e8\u7684\u6240\u6709 GroupBox \u7ee7\u627f */\n"
"QStackedWidget QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"}")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.page_0.setStyleSheet(u"QWidget { background-color: #d6e4f7; }\n"
"QWidget { \n"
"    color: #000000; \n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page_0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.start_env_check = QGroupBox(self.page_0)
        self.start_env_check.setObjectName(u"start_env_check")
        self.start_env_check.setStyleSheet(u"QGroupBox { background-color: #FFFFFF; }\n"
"QGroupBox{padding:0px;}")
        self.horizontalLayout_2 = QHBoxLayout(self.start_env_check)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, -1, -1)
        self.groupBox_2 = QGroupBox(self.start_env_check)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 180))
        self.groupBox_2.setMaximumSize(QSize(16777215, 180))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"    margin-top: 0px;\n"
"    padding: 0px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_adb_status = QLabel(self.groupBox_2)
        self.label_adb_status.setObjectName(u"label_adb_status")
        self.label_adb_status.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        self.label_adb_status.setFont(font)
        self.label_adb_status.setStyleSheet(u"QLabel {background-color : #FFFFFF;}")

        self.verticalLayout.addWidget(self.label_adb_status)

        self.label_ollama_status = QLabel(self.groupBox_2)
        self.label_ollama_status.setObjectName(u"label_ollama_status")
        self.label_ollama_status.setMaximumSize(QSize(16777215, 50))
        self.label_ollama_status.setFont(font)
        self.label_ollama_status.setStyleSheet(u"QLabel {background-color : #FFFFFF;}")

        self.verticalLayout.addWidget(self.label_ollama_status)

        self.btn_check_env = QPushButton(self.groupBox_2)
        self.btn_check_env.setObjectName(u"btn_check_env")
        self.btn_check_env.setMinimumSize(QSize(0, 40))
        self.btn_check_env.setStyleSheet(u"QPushButton{background-color:#FFFFFF;}")

        self.verticalLayout.addWidget(self.btn_check_env)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.line = QFrame(self.start_env_check)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setStyleSheet(u"QFrame{margin:15px;}")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.label_12 = QLabel(self.start_env_check)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(40, 0))
        self.label_12.setMaximumSize(QSize(40, 16777215))
        self.label_12.setStyleSheet(u"QLabel {\n"
"    /* 1. \u80cc\u666f\u4e0e\u5706\u89d2 */\n"
"    background-color: #ffffff;    /* \u7eaf\u767d\u80cc\u666f */\n"
"    border-radius: 6px;           /* \u7a0d\u5fae\u5e26\u4e00\u70b9\u5706\u89d2\uff0c\u914d\u5408\u6574\u4f53\u98ce\u683c */\n"
"    \n"
"    /* 2. \u6587\u5b57\u6837\u5f0f */\n"
"    color: #000000;               /* \u6587\u5b57\u9ed1\u8272 */\n"
"    font-size: 12pt;              /* \u5b57\u53f7 12 (\u6ce8\u610f\u5355\u4f4d\u662f pt \u6216 px) */\n"
"    font-weight: bold;            /* \u7c97\u4f53 */\n"
"}")
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_12)


        self.verticalLayout_2.addWidget(self.start_env_check)

        self.system_info = QGroupBox(self.page_0)
        self.system_info.setObjectName(u"system_info")
        self.system_info.setStyleSheet(u"QGroupBox {background-color: #FFFFFF;}\n"
"QGroupBox{padding:0px;}")
        self.horizontalLayout_3 = QHBoxLayout(self.system_info)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, -1, -1, -1)
        self.groupBox_4 = QGroupBox(self.system_info)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"    margin-top: 0px;\n"
"    padding: 0px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"QLabel {background-color : #FFFFFF;}")
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_device_model = QLabel(self.groupBox_4)
        self.label_device_model.setObjectName(u"label_device_model")

        self.gridLayout.addWidget(self.label_device_model, 0, 0, 1, 1)

        self.label_device_screen = QLabel(self.groupBox_4)
        self.label_device_screen.setObjectName(u"label_device_screen")

        self.gridLayout.addWidget(self.label_device_screen, 1, 0, 1, 1)

        self.label_device_screen_text = QLabel(self.groupBox_4)
        self.label_device_screen_text.setObjectName(u"label_device_screen_text")
        self.label_device_screen_text.setMaximumSize(QSize(120, 16777215))
        self.label_device_screen_text.setFont(font)

        self.gridLayout.addWidget(self.label_device_screen_text, 1, 1, 1, 1)

        self.label_device_model_text = QLabel(self.groupBox_4)
        self.label_device_model_text.setObjectName(u"label_device_model_text")
        self.label_device_model_text.setMaximumSize(QSize(120, 16777215))
        self.label_device_model_text.setFont(font)

        self.gridLayout.addWidget(self.label_device_model_text, 0, 1, 1, 1)

        self.label_Ollama_AIs = QLabel(self.groupBox_4)
        self.label_Ollama_AIs.setObjectName(u"label_Ollama_AIs")

        self.gridLayout.addWidget(self.label_Ollama_AIs, 2, 0, 1, 1)

        self.label_Ollama_AIs_text = QLabel(self.groupBox_4)
        self.label_Ollama_AIs_text.setObjectName(u"label_Ollama_AIs_text")
        self.label_Ollama_AIs_text.setMaximumSize(QSize(120, 16777215))
        self.label_Ollama_AIs_text.setFont(font)

        self.gridLayout.addWidget(self.label_Ollama_AIs_text, 2, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.line_2 = QFrame(self.system_info)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame{margin:15px;}")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.label_11 = QLabel(self.system_info)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(40, 0))
        self.label_11.setMaximumSize(QSize(40, 16777215))
        self.label_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_11.setStyleSheet(u"QLabel {background-color : #FFFFFF;}")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_11)


        self.verticalLayout_2.addWidget(self.system_info)

        self.content_stack.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QWidget { background-color: #d6e4f7; }\n"
"QWidget { \n"
"    color: #000000; \n"
"}\n"
"/* \u4f7f\u7528\u901a\u914d\u7b26\u6216\u786e\u4fdd\u6ca1\u6709 ID \u9650\u5236 */\n"
"QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"    margin-top: 20px;\n"
"	margin-left:15 px;\n"
"	margin-right:15px;\n"
"    padding: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_canvas = ClickableCanvas(self.page_1)
        self.label_canvas.setObjectName(u"label_canvas")
        self.label_canvas.setMinimumSize(QSize(1, 1))
        self.label_canvas.setMaximumSize(QSize(1, 1))
        self.label_canvas.setStyleSheet(u"QLabel{padding:0px;}")

        self.gridLayout_3.addWidget(self.label_canvas, 4, 1, 1, 1)

        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 250))
        self.groupBox.setMaximumSize(QSize(16777215, 250))
        self.groupBox.setStyleSheet(u"QPushButton{background-color:#FFFFFF;}\n"
"QGroupBox{padding:0px;\n"
"margin-buttom: 0px;}")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"    margin-top: 0px;\n"
"	margin-bottom:0px;\n"
"    padding: 0px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"QPushButton{\n"
"	margin:1px;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_refresh_config = QPushButton(self.groupBox_5)
        self.btn_refresh_config.setObjectName(u"btn_refresh_config")
        self.btn_refresh_config.setEnabled(True)
        self.btn_refresh_config.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.btn_refresh_config, 3, 1, 1, 1)

        self.combo_configs = QComboBox(self.groupBox_5)
        self.combo_configs.setObjectName(u"combo_configs")
        self.combo_configs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.combo_configs.setStyleSheet(u"/* 1. ComboBox \u672c\u4f53 */\n"
"QComboBox {\n"
"    border: 1px solid rgba(0, 0, 0, 185); \n"
"    border-radius: 8px;\n"
"    padding: 2px 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"/* 2. \u60ac\u505c\u548c\u6253\u5f00\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"QComboBox:hover {\n"
"    border: 1px solid #0078d7;\n"
"}\n"
"\n"
"QComboBox:on { /* \u5c55\u5f00\u65f6\u7684\u72b6\u6001 */\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"/* 1. \u4e0b\u62c9\u533a\u57df */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* 2. \u6838\u5fc3\uff1a\u753b\u4e00\u6761\u6a2a\u7ebf */\n"
"QComboBox::down-arrow {\n"
"    image: none; \n"
"    background-color: #666666; /* \u6a2a\u7ebf\u7684\u989c\u8272 */\n"
"    width: 10px;               /* \u6a2a\u7ebf\u7684\u957f\u5ea6 */\n"
""
                        "    height: 2px;               /* \u6a2a\u7ebf\u7684\u7c97\u7ec6 */\n"
"    \n"
"    /* \u8fd9\u91cc\u7684 margin \u53ef\u4ee5\u5fae\u8c03\u6a2a\u7ebf\u5728\u683c\u5b50\u91cc\u7684\u4f4d\u7f6e */\n"
"    margin-right: 10px; \n"
"}\n"
"\n"
"\n"
"/* 5. \u4e0b\u62c9\u51fa\u6765\u7684\u5217\u8868\u6846\u672c\u4f53 */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    selection-background-color: #0078d7; /* \u9009\u4e2d\u9879\u80cc\u666f */\n"
"    selection-color: #ffffff;            /* \u9009\u4e2d\u9879\u6587\u5b57 */\n"
"    outline: none;                       /* \u53bb\u6389\u865a\u7ebf\u6846 */\n"
"}\n"
"\n"
"/* 6. \u4e0b\u62c9\u5217\u8868\u91cc\u7684\u6bcf\u4e00\u9879 */\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 30px;\n"
"    padding-left: 10px;\n"
"}")

        self.gridLayout_4.addWidget(self.combo_configs, 0, 0, 1, 2)

        self.combo_ai_model = QComboBox(self.groupBox_5)
        self.combo_ai_model.setObjectName(u"combo_ai_model")
        self.combo_ai_model.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.combo_ai_model.setStyleSheet(u"/* 1. ComboBox \u672c\u4f53 */\n"
"QComboBox {\n"
"    border: 1px solid rgba(0, 0, 0, 185); \n"
"    border-radius: 8px;\n"
"    padding: 2px 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"/* 2. \u60ac\u505c\u548c\u6253\u5f00\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"QComboBox:hover {\n"
"    border: 1px solid #0078d7;\n"
"}\n"
"\n"
"QComboBox:on { /* \u5c55\u5f00\u65f6\u7684\u72b6\u6001 */\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* 2. \u6838\u5fc3\uff1a\u753b\u4e00\u6761\u6a2a\u7ebf */\n"
"QComboBox::down-arrow {\n"
"    image: none; \n"
"    background-color: #666666; /* \u6a2a\u7ebf\u7684\u989c\u8272 */\n"
"    width: 10px;               /* \u6a2a\u7ebf\u7684\u957f\u5ea6 */\n"
"    height: 2px;               /* \u6a2a"
                        "\u7ebf\u7684\u7c97\u7ec6 */\n"
"    \n"
"    /* \u8fd9\u91cc\u7684 margin \u53ef\u4ee5\u5fae\u8c03\u6a2a\u7ebf\u5728\u683c\u5b50\u91cc\u7684\u4f4d\u7f6e */\n"
"    margin-right: 10px; \n"
"}\n"
"\n"
"\n"
"/* 5. \u4e0b\u62c9\u51fa\u6765\u7684\u5217\u8868\u6846\u672c\u4f53 */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    selection-background-color: #0078d7; /* \u9009\u4e2d\u9879\u80cc\u666f */\n"
"    selection-color: #ffffff;            /* \u9009\u4e2d\u9879\u6587\u5b57 */\n"
"    outline: none;                       /* \u53bb\u6389\u865a\u7ebf\u6846 */\n"
"}\n"
"\n"
"/* 6. \u4e0b\u62c9\u5217\u8868\u91cc\u7684\u6bcf\u4e00\u9879 */\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 30px;\n"
"    padding-left: 10px;\n"
"}")

        self.gridLayout_4.addWidget(self.combo_ai_model, 2, 0, 1, 2)

        self.btn_load_config = QPushButton(self.groupBox_5)
        self.btn_load_config.setObjectName(u"btn_load_config")
        self.btn_load_config.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.btn_load_config, 4, 0, 1, 1)

        self.btn_create_config = QPushButton(self.groupBox_5)
        self.btn_create_config.setObjectName(u"btn_create_config")
        self.btn_create_config.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.btn_create_config, 3, 0, 1, 1)

        self.btn_delete_config = QPushButton(self.groupBox_5)
        self.btn_delete_config.setObjectName(u"btn_delete_config")
        self.btn_delete_config.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.btn_delete_config, 4, 1, 1, 1)

        self.btn_save_config = QPushButton(self.groupBox_5)
        self.btn_save_config.setObjectName(u"btn_save_config")
        self.btn_save_config.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.btn_save_config, 5, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"QFrame{margin:15px;}")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(40, 0))
        self.label_13.setMaximumSize(QSize(41, 16777215))
        self.label_13.setStyleSheet(u"QLabel {\n"
"    /* 1. \u80cc\u666f\u4e0e\u5706\u89d2 */\n"
"    background-color: #ffffff;    /* \u7eaf\u767d\u80cc\u666f */\n"
"    border-radius: 6px;           /* \u7a0d\u5fae\u5e26\u4e00\u70b9\u5706\u89d2\uff0c\u914d\u5408\u6574\u4f53\u98ce\u683c */\n"
"    \n"
"    /* 2. \u6587\u5b57\u6837\u5f0f */\n"
"    color: #000000;               /* \u6587\u5b57\u9ed1\u8272 */\n"
"    font-size: 12pt;              /* \u5b57\u53f7 12 (\u6ce8\u610f\u5355\u4f4d\u662f pt \u6216 px) */\n"
"    font-weight: bold;            /* \u7c97\u4f53 */\n"
"    \n"
"    /* 3. \u5c45\u4e2d\u5bf9\u9f50 (\u6837\u5f0f\u8868\u5199\u6cd5) */\n"
"    qproperty-alignment: 'AlignHCenter | AlignVCenter';\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_13)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 2, 2)

        self.groupBox_6 = QGroupBox(self.page_1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QLabel{background-color:#FFFFFF;}\n"
"QGroupBox{padding:0px;\n"
"	margin: 15px;\n"
"	margin-top: 10px;}\n"
"QLineEdit{background-color:#FFFFFF;\n"
"		border:none;}")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_3 = QGroupBox(self.groupBox_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"    margin-top: 5px;\n"
"	margin-bottom:0px;\n"
"    padding: 0px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 14)
        self.edit_d_x1 = QLineEdit(self.groupBox_3)
        self.edit_d_x1.setObjectName(u"edit_d_x1")
        self.edit_d_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_d_x1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_d_x1, 5, 3, 1, 1)

        self.edit_b_x2 = QLineEdit(self.groupBox_3)
        self.edit_b_x2.setObjectName(u"edit_b_x2")
        self.edit_b_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_b_x2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_b_x2, 3, 1, 1, 1)

        self.edit_c_x1 = QLineEdit(self.groupBox_3)
        self.edit_c_x1.setObjectName(u"edit_c_x1")
        self.edit_c_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_c_x1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_c_x1, 4, 3, 1, 1)

        self.edit_topic_x2 = QLineEdit(self.groupBox_3)
        self.edit_topic_x2.setObjectName(u"edit_topic_x2")
        self.edit_topic_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_topic_x2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_topic_x2, 1, 1, 1, 1)

        self.edit_c_y2 = QLineEdit(self.groupBox_3)
        self.edit_c_y2.setObjectName(u"edit_c_y2")
        self.edit_c_y2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_c_y2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_c_y2, 4, 0, 1, 1)

        self.edit_d_y2 = QLineEdit(self.groupBox_3)
        self.edit_d_y2.setObjectName(u"edit_d_y2")
        self.edit_d_y2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_d_y2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_d_y2, 5, 0, 1, 1)

        self.edit_topic_y2 = QLineEdit(self.groupBox_3)
        self.edit_topic_y2.setObjectName(u"edit_topic_y2")
        self.edit_topic_y2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_topic_y2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_topic_y2, 1, 0, 1, 1)

        self.edit_d_x2 = QLineEdit(self.groupBox_3)
        self.edit_d_x2.setObjectName(u"edit_d_x2")
        self.edit_d_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_d_x2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_d_x2, 5, 1, 1, 1)

        self.edit_c_y1 = QLineEdit(self.groupBox_3)
        self.edit_c_y1.setObjectName(u"edit_c_y1")
        self.edit_c_y1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_c_y1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_c_y1, 4, 2, 1, 1)

        self.edit_c_x2 = QLineEdit(self.groupBox_3)
        self.edit_c_x2.setObjectName(u"edit_c_x2")
        self.edit_c_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_c_x2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_c_x2, 4, 1, 1, 1)

        self.edit_topic_y1 = QLineEdit(self.groupBox_3)
        self.edit_topic_y1.setObjectName(u"edit_topic_y1")
        self.edit_topic_y1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_topic_y1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_topic_y1, 1, 2, 1, 1)

        self.edit_b_x1 = QLineEdit(self.groupBox_3)
        self.edit_b_x1.setObjectName(u"edit_b_x1")
        self.edit_b_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_b_x1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_b_x1, 3, 3, 1, 1)

        self.edit_a_x2 = QLineEdit(self.groupBox_3)
        self.edit_a_x2.setObjectName(u"edit_a_x2")
        self.edit_a_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_a_x2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_a_x2, 2, 1, 1, 1)

        self.edit_b_y2 = QLineEdit(self.groupBox_3)
        self.edit_b_y2.setObjectName(u"edit_b_y2")
        self.edit_b_y2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_b_y2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_b_y2, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 2, 4, 1, 1)

        self.edit_d_y1 = QLineEdit(self.groupBox_3)
        self.edit_d_y1.setObjectName(u"edit_d_y1")
        self.edit_d_y1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_d_y1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_d_y1, 5, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)

        self.edit_a_y2 = QLineEdit(self.groupBox_3)
        self.edit_a_y2.setObjectName(u"edit_a_y2")
        self.edit_a_y2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_a_y2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_a_y2, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 1, 4, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(120, 16777215))
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_4, 4, 4, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(120, 16777215))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_5, 5, 4, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 3, 4, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.edit_a_y1 = QLineEdit(self.groupBox_3)
        self.edit_a_y1.setObjectName(u"edit_a_y1")
        self.edit_a_y1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_a_y1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_a_y1, 2, 2, 1, 1)

        self.edit_b_y1 = QLineEdit(self.groupBox_3)
        self.edit_b_y1.setObjectName(u"edit_b_y1")
        self.edit_b_y1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_b_y1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_b_y1, 3, 2, 1, 1)

        self.edit_a_x1 = QLineEdit(self.groupBox_3)
        self.edit_a_x1.setObjectName(u"edit_a_x1")
        self.edit_a_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_a_x1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_a_x1, 2, 3, 1, 1)

        self.edit_topic_x1 = QLineEdit(self.groupBox_3)
        self.edit_topic_x1.setObjectName(u"edit_topic_x1")
        self.edit_topic_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_topic_x1.setReadOnly(True)

        self.gridLayout_5.addWidget(self.edit_topic_x1, 1, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_15, 6, 4, 1, 1)

        self.label_ai = ClickableCanvas(self.groupBox_3)
        self.label_ai.setObjectName(u"label_ai")
        self.label_ai.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_ai, 6, 0, 1, 4)


        self.horizontalLayout_5.addWidget(self.groupBox_3)

        self.line_4 = QFrame(self.groupBox_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"QFrame{margin:15px;}")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_4)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(40, 0))
        self.label_14.setMaximumSize(QSize(41, 16777215))
        self.label_14.setStyleSheet(u"QLabel {\n"
"    /* 1. \u80cc\u666f\u4e0e\u5706\u89d2 */\n"
"    background-color: #ffffff;    /* \u7eaf\u767d\u80cc\u666f */\n"
"    border-radius: 6px;           /* \u7a0d\u5fae\u5e26\u4e00\u70b9\u5706\u89d2\uff0c\u914d\u5408\u6574\u4f53\u98ce\u683c */\n"
"    \n"
"    /* 2. \u6587\u5b57\u6837\u5f0f */\n"
"    color: #000000;               /* \u6587\u5b57\u9ed1\u8272 */\n"
"    font-size: 12pt;              /* \u5b57\u53f7 12 (\u6ce8\u610f\u5355\u4f4d\u662f pt \u6216 px) */\n"
"    font-weight: bold;            /* \u7c97\u4f53 */\n"
"    \n"
"    /* 3. \u5c45\u4e2d\u5bf9\u9f50 (\u6837\u5f0f\u8868\u5199\u6cd5) */\n"
"    qproperty-alignment: 'AlignHCenter | AlignVCenter';\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_3.addWidget(self.groupBox_6, 3, 1, 1, 1)

        self.content_stack.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget { background-color: #d6e4f7; }\n"
"QWidget { \n"
"    color: #000000; \n"
"}\n"
"/* \u4f7f\u7528\u901a\u914d\u7b26\u6216\u786e\u4fdd\u6ca1\u6709 ID \u9650\u5236 */\n"
"QGroupBox {\n"
"    border: 0px solid #a0b0c5;\n"
"    border-radius: 12px;\n"
"    margin-top: 20px;\n"
"	margin-left:15 px;\n"
"	margin-right:15px;\n"
"    padding: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QPushButton{background-color:#FFFFFF;\n"
"	margin-left :10px;\n"
"	margin-right:10px;\n"
"	margin-top:20px;}\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btn_start_task = QPushButton(self.page_2)
        self.btn_start_task.setObjectName(u"btn_start_task")
        self.btn_start_task.setMinimumSize(QSize(0, 60))

        self.gridLayout_6.addWidget(self.btn_start_task, 0, 1, 1, 1)

        self.btn_stop_task = QPushButton(self.page_2)
        self.btn_stop_task.setObjectName(u"btn_stop_task")
        self.btn_stop_task.setMinimumSize(QSize(0, 60))

        self.gridLayout_6.addWidget(self.btn_stop_task, 0, 0, 1, 1)

        self.text_log_output = QTextEdit(self.page_2)
        self.text_log_output.setObjectName(u"text_log_output")
        self.text_log_output.setStyleSheet(u"QTextEdit{background-color:#FFFFFF;\n"
"	margin-left:10px;\n"
"	margin-right:10px;\n"
"	margin-top:10px;\n"
"	margin-bottom:20px;\n"
"	padding:10px;\n"
"	border: 1px solid rgba(0, 0, 0, 125); \n"
"    border-radius: 20px;}")
        self.text_log_output.setReadOnly(True)

        self.gridLayout_6.addWidget(self.text_log_output, 1, 0, 1, 2)

        self.content_stack.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.content_stack, 0, 0, 4, 1)

        self.GGB = QGroupBox(self.centralwidget)
        self.GGB.setObjectName(u"GGB")
        self.GGB.setMinimumSize(QSize(130, 0))
        self.GGB.setMaximumSize(QSize(200, 16777215))
        self.GGB.setStyleSheet(u"QGroupBox{background-color:#116fcd;\n"
"	margin:0px;\n"
"	padding:0px;\n"
"	border:0px;\n"
"}\n"
"")
        self.GGB.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GGB.setFlat(False)
        self.GGB.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.GGB)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_avatar = QLabel(self.GGB)
        self.label_avatar.setObjectName(u"label_avatar")
        self.label_avatar.setMinimumSize(QSize(64, 64))
        self.label_avatar.setMaximumSize(QSize(64, 64))
        self.label_avatar.setStyleSheet(u"QLabel{background-color: transparent;}")
        self.label_avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_avatar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_10 = QLabel(self.GGB)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel{color:rgb(247, 150, 153);\n"
"	font: 700 16pt \"Microsoft YaHei UI\";background-color:transparent;\n"
"margin-top:10px;}")

        self.verticalLayout_3.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.line_5 = QFrame(self.GGB)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"QFrame{margin:6px;}")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.nav_list = QListWidget(self.GGB)
        QListWidgetItem(self.nav_list)
        QListWidgetItem(self.nav_list)
        QListWidgetItem(self.nav_list)
        self.nav_list.setObjectName(u"nav_list")
        self.nav_list.setMinimumSize(QSize(100, 0))
        self.nav_list.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.nav_list.setFont(font1)
        self.nav_list.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.nav_list.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.nav_list.setAutoFillBackground(False)
        self.nav_list.setStyleSheet(u"/* 1. \u5217\u8868\u6574\u4f53\u5bb9\u5668 */\n"
"QListWidget {\n"
"    background-color: rgba(255,255,255,0); /* \u80cc\u666f\u900f\u660e\uff0c\u7531\u7236\u7ea7 GroupBox \u51b3\u5b9a\n"
" */\n"
"	border-radius:8px;\n"
"	font-weight: bold;\n"
"    border: none;                  /* \u53bb\u6389\u5916\u8fb9\u6846 */\n"
"    outline: none;                 /* \u53bb\u6389\u70b9\u51fb\u65f6\u7684\u865a\u7ebf\u6846 */\n"
"    padding: 10px 5px;             /* \u4e0a\u4e0b\u7559\u70b9\u547c\u5438\u7a7a\u95f4 */\n"
"}\n"
"\n"
"/* 2. \u6bcf\u4e00\u4e2a\u5bfc\u822a\u9009\u9879\uff08\u672a\u9009\u4e2d\u72b6\u6001\uff09 */\n"
"QListWidget::item {\n"
"    background-color: transparent;\n"
"    color: #FFFFFF;                /* \u6df1\u7070\u8272\u6587\u5b57 */\n"
"    border-radius: 6px;            /* \u5706\u89d2\u77e9\u5f62 */\n"
"    margin-bottom: 8px;            /* \u6bcf\u4e2a\u6309\u94ae\u4e4b\u95f4\u7684\u7eb5\u5411\u95f4\u8ddd */\n"
"    padding-top:10px;\n"
"	padding-bottom:10px;\n"
"	padding-left:8px;\n"
"	padd"
                        "ing-right:8px;\n"
"    border: 1px solid transparent; /* \u9884\u7559\u8fb9\u6846\u4f4d\u7f6e\u9632\u6b62\u95ea\u70c1 */\n"
"}\n"
"\n"
"/* 3. \u9f20\u6807\u60ac\u505c\uff08\u672a\u9009\u4e2d\u65f6\uff09 */\n"
"QListWidget::item:hover {\n"
"    background-color: rgba(0, 0, 0, 0.06); /* \u6781\u6d45\u7684\u7070\u8272\u906e\u7f69 */\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* 4. \u9009\u4e2d\u72b6\u6001\uff08\u91cd\u70b9\uff09 */\n"
"QListWidget::item:selected {\n"
"    background-color: #cbdcf7;     /* PCL \u7ecf\u5178\u7684\u84dd\u8272\uff08\u6216\u8005\u4f60\u559c\u6b22\u7684\u5f3a\u8c03\u8272\uff09 */\n"
"    color: #000000;                /* \u9009\u4e2d\u540e\u6587\u5b57\u53d8\u767d */\n"
"    font-weight: bold;             /* \u9009\u4e2d\u540e\u52a0\u7c97 */\n"
"}\n"
"\n"
"/* 5. \u9009\u4e2d\u4e14\u9f20\u6807\u60ac\u505c */\n"
"QListWidget::item:selected:hover {\n"
"    background-color: #a5c5f7;     /* \u989c\u8272\u7a0d\u5fae\u6df1\u4e00\u70b9\u70b9 */\n"
"}")
        self.nav_list.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.nav_list.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.nav_list.setMovement(QListView.Movement.Static)
        self.nav_list.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout_3.addWidget(self.nav_list, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_6 = QFrame(self.GGB)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"QFrame{margin:6px;}")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.btn_github = QPushButton(self.GGB)
        self.btn_github.setObjectName(u"btn_github")
        self.btn_github.setMinimumSize(QSize(100, 40))
        self.btn_github.setMaximumSize(QSize(100, 16777215))
        self.btn_github.setStyleSheet(u"QPushButton{margin-top:5px;\n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color:#000000;}")

        self.verticalLayout_3.addWidget(self.btn_github, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_blog = QPushButton(self.GGB)
        self.btn_blog.setObjectName(u"btn_blog")
        self.btn_blog.setMinimumSize(QSize(100, 50))
        self.btn_blog.setStyleSheet(u"QPushButton{margin-bottom:10px;\n"
"	margin-top:5px;font: 700 10pt \"Microsoft YaHei UI\";\n"
"color:#000000;}")

        self.verticalLayout_3.addWidget(self.btn_blog, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_2.addWidget(self.GGB, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.content_stack.setCurrentIndex(1)
        self.nav_list.setCurrentRow(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_env_check.setTitle("")
        self.groupBox_2.setTitle("")
        self.label_adb_status.setText(QCoreApplication.translate("MainWindow", u"ADB\u72b6\u6001: \u7b49\u5f85\u68c0\u6d4b", None))
        self.label_ollama_status.setText(QCoreApplication.translate("MainWindow", u"Ollama \u72b6\u6001: \u7b49\u5f85\u68c0\u6d4b", None))
        self.btn_check_env.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u68c0\u67e5\u73af\u5883", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7cfb</p><p>\u7edf</p><p>\u73af</p><p>\u5883</p></body></html>", None))
        self.system_info.setTitle("")
        self.groupBox_4.setTitle("")
        self.label_device_model.setText("")
        self.label_device_screen.setText("")
        self.label_device_screen_text.setText(QCoreApplication.translate("MainWindow", u"\u5c4f\u5e55\u5206\u8fa8\u7387", None))
        self.label_device_model_text.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u578b\u53f7", None))
        self.label_Ollama_AIs.setText("")
        self.label_Ollama_AIs_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ollama AI</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u914d</span></p><p><span style=\" font-size:12pt; font-weight:700;\">\u7f6e</span></p><p><span style=\" font-size:12pt; font-weight:700;\">\u4fe1</span></p><p><span style=\" font-size:12pt; font-weight:700;\">\u606f</span></p></body></html>", None))
        self.label_canvas.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox.setTitle("")
        self.groupBox_5.setTitle("")
        self.btn_refresh_config.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8\u5750\u6807\u914d\u7f6e", None))
        self.btn_load_config.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u914d\u7f6e", None))
        self.btn_create_config.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u914d\u7f6e", None))
        self.btn_delete_config.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u914d\u7f6e", None))
        self.btn_save_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u914d</p><p>\u7f6e</p><p>\u7f16</p><p>\u8f91</p></body></html>", None))
        self.groupBox_6.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"y1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9898\u76ee", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"x2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"y2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524dAI", None))
        self.label_ai.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5f53</p><p>\u524d</p><p>\u914d</p><p>\u7f6e</p></body></html>", None))
        self.btn_start_task.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.btn_stop_task.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u8fd0\u884c", None))
        self.GGB.setTitle("")
        self.label_avatar.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0kouhj", None))

        __sortingEnabled = self.nav_list.isSortingEnabled()
        self.nav_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.nav_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u68c0\u67e5", None))
        ___qlistwidgetitem1 = self.nav_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807\u6807\u5b9a", None))
        ___qlistwidgetitem2 = self.nav_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.nav_list.setSortingEnabled(__sortingEnabled)

        self.btn_github.setText(QCoreApplication.translate("MainWindow", u"\U0001f4e6Github", None))
        self.btn_blog.setText(QCoreApplication.translate("MainWindow", u"\U0001f4ddBlog", None))
    # retranslateUi

