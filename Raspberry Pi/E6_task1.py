import urequests as requests
from time import sleep
import network

ssid = 'KME670Group8'
password = 'or2i2hA00HVJsa1xMiIs'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())

try:
    connect()
except KeyboardInterrupt:
    machine.reset()

response = requests.get('http://localhost:8000')
print(response.text)