from machine import Pin, ADC
from time import sleep


potentiometer = ADC(Pin(27))
# button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
# button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
# button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)


red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
amber = Pin(20, Pin.OUT)

while True:

    p_value = potentiometer.read_u16()

    if p_value < 65535/3:
        red.value(1)
        green.value(0)
        amber.value(0)
    elif p_value > 65535 / 3 * 2:
        red.value(0)
        green.value(1)
        amber.value(0)
    else:
        red.value(0)
        green.value(0)
        amber.value(1)

    sleep(1)
