from machine import Timer
import network
import requests
import json
import time

from PicoSensor import Temperature


def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for connection
    print("Connecting to Wi-Fi...")
    for _ in range(10):
        if wlan.isconnected():
            break
        time.sleep(3)

    if wlan.isconnected():
        print("Connected!")
        print("IP Address:", wlan.ifconfig()[0])
        print("Status Code:", wlan.status())
        return True
    else:
        return False


def sense(timer):
    temp = sensor.read_temperature()
    print(temp)
    
    data = {"sensor_id": 3, "value": temp}
    response = requests.post(url, data=json.dumps(data))
    
    # Print response
    print("Response:", response.text)


# Load config
with open("config.json", "r") as file:
    config = json.load(file)

ssid = config.get("SSID")
password = config.get("PASSWORD")
url = config.get("API_URL")


# Connecto to WiFi and start sensing
connected = init_wifi(ssid, password)
try:
    timer = Timer()
    sensor = Temperature()
    timer.init(freq=0.5, mode=Timer.PERIODIC, callback=sense)

except Exception as e:
    print('Error during request:', e)


