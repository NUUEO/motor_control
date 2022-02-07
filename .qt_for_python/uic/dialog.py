# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(210, 220)
        self.clear = QPushButton(Dialog)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(10, 180, 60, 30))
        self.num_4 = QPushButton(Dialog)
        self.num_4.setObjectName(u"num_4")
        self.num_4.setGeometry(QRect(10, 100, 60, 30))
        self.num_2 = QPushButton(Dialog)
        self.num_2.setObjectName(u"num_2")
        self.num_2.setGeometry(QRect(75, 60, 60, 30))
        self.enter = QPushButton(Dialog)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(140, 180, 60, 30))
        self.num_1 = QPushButton(Dialog)
        self.num_1.setObjectName(u"num_1")
        self.num_1.setGeometry(QRect(10, 60, 60, 30))
        self.num_9 = QPushButton(Dialog)
        self.num_9.setObjectName(u"num_9")
        self.num_9.setGeometry(QRect(140, 140, 60, 30))
        self.display = QLineEdit(Dialog)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(10, 10, 190, 40))
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.num_0 = QPushButton(Dialog)
        self.num_0.setObjectName(u"num_0")
        self.num_0.setGeometry(QRect(75, 180, 60, 30))
        self.num_7 = QPushButton(Dialog)
        self.num_7.setObjectName(u"num_7")
        self.num_7.setGeometry(QRect(10, 140, 60, 30))
        self.num_8 = QPushButton(Dialog)
        self.num_8.setObjectName(u"num_8")
        self.num_8.setGeometry(QRect(75, 140, 60, 30))
        self.num_3 = QPushButton(Dialog)
        self.num_3.setObjectName(u"num_3")
        self.num_3.setGeometry(QRect(140, 60, 60, 30))
        self.num_6 = QPushButton(Dialog)
        self.num_6.setObjectName(u"num_6")
        self.num_6.setGeometry(QRect(140, 100, 60, 30))
        self.num_5 = QPushButton(Dialog)
        self.num_5.setObjectName(u"num_5")
        self.num_5.setGeometry(QRect(75, 100, 60, 30))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.clear.setText(QCoreApplication.translate("Dialog", u"C", None))
        self.num_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.num_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.enter.setText(QCoreApplication.translate("Dialog", u"\u2714", None))
        self.num_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.num_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.num_0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.num_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.num_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.num_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.num_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.num_5.setText(QCoreApplication.translate("Dialog", u"5", None))
    # retranslateUi

