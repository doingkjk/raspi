#-------------------------------------------------
import serial
import RPi.GPIO as GPIO
import time

#-------------------------------------------------
ser = serial.Serial('/dev/ttyS0',9600,timeout=0.001)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

currentStep = 0
uartString = ""
uartLength = 0

#-------------------------------------------------
pio_list = [22, 27, 17, 23, 24, 25]

for i in range(6):
    GPIO.setup(pio_list[i], GPIO.IN)

while True:
    if currentStep == 0:
        print("\nRaspberryPi Check Message Test 01\n")
        currentStep += 1
    
    elif currentStep == 1:
        if GPIO.input(pio_list[4]) == 0:
            print("Pressed Connect Button")
            ser.write("atd".encode())
            ser.write("083a5c1f11ac".encode())
            ser.write("\r".encode())
            time.sleep(0.3)
            uartString = ""
            currentStep += 1
    
    elif currentStep == 2:
        if ser.inWaiting():
            uartString += ser.read().decode()
            uartLength = len(uartString)
            if uartLength > 4 and uartString.find("\r\n",0,2) == 0 \
            and uartString.find("\r\n",uartLength-2) == uartLength - 2:
                currentStep += 1
    
    elif currentStep == 3:
        if uartString.find("\r\nOK\r\n",0,6) == 0:
            print("Received OK")
            time.sleep(0.3)
            uartString = ""
            currentStep += 1
    
    elif currentStep == 4:
        if ser.inWaiting():
            uartString += ser.read().decode()
            uartLength = len(uartString)
            if uartLength > 4 and uartString.find("\r\n",0,2) == 0 \
            and uartString.find("\r\n",uartLength-2) == uartLength - 2:
                currentStep += 1
    
    elif currentStep == 5:
        if uartString.find("\r\nCONNECT ",0,10) == 0:
            print("Received CONNECT")
            time.sleep(0.3)
            uartString = ""
            currentStep += 1
    
    elif currentStep == 6:
        if ser.inWaiting():
            ser.read()
        
        if GPIO.input(pio_list[5]) == 0:
            print("Pressed Disconnect Button")
            ser.write("ath".encode())
            ser.write("\r".encode())
            time.sleep(0.3)
            uartString = ""
            currentStep += 1
    
    elif currentStep == 7:
        if ser.inWaiting():
            uartString += ser.read().decode()
            uartLength = len(uartString)
            if uartLength > 4 and uartString.find("\r\n",0,2) == 0 \
            and uartString.find("\r\n",uartLength-2) == uartLength - 2:
                currentStep += 1
    
    elif currentStep == 8:
        if uartString.find("\r\nOK\r\n",0,6) == 0:
            print("Received OK")
            time.sleep(0.3)
            uartString = ""
            currentStep += 1
    
    elif currentStep == 9:
        if ser.inWaiting():
            uartString += ser.read().decode()
            uartLength = len(uartString)
            if uartLength > 4 and uartString.find("\r\n",0,2) == 0 \
            and uartString.find("\r\n",uartLength-2) == uartLength - 2:
                currentStep += 1
    
    elif currentStep == 10:
        if uartString.find("\r\nDISCONNECT",0,12) == 0:
            print("Received DISCONNECT")
            time.sleep(0.3)
            uartString = ""
            currentStep += 1
    
    elif currentStep == 11:
        if ser.inWaiting():
            uartString += ser.read().decode()
            uartLength = len(uartString)
            if uartLength > 4 and uartString.find("\r\n",0,2) == 0 \
            and uartString.find("\r\n",uartLength-2) == uartLength - 2:
                currentStep += 1
    
    elif currentStep == 12:
        if uartString.find("\r\nREADY",0,7) == 0:
            print("Received READY")
            time.sleep(0.3)
            uartString = ""
            currentStep = 1
