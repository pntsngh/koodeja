import urequests as requests
import ujson
from machine import Pin, I2C
import ssd1306


i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


APIKEY = "pbZRUi49X48I56oL1Lq8y8NDjq6rPfzX3AQeNo3a"
CLIENT_ID = "3pjgjdmamlj759te85icf0lucv"
CLIENT_SECRET = "111fqsli1eo7mejcrlffbklvftcnfl4keoadrdv1o45vt9pndlef"
LOGIN_URL = "https://kubioscloud.auth.eu-west-1.amazoncognito.com/login"
TOKEN_URL = "https://kubioscloud.auth.eu-west-1.amazoncognito.com/oauth2/token"
REDIRECT_URI = "https://analysis.kubioscloud.com/v1/portal/login"


response = requests.post(
url = TOKEN_URL,
data = 'grant_type=client_credentials&client_id={}'.format(CLIENT_ID),
headers = {'Content-Type':'application/x-www-form-urlencoded'},
auth = (CLIENT_ID, CLIENT_SECRET))
response = response.json() #Parse JSON response into a python dictionary
access_token = response["access_token"] #Parse access token out of the response dictionary
intervals = [828, 836, 852, 760, 800, 796, 856, 824, 808, 776, 724, 816, 800, 812, 812, 812, 756, 820, 812, 800]#Interval data to be sent to KubiosCloud


data_set = {
"type": "RRI",
"data": intervals,
"analysis": {
    "type": "readiness"}
}


#dataset creation HERE
# Make the readiness analysis with the given data
response = requests.post(
url = "https://analysis.kubioscloud.com/v2/analytics/analyze",
headers = { "Authorization": "Bearer {}".format(access_token), #use access token to access your KubiosCloud analysis session
"X-Api-Key": APIKEY },
json = data_set) #dataset will be automatically converted to JSON by the urequests library
response = response.json()

sns_index = response['analysis']['sns_index']
pns_index = response['analysis']['pns_index']


#Print out the SNS and PNS values on the OLED screen
oled.fill(0)
oled.text("SNS index: {}".format(sns_index), 0, 0, 1)
oled.text("PNS index: {}".format(pns_index), 0, 15, 1)
oled.show()
#print(sns_index, pns_index)