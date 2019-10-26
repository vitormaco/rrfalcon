import RPi.GPIO as GPIO
from constants import GAS_SENSOR_PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)

def readGasSensor():
  value = GPIO.input(GAS_SENSOR_PIN)
  if value == 1:
    return 'ta suave'
  elif value == 0:
    return 'deu ruim, ta td toxico'
  else:
    return "Failed to retrieve data from gas sensor"
