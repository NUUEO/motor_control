from PySide2.QtGui import Qt
from PySide2.QtWidgets import QDialog
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore
from PySide2.QtCore import Qt
from dis import dis

class Final(QDialog):
    def __init__(self, parent=None, label=''):
        super(Final, self).__init__(parent)
        self.sub_ui = QUiLoader().load('sub_1.ui')
        self.setup_ui(label)
    @property
    def window(self):
        return self.sub_ui

    def setup_ui(self,label):
        self.sub_ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) #使其無邊框
        self.sub_ui.resize(800,480)
        self.sub_ui.move(0,0)
        
        self.sub_ui.Done.clicked.connect(self.done)
        self.sub_ui.Cancel.clicked.connect(self.cancel)
        
        self.sub_ui.lineEdit.setText(label)
        self.num_str = ''
        self.num = 0
        self.value = None

    
    #功能按鍵
    def cancel(self):
        self.value = 0
        self.sub_ui.close()

        
    @QtCore.Slot()
    def done(self):
        self.value = 1
        self.sub_ui.close()

  
    @classmethod
    def getValue(cls, parent, label=''):
        dialog = cls(parent, label)
        dialog.window.exec_()
        return dialog.value
