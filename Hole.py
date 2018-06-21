from Switch import Switch
import RPi.GPIO as GPIO

class Hole(object):
    HIGH = 0
    LOW = 1
    def __init__(self,name, coilPin, switch):
        self.maxTimeEnabled = 0.5
        self.delayTime = 1.0
        self.timeEnabled = 0.0
        self.enabled = False
        self.switch = switch
        self.name = name
        self.coilPin = coilPin
        self.ballDetected = False
        self.timeDetected = 0.0
        self.score = 50
    def update(self, deltaTime):
        if not self.enabled:
            #print "Hole Disabled"
            if self.switch.getState() == 1:
                #print "Switch Pressed!"
                if self.ballDetected == False:
                    self.ballDetected = True
                    self.timeDetected = 0.0
                else:
                    #print "timedetected : " + str(self.timeDetected) + "deltaTime : " + str(deltaTime) 
                    self.timeDetected += deltaTime
                    if self.timeDetected >= self.delayTime:
                        self.timeEnabled = 0.0
                        self.timeDetected = 0.0
                        self.enabled = True
                        print ("setting coil high")
                        GPIO.output(self.coilPin, self.HIGH)
                        return self.score
        else:
            self.ballDetected = False
            self.timeEnabled += deltaTime
            if self.timeEnabled>self.maxTimeEnabled:
                self.enabled = False
                GPIO.output(self.coilPin, self.LOW)

            if self.switch.getState() == 0:
                self.enabled = False
                GPIO.output(self.coilPin, self.LOW)
        return 0
    
    def disable(self):
        self.enabled = False
        while self.switch.getState() ==1:
            GPIO.output(self.coilPin, self.HIGH) #veilig om dit te doen?

        GPIO.output(self.coilPin, self.LOW)

    def __str__(self):
        return "coil enabled: %s time enabled: %s" % (self.enabled, self.timeEnabled)
