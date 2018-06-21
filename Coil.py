class Coil(object):

    def __init__(self, triggerPin):
        self.triggerPin = triggerPin

    def update(self):
        print("update called...")

class Hole(Coil):

    def __init__(self, triggerPin, switchPin):
        Coil.__init__(self, triggerPin)
        self.switchPin = switchPin
        self.maxTimeEnabled = 500
        self.timeEnabled = 0
        self.enabled = False

    def switchPinEnabled(self):
        self.switchPin = True

    def switchPinDisabled(self):
        self.switchPin = False

    def update(self, deltaTime):
        if not self.enabled:

            if self.switchPin:
                self.enabled = True
                self.timeEnabled = 0
                self.triggerPin = True

        else:

            self.timeEnabled += deltaTime

            if self.timeEnabled>self.maxTimeEnabled:
                self.triggerPin = False
                self.enabled = False

            if not self.switchPin:
                self.triggerPin = False
                self.enabled = False
                

    def __str__(self):
        return "coil enabled: %s time enabled: %s" % (self.enabled, self.timeEnabled)


        
        
