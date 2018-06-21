from Switch import Switch
import RPi.GPIO as GPIO

class Bumper(object):
    HIGH = 0
    LOW = 1
    def __init__(self,name, coilPin, detectionSwitch, disableSwitch):
        self.timeOut = False;
        self.timeOutTime = 0.0;
        self.maxTimeOutTime = 5.0;
        self.maxTimeEnabled = 0.5
        self.timeEnabled = 0
        self.enabled = False
        self.detectionSwitch = detectionSwitch
        self.disableSwitch = disableSwitch
        self.name = name
        self.coilPin = coilPin
        self.score = 10
    def update(self, deltaTime):
        if self.timeOut:
            self.timeOutTime+=deltaTime
            if self.timeOutTime>self.maxTimeOutTime:
                self.timeOut = False
                self.timeOutTime = 0.0
        elif not self.enabled:
            if self.detectionSwitch.getState() == 1:
                self.timeEnabled = 0
                self.enabled = True
                GPIO.output(self.coilPin, self.HIGH)
                return self.score
        else:
            self.timeEnabled += deltaTime
            if self.timeEnabled>self.maxTimeEnabled:
                self.enabled = False
                GPIO.output(self.coilPin, self.LOW)
                self.timeOut=True

            elif self.disableSwitch.getState() == 0:
                self.enabled = False
                GPIO.output(self.coilPin, self.LOW)
        return 0
    def disable(self):
        self.enabled = False
        GPIO.output(self.coilPin, self.LOW)

    def __str__(self):
        return "coil enabled: %s time enabled: %s" % (self.enabled, self.timeEnabled)



