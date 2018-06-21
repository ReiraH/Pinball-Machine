# External module imports
import RPi.GPIO as GPIO
import time

'''# Pin Definitons:
# Rechtse Relay van het speelveld
scrubeModeAan = 10 # R1
scrubeModeUit = 9 # R2
bumperRight = 11 # R3
bumperLeft = 5 # R4
topRightKicker = 6 # R5
topLeftKicker = 13 # R6
bottomRightKicker = 19 # R7
bottomLeftKicker =  26 # R8

# Linkse Relay van het speelveld
beideFlippers = 8 # R1
noobModeHekjeBijStart = 7 # R2
ballPusher = 12 # R3
rightPit = 16 # L5
middelPit = 20 # L6
leftPit = 21 # L7

#pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
#ledPin = 23 # Broadcom pin 23 (P1 pin 16)
#butPin = 17 # Broadcom pin 17 (P1 pin 11)

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

#GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
#pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
#GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for SOLENOIDS:
GPIO.output(scrubeModeAan, GPIO.LOW)
GPIO.output(scrubeModeUit, GPIO.LOW)
GPIO.output(bumperRight, GPIO.LOW)
GPIO.output(bumperLeft, GPIO.LOW)
GPIO.output(topRightKicker, GPIO.LOW)
GPIO.output(topLeftKicker, GPIO.LOW)
GPIO.output(bottomRightKicker, GPIO.LOW)
GPIO.output(bottomLeftKicker, GPIO.LOW)

GPIO.output(beideFlippers, GPIO.LOW)
GPIO.output(noobModeHekjeBijStart, GPIO.LOW)
GPIO.output(ballPusher, GPIO.LOW)
GPIO.output(rightPit, GPIO.LOW)
GPIO.output(middelPit, GPIO.LOW)
GPIO.output(leftPit, GPIO.LOW)
#pwm.start(dc)
'''
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering


#reeksSolenoids = [scrubeModeAan, scrubeModeUit, bumperRight, bumperLeft, topRightKicker, topLeftKicker, bottomRightKicker, bottomLeftKicker, beideFlippers, noobModeHekjeBijStart, ballPusher, rightPit, middelPit, leftPit]
topRightKicker = 6 # R5
topLeftKicker = 13 # R6
GPIO.setup(topRightKicker, GPIO.OUT) # R5 pin set as output
GPIO.setup(topLeftKicker, GPIO.OUT) # R6 pin set as output
GPIO.output(topRightKicker, GPIO.LOW)
GPIO.output(topLeftKicker, GPIO.LOW)

reeks = [topRightKicker, topLeftKicker]

print("Here we go! Press CTRL+C to exit")
for i in range(len(reeks)):
    GPIO.output(reeks[i], GPIO.HIGH)
    time.sleep(1)
    GPIO.output(reeks[i], GPIO.LOW)
    time.sleep(1)
    
#try:
#    while 1:
#        if GPIO.input(butPin): # button is released
#            pwm.ChangeDutyCycle(dc)
#            GPIO.output(ledPin, GPIO.LOW)
#        else: # button is pressed:
#            pwm.ChangeDutyCycle(100-dc)
#            GPIO.output(ledPin, GPIO.HIGH)
#            time.sleep(0.075)
#            GPIO.output(ledPin, GPIO.LOW)
#            time.sleep(0.075)
#except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
#    pwm.stop() # stop PWM
#    GPIO.cleanup() # cleanup all GPIO
