import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 14

def readDHTSensor():
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
  if humidity is not None and temperature is not None:
    return "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity)
  else:
    return "Failed to retrieve data from humidity sensor"
