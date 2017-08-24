import gspread, datetime, time, random
from oauth2client.service_account import ServiceAccountCredentials
from ds18b20 import DS18B20

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', ['https://spreadsheets.google.com/feeds'])
client = gspread.authorize(creds)
probes = DS18B20()

sheet = client.open("Temperature Sensing").sheet1

def updatesheet(temp1, temp2):
    values = [datetime.datetime.now(), temp1, temp2]
    sheet.append_row(values)

while True:
    probe1 = probes.tempC(0) # First Probe
    probe2 = probes.tempC(1) # Second Probe
    updatesheet(probe1, probe2)
    time.sleep(15)
