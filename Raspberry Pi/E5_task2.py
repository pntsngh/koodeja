from machine import Pin, I2C
import ssd1306

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def calculate_hrv(ppi_values):
    mean_ppi = sum(ppi_values) / len(ppi_values)
    mean_hr = (60000 / mean_ppi)
    sdnn = (sum((x - mean_ppi) ** 2 for x in ppi_values) / (len(ppi_values) - 1)) ** 0.5
    rmssd = ((sum((x - y) ** 2 for x, y in zip(ppi_values[1:], ppi_values[:-1])) / (len(ppi_values) - 1)) ** 0.5)
    
    return mean_ppi, mean_hr, sdnn, rmssd

ppi_values = [828, 836, 852, 760, 800, 796, 856, 824, 808, 776, 724, 816, 800, 812, 812,
812, 756, 820, 812, 800]

mean_ppi, mean_hr, sdnn, rmssd = calculate_hrv(ppi_values)

oled.fill(0)
oled.text("Mean PPI: {:d} ms".format(round(mean_ppi)), 0, 0, 1)
oled.text("Mean HR: {:d} bpm".format(round(mean_hr)), 0, 15, 1)
oled.text("SDNN: {:d} ms".format(round(sdnn)), 0, 30, 1)
oled.text("RMSSD: {:d} ms".format(round(rmssd)), 0, 45, 1)
oled.show()
