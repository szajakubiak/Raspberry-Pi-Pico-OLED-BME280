 # Display Image & text on I2C driven SH1106 OLED display 
from machine import I2C, ADC, Pin
from sh1106 import SH1106_I2C
from bme280 import BME280
from time import sleep

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c = I2C(1, scl=Pin(15), sda=Pin(14))                  # Init I2C using I2C1, SCL=Pin(GP15), SDA=Pin(GP14), freq=400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Address      : "+hex(i2c.scan()[1]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)                   # Init oled display
oled.rotate(True)

bme = BME280(i2c = i2c)                                 # Init BME280 sensor

def get_data():
    temp, press, hum = bme.read_compensated_data()
    temp = temp / 100
    press = press / 25600
    hum = hum / 1024
    return (temp, hum, press)

def print_data(data):
    temp, hum, press = data
    oled.fill(0)
    oled.text("Temperature:",5,5)
    oled.text(" %.1f deg. C" % temp,5,15)
    oled.text("Rel. humidity:",5,25)
    oled.text(" %.1f" % hum + " %",5,35)
    oled.text("Pressure:",5,45)
    oled.text(" %.1f hPa" % press,5,55)
    oled.show()

while True:
    print_data(get_data())
    sleep(1)
