from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from led import Led
import utime

import machine
import utime

led_pins = [machine.Pin(22, machine.Pin.OUT), machine.Pin(21, machine.Pin.OUT), machine.Pin(20, machine.Pin.OUT)]


button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
clk = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)
dt = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)


led_pwms = [machine.PWM(pin) for pin in led_pins]


led_index = 0
led_brightness = 0


def rotary_interrupt(pin):
    global led_index, led_brightness
    if pin == button:
        led_index = (led_index + 1) % len(led_pins)
        led_brightness = 0
    else:
        if pin == clk and dt.value():
            led_brightness += 10
        elif pin == dt and clk.value():
            led_brightness -= 10
        led_brightness = min(255, max(0, led_brightness))
        led_pwms[led_index].duty_u16(int(led_brightness * 65535 / 255))


button.irq(rotary_interrupt, machine.Pin.IRQ_FALLING)
clk.irq(rotary_interrupt, machine.Pin.IRQ_FALLING)
dt.irq(rotary_interrupt, machine.Pin.IRQ_FALLING)


while True:
    utime.sleep_ms(10)