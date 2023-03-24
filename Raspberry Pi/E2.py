from machine import Pin, I2C
import time
import ssd1306

led1= Pin(22, Pin.OUT)
led2= Pin(21, Pin.OUT)
led3= Pin(20, Pin.OUT)
button1= Pin(9, mode = Pin.IN, pull = Pin.PULL_UP)
button2= Pin(8, mode = Pin.IN, pull = Pin.PULL_UP)
button3= Pin(7, mode = Pin.IN, pull = Pin.PULL_UP)
button= Pin(12, mode = Pin.IN, pull = Pin.PULL_UP)

def button_handler(pin):
    led1.value(0)
    led2.value(0)
    led3.value(0)
    
button.irq(handler = button_handler, trigger = Pin.IRQ_FALLING)

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    if button1.value()==0 and not button1_pressed:
        button1_pressed = True
        led1.toggle()
        time.sleep(0.2)
    elif button1.value() == 1:
        button1_pressed = False
    
    if button2.value()==0 and not button2_pressed:
        button2_pressed = True
        led2.toggle()
        time.sleep(0.2)
    elif button2.value() == 1:
        button2_pressed = False
    
    if button3.value()==0 and not button3_pressed:
        button3_pressed = True
        led3.toggle()
        time.sleep(0.2)
    elif button3.value() == 1:
        button3_pressed = False
    display.fill(0)
    display.text('LED1: ' + str(led1.value()), 0, 0, 1)
    display.text('LED2: ' + str(led2.value()), 0, 15, 1)
    display.text('LED3: ' + str(led3.value()), 0, 30, 1)
    display.show()