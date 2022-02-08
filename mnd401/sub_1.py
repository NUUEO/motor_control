from PySide2.QtGui import Qt
from PySide2.QtWidgets import QDialog
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore
from PySide2.QtCore import Qt
from dis import dis

class Final(QDialog):
    def __init__(self, parent=None, label=''):
        super(Final, self).__init__(parent)
        self.sub_ui = QUiLoader().load('/home/pi/motor_control/mnd401/sub_1.ui')
        self.setup_ui(label)
    @property
    def window(self):
        return self.sub_ui

    def setup_ui(self,label):
        self.sub_ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) #使其無邊框
        self.sub_ui.resize(800,480)
        self.sub_ui.move(0,0)
        #功能按鍵
        self.sub_ui.Done.clicked.connect(self.done)
        self.sub_ui.Cancel.clicked.connect(self.cancel)
        #顯示視窗
        self.sub_ui.lineEdit.setText(label)
        #核選方塊
        self.checkBox_list = [None]*10
        #內建參數
        self.num_str = ''
        self.num = 0
        self.value = None

    
    #功能按鍵
    def cancel(self):
        self.value = 0
        self.sub_ui.close()

        
    @QtCore.Slot()
    def done(self):
        x = 0
        #更新核選方塊布林值
        self.checkBox_list[0] = self.sub_ui.checkBox_1.isChecked()
        self.checkBox_list[1] = self.sub_ui.checkBox_2.isChecked()
        self.checkBox_list[2] = self.sub_ui.checkBox_3.isChecked()
        self.checkBox_list[3] = self.sub_ui.checkBox_4.isChecked()
        self.checkBox_list[4] = self.sub_ui.checkBox_5.isChecked()
        self.checkBox_list[5] = self.sub_ui.checkBox_6.isChecked()
        self.checkBox_list[6] = self.sub_ui.checkBox_7.isChecked()
        self.checkBox_list[7] = self.sub_ui.checkBox_8.isChecked()
        self.checkBox_list[8] = self.sub_ui.checkBox_9.isChecked()
        self.checkBox_list[9] = self.sub_ui.checkBox_10.isChecked()

        #計數布林值
        for i in self.checkBox_list:
            if i:
                x += 1
        if x >= 8:
            self.value = 1
            
        else:
            self.value = 2
        self.sub_ui.close()

  
    @classmethod
    def getValue(cls, parent, label=''):
        dialog = cls(parent, label)
        dialog.window.exec_()
        return dialog.value

