#-------------------------------------------------
import serial
import RPi.GPIO as GPIO
import time
import spidev

#-------------------------------------------------
ser = serial.Serial('/dev/ttyS0',9600,timeout=0.001)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

startBit = 0xf0
commandBit  = 0xa1
roll  = 100
pitch = 100
yaw = 100
throttle = 0
operationBit = 0x01
checkSum = 0

#-------------------------------------------------
def analog_read(channel):
    data = spi.xfer2([1, (0x08 + channel) << 4, 0])
    adc_out = ((data[1] & 0x03) << 8) + data[2]
    time.sleep(0.01)
    
    return adc_out

def checkThrottle():
    global throttle
    
    if GPIO.input(switch_list[1]) == 0:
        if throttle > 59:
            throttle -= 20
        elif throttle > 3:
            throttle -= 4
    
    if GPIO.input(switch_list[0]) == 0:
        if throttle < 20:
           throttle = 20
        elif throttle < 181:
            throttle += 20

def checkPitch():
    global pitch

    secondPitch = analog_read(3)
    
    if secondPitch < 400:
        pitch = 50
    elif secondPitch > 600:
        pitch = 150
    else:
        pitch = 100

def checkRoll():
    global roll

    secondRoll = analog_read(2)
    
    if secondRoll < 400:
        roll = 50
    elif secondRoll > 600:
        roll = 150
    else:
        roll = 100

def checkCRC():
    global commandBit
    global roll
    global pitch
    global yaw
    global throttle
    global operationBit
    global checkSum

    checkSum = commandBit + roll + pitch + yaw + throttle + operationBit
    checkSum = checkSum & 0x00ff

#-------------------------------------------------
switch_list = [22, 27, 17, 23, 24, 25]

for i in range(6):
    GPIO.setup(switch_list[i], GPIO.IN)

print("\nRaspberryPi Data Packet 05\n")

time.sleep(0.5)
ser.write("atd".encode())
ser.write("083a5c1f1505".encode())
ser.write("\r".encode())
time.sleep(0.5)

while True:
    checkThrottle()
    checkPitch()
    checkRoll()
    checkCRC()

    ser.write("at+writeh000d".encode())
        
    ser.write((hex(startBit)[2:4]).encode())
    ser.write((hex(commandBit)[2:4]).encode())
    ser.write((hex(roll)[2:4]).encode())
    ser.write((hex(pitch)[2:4]).encode())
    ser.write((hex(yaw)[2:4]).encode())

    if throttle < 0x10:
        ser.write(('0'+hex(throttle)[2:4]).encode())
    else:
        ser.write((hex(throttle)[2:4]).encode())

    ser.write("01".encode())

    if checkSum < 0x10:
        ser.write(('0'+hex(checkSum)[2:4]).encode())
    else:
        ser.write((hex(checkSum)[2:4]).encode())

    ser.write("\r".encode())
    time.sleep(0.1)
