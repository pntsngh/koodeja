from machine import Pin, Timer
leds = [Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(20, Pin.OUT), Pin("LED", Pin.OUT)]
 
def leds_off():
    for led in leds:
        led.value(0)
 
leds_off()