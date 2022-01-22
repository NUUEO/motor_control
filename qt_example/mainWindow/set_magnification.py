from PySide2.QtGui import Qt
from PySide2.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QMessageBox,
                               QSpinBox, QVBoxLayout)
from PySide2.QtUiTools import QUiLoader

class spinBoxInputDialog(QDialog):
    def __init__(self, parent=None, title='', label='', reg=''):
        super(spinBoxInputDialog, self).__init__(parent)
        self.ui =QUiLoader().load("form.ui")
        self.ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) #使其無邊框
        self.ui.move(300,129)
        self.ui.num_0.clicked.connect(self.num_0)
        self.ui.num_1.clicked.connect(self.num_1)
        self.ui.num_2.clicked.connect(self.num_2)
        self.ui.num_3.clicked.connect(self.num_3)
        self.ui.num_4.clicked.connect(self.num_4)
        self.ui.num_5.clicked.connect(self.num_5)
        self.ui.num_6.clicked.connect(self.num_6)
        self.ui.num_7.clicked.connect(self.num_7)
        self.ui.num_8.clicked.connect(self.num_8)
        self.ui.num_9.clicked.connect(self.num_9)
        self.ui.enter.clicked.connect(self.enter)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.display.setText("請輸入衰減倍率0~999")
        self.num_str = ''
        self.num = 0
        self.value = None
        self.ui.show()
    def num_0(self):
        self.num_str = self.num_str + '0'
        self.display()
    def num_1(self):
        self.num_str = self.num_str + '1'
        self.display()
    def num_2(self):
        self.num_str = self.num_str + '2'
        self.display()
    def num_3(self):
        self.num_str = self.num_str + '3'
        self.display()
    def num_4(self):
        self.num_str = self.num_str + '4'
        self.display()
    def num_5(self):
        self.num_str = self.num_str + '5'
        self.display()
    def num_6(self):
        self.num_str = self.num_str + '6'
        self.display()
    def num_7(self):
        self.num_str = self.num_str + '7'
        self.display()
    def num_8(self):
        self.num_str = self.num_str + '8'
        self.display()
    def num_9(self):
        self.num_str = self.num_str + '9'
        self.display()
    def clear(self):
        self.ui.display.setText('')
        self.num_str = ''
        self.display()
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
            if self.num > 999:
                self.num = 999
                self.num_str = '999'
            else:
                pass
        self.ui.display.setText(self.num_str)
    def enter(self):
        self.value = self.ui.display.text()
        self.ui.close()
        return self.value