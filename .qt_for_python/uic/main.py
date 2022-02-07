# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        font = QFont()
        font.setFamilies([u"Noto Sans CJK TC"])
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(370, 190, 120, 100))
        self.Display = QTextBrowser(self.centralwidget)
        self.Display.setObjectName(u"Display")
        self.Display.setGeometry(QRect(370, 10, 420, 170))
        self.Theoretical_distance = QLineEdit(self.centralwidget)
        self.Theoretical_distance.setObjectName(u"Theoretical_distance")
        self.Theoretical_distance.setGeometry(QRect(230, 60, 120, 30))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 220, 30))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(350, 10, 20, 391))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Stop = QPushButton(self.centralwidget)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setGeometry(QRect(520, 190, 120, 100))
        self.Shutdown = QPushButton(self.centralwidget)
        self.Shutdown.setObjectName(u"Shutdown")
        self.Shutdown.setGeometry(QRect(670, 190, 120, 100))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 220, 30))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Measure_distance = QLineEdit(self.centralwidget)
        self.Measure_distance.setObjectName(u"Measure_distance")
        self.Measure_distance.setGeometry(QRect(230, 100, 120, 30))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 220, 30))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.select_wavelength = QSpinBox(self.centralwidget)
        self.select_wavelength.setObjectName(u"select_wavelength")
        self.select_wavelength.setGeometry(QRect(230, 140, 120, 38))
        self.Clean = QPushButton(self.centralwidget)
        self.Clean.setObjectName(u"Clean")
        self.Clean.setGeometry(QRect(370, 300, 120, 100))
        self.Backhome = QPushButton(self.centralwidget)
        self.Backhome.setObjectName(u"Backhome")
        self.Backhome.setGeometry(QRect(520, 300, 120, 100))
        self.Select = QPushButton(self.centralwidget)
        self.Select.setObjectName(u"Select")
        self.Select.setGeometry(QRect(670, 300, 120, 100))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 40, 341, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 220, 30))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 180, 341, 21))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(20, 200, 330, 200))
        self.picture.setPixmap(QPixmap(u"logo.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 40))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb\u91cf\u6e2c", None))
        self.Display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans CJK TC'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u89aa\u611b\u7684\u4f7f\u7528\u8005\uff0c\u60a8\u597d</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u6e2c\u8a66\u8ddd\u96e2(m)", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6b62\u99ac\u9054", None))
        self.Shutdown.setText(QCoreApplication.translate("MainWindow", u"\u95dc\u6a5f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5be6\u9a57\u91cf\u6e2c\u8ddd\u96e2(m)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6e2c\u8a66\u6ce2\u9577(nm)", None))
        self.select_wavelength.setSpecialValueText("")
        self.Clean.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u6f54", None))
        self.Backhome.setText(QCoreApplication.translate("MainWindow", u"\u56de\u539f\u9ede", None))
        self.Select.setText(QCoreApplication.translate("MainWindow", u"\u9078\u64c7\u500d\u7387", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53c3\u6578\u8a2d\u5b9a", None))
        self.picture.setText("")
    # retranslateUi

