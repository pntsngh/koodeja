from machine import Pin, Timer
import time
led= Pin('LED', Pin.OUT)
led1= Pin(22, Pin.OUT)
led2= Pin(21, Pin.OUT)
led3= Pin(20, Pin.OUT)
leds = [led1, led2, led3]
timer = Timer()

while True:
    led.on()
    led.off()
    led1.on()
    time.sleep(1)
    led1.off()
    
    led.on()
    led.off()
    led2.on()
    time.sleep(1)
    led2.off()
    
    led.on()
    led.off()
    led1.on()
    led2.on()
    time.sleep(1)
    led1.off()
    led2.off()
    
    led.on()
    led.off()
    led3.on()
    time.sleep(1)
    led3.off()
    
    led.on()
    led.off()
    led3.on()
    led1.on()
    time.sleep(1)
    led3.off()
    led1.off()
    
    led.on()
    led.off()
    led3.on()
    led2.on()
    time.sleep(1)
    led3.off()
    led2.off()
    
    led.on()
    led.off()
    led1.on()
    led2.on()
    led3.on()
    time.sleep(1)
    
    led.on()
    led.off()
    led1.off()
    led2.off()
    led3.off()
    time.sleep(1) 
    
    
#000
#001
#010
#011
#100
#101
#110
#111