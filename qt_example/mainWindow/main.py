#!/usr/bin/python
# -*- coding: UTF-8 -*-

from dis import dis
import platform #確認系統類型
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QDialog
from PySide2 import QtCore
from PySide2.QtCore import Qt, QTimer
from PySide2.QtUiTools import QUiLoader
from command import Command
from set_magnification import InputDialog
from angle_data import angleData
import serial
import os

#系統類型確認
os_name = platform.system()
if os_name== 'Windows':
    uartport = 'COM1' #測試用連接阜
    path = './main.ui'
else:
    uartport = '/dev/tty'  #測試用連接阜
    path = "/home/pi/motor_control/qt_example/mainWindow/main.ui"

com = Command()
data = angleData()
keylist = list(data)
# export DISPLAY=':0.0' 利用該指令遠端ssh開啟gui程式
class Stats(QMainWindow):
    def __init__(self):
        #初始化UI
        super().__init__()
        self.ui =QUiLoader().load(path)
        self.ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) #使其無邊框
        self.ui.resize(800,480)
        self.ui.move(0,0)
        self.ui.stop.clicked.connect(self.stop)
        self.ui.shutdown.clicked.connect(self.shutdown)
        self.ui.set.clicked.connect(self.set)
        self.ui.backhome.clicked.connect(self.backhome)
        self.ui.add.clicked.connect(self.add)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.clean.clicked.connect(self.clean)
        self.ui.textBrowser.setText("歡迎使用雷射衰減程式\n")
        self.magnification = keylist[0]
        self.key = keylist
        self.key_num = 0
        self.data = data
        #顯示ui視窗
        self.ui.show()
        #初始化計時器
        self.timer = QTimer()
        #初始化序列阜
        self.ser = serial.Serial(uartport,9600,timeout=1)
        for i in com.scan():
            self.ser.write(bytes(i,encoding='ASCII'))
        #初始化馬達
        self.backhome()

    def stop(self):
        self.timer.singleShot(300,lambda:self.ser.write(bytes(com.stop(1),encoding='ASCII')))
        self.timer.singleShot(600,lambda:self.ser.write(bytes(com.stop(2),encoding='ASCII')))
        self.timer.singleShot(900,lambda:self.ser.write(bytes(com.stop(3),encoding='ASCII')))
        self.ui.textBrowser.setText("中止馬達運作")
        
    def backhome(self):
        self.ui.textBrowser.setText("執行回原點作業\n")
        
        self.timer.singleShot(300,lambda:self.ser.write(bytes(com.home(1),encoding='ASCII')))
        self.timer.singleShot(300,lambda:self.ui.textBrowser.setText("馬達1回原點\n"))
        self.timer.singleShot(600,lambda:self.ser.write(bytes(com.home(2),encoding='ASCII')))
        self.timer.singleShot(600,lambda:self.ui.textBrowser.append("馬達2回原點\n"))
        self.timer.singleShot(900,lambda:self.ser.write(bytes(com.home(3),encoding='ASCII')))
        self.timer.singleShot(900,lambda:self.ui.textBrowser.append("馬達3回原點\n"))
        self.timer.singleShot(2000,lambda:self.display(self.magnification))
            
    def clean(self):
        cleantime = 30000
        self.ui.textBrowser.setText("馬達清潔指令，預計30秒後結束")
        self.timer.singleShot(1000,lambda:self.ser.write(bytes(com.clean(1),encoding='ASCII')))
        self.timer.singleShot(2000,lambda:self.ser.write(bytes(com.clean(2),encoding='ASCII')))
        self.timer.singleShot(3000,lambda:self.ser.write(bytes(com.clean(3),encoding='ASCII')))
        self.timer.singleShot(cleantime,lambda:self.ser.write(bytes(com.stop(1),encoding='ASCII')))
        self.timer.singleShot(cleantime+1000,lambda:self.ser.write(bytes(com.stop(2),encoding='ASCII')))
        self.timer.singleShot(cleantime+2000,lambda:self.ser.write(bytes(com.stop(3),encoding='ASCII')))
        self.timer.singleShot(cleantime,lambda:self.ui.textBrowser.setText("馬達已完成清潔"))
    def sub(self):
        if self.key_num == 0:
            self.key_num = 0
        else :
            self.key_num -= 1
            self.magnification = self.key[self.key_num]
            angleData = self.data[str(self.magnification)]
            self.display(self.magnification)
            self.move(angleData)
    def add(self):
        if self.key_num >= len(self.key)-1:
            self.key_num = len(self.key)-1
        else :
            self.key_num += 1
            self.magnification = self.key[self.key_num]
            angleData = self.data[str(self.magnification)]
            self.display(self.magnification)
            self.move(angleData)
        
    def display(self,magnification):
        self.timer.singleShot(100,lambda:self.ui.textBrowser.setText(f"目前倍率{magnification}"))
    def move(self,angleData):
        self.timer.singleShot(100,lambda:self.ser.write(bytes(com.ma(1,angleData[0]),encoding='ASCII')))
        self.timer.singleShot(200,lambda:self.ser.write(bytes(com.ma(2,angleData[1]),encoding='ASCII')))
        self.timer.singleShot(300,lambda:self.ser.write(bytes(com.ma(3,angleData[2]),encoding='ASCII')))

    @QtCore.Slot()
    def set(self):
        dialog = InputDialog.getValue(self)
        self.setValue = dialog
        tmp = str(self.setValue)+'x'
        self.display(tmp)
        self.move(data[tmp])
        self.key_num = keylist.index(tmp)
    def shutdown(self):
        qm = QMessageBox.question(self.ui,"您確定要關機","確定嗎？",QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes)
        if qm == QMessageBox.Yes:
            self.stop()
            self.timer.singleShot(300,lambda:self.ui.textBrowser.setText("已關閉序列阜，正在關機"))
            self.timer.singleShot(1000,lambda:app.quit())
            os.system('cd /home/pi/motor_control/')
            os.system('git pull')
            os.system("sudo poweroff")
        else:
            self.ui.textBrowser.setText("未完成關機")

app = QApplication([])
window = Stats()
app.exec_()
