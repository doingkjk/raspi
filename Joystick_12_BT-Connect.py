#-------------------------------------------------
import serial
import RPi.GPIO as GPIO

#-------------------------------------------------
ser = serial.Serial('/dev/ttyS0',9600,timeout=0.001)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#-------------------------------------------------
pio_list = [22, 27, 17, 23, 24, 25]

for i in range(6):
    GPIO.setup(pio_list[i], GPIO.IN)

currentStep = 0

#-------------------------------------------------

while True:
    if currentStep == 0:
        print("\nRaspberryPi BT Connect Test\n")
        currentStep += 1
    elif currentStep == 1:
        if GPIO.input(pio_list[4]) == 0:
            print("Pressed Connect Button")
            ser.write("atd".encode())
            ser.write("083a5c1f11ac".encode())
            ser.write("\r".encode())
            currentStep += 1
    elif currentStep == 2:
        if GPIO.input(pio_list[5]) == 0:
            print("Pressed Disconnect Button")
            ser.write("ath".encode())
            ser.write("\r".encode())
            currentStep = 1
