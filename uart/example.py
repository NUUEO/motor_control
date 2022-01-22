import serial
import time
from command import Command

com = Command()
with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser: #針對傳輸阜及鮑率與serial設定
    try:
        time.sleep(3)
        ser.write(bytes(com.home(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.set_jog_step_size(1,30),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.backward(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.forward(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.ma(1,350),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.home(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.mr(1,20),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.clean(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
        ser.write(bytes(com.stop(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        time.sleep(0.5)
    except KeyboardInterrupt:
        ser.write(bytes(com.stop(1),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        ser.write(bytes(com.stop(2),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
        ser.write(bytes(com.stop(3),encoding='ASCII')) #僅str可以使用bytes 進行轉碼

ser.close()