import RPi.GPIO as GPIO
from constants import DIRECTION_SERVO_PIN, SERVO_MIDDLE_PWM

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIRECTION_SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(DIRECTION_SERVO_PIN, 50)
servo.start(SERVO_MIDDLE_PWM)

def turnDirectionServo(degrees):
  servo.ChangeDutyCycle(SERVO_MIDDLE_PWM + degrees/100)
