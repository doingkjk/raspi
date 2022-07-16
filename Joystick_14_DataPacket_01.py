#-------------------------------------------------
import serial
import RPi.GPIO as GPIO
import time

#-------------------------------------------------
ser = serial.Serial('/dev/ttyS0',9600,timeout=0.001)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#-------------------------------------------------
switch_list = [22, 27, 17, 23, 24, 25]

for i in range(6):
    GPIO.setup(switch_list[i], GPIO.IN)

print("\nRaspberryPi Data Packet 01\n")

time.sleep(0.5)
ser.write("atd".encode())
ser.write("083a5c1f1505".encode())
ser.write("\r".encode())
time.sleep(0.5)

while True:
    if GPIO.input(switch_list[0]) == 0:
        ser.write("at+writeh000d".encode())

        ser.write("f0".encode())
        ser.write("a1".encode())
        ser.write("64".encode())
        ser.write("64".encode())
        ser.write("64".encode())
        ser.write("aa".encode())
        ser.write("01".encode())
        ser.write("78".encode())
        
        ser.write("\r".encode())
        time.sleep(0.3)
