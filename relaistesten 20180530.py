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

# Linkse Relay van het speelveld
beideFlippers = 6 # L1
noobModeHekjeBijStart = 12 # L2
ballPusher = 24 # L3
rightPit = 18 # L5
middelPit = 19 # L6
leftPit = 17 # L7

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

GPIO.setup(beideFlippers, GPIO.OUT) # L1 pin set as output
GPIO.setup(noobModeHekjeBijStart, GPIO.OUT) # L2 pin set as output
GPIO.setup(ballPusher, GPIO.OUT) # L3 pin set as output
GPIO.setup(rightPit, GPIO.OUT) # L5 pin set as output
GPIO.setup(middelPit, GPIO.OUT) # L6 pin set as output
GPIO.setup(leftPit, GPIO.OUT) # L7 pin set as output

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

GPIO.output(beideFlippers, GPIO.HIGH)
GPIO.output(noobModeHekjeBijStart, GPIO.HIGH)
GPIO.output(ballPusher, GPIO.HIGH)
GPIO.output(rightPit, GPIO.HIGH)
GPIO.output(middelPit, GPIO.HIGH)
GPIO.output(leftPit, GPIO.HIGH)


reeksSolenoids = [scrubeModeAan, scrubeModeUit, bumperRight, bumperLeft, topRightKicker, topLeftKicker, bottomRightKicker, bottomLeftKicker, beideFlippers, noobModeHekjeBijStart, ballPusher, rightPit, middelPit, leftPit]

print("Here we go! Press CTRL+C to exit")
#for i in range(len(reeksSolenoids))
#for i in range(1:2):

GPIO.output(middelPit, GPIO.LOW)
time.sleep(0.50)
GPIO.output(middelPit, GPIO.HIGH)
time.sleep(1)
print("gedaan")
'''    GPIO.output(reeksSolenoids[i], GPIO.LOW)
    time.sleep(0.50)
    GPIO.output(reeksSolenoids[i], GPIO.HIGH)
    time.sleep(1)
'''
