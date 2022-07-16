#-------------------------------------------------
import time
import spidev

#-------------------------------------------------
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

#-------------------------------------------------
#-------------------------------------------------

print("\nRaspberryPi SPI-Adc Test 02\n")

while True:
    data = spi.xfer2([1, (0x08 + 2) << 4, 0])
    adc_out2 = ((data[1] & 0x03) << 8) + data[2]
    time.sleep(0.01)

    data = spi.xfer2([1, (0x08 + 3) << 4, 0])
    adc_out3 = ((data[1] & 0x03) << 8) + data[2]
    time.sleep(0.01)

    print("adc2 = %d   adc3 = %d" %(adc_out2, adc_out3))
    time.sleep(0.01)
