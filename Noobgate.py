from Switch import Switch
import RPi.GPIO as GPIO

class Noobgate(object):
    HIGH = 0
    LOW = 1
    def __init__(self,name, coilPin, detectionSwitch,ballLaunchSwitch ):
        self.detectionSwitch = detectionSwitch
        self.ballLaunchSwitch = ballLaunchSwitch
        self.ballDetected = False
        self.name = name
        self.coilPin = coilPin
    def update(self, deltaTime):
        if self.ballDetected == False:
            if self.detectionSwitch.getState() == 1:
                self.ballDetected = True
        else:
            if self.ballLaunchSwitch.getState() == 0:
                GPIO.output(self.coilPin, self.LOW)
        return 0
    def reset(self):
        self.ballDetected = False
        GPIO.output(self.coilPin, self.HIGH)

    def disable(self):
        GPIO.output(self.coilPin, self.LOW)

    def __str__(self):
        return "coil enabled: %s time enabled: %s" % (self.enabled, self.timeEnabled)
