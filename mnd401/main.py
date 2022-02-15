from dis import dis
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide2 import QtCore
from PySide2.QtCore import Qt, QTimer, Signal 
from PySide2.QtUiTools import QUiLoader
from command import Command
from set_magnification import InputDialog
from sub_1 import Final
from angle_data import angleData
import serial
import os

path = "./main.ui"
com = Command()
uartport = "/dev/ttyUSB0"
#uartport = "COM10"
class MyLineEdit(QLineEdit):#修改QlineEdit的觸發信號
    clicked = Signal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            self.clicked.emit()
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

        #修改QLinetext的觸發屬性
        self.ui.Theoretical_distance = MyLineEdit(self.ui.Theoretical_distance)
        self.ui.Theoretical_distance.clicked.connect(self.set_Theoretical_distance)
        self.Theoretical_distance = 10000
        self.ui.Theoretical_distance.setText(str(self.Theoretical_distance)) 

        self.ui.Measure_distance = MyLineEdit(self.ui.Measure_distance)
        self.ui.Measure_distance.clicked.connect(self.set_Measure_distance)
        self.Measure_distance = 100
        self.ui.Measure_distance.setText(str(self.Measure_distance)) 
        #===========================================================#

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
    
    def sub(self):
        self.key_num = self.keylist.index(self.magnification)
        if self.key_num == 0:
            self.key_num = 1
        else :
            self.key_num -= 1
            self.magnification = self.keylist[self.key_num]
            angleData = self.data[str(self.magnification)]
            self.display(1000,f"目前倍率{self.magnification}")
            self.move(angleData)
    def add(self):
        self.key_num = self.keylist.index(self.magnification)
        if self.key_num >= len(self.keylist)-1:
            self.key_num = len(self.keylist)-1
        else :
            self.key_num += 1
            self.magnification = self.keylist[self.key_num]
            angleData = self.data[str(self.magnification)]
            self.display(1000,f"目前倍率{self.magnification}")
            self.move(angleData)

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

    def set_Theoretical_distance(self):
        dialog = InputDialog.getValue(self,"最大測程","請輸入最大量測距離",'',100000,0)
        self.setValue = dialog
        self.Theoretical_distance = str(self.setValue)
        self.ui.Theoretical_distance.setText(self.Theoretical_distance)

    def set_Measure_distance(self):
        dialog = InputDialog.getValue(self,"量測距離","請輸入實驗距離",'',10000,0)
        self.setValue = dialog
        self.Measure_distance = str(self.setValue)
        self.ui.Measure_distance.setText(self.Measure_distance)         

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
        qm = QMessageBox.question(self.ui,"確認輸入參數正確",f"理論距離：{int(int(self.Theoretical_distance)/1000)}公里\n量測距離：{self.Measure_distance}公尺\n測試波長：{self.ui.Select_wavelength.currentText()}",QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes)
        if qm == QMessageBox.Yes:
            if self.ui.Select_wavelength.currentText() == "1550nm":
                self.c = 0.731 
            elif self.ui.Select_wavelength.currentText() == "1064nm":
                self.c = 0.712
            elif self.ui.Select_wavelength.currentText() == "905nm":
                self.c = 0.692
            elif self.ui.Select_wavelength.currentText() == "808nm":
                self.c = 0.633
            else:
                self.c = 1
    
            self.display(100,"開始量測")
            self.recommend_magnification = int(round(int(self.Theoretical_distance)/int(self.Measure_distance)/1,0))#視情況要不要除以波長倍率self.c
            self.magnification = str(self.recommend_magnification)+'x'
            self.display(200,f"建議倍率為{self.magnification}",1)
            self.display(300,f"正在調整倍率...",1)
            self.move(self.data[self.magnification])#轉動馬達到指定倍率
            self.display(4000,f"目前倍率{self.magnification}",1)
            self.timer.singleShot(4100,lambda:self.limit())
        else:
            self.display(100,"請確認參數")

    def limit(self):
        q1 = QMessageBox.question(self.ui,"請確認可否量測",f"目前倍率{self.magnification}",QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes)
        if q1 == QMessageBox.Yes:
            self.display(100,"增加倍率")
            self.timer.singleShot(1000,lambda:self.add())
            self.timer.singleShot(1500,lambda:self.limit_add())
        else:
            self.display(100,"減少倍率")
            self.timer.singleShot(1000,lambda:self.sub())
            self.timer.singleShot(1500,lambda:self.limit_sub())

    def limit_add(self):
        while True:
            q_add = QMessageBox.question(self.ui,"請確認可否量測","請稍後馬達增加倍率",QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes)
            if q_add == QMessageBox.Yes:
                self.timer.singleShot(1000,lambda:self.add())
            else:
                break
        self.display(100,f"臨界倍率為{self.keylist[self.key_num-1]}")
        self.magnification = self.keylist[self.key_num-1]
        self.move(self.data[self.magnification])
        self.timer.singleShot(1000,lambda:self.final_test())
    def limit_sub(self):
        while True:
            q_sub = QMessageBox.question(self.ui,"請確認可否量測","請稍後馬達減少倍率",QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes)
            if q_sub == QMessageBox.No:
                self.timer.singleShot(1000,lambda:self.sub())
            else:
                break
        self.display(100,f"臨界倍率為{self.keylist[self.key_num]}")
        self.timer.singleShot(1000,lambda:self.final_test())

    def final_test(self):
        dialog = Final.getValue(self,self.magnification)
        if dialog == 0:
            self.display(100,"使用者取消")
            self.display(200,"請重新開始",1)
            self.backhome()
        elif dialog == 1:
            self.display(100,"通過臨界倍率測試")
            temp = int(round(self.recommend_magnification/self.c,0)) #對應波長下應該的衰減倍率
            tm = int(self.magnification.replace('x','')) #實際倍率
            distance = round(tm*self.c*int(self.Measure_distance)/1000,1)
            if tm >= temp:
                self.display(200,f"通過測試，最大測程大於標示距離：{int(int(self.Theoretical_distance)/1000)}公里")
                self.display(300,f"推算數據測程可達{distance}公里",1)
            else:
                self.display(200,f"該雷射測距儀未通過測試，未達{int(int(self.Theoretical_distance)/1000)}公里")
                self.display(300,f"推算數據測程僅達{distance}公里",1)
        else:
            self.display(100,"未通過測試，請重新開始")
            self.backhome()


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


