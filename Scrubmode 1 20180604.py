from Switch import Switch
import RPi.GPIO as GPIO

class Scrubmode(object):
    HIGH = 0
    LOW = 1
    def __init__(self,name, coilPinOne,coilPinTwo, lowerRightSwitch,middleRightSwitch,lowerLeftSwitch,middleLeftSwitch,scrubModePositionDetectionSwitch):
        self.maxTimeEnabled = 0.05
        self.timeEnabled = 0.0
        self.inTransition = 0
        self.transitionState = 0
        self.name = name
        self.coilPinOne = coilPinOne
        self.coilPinTwo = coilPinTwo
        self.lowerRightSwitch = lowerRightSwitch
        self.middleRightSwitch = middleRightSwitch
        self.lowerLeftSwitch = lowerLeftSwitch
        self.middleLeftSwitch = middleLeftSwitch
        self.scrubModePositionDetectionSwitch = scrubModePositionDetectionSwitch
    def update(self, deltaTime):
        if self.inTransition == 0:
            if self.scrubModePositionDetectionSwitch.getState() == 0 and (self.middleLeftSwitch.getState() == 1 or self.middleRightSwitch.getState() == 1):
                self.timeEnabled = 0
                self.transitionState = 2
                self.inTransition = 1
                GPIO.output(self.coilPinOne, self.HIGH)
                GPIO.output(self.coilPinTwo, self.HIGH)


            
            elif self.scrubModePositionDetectionSwitch.getState() == 1 and (self.lowerLeftSwitch.getState() == 1 or self.lowerRightSwitch.getState() == 1):
                self.timeEnabled = 0
                GPIO.output(self.coilPinOne, self.HIGH)
                self.inTransition = 2
        
        elif self.inTransition == 1:
            self.timeEnabled += deltaTime
            if self.transitionState == 1:
                #print "state 1 --" + str(self.timeEnabled)
                if self.timeEnabled>self.maxTimeEnabled:
                    self.transitionState = 2
                    GPIO.output(self.coilPinTwo, self.HIGH)
                    self.timeEnabled = 0
            elif self.transitionState == 2:
                #print "state 2"
                if self.timeEnabled>self.maxTimeEnabled:
                    self.transitionState = 3
                    GPIO.output(self.coilPinOne, self.LOW)
                    self.timeEnabled = 0
            elif self.transitionState == 3:
                #print "state 3"
                if self.timeEnabled>self.maxTimeEnabled:
                    self.transitionState = 0
                    GPIO.output(self.coilPinTwo, self.LOW)
                    self.timeEnabled = 0
                    self.inTransition = 0

        elif self.inTransition == 2:
            self.timeEnabled += deltaTime
            if self.timeEnabled>self.maxTimeEnabled:
                self.timeEnabled = 0
                GPIO.output(self.coilPinOne, self.LOW)
                self.inTransition = 0
        return 0

    def disable(self):
        self.enabled = False
        GPIO.output(self.coilPinTwo, self.LOW)
        while self.scrubModePositionDetectionSwitch.getState() == 1:
            GPIO.output(self.coilPinOne, self.HIGH) #veilig om dit te doen?
        GPIO.output(self.coilPinOne, self.LOW)

    def __str__(self):
        return "coil enabled: %s" % (self.scrubModePositionDetectionSwitch.getState())



