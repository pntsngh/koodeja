from machine import Pin, PWM
import time
led= Pin('LED', Pin.OUT)
led1= Pin(22, Pin.OUT)
led2= Pin(21, Pin.OUT)
led3= Pin(20, Pin.OUT)
leds = [led1, led2, led3]
p1= PWM(led1)
p1.freq(1000)
p2=PWM(led2)
p2.freq(1000)
p3= PWM(led3)
p3.freq(1000)

while True:
    for duty in range(65025):
        p1.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        p1.duty_u16(duty)
        time.sleep(0.0001)
    
    for duty in range(65025):
        p2.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        p2.duty_u16(duty)
        time.sleep(0.0001)

    for duty in range(65025):
        p1.duty_u16(duty)
        p2.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        p1.duty_u16(duty)
        p2.duty_u16(duty)
        time.sleep(0.0001)
        
    for duty in range(65025):
        p3.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        p3.duty_u16(duty)
        time.sleep(0.0001)
        
    for duty in range(65025):
        p3.duty_u16(duty)
        p1.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        p3.duty_u16(duty)
        p1.duty_u16(duty)
        time.sleep(0.0001)
    
    for duty in range(65025):
        p3.duty_u16(duty)
        p2.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        p3.duty_u16(duty)
        p2.duty_u16(duty)
        time.sleep(0.0001)
        
    for duty in range(65025):
        p1.duty_u16(duty)
        p2.duty_u16(duty)
        p3.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65025, 0, -1):
        p1.duty_u16(duty)
        p2.duty_u16(duty)
        p3.duty_u16(duty)
        time.sleep(0.0001)
        
    time.sleep(1) 
