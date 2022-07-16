#-------------------------------------------------
import time

#-------------------------------------------------
#-------------------------------------------------
data1 = 0xa1
data2 = 0x64
data3 = 0x64
data4 = 0x64
data5 = 0x78
data6 = 0x01
checkSum = 0

#-------------------------------------------------

print("\nRaspberryPi Checksum Test 02\n")

while True:
    checkSum = data1 + data2 + data3 + data4 + data5 + data6
    checkSum = checkSum & 0x00ff
    print(hex(checkSum))
    time.sleep(0.5)
