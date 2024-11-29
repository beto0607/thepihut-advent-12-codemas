from machine import Pin
from time import sleep


button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)


red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
amber = Pin(20, Pin.OUT)

while True:
    sleep(0.5)

    if (button1.value() == 1):
        red.toggle()
    # red.value(button3.value())
    # green.value(button2.value())
    # amber.value(button1.value())
