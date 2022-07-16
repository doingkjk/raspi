#-------------------------------------------------
import time
import RPi.GPIO as GPIO

#-------------------------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#-------------------------------------------------
pio_list = [22, 27, 17, 23, 24, 25]

for i in range(6):
    GPIO.setup(pio_list[i], GPIO.IN)

#-------------------------------------------------

print("\nRaspberryPi Pio Test 01\n")

while True:
    if GPIO.input(pio_list[4]) == 0:
        print("Press 4")
        time.sleep(0.1)


