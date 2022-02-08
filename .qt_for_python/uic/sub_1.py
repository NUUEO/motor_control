# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_1.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(800, 480)
        self.gridLayoutWidget = QWidget(dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 70, 361, 405))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_1 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.checkBox_1.setFont(font)

        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setFont(font)

        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setFont(font)

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setFont(font)

        self.gridLayout.addWidget(self.checkBox_5, 4, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setFont(font)

        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setFont(font)

        self.gridLayout.addWidget(self.checkBox_6, 0, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)
        self.checkBox_7.setFont(font)

        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)
        self.checkBox_8.setFont(font)

        self.gridLayout.addWidget(self.checkBox_8, 2, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)
        self.checkBox_9.setFont(font)

        self.gridLayout.addWidget(self.checkBox_9, 3, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy)
        self.checkBox_10.setFont(font)

        self.gridLayout.addWidget(self.checkBox_10, 4, 1, 1, 1)

        self.line = QFrame(dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 50, 771, 31))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 521, 41))
        self.label.setFont(font)
        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 20, 131, 41))
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(670, 20, 113, 37))
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Done = QPushButton(dialog)
        self.Done.setObjectName(u"Done")
        self.Done.setGeometry(QRect(400, 340, 141, 131))
        self.Done.setFont(font)
        self.Cancel = QPushButton(dialog)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setGeometry(QRect(650, 340, 141, 131))
        self.Cancel.setFont(font)
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 80, 381, 141))
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 30, 261, 31))
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u81e8\u754c\u500d\u7387\u6e2c\u8a66\u7a0b\u5f0f", None))
        self.checkBox_1.setText(QCoreApplication.translate("dialog", u"\u7b2c\u4e00\u6b21", None))
        self.checkBox_3.setText(QCoreApplication.translate("dialog", u"\u7b2c\u4e09\u6b21", None))
        self.checkBox_2.setText(QCoreApplication.translate("dialog", u"\u7b2c\u4e8c\u6b21", None))
        self.checkBox_5.setText(QCoreApplication.translate("dialog", u"\u7b2c\u4e94\u6b21", None))
        self.checkBox_4.setText(QCoreApplication.translate("dialog", u"\u7b2c\u56db\u6b21", None))
        self.checkBox_6.setText(QCoreApplication.translate("dialog", u"\u7b2c\u516d\u6b21", None))
        self.checkBox_7.setText(QCoreApplication.translate("dialog", u"\u7b2c\u4e03\u6b21", None))
        self.checkBox_8.setText(QCoreApplication.translate("dialog", u"\u7b2c\u516b\u6b21", None))
        self.checkBox_9.setText(QCoreApplication.translate("dialog", u"\u7b2c\u4e5d\u6b21", None))
        self.checkBox_10.setText(QCoreApplication.translate("dialog", u"\u7b2c\u5341\u6b21", None))
        self.label.setText(QCoreApplication.translate("dialog", u"\u81e8\u754c\u500d\u7387\u6e2c\u8a66", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"\u76ee\u524d\u500d\u7387\uff1a", None))
        self.lineEdit.setText(QCoreApplication.translate("dialog", u"0x", None))
        self.Done.setText(QCoreApplication.translate("dialog", u"\u5b8c\u6210", None))
        self.Cancel.setText(QCoreApplication.translate("dialog", u"\u53d6\u6d88\u6e2c\u8a66", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u8acb\u4f9d\u5e8f\u91cf\u6e2c\u8a72\u81e8\u754c\u500d\u7387\u4e0b\u3002\n"
"\u662f\u5426\u6709\u6e2c\u8a66\u6578\u64da\n"
"\u82e5\u6709\u8cc7\u6599\u8acb\u5728\u8a72\u6e2c\u9805\u52fe\u9078\u3002", None))
        self.label_4.setText(QCoreApplication.translate("dialog", u"\uff08\u672a\u52fe\u9078\u8996\u70ba\u7121\u6cd5\u91cf\u6e2c\uff09", None))
    # retranslateUi

