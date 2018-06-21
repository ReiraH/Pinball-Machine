import RPi.GPIO as GPIO
from time import sleep
HIGH = 0
LOW = 1
digitOnes = 24
digitTens = 23
digitHundreds = 15
digitThousands = 18

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

GPIO.setup(digitOnes, GPIO.OUT)
GPIO.output(digitOnes, LOW)

GPIO.setup(digitTens, GPIO.OUT)
GPIO.output(digitTens, LOW)

GPIO.setup(digitHundreds, GPIO.OUT)
GPIO.output(digitHundreds, LOW)

GPIO.setup(digitThousands, GPIO.OUT)
GPIO.output(digitThousands, LOW)


for thousands in range(0,10):
    for hundreds in range(0,10):
        for tens in range(0,10):
            for ones in range(0,10):
                GPIO.output(digitOnes, HIGH)
                sleep(0.07)
                GPIO.output(digitOnes, LOW)
                sleep(0.07)
            GPIO.output(digitTens, HIGH)
            sleep(0.07)
            GPIO.output(digitTens, LOW)
            sleep(0.07)
        GPIO.output(digitHundreds, HIGH)
        sleep(0.07)
        GPIO.output(digitHundreds, LOW)
        sleep(0.07) 
    GPIO.output(digitThousands, HIGH)
    sleep(0.07)
    GPIO.output(digitThousands, LOW)
    sleep(0.07)

GPIO.cleanup()
