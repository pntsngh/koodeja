from machine import Pin, Timer
import time
leds = [Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(20, Pin.OUT)]
timer = Timer()

while True:
    for led in leds:
        led.on()
        time.sleep(1)
        led.off()
    time.sleep(1)