#-------------------------------------------------
import serial
import RPi.GPIO as GPIO
import time

#-------------------------------------------------
ser = serial.Serial('/dev/ttyS0',9600,timeout=0.001)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

startBit = 0xf0
commandBit  = 0xa1
roll  = 100
pitch = 100
yaw = 100
throttle = 0
operationBit = 0x05
checkSum = 0

route_action = 0
droneMoving = 0
previousTime = 0
#-------------------------------------------------

def checkDronevalue(roll_V, pitch_V, yaw_V, throttle_V, operationBit_V):
    global roll
    global pitch
    global yaw
    global throttle
    global operationBit
    
    roll = roll_V
    pitch = pitch_V
    yaw = yaw_V
    throttle = throttle_V
    operationBit = operationBit_V

def checkButton():
    global route_action
    global droneMoving
    global previousTime

    if droneMoving == 0:
        if GPIO.input(switch_list[0]) == 0:
            route_action = 5

        if route_action != 0:
            droneMoving = 1
            previousTime = time.time()
    #
    if GPIO.input(switch_list[4]) == 0 and route_action != 9:
        route_action = 9
        droneMoving = 1
        previousTime = time.time()
            
    return route_action

def check_time(t_value):
    global currentTime
    
    currentTime = time.time()
    
    if currentTime - previousTime < t_value:
        return 1
    else:
        return 0

def route_1():
    global droneMoving
    global route_action
    
    if check_time(5):
        checkDronevalue(100, 100, 100, 100, 5)
        checkCRC()
        sendDroneCommand()
        
    elif check_time(10):
        checkDronevalue(100, 100, 100, 0, 5)
        checkCRC()
        sendDroneCommand()
        
    else:
        droneMoving = 0
        route_action = 0

def route_Emergency():
    global droneMoving
    global route_action
    
    if check_time(0.5):
        checkDronevalue(100, 100, 100, 0, 5)
        checkCRC()
        sendDroneCommand()
    else:
        droneMoving = 0
        route_action = 0

def sendDroneCommand():
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

    ser.write(('0'+hex(operationBit)[2:4]).encode())

    if checkSum < 0x10:
        ser.write(('0'+hex(checkSum)[2:4]).encode())
    else:
        ser.write((hex(checkSum)[2:4]).encode())

    ser.write("\r".encode())
    time.sleep(0.05)

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

print("\nRoute of Flight Test!\n")

time.sleep(0.5)
ser.write("atd".encode())
ser.write("083a5c1f14ff".encode())
ser.write("\r".encode())
time.sleep(0.5)

while True:
    if checkButton():
        if route_action == 5:
            route_1()
        elif route_action == 9:
            route_Emergency()
