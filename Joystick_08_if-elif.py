#-------------------------------------------------
import time

#-------------------------------------------------
#-------------------------------------------------
currentStep = 1
#-------------------------------------------------

print("\nRaspberryPi if-elif Test\n")

while True:
    if currentStep == 1:
        print("if-elif 1-step Operation")
        currentStep = 5
        time.sleep(0.5)
    elif currentStep == 5:
        print("if-elif 5-step Operation")
        currentStep += 1
        time.sleep(0.5)
    else:
        print("if-elif default Operation")
        time.sleep(0.5)
