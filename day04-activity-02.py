from machine import Pin, ADC
from time import sleep

potentiometer = ADC(Pin(27))
# button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
# button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
# button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

delay = 0

red = Pin(18, Pin.OUT)
# green = Pin(19, Pin.OUT)
# amber = Pin(20, Pin.OUT)

while True:

    p_value = potentiometer.read_u16()
    delay = p_value / 65535

    red.value(1)
    sleep(delay)
    red.value(0)
    sleep(delay)
