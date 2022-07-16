#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
testString = "1234567890"
uartLength = 0
#-------------------------------------------------

print("\nRaspberryPi Find Test 01\n")

print(testString.find("ab",0,10))

print(testString.find("12",0,3))

uartLength = len(testString)
print("Length: %d" %(uartLength-2))

print(testString.find("90",uartLength-2))

while True:
    continue
