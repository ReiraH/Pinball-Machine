from Switch import Switch
import RPi.GPIO as GPIO

class Scrubmode(object):
    HIGH = 0
    LOW = 1
    def __init__(self,name, coilPinOne,coilPinTwo, GPB0_L_BVN10_S1_GELE_TARGET_RECHTS_BENEDEN,GPB1_L_BVN9_S3_GELE_TARGET_RECHTS_MIDDEN,GPA7_L_OND10_S20_GELE_TARGET_LINKS_BENEDEN,GPA6_L_OND9_S18_GELE_TARGET_LINKS_MIDDEN,GPB2_L_BVN8_S7_GELE_TARGET_RECHTS_BOVEN, GPA5_L_OND8_S14_GELE_TARGET_LINKS_BOVEN, GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE):
        self.maxTimeEnabled = 0.05
        self.timeEnabled = 0.0
        self.inTransition = 0
        self.transitionState = 0
        self.name = name
        self.coilPinOne = coilPinOne
        self.coilPinTwo = coilPinTwo
        self.GPB0_L_BVN10_S1_GELE_TARGET_RECHTS_BENEDEN = GPB0_L_BVN10_S1_GELE_TARGET_RECHTS_BENEDEN
        self.GPB1_L_BVN9_S3_GELE_TARGET_RECHTS_MIDDEN = GPB1_L_BVN9_S3_GELE_TARGET_RECHTS_MIDDEN
        self.GPA7_L_OND10_S20_GELE_TARGET_LINKS_BENEDEN = GPA7_L_OND10_S20_GELE_TARGET_LINKS_BENEDEN
        self.GPA6_L_OND9_S18_GELE_TARGET_LINKS_MIDDEN = GPA6_L_OND9_S18_GELE_TARGET_LINKS_MIDDEN
        self.GPB2_L_BVN8_S7_GELE_TARGET_RECHTS_BOVEN = GPB2_L_BVN8_S7_GELE_TARGET_RECHTS_BOVEN
        self.GPA5_L_OND8_S14_GELE_TARGET_LINKS_BOVEN = GPA5_L_OND8_S14_GELE_TARGET_LINKS_BOVEN
        self.GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE = GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE
    def update(self, deltaTime):
        if self.inTransition == 0:
            #rhea heeft dit en de volgende elif aangepast, omdat er geen rechtsBovenSwitch en rechtsBenedenSwitch bestond
            if self.GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE.getState() == 0 and (self.GPB2_L_BVN8_S7_GELE_TARGET_RECHTS_BOVEN.getState() == 1 or self.GPA5_L_OND8_S14_GELE_TARGET_LINKS_BOVEN.getState() == 1):
                self.timeEnabled = 0
                self.transitionState = 2
                self.inTransition = 1
                GPIO.output(self.coilPinOne, self.HIGH)
                GPIO.output(self.coilPinTwo, self.HIGH)

                
            elif self.GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE.getState() == 1 and (self.GPA6_L_OND9_S18_GELE_TARGET_LINKS_MIDDEN.getState() == 1 or self.GPB1_L_BVN9_S3_GELE_TARGET_RECHTS_MIDDEN.getState() == 1):
                self.timeEnabled = 0
                GPIO.output(self.coilPinOne, self.HIGH)
                self.inTransition = 2

            
            elif self.GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE.getState() == 1 and (self.GPA7_L_OND10_S20_GELE_TARGET_LINKS_BENEDEN.getState() == 1 or self.GPB0_L_BVN10_S1_GELE_TARGET_RECHTS_BENEDEN.getState() == 1):
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
        while self.GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE.getState() == 1:
              GPIO.output(self.coilPinOne, self.HIGH) #veilig om dit te doen?
        GPIO.output(self.coilPinOne, self.LOW)

    def __str__(self):
        return "coil enabled: %s" % (self.GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE.getState())



