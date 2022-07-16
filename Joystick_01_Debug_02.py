#-------------------------------------------------
import time

#-------------------------------------------------
i = 0
#-------------------------------------------------

print("\nRaspberryPi Debug Test 02\n")

while True:
    print(i)
    i += 1

    if i > 10:
        i = 0
        print("Console Test\n")

    time.sleep(0.5)

