#-------------------------------------------------
import time
import serial

#-------------------------------------------------
ser = serial.Serial('/dev/ttyS0',9600,timeout=0.001)

#-------------------------------------------------
testString = ""

#-------------------------------------------------

print("\nRaspberryPi AT Command Test\n")

time.sleep(0.5)
ser.write("at".encode())
ser.write("\r".encode())
time.sleep(0.5)

while True:
    if ser.inWaiting():
        testString = ""
        time.sleep(0.5)
        while ser.inWaiting():
            testString += ser.read().decode()

        print(testString)
        testString = ""

    testString = input("Enter AT Command: ")
    ser.write(testString.encode())
    ser.write("\r".encode())
    print("Wait Response Command for 3s...")
    time.sleep(3)
