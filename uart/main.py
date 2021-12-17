import serial
import time
from command import Command

com = Command()

data = {
        '3x':[0,35.26,35.26],
        '5x':[0,50.77,50.77],
        '10x':[0,63.43,63.43],
        '15x':[0,68.58,68.58],
        '20x':[0,71.57,71.57],
        '22x':[0,52.91,112.91],
        '24x':[0,54.74,114.74],
        '26x':[0,56.31,116.31],
        '28x':[0,57.69,117.69],
        '30x':[0,58.91,118.91],
        '32x':[0,60,120],
        '34x':[0,60.98,120.98],
        '36x':[0,61.87,121.87],
        '38x':[0,62.69,122.69],
        '40x':[0,63.43,123.43],
        '42x':[0,64.12,124.76],
        '44x':[0,64.76,124.76],
        '46x':[0,65.35,125.35],
        '48x':[0,65.91,125.91],
        '50x':[0,66.42,126.42]
        }
keylist = list(data)

def confirm(magnification):
    print(f"目前倍率為{magnification}")
    p = keylist.index(magnification)
    try:
        x = input(f"請確認是否要衰減{keylist[p+1]}(繼續請按Enter，停止請輸入任意值)=\n")
        if x == '':
            return True
        else:
            return False
    except IndexError:
        print("已經到底了\n")
        return False


with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
    for i in com.scan():
        ser.write(bytes(i,encoding='ASCII'))
        time.sleep(0.5)
    #初始化
    ser.write(bytes(com.home(1),encoding='ASCII'))
    print("回原點")
    ser.write(bytes(com.home(1),encoding='ASCII')) 
    time.sleep(3)
    ser.write(bytes(com.home(2),encoding='ASCII')) 
    time.sleep(3)
    ser.write(bytes(com.home(3),encoding='ASCII')) 
    time.sleep(3)
    x = input("準備好了嗎？")
    if x == '':
        ser.write(bytes(com.mr(1,360),encoding='ASCII')) 
        time.sleep(3)

        ser.write(bytes(com.home(1),encoding='ASCII')) 
        time.sleep(3)
        for i in keylist:
            if confirm(i):
                print("===轉動馬達===")
                ser.write(bytes(com.ma(1,data[i][0]),encoding='ASCII')) 
                time.sleep(0.5)
                ser.write(bytes(com.ma(2,data[i][1]),encoding='ASCII')) 
                time.sleep(0.5)
                ser.write(bytes(com.ma(3,data[i][2]),encoding='ASCII')) 
                time.sleep(0.5)
            else:
                print("=========")
                print(f"衰減倍數為{i}")
                print("=========")
                break

    #關閉程序
    ser.write(bytes(com.stop(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
    ser.write(bytes(com.stop(2),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
    ser.write(bytes(com.stop(3),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
    ser.close()

print("結束程式")
