#-------------------------------------------------
import time

#-------------------------------------------------
#-------------------------------------------------
data1 = 0x00
data2 = 0x00
data3 = 0x00
data4 = 0x00
data5 = 0x00
data6 = 0x00
checkSum = 0

#-------------------------------------------------

print("\nRaspberryPi Checksum Test 01\n")

for data1 in range(20):
    checkSum = data1 + data2 + data3 + data4 + data5 + data6
    checkSum = checkSum & 0x00ff
    print(hex(checkSum))
    time.sleep(0.1)

while True:
    continue
