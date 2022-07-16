#-------------------------------------------------
import time
import spidev

#-------------------------------------------------
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

#-------------------------------------------------
#-------------------------------------------------

print("\nRaspberryPi SPI-Adc Test 01\n")

while True:
    data = spi.xfer2([1, (0x08 + 2) << 4, 0])
    adc_out = ((data[1] & 0x03) << 8) + data[2]
    time.sleep(0.01)
    
    print(adc_out)
    time.sleep(0.01)
