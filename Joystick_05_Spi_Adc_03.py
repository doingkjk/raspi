#-------------------------------------------------
import time
import spidev

#-------------------------------------------------
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

#-------------------------------------------------
def analog_read(channel):
    data = spi.xfer2([1, (0x08 + channel) << 4, 0])
    adc_out = ((data[1] & 0x03) << 8) + data[2]
    time.sleep(0.01)
    
    return adc_out

#-------------------------------------------------

print("\nRaspberryPi SPI-Adc Test 03\n")

while True:
    adc2 = analog_read(2)
    adc3 = analog_read(3)
    
    print("adc2 = %d   adc3 = %d" %(adc2, adc3))
    time.sleep(0.01)
