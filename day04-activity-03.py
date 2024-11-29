from machine import Pin, ADC, PWM
from time import sleep

potentiometer = ADC(Pin(27))

delay = 0

red = PWM(Pin(18))
green = PWM(Pin(19))
amber = PWM(Pin(20))

red.freq(1000)
amber.freq(1000)
green.freq(1000)

p_value = 0

while True:

    p_value = potentiometer.read_u16()

    red.duty_u16(p_value)
    amber.duty_u16(p_value)
    green.duty_u16(p_value)
    sleep(0.001)
