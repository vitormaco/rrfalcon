import Adafruit_DHT
from constants import DHT_SENSOR_PIN

DHT_SENSOR = Adafruit_DHT.DHT22

def readDHTSensor():
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_SENSOR_PIN)
  if humidity is not None and temperature is not None:
    return "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity)
  else:
    return "Failed to retrieve data from humidity sensor"
