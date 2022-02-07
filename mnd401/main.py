from dis import dis
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2 import QtCore
from PySide2.QtCore import Qt, QTimer
from PySide2.QtUiTools import QUiLoader
from command import Command
from set_magnification import InputDialog
from angle_data import angleData
import serial
import os

path = "./main.ui"
com = Command()
#uartport = "/dev/ttyUSB0"
uartport = "COM1"

class Stats(QMainWindow):
    def __init__(self):
        

        super().__init__()
        self.ui =QUiLoader().load(path)
        self.ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) #使其無邊框
        self.ui.resize(800,480)
        self.ui.move(0,0)
        
        self.ui.Stop.clicked.connect(self.stop)
        self.ui.Start.clicked.connect(self.start)
        self.ui.Shutdown.clicked.connect(self.shutdown)
        self.ui.Select.clicked.connect(self.select)
        self.ui.Backhome.clicked.connect(self.backhome)
        self.ui.Clean.clicked.connect(self.clean)

        self.ui.Display.setText("歡迎使用雷射衰減程式\n")
        self.ui.show()
        self.timer = QTimer()

        self.initialization_hardware()

        #內部參數設定
        self.uarttime = 1000 #Uart傳輸時間基數
        self.compensate_motor_2 = 105 #馬達二補償角度
        self.compensate_motor_3 = 100 #馬達三補償角度
        self.data = angleData() #取得衰減角度資料
        self.keylist = list(self.data) #將衰減角度鍵值轉為清單
        self.key_num = 0 #設定list數為0
        self.magnification = self.keylist[0] #將衰減倍率預設為零

# 硬體功能
    def initialization_hardware(self):
        #初始化序列阜
        self.ser = serial.Serial(uartport,9600,timeout=1)
        for i in com.scan():
            self.ser.write(bytes(i,encoding='ASCII'))

    def move(self,angleData):
        self.timer.singleShot(self.uarttime*1,lambda:self.ser.write(bytes(com.ma(2,angleData[1]+self.compensate_motor_2),encoding='ASCII')))
        self.timer.singleShot(self.uarttime*2,lambda:self.ser.write(bytes(com.ma(3,angleData[2]+self.compensate_motor_3),encoding='ASCII')))
        

# 功能鍵程式
    def stop(self):
        self.timer.singleShot(self.uarttime*0,lambda:self.ser.write(bytes(com.stop(2),encoding='ASCII')))
        self.timer.singleShot(self.uarttime*1,lambda:self.ser.write(bytes(com.stop(3),encoding='ASCII')))
        self.display(100,"中止馬達運作")

    def clean(self):
        cleantime = 30000
        self.display(100,"開始馬達清潔，預計30秒結束")
        self.timer.singleShot(self.uarttime*1,lambda:self.ser.write(bytes(com.clean(2),encoding='ASCII')))
        self.timer.singleShot(self.uarttime*2,lambda:self.ser.write(bytes(com.clean(3),encoding='ASCII')))
        self.timer.singleShot(cleantime+2000,lambda:self.ser.write(bytes(com.stop(2),encoding='ASCII')))
        self.timer.singleShot(cleantime+3000,lambda:self.ser.write(bytes(com.stop(3),encoding='ASCII')))
        self.display(cleantime+3000,"馬達已清潔完成")
        self.timer.singleShot(cleantime+4000,lambda:self.backhome())

    def shutdown(self):
        qm = QMessageBox.question(self.ui,"您確定要關機","確定嗎？",QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes)
        if qm == QMessageBox.Yes:
            self.stop()
            self.display(100,"正在關機...")
            self.timer.singleShot(1000,lambda:app.quit())

            '''
            os.system('cd /home/pi/motor_control/')
            os.system('git pull')
            os.system("sudo poweroff")
            '''
        else:
            self.display(100,"未完成關機")

    def backhome(self):
        self.display(100,"執行回原點作業")
        self.display(1000,"馬達1回原點")
        self.display(1100,"馬達2回原點",1)
        self.display(1200,"馬達3回原點",1)
        self.display(3000,"歡迎使用雷射測距程式")
        self.timer.singleShot(self.uarttime*1,lambda:self.ser.write(bytes(com.home(2),encoding='ASCII')))
        self.timer.singleShot(self.uarttime*2,lambda:self.ser.write(bytes(com.home(3),encoding='ASCII')))
        self.magnification = '0x'
        self.key_num = 0
        self.move(self.data[self.magnification])
        self.display(4000,f"目前倍率{self.magnification}",1)

    @QtCore.Slot()
    def start(self):
        dialog = InputDialog.getValue(self,"最大測程","請輸入最大量測距離",'',100000,0)
        self.setValue = dialog
        self.Theoretical_distance = str(self.setValue)
        dialog = InputDialog.getValue(self,"量測距離","請輸入實驗距離",'',10000,0)
        self.setValue = dialog
        self.Measure_distance = str(self.setValue)

    @QtCore.Slot()
    def select(self):
        dialog = InputDialog.getValue(self,"衰減倍率","請輸入衰減倍率")
        self.setValue = dialog
        tmp = str(self.setValue)+'x'
        self.display(100,"目前倍率"+tmp,0)
        self.key_num = self.keylist.index(tmp)
        self.move(self.data[tmp])
        

#螢幕視窗功能
    def display(self,time=100,message="",type=0):
        if type == 0:
            self.timer.singleShot(time,lambda:self.ui.Display.setText(message))
        elif type ==1:
            self.timer.singleShot(time,lambda:self.ui.Display.append(message))

app = QApplication([])
window = Stats()
app.exec_()