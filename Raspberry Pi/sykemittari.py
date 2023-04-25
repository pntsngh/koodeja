from machine import Pin, ADC, I2C
import ssd1306
from led import Led
from piotimer import Piotimer
from fifo import Fifo
import utime

adc = ADC(Pin(26))
led = Led(22)
samples = Fifo(750)
avg_fifo = Fifo(20)

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def read_sample(tmr):
        samples.put(adc.read_u16())
        
def update_oled(bpm):
    oled.fill(0)
    oled.text("BPM " + str(bpm), 36, 24)
    oled.show()
    

tmr = Piotimer(mode = Piotimer.PERIODIC, freq = 250, callback = read_sample)

utime.sleep(3)
laskuri = 0
th = 0
cur_max = 0
prev_max = 0
cur_index = 0
prev_index = 0




while True:
    if not samples.empty():
        laskuri += 1
        #get one value from fifo
        value = samples.get()
        avg_fifo.put(value)
        
        average = round(avg_fifo.average())
        avg_fifo.get()
        
        if average > cur_max and average > th:
            cur_max = average
            cur_index = laskuri
        if average < th and cur_max != 0:
            if prev_index != 0:
                ppi_ms = 4 * (cur_index - prev_index)
                bpm = int(60/(ppi_ms/1000))
                #print(bpm)
                update_oled(bpm)
            cur_max = 0
            prev_index = cur_index
                
        
        if laskuri % 750 == 0:
            th = round(samples.threshold(0.3))
            #laskuri = 0
            

        if laskuri % 10 == 0:
            #pass
            print(average, th)
            
