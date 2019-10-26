import RPi.GPIO as GPIO
from constants import DCMOTOR_PIN_A, DCMOTOR_PIN_B

GPIO.setmode(GPIO.BCM)
GPIO.setup(DCMOTOR_PIN_A, GPIO.OUT)
GPIO.setup(DCMOTOR_PIN_B, GPIO.OUT)
outA = GPIO.PWM(DCMOTOR_PIN_A, 1000)
outB = GPIO.PWM(DCMOTOR_PIN_B, 1000)
outA.start(0)
outB.start(0)

def moveDCMotor(speed):
  moveForward(speed) if speed > 0 else moveBackwards(speed)

def moveForward(speed):
  outA.ChangeDutyCycle(speed)
  outB.ChangeDutyCycle(0)

def moveBackwards(speed):
  outA.ChangeDutyCycle(0)
  outB.ChangeDutyCycle(-speed)

