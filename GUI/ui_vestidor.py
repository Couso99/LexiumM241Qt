# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 755)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 720))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 2px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("/* LINE EDIT */\n"
"QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(0, 0, 200);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(0, 0, 200);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(85, 170, 255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_toggle = QtWidgets.QFrame(self.frame_top)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_toggle_menu = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_toggle_menu.setText("")
        self.btn_toggle_menu.setObjectName("btn_toggle_menu")
        self.verticalLayout_3.addWidget(self.btn_toggle_menu)
        self.horizontalLayout_3.addWidget(self.frame_toggle)
        self.frame_top_right = QtWidgets.QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_minimize.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_5.addWidget(self.btn_minimize)
        self.btn_maximize_restore = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize_restore.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_close.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_5.addWidget(self.btn_close)
        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_top_btns)
        self.frame_top_info = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_top_info_1 = QtWidgets.QLabel(self.frame_top_info)
        self.label_top_info_1.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.label_top_info_1.setText("")
        self.label_top_info_1.setObjectName("label_top_info_1")
        self.horizontalLayout_8.addWidget(self.label_top_info_1)
        self.label_top_info_2 = QtWidgets.QLabel(self.frame_top_info)
        self.label_top_info_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QtCore.QSize(250, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_top_info_2.setObjectName("label_top_info_2")
        self.horizontalLayout_8.addWidget(self.label_top_info_2)
        self.verticalLayout_2.addWidget(self.frame_top_info)
        self.horizontalLayout_3.addWidget(self.frame_top_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.frame_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menus.setObjectName("frame_menus")
        self.layout_menus = QtWidgets.QVBoxLayout(self.frame_menus)
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName("layout_menus")
        self.verticalLayout_5.addWidget(self.frame_menus, 0, QtCore.Qt.AlignTop)
        self.frame_extra_menus = QtWidgets.QFrame(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy)
        self.frame_extra_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extra_menus.setObjectName("frame_extra_menus")
        self.layout_menu_bottom = QtWidgets.QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName("layout_menu_bottom")
        self.label_user_icon = QtWidgets.QLabel(self.frame_extra_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy)
        self.label_user_icon.setMinimumSize(QtCore.QSize(60, 60))
        self.label_user_icon.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_user_icon.setFont(font)
        self.label_user_icon.setStyleSheet("QLabel {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(44, 49, 60);\n"
"    border: 5px solid rgb(39, 44, 54);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_icon.setObjectName("label_user_icon")
        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_content_right = QtWidgets.QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QtWidgets.QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_new_user = QtWidgets.QWidget()
        self.page_new_user.setObjectName("page_new_user")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_new_user)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.page_new_user)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(245,245,245);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.frame_10 = QtWidgets.QFrame(self.page_new_user)
        self.frame_10.setStyleSheet("QFrame {\n"
"    background-color: rgb(245,245,245);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.userAddedFrame = QtWidgets.QFrame(self.frame_10)
        self.userAddedFrame.setMaximumSize(QtCore.QSize(280, 90))
        self.userAddedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userAddedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userAddedFrame.setObjectName("userAddedFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.userAddedFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.positionTextLabel = QtWidgets.QLabel(self.userAddedFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.positionTextLabel.setFont(font)
        self.positionTextLabel.setStyleSheet("color:rgb(0,0,0);")
        self.positionTextLabel.setObjectName("positionTextLabel")
        self.gridLayout_3.addWidget(self.positionTextLabel, 1, 0, 1, 1)
        self.personIDTextLabel = QtWidgets.QLabel(self.userAddedFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.personIDTextLabel.setFont(font)
        self.personIDTextLabel.setStyleSheet("color:rgb(0,0,0);")
        self.personIDTextLabel.setObjectName("personIDTextLabel")
        self.gridLayout_3.addWidget(self.personIDTextLabel, 0, 0, 1, 1)
        self.newPersonIDLabel = QtWidgets.QLabel(self.userAddedFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newPersonIDLabel.setFont(font)
        self.newPersonIDLabel.setStyleSheet("color:rgb(0,0,0);")
        self.newPersonIDLabel.setObjectName("newPersonIDLabel")
        self.gridLayout_3.addWidget(self.newPersonIDLabel, 0, 1, 1, 1)
        self.newPositionLabel = QtWidgets.QLabel(self.userAddedFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newPositionLabel.setFont(font)
        self.newPositionLabel.setStyleSheet("color:rgb(0,0,0);")
        self.newPositionLabel.setObjectName("newPositionLabel")
        self.gridLayout_3.addWidget(self.newPositionLabel, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.userAddedFrame, 0, 2, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setMaximumSize(QtCore.QSize(250, 90))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.formLayout = QtWidgets.QFormLayout(self.frame_13)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(-1, 10, -1, 12)
        self.formLayout.setObjectName("formLayout")
        self.frame_11 = QtWidgets.QFrame(self.frame_13)
        self.frame_11.setMinimumSize(QtCore.QSize(75, 16))
        self.frame_11.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.frame_11.setFont(font)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setGeometry(QtCore.QRect(60, 0, 16, 16))
        self.label_3.setStyleSheet("color: rgb(255,0,0);\n"
"background:transparent;")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame_11)
        self.label.setGeometry(QtCore.QRect(0, 0, 81, 16))
        self.label.setMinimumSize(QtCore.QSize(80, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0,0,0);")
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_3.raise_()
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_11)
        self.nameLineEdit = QtWidgets.QLineEdit(self.frame_13)
        self.nameLineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.nameLineEdit.setStyleSheet("color:rgb(0,0,0);")
        self.nameLineEdit.setText("")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.frame_12 = QtWidgets.QFrame(self.frame_13)
        self.frame_12.setMinimumSize(QtCore.QSize(75, 16))
        self.frame_12.setMaximumSize(QtCore.QSize(75, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        self.label_4.setGeometry(QtCore.QRect(60, 0, 16, 16))
        self.label_4.setStyleSheet("color: rgb(255,0,0);\n"
"background:transparent;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_12)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 80, 16))
        self.label_5.setMinimumSize(QtCore.QSize(80, 16))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(0,0,0);")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label_4.raise_()
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.frame_12)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.frame_13)
        self.lastNameLineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lastNameLineEdit.setStyleSheet("color:rgb(0,0,0);")
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.gridLayout_5.addWidget(self.frame_13, 0, 0, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.frame_10)
        self.frame_16.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.assignPositionRadioButton = QtWidgets.QRadioButton(self.frame_16)
        self.assignPositionRadioButton.setGeometry(QtCore.QRect(10, 10, 143, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.assignPositionRadioButton.setFont(font)
        self.assignPositionRadioButton.setStyleSheet("color:rgb(0,0,0);\n"
"")
        self.assignPositionRadioButton.setChecked(False)
        self.assignPositionRadioButton.setObjectName("assignPositionRadioButton")
        self.gridLayout_5.addWidget(self.frame_16, 3, 0, 1, 1)
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        self.frame_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.addUserButton = QtWidgets.QPushButton(self.frame_15)
        self.addUserButton.setMinimumSize(QtCore.QSize(60, 25))
        self.addUserButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"")
        self.addUserButton.setObjectName("addUserButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.addUserButton)
        self.deleteNewUserButton = QtWidgets.QPushButton(self.frame_15)
        self.deleteNewUserButton.setMinimumSize(QtCore.QSize(60, 25))
        self.deleteNewUserButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.deleteNewUserButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(39, 44, 54);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.deleteNewUserButton.setObjectName("deleteNewUserButton")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.deleteNewUserButton)
        self.gridLayout_5.addWidget(self.frame_15, 0, 1, 1, 1)
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        self.frame_14.setMinimumSize(QtCore.QSize(400, 150))
        self.frame_14.setMaximumSize(QtCore.QSize(400, 150))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_17 = QtWidgets.QFrame(self.frame_14)
        self.frame_17.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_8 = QtWidgets.QLabel(self.frame_17)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 150, 19))
        self.label_8.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(0,0,0);")
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.frame_17)
        self.label_14.setGeometry(QtCore.QRect(136, 0, 20, 20))
        self.label_14.setStyleSheet("color: rgb(255,0,0);\n"
"background:transparent;")
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.frame_17, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(0,0,0);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(0,0,0);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.correoLineEdit = QtWidgets.QLineEdit(self.frame_14)
        self.correoLineEdit.setStyleSheet("color:rgb(0,0,0);")
        self.correoLineEdit.setObjectName("correoLineEdit")
        self.gridLayout_2.addWidget(self.correoLineEdit, 1, 1, 1, 1)
        self.telefonoLineEdit = QtWidgets.QLineEdit(self.frame_14)
        self.telefonoLineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.telefonoLineEdit.setStyleSheet("color:rgb(0,0,0);")
        self.telefonoLineEdit.setObjectName("telefonoLineEdit")
        self.gridLayout_2.addWidget(self.telefonoLineEdit, 2, 1, 1, 1)
        self.direccionLineEdit = QtWidgets.QLineEdit(self.frame_14)
        self.direccionLineEdit.setStyleSheet("color:rgb(0,0,0);")
        self.direccionLineEdit.setObjectName("direccionLineEdit")
        self.gridLayout_2.addWidget(self.direccionLineEdit, 5, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_14, 1, 0, 1, 1)
        self.addUserOutcomeLabel = QtWidgets.QLabel(self.frame_10)
        self.addUserOutcomeLabel.setStyleSheet("color:rgb(0,0,0);")
        self.addUserOutcomeLabel.setText("")
        self.addUserOutcomeLabel.setObjectName("addUserOutcomeLabel")
        self.gridLayout_5.addWidget(self.addUserOutcomeLabel, 1, 1, 2, 2)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.widget = QtWidgets.QWidget(self.page_new_user)
        self.widget.setMinimumSize(QtCore.QSize(0, 180))
        self.widget.setObjectName("widget")
        self.verticalLayout_7.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_new_user)
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_home)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QFrame(self.page_home)
        self.frame.setMinimumSize(QtCore.QSize(0, 265))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 380))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lastMovementsTable = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastMovementsTable.sizePolicy().hasHeightForWidth())
        self.lastMovementsTable.setSizePolicy(sizePolicy)
        self.lastMovementsTable.setMinimumSize(QtCore.QSize(0, 260))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lastMovementsTable.setPalette(palette)
        self.lastMovementsTable.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.lastMovementsTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lastMovementsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lastMovementsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.lastMovementsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lastMovementsTable.setAlternatingRowColors(False)
        self.lastMovementsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lastMovementsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lastMovementsTable.setShowGrid(True)
        self.lastMovementsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.lastMovementsTable.setObjectName("lastMovementsTable")
        self.lastMovementsTable.setColumnCount(4)
        self.lastMovementsTable.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.lastMovementsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lastMovementsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lastMovementsTable.setItem(0, 3, item)
        self.lastMovementsTable.horizontalHeader().setVisible(False)
        self.lastMovementsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.lastMovementsTable.horizontalHeader().setDefaultSectionSize(200)
        self.lastMovementsTable.horizontalHeader().setStretchLastSection(True)
        self.lastMovementsTable.verticalHeader().setVisible(False)
        self.lastMovementsTable.verticalHeader().setCascadingSectionResizes(False)
        self.lastMovementsTable.verticalHeader().setHighlightSections(False)
        self.lastMovementsTable.verticalHeader().setStretchLastSection(True)
        self.gridLayout_8.addWidget(self.lastMovementsTable, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_home)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(245,245,245);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)
        self.controlStackedWidget = QtWidgets.QStackedWidget(self.page_home)
        self.controlStackedWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.controlStackedWidget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.controlStackedWidget.setStyleSheet("QFrame {\n"
"    background-color: rgb(245,245,245);\n"
"    border-radius: 10px;\n"
"}")
        self.controlStackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controlStackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controlStackedWidget.setObjectName("controlStackedWidget")
        self.page_pythonControl = QtWidgets.QWidget()
        self.page_pythonControl.setObjectName("page_pythonControl")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_pythonControl)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_8 = QtWidgets.QFrame(self.page_pythonControl)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 140))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setContentsMargins(0, 4, 0, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_6 = QtWidgets.QFrame(self.frame_8)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_6.setMaximumSize(QtCore.QSize(170, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.tickOrCrossLabel = QtWidgets.QLabel(self.frame_6)
        self.tickOrCrossLabel.setMinimumSize(QtCore.QSize(25, 25))
        self.tickOrCrossLabel.setText("")
        self.tickOrCrossLabel.setObjectName("tickOrCrossLabel")
        self.gridLayout.addWidget(self.tickOrCrossLabel, 1, 1, 1, 1)
        self.personIdLineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.personIdLineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.personIdLineEdit.setMaximumSize(QtCore.QSize(107, 16777215))
        self.personIdLineEdit.setStyleSheet("\n"
"color:rgb(0,0,0);")
        self.personIdLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.personIdLineEdit.setObjectName("personIdLineEdit")
        self.gridLayout.addWidget(self.personIdLineEdit, 1, 0, 1, 1)
        self.greetingLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.greetingLabel.setFont(font)
        self.greetingLabel.setStyleSheet("color: rgb(98, 114, 164);")
        self.greetingLabel.setText("")
        self.greetingLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.greetingLabel.setObjectName("greetingLabel")
        self.gridLayout.addWidget(self.greetingLabel, 3, 0, 1, 2)
        self.personIdLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.personIdLabel.setFont(font)
        self.personIdLabel.setStyleSheet("color: rgb(0,0,0);")
        self.personIdLabel.setObjectName("personIdLabel")
        self.gridLayout.addWidget(self.personIdLabel, 0, 0, 1, 1)
        self.goToPositionButton = QtWidgets.QPushButton(self.frame_6)
        self.goToPositionButton.setEnabled(False)
        self.goToPositionButton.setMinimumSize(QtCore.QSize(0, 20))
        self.goToPositionButton.setMaximumSize(QtCore.QSize(107, 16777215))
        self.goToPositionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goToPositionButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.goToPositionButton.setObjectName("goToPositionButton")
        self.gridLayout.addWidget(self.goToPositionButton, 2, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.unioviLabel = QtWidgets.QLabel(self.frame_9)
        self.unioviLabel.setMinimumSize(QtCore.QSize(94, 73))
        self.unioviLabel.setMaximumSize(QtCore.QSize(94, 73))
        self.unioviLabel.setStyleSheet("background-image: url(:/logos/icons/logos/uniovi.png);")
        self.unioviLabel.setText("")
        self.unioviLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.unioviLabel.setObjectName("unioviLabel")
        self.gridLayout_4.addWidget(self.unioviLabel, 1, 2, 1, 1)
        self.noPositionLabel = QtWidgets.QLabel(self.frame_9)
        self.noPositionLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.noPositionLabel.setMaximumSize(QtCore.QSize(200, 50))
        self.noPositionLabel.setStyleSheet("color: rgb(0,0,0);")
        self.noPositionLabel.setObjectName("noPositionLabel")
        self.gridLayout_4.addWidget(self.noPositionLabel, 1, 0, 1, 1)
        self.EPIGijonLabel = QtWidgets.QLabel(self.frame_9)
        self.EPIGijonLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.EPIGijonLabel.setFont(font)
        self.EPIGijonLabel.setStyleSheet("color: rgb(98, 103, 111);")
        self.EPIGijonLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EPIGijonLabel.setObjectName("EPIGijonLabel")
        self.gridLayout_4.addWidget(self.EPIGijonLabel, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.horizontalLayout_13.addWidget(self.frame_9)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.page_pythonControl)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.progressBar = QtWidgets.QProgressBar(self.frame_5)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(27, 29, 35);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(57,255,20, 255), stop:1 rgba(11,218,81, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_9.addWidget(self.progressBar)
        self.positionLabel = QtWidgets.QLabel(self.frame_5)
        self.positionLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.positionLabel.setStyleSheet("color: rgb(0,0,0);\n"
"")
        self.positionLabel.setText("")
        self.positionLabel.setObjectName("positionLabel")
        self.horizontalLayout_9.addWidget(self.positionLabel)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.controlStackedWidget.addWidget(self.page_pythonControl)
        self.page_localControl = QtWidgets.QWidget()
        self.page_localControl.setObjectName("page_localControl")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.page_localControl)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_28 = QtWidgets.QFrame(self.page_localControl)
        self.frame_28.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.formLayout_7 = QtWidgets.QFormLayout(self.frame_28)
        self.formLayout_7.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_7.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_7.setObjectName("formLayout_7")
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setStyleSheet("QFrame#frame_29 {\n"
"    background-color: rgb(245,245,245);\n"
"    color: rgb(0,0,0);\n"
"    border-width: 2;\n"
"    border-radius: 3; \n"
"    border-style: solid; \n"
"    border-color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_24 = QtWidgets.QLabel(self.frame_29)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:rgb(0,0,0);")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_11.addWidget(self.label_24)
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_29)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_7.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_25 = QtWidgets.QLabel(self.frame_28)
        self.label_25.setMinimumSize(QtCore.QSize(50, 50))
        self.label_25.setStyleSheet("QLabel{background-image: url(:/24x24/icons/24x24/cil-wifi-signal-off.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"border: none;\n"
"background-color: rgb(0,0,0);}")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_25)
        self.label_20 = QtWidgets.QLabel(self.frame_28)
        font = QtGui.QFont()
        font.setFamily(".Al Bayan PUA")
        font.setPointSize(22)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(0);")
        self.label_20.setObjectName("label_20")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_20)
        self.horizontalLayout_11.addWidget(self.frame_28)
        self.frame_24 = QtWidgets.QFrame(self.page_localControl)
        self.frame_24.setMinimumSize(QtCore.QSize(170, 160))
        self.frame_24.setMaximumSize(QtCore.QSize(170, 160))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.EPIGijonLabel_2 = QtWidgets.QLabel(self.frame_24)
        self.EPIGijonLabel_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.EPIGijonLabel_2.setFont(font)
        self.EPIGijonLabel_2.setStyleSheet("color: rgb(98, 103, 111);")
        self.EPIGijonLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EPIGijonLabel_2.setObjectName("EPIGijonLabel_2")
        self.gridLayout_14.addWidget(self.EPIGijonLabel_2, 0, 0, 1, 1)
        self.unioviLabel_2 = QtWidgets.QLabel(self.frame_24)
        self.unioviLabel_2.setMinimumSize(QtCore.QSize(94, 73))
        self.unioviLabel_2.setMaximumSize(QtCore.QSize(94, 73))
        self.unioviLabel_2.setStyleSheet("background-image: url(:/logos/icons/logos/uniovi.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;")
        self.unioviLabel_2.setText("")
        self.unioviLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.unioviLabel_2.setObjectName("unioviLabel_2")
        self.gridLayout_14.addWidget(self.unioviLabel_2, 1, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.frame_24)
        self.controlStackedWidget.addWidget(self.page_localControl)
        self.page_stopped = QtWidgets.QWidget()
        self.page_stopped.setObjectName("page_stopped")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.page_stopped)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.frame_25 = QtWidgets.QFrame(self.page_stopped)
        self.frame_25.setMaximumSize(QtCore.QSize(170, 160))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_25)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.unioviLabel_3 = QtWidgets.QLabel(self.frame_25)
        self.unioviLabel_3.setMinimumSize(QtCore.QSize(94, 73))
        self.unioviLabel_3.setMaximumSize(QtCore.QSize(94, 73))
        self.unioviLabel_3.setStyleSheet("background-image: url(:/logos/icons/logos/uniovi.png);")
        self.unioviLabel_3.setText("")
        self.unioviLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.unioviLabel_3.setObjectName("unioviLabel_3")
        self.gridLayout_15.addWidget(self.unioviLabel_3, 1, 0, 1, 1)
        self.EPIGijonLabel_3 = QtWidgets.QLabel(self.frame_25)
        self.EPIGijonLabel_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.EPIGijonLabel_3.setFont(font)
        self.EPIGijonLabel_3.setStyleSheet("color: rgb(98, 103, 111);")
        self.EPIGijonLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EPIGijonLabel_3.setObjectName("EPIGijonLabel_3")
        self.gridLayout_15.addWidget(self.EPIGijonLabel_3, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.frame_25, 0, 1, 2, 1)
        self.frame_26 = QtWidgets.QFrame(self.page_stopped)
        self.frame_26.setStyleSheet("QFrame {\n"
"    background-color: rgb(200,0,0);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.frame_27 = QtWidgets.QFrame(self.frame_26)
        self.frame_27.setGeometry(QtCore.QRect(10, 10, 221, 73))
        self.frame_27.setStyleSheet("QFrame {\n"
"    background-color: rgb(245,245,245);\n"
"    color: rgb(0,0,0);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_21 = QtWidgets.QLabel(self.frame_27)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_6.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.frame_27)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_6.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame_26)
        self.label_23.setGeometry(QtCore.QRect(20, 120, 631, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_16.addWidget(self.frame_26, 0, 0, 2, 1)
        self.controlStackedWidget.addWidget(self.page_stopped)
        self.gridLayout_7.addWidget(self.controlStackedWidget, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_home)
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.page_login)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(245,245,245);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.frame_4 = QtWidgets.QFrame(self.page_login)
        self.frame_4.setStyleSheet("QFrame {\n"
"    background-color: rgb(245,245,245);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.loginMailLabel = QtWidgets.QLabel(self.frame_2)
        self.loginMailLabel.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginMailLabel.setFont(font)
        self.loginMailLabel.setStyleSheet("color:rgb(0,0,0);")
        self.loginMailLabel.setObjectName("loginMailLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.loginMailLabel)
        self.loginMailLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.loginMailLineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.loginMailLineEdit.setStyleSheet("color:rgb(0,0,0);")
        self.loginMailLineEdit.setText("")
        self.loginMailLineEdit.setObjectName("loginMailLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginMailLineEdit)
        self.loginPassLabel = QtWidgets.QLabel(self.frame_2)
        self.loginPassLabel.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginPassLabel.setFont(font)
        self.loginPassLabel.setStyleSheet("color:rgb(0,0,0);")
        self.loginPassLabel.setObjectName("loginPassLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.loginPassLabel)
        self.loginPassLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.loginPassLineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.loginPassLineEdit.setStyleSheet("color:rgb(0,0,0);")
        self.loginPassLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.loginPassLineEdit.setText("")
        self.loginPassLineEdit.setObjectName("loginPassLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.loginPassLineEdit)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_2)
        self.loginButton = QtWidgets.QPushButton(self.frame_4)
        self.loginButton.setMinimumSize(QtCore.QSize(80, 20))
        self.loginButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.loginButton)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.widget_3 = QtWidgets.QWidget(self.page_login)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 180))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_10.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.page_login)
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setObjectName("page_settings")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_settings)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_2 = QtWidgets.QWidget(self.page_settings)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 180))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_6.addWidget(self.widget_2, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_settings)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(245,245,245);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.page_settings)
        self.frame_7.setStyleSheet("QFrame#frame_7 {\n"
"    background-color: rgb(245,245,245);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.frame_23 = QtWidgets.QFrame(self.frame_7)
        self.frame_23.setMinimumSize(QtCore.QSize(400, 80))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.formLayout_6 = QtWidgets.QFormLayout(self.frame_23)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_6.setObjectName("formLayout_6")
        self.resetLXMButton = QtWidgets.QPushButton(self.frame_23)
        self.resetLXMButton.setMinimumSize(QtCore.QSize(113, 30))
        self.resetLXMButton.setStyleSheet("")
        self.resetLXMButton.setObjectName("resetLXMButton")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.resetLXMButton)
        self.doHomeButton = QtWidgets.QPushButton(self.frame_23)
        self.doHomeButton.setMinimumSize(QtCore.QSize(152, 30))
        self.doHomeButton.setStyleSheet("")
        self.doHomeButton.setObjectName("doHomeButton")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.doHomeButton)
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_23)
        self.frame_21 = QtWidgets.QFrame(self.frame_7)
        self.frame_21.setMinimumSize(QtCore.QSize(400, 130))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setMinimumSize(QtCore.QSize(280, 30))
        self.frame_22.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame_22.setFont(font)
        self.frame_22.setStyleSheet("QFrame#frame_22{border-width: 2;border-radius: 3; border-style: solid; border-color: rgb(45,45,45);border-radius: 10px;}")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_22.setLineWidth(1)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.assignNewVelocity = QtWidgets.QPushButton(self.frame_22)
        self.assignNewVelocity.setMinimumSize(QtCore.QSize(80, 25))
        self.assignNewVelocity.setMaximumSize(QtCore.QSize(160, 16777215))
        self.assignNewVelocity.setStyleSheet("QPushButton {\n"
"color: rgb(220, 220, 220);\n"
"background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.assignNewVelocity.setObjectName("assignNewVelocity")
        self.gridLayout_12.addWidget(self.assignNewVelocity, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:rgb(0,0,0);")
        self.label_17.setObjectName("label_17")
        self.gridLayout_12.addWidget(self.label_17, 0, 0, 1, 1)
        self.outputVelocityLabel = QtWidgets.QLabel(self.frame_22)
        self.outputVelocityLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.outputVelocityLabel.setStyleSheet("color:rgb(0,0,0);")
        self.outputVelocityLabel.setText("")
        self.outputVelocityLabel.setObjectName("outputVelocityLabel")
        self.gridLayout_12.addWidget(self.outputVelocityLabel, 2, 0, 1, 1)
        self.newVelocitySpinBox = QtWidgets.QSpinBox(self.frame_22)
        self.newVelocitySpinBox.setStyleSheet("color:rgb(0,0,0);")
        self.newVelocitySpinBox.setMinimum(100)
        self.newVelocitySpinBox.setMaximum(500)
        self.newVelocitySpinBox.setProperty("value", 200)
        self.newVelocitySpinBox.setObjectName("newVelocitySpinBox")
        self.gridLayout_12.addWidget(self.newVelocitySpinBox, 0, 1, 1, 1)
        self.gridLayout_13.addWidget(self.frame_22, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_21)
        self.label_19.setStyleSheet("color:rgb(0)")
        self.label_19.setObjectName("label_19")
        self.gridLayout_13.addWidget(self.label_19, 1, 1, 1, 1)
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_21)
        self.frame_18 = QtWidgets.QFrame(self.frame_7)
        self.frame_18.setMinimumSize(QtCore.QSize(300, 150))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.frame_3 = QtWidgets.QFrame(self.frame_18)
        self.frame_3.setGeometry(QtCore.QRect(10, 30, 280, 115))
        self.frame_3.setMinimumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("QFrame#frame_3{border-width: 2;border-radius: 3; border-style: solid; border-color: rgb(45,45,45);border-radius: 10px;}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(0,0,0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)
        self.newPassPersonID = QtWidgets.QLineEdit(self.frame_3)
        self.newPassPersonID.setStyleSheet("color:rgb(0,0,0);")
        self.newPassPersonID.setObjectName("newPassPersonID")
        self.gridLayout_9.addWidget(self.newPassPersonID, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(0,0,0);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 1, 0, 1, 1)
        self.newPassPassword = QtWidgets.QLineEdit(self.frame_3)
        self.newPassPassword.setStyleSheet("color:rgb(0,0,0);")
        self.newPassPassword.setObjectName("newPassPassword")
        self.gridLayout_9.addWidget(self.newPassPassword, 1, 1, 1, 1)
        self.registerNewPasswordButton = QtWidgets.QPushButton(self.frame_3)
        self.registerNewPasswordButton.setMinimumSize(QtCore.QSize(80, 25))
        self.registerNewPasswordButton.setStyleSheet("QPushButton {\n"
"color: rgb(220, 220, 220);\n"
"background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.registerNewPasswordButton.setObjectName("registerNewPasswordButton")
        self.gridLayout_9.addWidget(self.registerNewPasswordButton, 2, 1, 1, 1)
        self.outputLabelNewPassword = QtWidgets.QLabel(self.frame_3)
        self.outputLabelNewPassword.setStyleSheet("color:rgb(0,0,0);")
        self.outputLabelNewPassword.setText("")
        self.outputLabelNewPassword.setObjectName("outputLabelNewPassword")
        self.gridLayout_9.addWidget(self.outputLabelNewPassword, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_18)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.label_15.setStyleSheet("color:rgb(0)")
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_7)
        self.frame_19.setMinimumSize(QtCore.QSize(400, 130))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_18 = QtWidgets.QLabel(self.frame_19)
        self.label_18.setStyleSheet("color:rgb(0)")
        self.label_18.setObjectName("label_18")
        self.gridLayout_11.addWidget(self.label_18, 0, 0, 1, 1)
        self.frame_20 = QtWidgets.QFrame(self.frame_19)
        self.frame_20.setMinimumSize(QtCore.QSize(280, 30))
        self.frame_20.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame_20.setFont(font)
        self.frame_20.setStyleSheet("QFrame#frame_20{border-width: 2;border-radius: 3; border-style: solid; border-color: rgb(45,45,45);border-radius: 10px;}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_20.setLineWidth(1)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_16 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:rgb(0,0,0);")
        self.label_16.setObjectName("label_16")
        self.gridLayout_10.addWidget(self.label_16, 0, 0, 1, 1)
        self.outputPositionLabel = QtWidgets.QLabel(self.frame_20)
        self.outputPositionLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.outputPositionLabel.setStyleSheet("color:rgb(0,0,0);")
        self.outputPositionLabel.setText("")
        self.outputPositionLabel.setObjectName("outputPositionLabel")
        self.gridLayout_10.addWidget(self.outputPositionLabel, 1, 0, 1, 1)
        self.newPositionPersonID = QtWidgets.QLineEdit(self.frame_20)
        self.newPositionPersonID.setMaximumSize(QtCore.QSize(160, 16777215))
        self.newPositionPersonID.setStyleSheet("color:rgb(0,0,0);")
        self.newPositionPersonID.setObjectName("newPositionPersonID")
        self.gridLayout_10.addWidget(self.newPositionPersonID, 0, 1, 1, 1)
        self.assignNewPositionButton = QtWidgets.QPushButton(self.frame_20)
        self.assignNewPositionButton.setMinimumSize(QtCore.QSize(80, 25))
        self.assignNewPositionButton.setMaximumSize(QtCore.QSize(160, 16777215))
        self.assignNewPositionButton.setStyleSheet("QPushButton {\n"
"color: rgb(220, 220, 220);\n"
"background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.assignNewPositionButton.setObjectName("assignNewPositionButton")
        self.gridLayout_10.addWidget(self.assignNewPositionButton, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.frame_20, 1, 0, 1, 1)
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frame_19)
        self.gridLayout_6.addWidget(self.frame_7, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_settings)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.frame_grip = QtWidgets.QFrame(self.frame_content_right)
        self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_label_bottom = QtWidgets.QFrame(self.frame_grip)
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_credits_2 = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.label_credits_2.setFont(font)
        self.label_credits_2.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_credits_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_credits_2.setObjectName("label_credits_2")
        self.horizontalLayout_7.addWidget(self.label_credits_2)
        self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.frame_size_grip = QtWidgets.QFrame(self.frame_grip)
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
"    background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_6.addWidget(self.frame_size_grip)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.horizontalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.controlStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        MainWindow.setTabOrder(self.btn_maximize_restore, self.btn_close)
        MainWindow.setTabOrder(self.btn_close, self.btn_toggle_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Control de un <strong>vestidor<strong>"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label_top_info_2.setText(_translate("MainWindow", "| HOME"))
        self.label_user_icon.setText(_translate("MainWindow", "UO"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Nuevo<span style=\" font-weight:600;\"> usuario</span></p></body></html>"))
        self.positionTextLabel.setText(_translate("MainWindow", "Tu posición es:"))
        self.personIDTextLabel.setText(_translate("MainWindow", "Tu nuevo ID es:"))
        self.newPersonIDLabel.setText(_translate("MainWindow", "18"))
        self.newPositionLabel.setText(_translate("MainWindow", "800000"))
        self.label_3.setText(_translate("MainWindow", "*"))
        self.label.setText(_translate("MainWindow", "Nombre  :"))
        self.label_4.setText(_translate("MainWindow", "*"))
        self.label_5.setText(_translate("MainWindow", "Apellido  :"))
        self.assignPositionRadioButton.setText(_translate("MainWindow", "Asignar posición"))
        self.addUserButton.setText(_translate("MainWindow", "Añadir"))
        self.deleteNewUserButton.setText(_translate("MainWindow", "Borrar"))
        self.label_8.setText(_translate("MainWindow", "Correo electrónico  :"))
        self.label_14.setText(_translate("MainWindow", "*"))
        self.label_9.setText(_translate("MainWindow", "Teléfono móvil:"))
        self.label_10.setText(_translate("MainWindow", "Dirección:"))
        self.lastMovementsTable.setSortingEnabled(False)
        item = self.lastMovementsTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.lastMovementsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.lastMovementsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.lastMovementsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.lastMovementsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        __sortingEnabled = self.lastMovementsTable.isSortingEnabled()
        self.lastMovementsTable.setSortingEnabled(False)
        item = self.lastMovementsTable.item(0, 0)
        item.setText(_translate("MainWindow", "Persona ID"))
        item = self.lastMovementsTable.item(0, 1)
        item.setText(_translate("MainWindow", "Apellidos, Nombre"))
        item = self.lastMovementsTable.item(0, 2)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.lastMovementsTable.item(0, 3)
        item.setText(_translate("MainWindow", "Día"))
        self.lastMovementsTable.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Control del<span style=\" font-weight:600;\"> vestidor</span></p></body></html>"))
        self.personIdLabel.setText(_translate("MainWindow", "Persona <strong>ID<strong>:"))
        self.goToPositionButton.setText(_translate("MainWindow", "Ir a mi sección"))
        self.noPositionLabel.setText(_translate("MainWindow", "<html><head/><body><p>Parece que no hay ninguna</p><p>posición asocida con su ID.</p></body></html>"))
        self.EPIGijonLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">EPI </span>Gijón</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Control local</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "Está activado el control local.\n"
"Cambiar el control girando el interruptor \"Halt\"."))
        self.EPIGijonLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">EPI </span>Gijón</p></body></html>"))
        self.EPIGijonLabel_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">EPI </span>Gijón</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">STOP</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "Torque demasiado alto"))
        self.label_23.setText(_translate("MainWindow", "Verifique si algo está impidiendo el movimiento del vestidor,\n"
"retírelo con cuidado y desactive el error manualmente en el PLC "))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Acceder</span></p></body></html>"))
        self.loginMailLabel.setText(_translate("MainWindow", "Correo electrónico:"))
        self.loginPassLabel.setText(_translate("MainWindow", "Contraseña:"))
        self.loginButton.setText(_translate("MainWindow", "Log In"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Ajustes</span></p></body></html>"))
        self.resetLXMButton.setText(_translate("MainWindow", "Reset LXM"))
        self.doHomeButton.setText(_translate("MainWindow", "Establecer home LXM"))
        self.assignNewVelocity.setText(_translate("MainWindow", "Asignar velocidad"))
        self.label_17.setText(_translate("MainWindow", "Nueva velocidad:"))
        self.label_19.setText(_translate("MainWindow", "Asignar nueva velocidad de crucero"))
        self.label_2.setText(_translate("MainWindow", "Persona ID:"))
        self.label_13.setText(_translate("MainWindow", "Contraseña:"))
        self.registerNewPasswordButton.setText(_translate("MainWindow", "Registrar"))
        self.label_15.setText(_translate("MainWindow", "Autorizar nuevo usuario"))
        self.label_18.setText(_translate("MainWindow", "Asignar nueva posición"))
        self.label_16.setText(_translate("MainWindow", "Persona ID:"))
        self.assignNewPositionButton.setText(_translate("MainWindow", "Asignar posición nueva"))
        self.label_credits_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Created by</span>: Pablo Couso</p></body></html>"))
        self.label_version.setText(_translate("MainWindow", "v1.0.9"))

import GUI.resources.resources_file
