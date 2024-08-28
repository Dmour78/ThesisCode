import network
import machine
from umqtt.simple import MQTTClient
import json
import utime

# Set up the Wi-Fi module
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Connect to the Wi-Fi network
wifi.connect('Umniah Fiber_c6b0', 'wlan01394f')

# Wait for the connection to be established
while not wifi.isconnected():
    pass

# Print the IP address of the Raspberry Pi Pico
print('IP address:', wifi.ifconfig()[0])



# Wireless network settings
WIFI_SSID = "Umniah Fiber_c6b0"
WIFI_PASSWORD = "wlan01394f"

# MQTT broker settings
MQTT_ADDRESS = "192.168.1.80"
MQTT_USER = "mosq"
MQTT_PASSWORD = "Jordan@2020"
MQTT_TOPIC = "ESP32Topic"

# JSON data
json_data = {
    "var1": "Rasp Pico",
    "var2": "value2",
    "var3": "value3",
    "var4": "value4",
    "var5": "value5",
    "var6": "value6",
    "var7": "value7",
    "var8": "value8"
}

# Connect to the Wi-Fi network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)
while not wifi.isconnected():
    pass
print("Connected to Wi-Fi")

# Create MQTT client instance
mqtt_client = MQTTClient("pico_client", MQTT_ADDRESS, user=MQTT_USER, password=MQTT_PASSWORD)

# Connect to the MQTT broker
mqtt_client.connect()

# Send JSON data in a loop every second
while True:
    # Publish the JSON data to the MQTT topic
    mqtt_client.publish(MQTT_TOPIC, json.dumps(json_data))
    
    # Delay for 1 second
    utime.sleep(1)

# Disconnect from the MQTT broker
mqtt_client.disconnect()

# Disconnect from the Wi-Fi network
wifi.disconnect()
wifi.active(False)
print("Disconnected from Wi-Fi")