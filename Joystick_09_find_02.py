#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
testString = "1234567890"
uartLength = 0
#-------------------------------------------------

print("\nRaspberryPi Find Test 02\n")

uartLength = len(testString)
print("Length: %d" %uartLength)

if testString.find("12",0,2) == 0:
    print("Start find OK")

if testString.find("90",uartLength-2) == uartLength-2:
    print("End find OK")

while True:
    continue
