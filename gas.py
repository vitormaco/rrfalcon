import RPi.GPIO as GPIO

gaspin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(gaspin, GPIO.IN)

def readGasSensor():
  value = GPIO.input(gaspin)
  if value == 1:
    return 'ta suave'
  elif value == 0:
    return 'deu ruim, ta td toxico'
  else:
    return "Failed to retrieve data from gas sensor"
