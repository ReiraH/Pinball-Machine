# External module imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Pin Definitons:
# Rechtse Relay van het speelveld
scrubeModeAan = 4 # R1
scrubeModeUit = 5 # R2
bumperRight = 16 # R3
bumperLeft = 13 # R4
topRightKicker = 21 # R5
topLeftKicker = 20 # R6
bottomRightKicker = 22 # R7
bottomLeftKicker =  23 # R8

dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(scrubeModeAan, GPIO.OUT) # R1 pin set as output
GPIO.setup(scrubeModeUit, GPIO.OUT) # R2 pin set as output
GPIO.setup(bumperRight, GPIO.OUT) # R3 pin set as output
GPIO.setup(bumperLeft, GPIO.OUT) # R4 pin set as output
GPIO.setup(topRightKicker, GPIO.OUT) # R5 pin set as output
GPIO.setup(topLeftKicker, GPIO.OUT) # R6 pin set as output
GPIO.setup(bottomRightKicker, GPIO.OUT) # R7 pin set as output
GPIO.setup(bottomLeftKicker, GPIO.OUT) # R8 pin set as output

#GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for SOLENOIDS:
GPIO.output(scrubeModeAan, GPIO.HIGH)
GPIO.output(scrubeModeUit, GPIO.HIGH)
GPIO.output(bumperRight, GPIO.HIGH)
GPIO.output(bumperLeft, GPIO.HIGH)
GPIO.output(topRightKicker, GPIO.HIGH)
GPIO.output(topLeftKicker, GPIO.HIGH)
GPIO.output(bottomRightKicker, GPIO.HIGH)
GPIO.output(bottomLeftKicker, GPIO.HIGH)


reeksSolenoids = [scrubeModeAan, scrubeModeUit, bumperRight, bumperLeft, topRightKicker, topLeftKicker, bottomRightKicker, bottomLeftKicker]

print("Here we go! Press CTRL+C to exit")
for i in range(len(reeksSolenoids)):
    GPIO.output(reeksSolenoids[i], GPIO.LOW)
    time.sleep(0.50)
    GPIO.output(reeksSolenoids[i], GPIO.HIGH)
    time.sleep(1)
