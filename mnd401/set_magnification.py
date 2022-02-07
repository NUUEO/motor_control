from PySide2.QtGui import Qt
from PySide2.QtWidgets import QDialog
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore
from PySide2.QtCore import Qt
from dis import dis


class InputDialog(QDialog):
    def __init__(self, parent=None, title='', label='', reg='',maximum=99999,minimum=0):
        super(InputDialog, self).__init__(parent)
        self.sub_ui = QUiLoader().load('dialog.ui')
        self.setup_ui(title,label)
        self.maximum = maximum
        self.minimum = minimum
    @property
    def window(self):
        return self.sub_ui

    def setup_ui(self,title,label):
        #self.sub_ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) #使其無邊框
        self.sub_ui.setWindowTitle(title)
        self.sub_ui.move(300,129)
        self.sub_ui.num_0.clicked.connect(self.num_button)
        self.sub_ui.num_1.clicked.connect(self.num_button)
        self.sub_ui.num_2.clicked.connect(self.num_button)
        self.sub_ui.num_3.clicked.connect(self.num_button)
        self.sub_ui.num_4.clicked.connect(self.num_button)
        self.sub_ui.num_5.clicked.connect(self.num_button)
        self.sub_ui.num_6.clicked.connect(self.num_button)
        self.sub_ui.num_7.clicked.connect(self.num_button)
        self.sub_ui.num_8.clicked.connect(self.num_button)
        self.sub_ui.num_9.clicked.connect(self.num_button)
        self.sub_ui.enter.clicked.connect(self.enter)
        self.sub_ui.clear.clicked.connect(self.clear)
        self.sub_ui.display.setText(label)
        self.num_str = ''
        self.num = 0
        self.value = None

    def num_button(self):
        num = self.sender().text()
        self.num_str = self.num_str + num
        self.display()

    
    #功能按鍵
    def clear(self):
        self.sub_ui.display.setText('')
        self.num_str = ''
        self.display()
        
    @QtCore.Slot()
    def enter(self):
        try:
            self.value = int(self.sub_ui.display.text())
            if self.value < 3:
                self.value = 0
            else:
                pass
        except ValueError:
            self.value = 0
        self.sub_ui.close()

    #顯示功能與限制倍率
    def display(self):
        try:
            while self.num_str[0] == '0':
                self.num_str = self.num_str[1:]
        except IndexError:
            pass
        if self.num_str =='':
            self.num = 0
        else:
            self.num = int(self.num_str)
            if self.num > self.maximum:
                self.num = self.maximum
                self.num_str = str(self.maximum)
            else:
                pass
        self.sub_ui.display.setText(self.num_str)

    @classmethod
    def getValue(cls, parent, title='', label='', reg='[0-9]+$',maximum=9999,minimum=0):
        dialog = cls(parent, title, label, reg, maximum, minimum)
        dialog.window.exec_()
        return dialog.value
