import RPi.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017
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
print("oneamount pls")
oneAmount = 10 - int(input())
print("tensamount pls")
tenAmount = 10 - int(input())
print("hundredamount pls")
hundredAmount = 10 - int(input())
print("thousandamount pls")
thousandAmount = 10 - int(input())

if oneAmount != 10:
    for ones in range(0,oneAmount):
        GPIO.output(digitOnes, HIGH)
        sleep(0.1)
        GPIO.output(digitOnes, LOW)
        sleep(0.1)
        
if tenAmount != 10:
    for tens in range(0,tenAmount):
                
        GPIO.output(digitTens, HIGH)
        sleep(0.1)
        GPIO.output(digitTens, LOW)
        sleep(0.1)
        
if hundredAmount != 10:
    for hundreds in range(0,hundredAmount):
            
        GPIO.output(digitHundreds, HIGH)
        sleep(0.1)
        GPIO.output(digitHundreds, LOW)
        sleep(0.1)

if thousandAmount != 10:          
    for thousands in range(0,thousandAmount):
         
        GPIO.output(digitThousands, HIGH)
        sleep(0.1)
        GPIO.output(digitThousands, LOW)
        sleep(0.1)

GPIO.cleanup()
