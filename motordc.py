import RPi.GPIO as GPIO

in1 = 14
in2 = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
outA = GPIO.PWM(in1, 1000)
outB = GPIO.PWM(in2, 1000)
outA.start(0)
outB.start(0)

def moveDCMotor(speed):
  moveForward(speed) if speed > 0 else moveBackwards(speed)

def moveForward(speed):
  outA.ChangeDutyCycle(speed)
  outB.ChangeDutyCycle(0)

def moveBackwards(speed):
  outA.ChangeDutyCycle(0)
  outB.ChangeDutyCycle(speed)

