import RPi.GPIO as GPIO

servopin = 18
SERVO_MIDDLE = 7.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT)
servo = GPIO.PWM(servopin, 50)
servo.start(SERVO_MIDDLE)

def turnDirectionServo(degrees):
  servo.ChangeDutyCycle(SERVO_MIDDLE + degrees/100)
