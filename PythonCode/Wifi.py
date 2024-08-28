from machine import Pin
from utime import sleep
from machine import I2C
from time import sleep
import bme280
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
while True:
    bme = bme280.BME280(i2c=i2c)
    temp = bme.values[0]
    pressure = bme.values[1]
    humidity = bme.values [2]
    reading = 'Tempreature:' + temp + 'Pressure:' + pressure + 'Humidity:' + humidity
    print(reading)
    sleep(10)