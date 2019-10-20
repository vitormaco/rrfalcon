"""DC motor test."""
import RPi.GPIO as GPIO

in1 = 14
in2 = 15
servopin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(servopin, GPIO.OUT)
outA = GPIO.PWM(in1, 1000)
outB = GPIO.PWM(in2, 1000)
servo = GPIO.PWM(servopin, 50)
outA.start(0)
outB.start(0)
servo.start(7.5)

print("\n")
print("w-frente s-tras x-para q-sai")
print("a-esquerda d-direita c-reto 1,2,3,4,5 - velocidades")
print("\n")

speed = 100

while True:

    x = input()
    if x == 'x':
        print("parei")
        outA.ChangeDutyCycle(0)
        outB.ChangeDutyCycle(0)
        x = 'z'

    elif x == 'w':
        print("andando")
        outA.ChangeDutyCycle(speed)
        outB.ChangeDutyCycle(0)
        x = 'z'

    elif x == 's':
        print("voltando")
        outA.ChangeDutyCycle(0)
        outB.ChangeDutyCycle(speed)
        x = 'z'

    elif x == 'a':
        print("virando pra esquerda")
        servo.ChangeDutyCycle(6)
        x = 'z'

    elif x == 'd':
        print("virando pra direita")
        servo.ChangeDutyCycle(9)
        x = 'z'

    elif x == 'c':
        print("reto")
        servo.ChangeDutyCycle(7.5)
        x = 'z'

    elif x == '1':
        print("marcha 1")
        speed = 20
        x = 'z'

    elif x == '2':
        print("marcha 2")
        speed = 40
        x = 'z'

    elif x == '3':
        print("marcha 3")
        speed = 60
        x = 'z'

    elif x == '4':
        print("marcha 4")
        speed = 80
        x = 'z'

    elif x == '5':
        print("marcha 5")
        speed = 100
        x = 'z'

    elif x == 'q':
        GPIO.cleanup()
        print("flws")
        break

