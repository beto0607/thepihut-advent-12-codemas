from machine import Pin
from time import sleep


button = Pin(13, Pin.IN, Pin.PULL_DOWN)
red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)

v = 1
while True:
    sleep(0.2)
    green.value(button.value())
    if button.value() == 1:
        print('button pressed')

    red.value(v)
    v = 0 if v == 1 else 1
