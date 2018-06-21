from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.config import Config
import RPi.GPIO as GPIO
from Hole import *
from Kicker import *
from Switch import *
from Bumper import *
from Scrubmode import *
from Noobgate import *
from time import sleep
from MCP23017 import MCP23017
#from ScoreChanger import *

class FlipperGame(Widget):

    GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

    #MCP I2C adresses
    CHIPONE = 0x20
    CHIPTWO = 0x21
    CHIPTHREE = 0x22

    #relais are turned off at a high signal
    HIGH = 0
    LOW = 1


    #Switch creation
    print "Creating Switches"

    # MCP23017 1

    GPA0_R_OND5_S4_RUBBERBAND_KICKER_RECHTS_MIDDEN = Switch("GPA0_R_OND5_S4_RUBBERBAND_KICKER_RECHTS_MIDDEN", CHIPONE, 0)
    GPA1_R_OND6_S9_2_RUBBERBAND_KICKER_RECHTS_BOVEN_BOVENSTE = Switch("GPA1_R_OND6_S9_2_RUBBERBAND_KICKER_RECHTS_BOVEN_BOVENSTE", CHIPONE, 1)
    GPA2_R_OND7_S12_2_RUBBERBAND_KICKER_LINKS_BOVEN_ONDERSTE = Switch("GPA2_R_OND7_S12_2_RUBBERBAND_KICKER_LINKS_BOVEN_ONDERSTE", CHIPONE, 2)
    GPA3_R_OND8_S13_PADDRAAD_LINKS_BOVEN = Switch("GPA3_R_OND8_S13_PADDRAAD_LINKS_BOVEN", CHIPONE, 3)
    GPA4_R_OND5_S27_TILT_SENSOR = Switch("GPA4_R_OND5_S27_TILT_SENSOR", CHIPONE, 4)
    GPA5_LEEG = 5
    GPA6_LEEG = 6
    GPA7_LEEG = 7

    GPB0_LEEG = 8
    GPB1_LEEG = 9
    GPB2_LEEG = 10
    GPB3_R_BVN9_S100_SWITCH_WIT_BOVENAAN = Switch("GPB3_R_BVN9_S100_SWITCH_WIT_BOVENAAN", CHIPONE, 11)
    GPB4_R_BVN8_S8_PADDRAAD_RECHTS_BOVEN = Switch("GPB4_R_BVN8_S8_PADDRAAD_RECHTS_BOVEN", CHIPONE, 12)
    GPB5_R_BVN7_S21_RUBBERBAND_KICKER_LINKS_BOVEN_BOVENSTE = Switch("GPB5_R_BVN7_S21_RUBBERBAND_KICKER_LINKS_BOVEN_BOVENSTE", CHIPONE, 13)
    GPB6_R_BVN6_S9_1_RUBBERBAND_KICKER_RECHTS_BOVEN_ONDERSTE = Switch("GPB6_R_BVN6_S9_1_RUBBERBAND_KICKER_RECHTS_BOVEN_ONDERSTE", CHIPONE, 14)
    GPB7_R_BVN5_S16_RUBBERBAND_KICKER_LINKS_MIDDEN = Switch("GPB7_R_BVN5_S16_RUBBERBAND_KICKER_LINKS_MIDDEN", CHIPONE, 15)

    print ("Chip One Done")



    # MCP23017 2

    GPA0_R_OND1_S26_PADDRAAD_RECHTS_BENEDEN = Switch("GPA0_R_OND1_S26_PADDRAAD_RECHTS_BENEDEN", CHIPTWO, 0)
    GPA1_R_OND2_S24_PADDRAAD_START_BALSCHIETEN = Switch("GPA1_R_OND2_S24_PADDRAAD_START_BALSCHIETEN", CHIPTWO, 1)
    GPA2_R_OND3_S10_WHEEL_MIDDLE = Switch("GPA2_R_OND3_S10_WHEEL_MIDDLE", CHIPTWO, 2)
    GPA3_R_OND4_S2_WHEEL_RIGHT = Switch("GPA3_R_OND4_S2_WHEEL_RIGHT", CHIPTWO, 3)
    GPA4_L_OND1_S17_BUMPER_METAAL_LINKS_BENEDEN = Switch("GPA4_L_OND1_S17_BUMPER_METAAL_LINKS_BENEDEN", CHIPTWO, 4)
    GPA5_L_OND2_S5_BUMPER_METAAL_RECHTS_BOVEN = Switch("GPA5_L_OND2_S5_BUMPER_METAAL_RECHTS_BOVEN", CHIPTWO, 5)
    GPA6_L_OND3_S6_BUMPER_METAAL_RECHTS_BENEDEN = Switch("GPA6_L_OND3_S6_BUMPER_METAAL_RECHTS_BENEDEN", CHIPTWO, 6)
    GPA7_L_OND4_S15_BUMPER_METAAL_LINKS_BOVEN = Switch("GPA7_L_OND4_S15_RUBBERBAND_KICKER_RECHTS_MIDDEN", CHIPTWO, 7)


    GPB0_L_BVN4_S15_BUMPER_PLASTIC_LINKS_BOVEN = Switch("GPB0_L_BVN4_S15_BUMPER_METAAL_LINKS_BOVEN", CHIPTWO, 8)
    GPB1_L_BVN3_S6_BUMPER_PLASTIC_RECHTS_BENEDEN = Switch("GPB1_L_BVN3_S6_BUMPER_PLASTIC_RECHTS_BENEDEN", CHIPTWO, 9)
    GPB2_L_BVN2_S5_BUMPER_PLASTIC_RECHTS_BOVEN = Switch("GPB2_L_BVN2_S5_BUMPER_PLASTIC_RECHTS_BOVEN", CHIPTWO, 10)
    GPB3_L_BVN1_S17_BUMPER_PLASTIC_LINKS_BENEDEN = Switch("GPB3_L_BVN1_S17_BUMPER_PLASTIC_LINKS_BENEDEN", CHIPTWO, 11)
    GPB4_R_BVN4_S17_WHEEL_LEFT = Switch("GPB4_R_BVN4_S17_WHEEL_LEFT", CHIPTWO, 12)
    GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE = Switch("GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE", CHIPTWO, 13)
    GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER = Switch("GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER", CHIPTWO, 14)
    GPB7_R_BVN1_S21_PADDRAAD_LINKS_BENEDEN = Switch("GPB7_R_BVN1_S21_PADDRAAD_LINKS_BENEDEN", CHIPTWO, 15)

    print ("Chip Two Done")


    # MCP23017 3

    GPA0_LEEG = 0
    GPA1_LEEG = 1
    GPA2_L_OND5_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_BOVENSTE = Switch("GPA2_L_OND5_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_BOVENSTE", CHIPTHREE, 2)
    GPA3_L_OND6_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_ONDERSTE = Switch("GPA3_L_OND6_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_ONDERSTE", CHIPTHREE, 3)
    GPA4_L_OND7_S103_RUBBERBAND_KICKER_RECHTS_BENEDEN_SOLENOID = Switch("GPA4_L_OND7_S103_RUBBERBAND_KICKER_RECHTS_BENEDEN_SOLENOID", CHIPTHREE, 4)
    GPA5_L_OND8_S14_GELE_TARGET_LINKS_BOVEN = Switch("GPA5_L_OND8_S14_GELE_TARGET_LINKS_BOVEN", CHIPTHREE, 5)
    GPA6_L_OND9_S18_GELE_TARGET_LINKS_MIDDEN = Switch("GPA6_L_OND9_S18_GELE_TARGET_LINKS_MIDDEN", CHIPTHREE, 6)
    GPA7_L_OND10_S20_GELE_TARGET_LINKS_BENEDEN = Switch("GPA7_L_OND10_S20_GELE_TARGET_LINKS_BENEDEN", CHIPTHREE, 7)


    GPB0_L_BVN10_S1_GELE_TARGET_RECHTS_BENEDEN = Switch("GPB0_L_BVN10_S1_GELE_TARGET_RECHTS_BENEDEN", CHIPTHREE, 8)
    GPB1_L_BVN9_S3_GELE_TARGET_RECHTS_MIDDEN = Switch("GPB1_L_BVN9_S3_GELE_TARGET_RECHTS_MIDDEN", CHIPTHREE, 9)
    GPB2_L_BVN8_S7_GELE_TARGET_RECHTS_BOVEN = Switch("GPB2_L_BVN8_S7_GELE_TARGET_RECHTS_BOVEN", CHIPTHREE, 10)
    GPB3_L_BVN7_S105_RUBBERBAND_KICKER_LINKS_BENEDEN_BOVENSTE_SOLENOID = Switch("GPB3_L_BVN7_S105_RUBBERBAND_KICKER_LINKS_BENEDEN_BOVENSTE_SOLENOID", CHIPTHREE, 11)
    GPB4_L_BVN6_S104_RUBBERBAND_KICKER_LINKS_BENEDEN_ONDERSTE = Switch("GPB4_L_BVN6_S104_RUBBERBAND_KICKER_LINKS_BENEDEN_ONDERSTE", CHIPTHREE, 12)
    GPB5_L_BVN5_S22_RUBBERBAND_KICKER_LINKS_BENEDEN_BOVENSTE = Switch("GPB5_L_BVN5_S22_RUBBERBAND_KICKER_LINKS_BENEDEN_BOVENSTE", CHIPTHREE, 13)
    leftFlipperSwitch = Switch("Left Flipper Switch", CHIPTHREE, 14)
    startResetSwitch = Switch("Start Switch", CHIPTHREE, 15)

    print ("Chip Three Done")


    #Coils Creation
    print ("Creating Coils" )
    
    #flippers
    GPIO.setup(6, GPIO.OUT,initial=LOW)
    
    #ball pusher
    #GPIO.setup(24, GPIO.OUT,initial=LOW)

    SOLENOID_GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER = Hole("GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER",24,GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER)
    GPIO.setup(SOLENOID_GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER.coilPin, GPIO.OUT,initial=LOW)
    
    SOLENOID_GPA2_R_OND3_S10_WHEEL_MIDDLE = Hole("GPA2_R_OND3_S10_WHEEL_MIDDLE",19,GPA2_R_OND3_S10_WHEEL_MIDDLE)
    GPIO.setup(SOLENOID_GPA2_R_OND3_S10_WHEEL_MIDDLE.coilPin, GPIO.OUT,initial=LOW)

    SOLENOID_GPA3_R_OND4_S2_WHEEL_RIGHT = Hole("GPA3_R_OND4_S2_WHEEL_RIGHT",18,GPA3_R_OND4_S2_WHEEL_RIGHT)
    GPIO.setup(SOLENOID_GPA3_R_OND4_S2_WHEEL_RIGHT.coilPin, GPIO.OUT,initial=LOW)

    SOLENOID_GPB4_R_BVN4_S17_WHEEL_LEFT = Hole("GPB4_R_BVN4_S17_WHEEL_LEFT",17,GPB4_R_BVN4_S17_WHEEL_LEFT)
    GPIO.setup(SOLENOID_GPB4_R_BVN4_S17_WHEEL_LEFT.coilPin, GPIO.OUT,initial=LOW)

    rightKicker = Kicker("rightKicker",16,GPA2_L_OND5_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_BOVENSTE, GPA3_L_OND6_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_ONDERSTE, GPA4_L_OND7_S103_RUBBERBAND_KICKER_RECHTS_BENEDEN_SOLENOID)
    GPIO.setup(rightKicker.coilPin, GPIO.OUT,initial=LOW)

    leftKicker = Kicker("leftKicker",13,GPB3_L_BVN7_S105_RUBBERBAND_KICKER_LINKS_BENEDEN_BOVENSTE_SOLENOID,GPB4_L_BVN6_S104_RUBBERBAND_KICKER_LINKS_BENEDEN_ONDERSTE,GPA4_L_OND7_S103_RUBBERBAND_KICKER_RECHTS_BENEDEN_SOLENOID)
    GPIO.setup(leftKicker.coilPin, GPIO.OUT,initial=LOW)

    lowerLeftBumper = Bumper("lowerLeftBumper",23,GPB3_L_BVN1_S17_BUMPER_PLASTIC_LINKS_BENEDEN,GPA4_L_OND1_S17_BUMPER_METAAL_LINKS_BENEDEN)
    GPIO.setup(lowerLeftBumper.coilPin, GPIO.OUT,initial=LOW)

    topLeftBumper = Bumper("topLeftBumper",20, GPB0_L_BVN4_S15_BUMPER_PLASTIC_LINKS_BOVEN, GPA7_L_OND4_S15_BUMPER_METAAL_LINKS_BOVEN)
    GPIO.setup(topLeftBumper.coilPin, GPIO.OUT,initial=LOW)

    lowerRightBumper = Bumper("lowerRightBumper",22,GPB1_L_BVN3_S6_BUMPER_PLASTIC_RECHTS_BENEDEN,GPA6_L_OND3_S6_BUMPER_METAAL_RECHTS_BENEDEN)
    GPIO.setup(lowerRightBumper.coilPin, GPIO.OUT,initial=LOW)

    topRightBumper = Bumper("topRightBumper",21,GPB2_L_BVN2_S5_BUMPER_PLASTIC_RECHTS_BOVEN,GPA5_L_OND2_S5_BUMPER_METAAL_RECHTS_BOVEN)
    GPIO.setup(topRightBumper.coilPin, GPIO.OUT,initial=LOW)

    scrubMode = Scrubmode("Scrubmode",4,5,GPA5_L_OND8_S14_GELE_TARGET_LINKS_BOVEN, GPA6_L_OND9_S18_GELE_TARGET_LINKS_MIDDEN, GPA7_L_OND10_S20_GELE_TARGET_LINKS_BENEDEN,GPB0_L_BVN10_S1_GELE_TARGET_RECHTS_BENEDEN,GPB1_L_BVN9_S3_GELE_TARGET_RECHTS_MIDDEN,GPB2_L_BVN8_S7_GELE_TARGET_RECHTS_BOVEN,GPB5_R_BVN3_S101_RODE_KNOP_SCROBMODE)
    GPIO.setup(scrubMode.coilPinOne, GPIO.OUT,initial=LOW)
    GPIO.setup(scrubMode.coilPinTwo, GPIO.OUT,initial=LOW)

    noobGate = Noobgate("Noobgate",12,GPA0_R_OND1_S26_PADDRAAD_RECHTS_BENEDEN,GPA1_R_OND2_S24_PADDRAAD_START_BALSCHIETEN)
    GPIO.setup(noobGate.coilPin, GPIO.OUT,initial=LOW)


    coilList = [rightKicker, leftKicker, lowerLeftBumper, topLeftBumper, lowerRightBumper, topRightBumper, SOLENOID_GPA2_R_OND3_S10_WHEEL_MIDDLE, GPA3_R_OND4_S2_WHEEL_RIGHT, GPB4_R_BVN4_S17_WHEEL_LEFT]

    
    state = 0
    resetSwitchDuration = 0.0
    resetMaxDuration = 2.0
    firstBall = True

    score = 0
    lives = 0
    screenScore = NumericProperty(score)
    screenLives = NumericProperty(lives)

    #scoreChanger = ScoreChanger()


    
    filename="highscore.txt" 
    file=open(filename,'r')
    plaats1=file.readline()
    plaats2=file.readline()
    plaats3 = file.readline()
    isRunning = True
    high_score1 = plaats1.split()
    highscore1 = high_score1[1]
    high_score2 = plaats2.split()
    highscore2 = high_score2[1]
    high_score3 = plaats3.split()
    highscore3 = high_score3[1]

    elapsedTime = 0.0

    scoreActive = False

    #STATES:
    #0 - Not Active
    #1 - Initializing
    #2 - New Ball
    #3 - Game Logic
    #4 - Tilt
    #5 - Game Over
    #-1 - Reset

    #State 0
    def notActive(self, deltaTime):
        #print ("STATE 000000000000000000000000")
        if self.startResetSwitch.getState() == 1:
            print ("STATE 000000000000000000000000 iiiiiiiiiiiiffffffffffff statement")
            self.state = 1

    #state 1
    def Initialize(self, deltaTime):
        print ("STATE 11111111111111111111")
        self.lives = 3
        self.score = 0 
        self.state = 2
        self.firstBall = True

        
        
    def disableCoils(self, disableFlippers):
        #for x in self.coilList:
            #print ("disablecoils functie, for x in self.coilList:")
         #   x.disable()
        if disableFlippers == True:
            print ("disablecoils functie, if disableFlippers == TRUE")
            self.scrubMode.disable()
            self.noobGate.disable()
            GPIO.output(6, self.LOW) #flippers

    #state 2
    def NewBall(self, deltaTime):
        print ("STATE 2222222222222222222222222")
        self.disableCoils(True)
        if self.GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER.getState() == 1:
           print ("eerste if is geactiveerd")
           if self.firstBall == False:
               self.lives-=1
               print ("tweede if is geactiveerd")
               if self.lives <= 0:
                  self.state = -1
                  print ("derde if is geactiveerd")
                  return
                
           print ("BALL PUSHER ..........................")
           GPIO.output(24, self.HIGH) #ball pusher
           print ("BALL PUSHER IS AAN")
           sleep(0.2)
           GPIO.output(24, self.LOW) #ball pusher
           print ("BALL PUSHER IS UIT")
           sleep(0.5)

        
        if self.GPA1_R_OND2_S24_PADDRAAD_START_BALSCHIETEN.getState() == 0:
           print ("GPA1_R_OND2_S24_PADDRAAD_START_BALSCHIETEN is gelijk aan 0")
           self.state=3
           print ("state wordt 3")
           self.firstBall = False
           print ("firstbal is FALSE")
           self.noobGate.reset()
           print ("noobGate resetten")
           GPIO.output(12, self.HIGH) #hekje
           print ("hekje aan")
           #Turn on Flippers            
           GPIO.output(6, self.HIGH) ##flippers
           print ("flippers aan")

    def CheckOtherInputs(self):
        if(self.GPB3_R_BVN9_S100_SWITCH_WIT_BOVENAAN.getState() == 1 or self.GPA3_R_OND8_S13_PADDRAAD_LINKS_BOVEN.getState() == 1 or self.upperRightBallGate.getState() == 1):
            if self.scoreActive == False:
                self.score += 100
            self.scoreActive == True;
        else:
            self.scoreActive = False
        if(self.GPA2_L_OND5_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_BOVENSTE.getState() == 1 or self.GPA3_L_OND6_S25_RUBBERBAND_KICKER_RECHTS_BENEDEN_ONDERSTE.getState() == 1 or self.GPA2_R_OND7_S12_2_RUBBERBAND_KICKER_LINKS_BOVEN_ONDERSTE.getState() == 1 or self.GPB5_R_BVN7_S21_RUBBERBAND_KICKER_LINKS_BOVEN_BOVENSTE.getState() == 1 or self.GPB6_R_BVN6_S9_1_RUBBERBAND_KICKER_RECHTS_BOVEN_ONDERSTE.getState() == 1 or self.GPB7_R_BVN5_S16_RUBBERBAND_KICKER_LINKS_MIDDEN.getState() == 1):
            if self.scoreActive == False:
                self.score += 2
                self.scoreActive == True;
        else:
            self.scoreActive = False 
        if(self.GPB7_R_BVN1_S21_PADDRAAD_LINKS_BENEDEN.getState() == 1 or self.GPA0_R_OND1_S26_PADDRAAD_RECHTS_BENEDEN.getState() == 1):
            if self.scoreActive == False:
                self.score += 15
                self.scoreActive == True;
        else:
            self.scoreActive = False 

    #state 3
    def GameLogic(self, deltaTime):
        print ("STATE 3333333333333333333333333333")

        for x in self.coilList:
            self.score += x.update(deltaTime)
        self.scrubMode.update(deltaTime)
        self.noobGate.update(deltaTime)
        #self.CheckOtherInputs()
        if self.GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER.getState() == 1:
            self.state = 2
        #elif self.tiltSwitch.getState() == 1:
            #self.state = 4
        


    #state 4
    def Tilt(self, deltaTime):
        print ("STATE 4444444444444444444444")
        #Zet alle Coils even aan
        self.disableCoils(True)
        if self.GPB6_R_BVN2_S23_PADDRAAD_BALLPUSHER.getState() == 1 or self.GPA1_R_OND2_S24_PADDRAAD_START_BALSCHIETEN.getState() == 0:
            self.state = 2

    #state 5
    def GameOver(self, deltaTime):
        print ("STATE 555555555555555555555555")
        self.disableCoils(True)

        #handle topscoreshizzle


        print("haat piraat")
        if self.score >= FlipperGame.highscore3:
            high = Highscore()

            #Clock.schedule_interval(high.update, 1.0/60)
            if self.score >= FlipperGame.highscore2:
                if self.score >= FlipperGame.highscore1:
                    print("plek 3 gekomen")
                    high.deplaats =1
                    high.setScores()
                    
                else:
                    high.deplaats =2
                    print("plek 2 gekomen")
                    high.setScores()
                    
            else:
                high.deplaats =3
                print("plek 3 gekomen")
                high.setScores()
                
            
        
        self.state = -1

    #state -1
    def Reset(self, deltaTime):
        print ("STATE -------------11111111111111111111")
        self.disableCoils(True)
        #self.scoreChanger.resetScoreReels
        self.scrubMode.disable()
        self.state = 0


    #creation of state dictionary

    stateFunctionsDict = {0: notActive, 1: Initialize, 2:NewBall, 3:GameLogic, 4:Tilt, 5:GameOver, -1:Reset}
    oldDebugMessage = ""

    #########################################
    #main function. called every 1/60 second#
    #########################################

    def update(self, dt):
        #calculate the time since the last call and update the elapsed time
        deltaTime = dt - self.elapsedTime
        self.elapsedTime = dt
        deltaTime = 1.0 / 60
        #print "State: -1 " + " Score:  0" +  " Lives: " + str(self.lives)
        #print ("State: ")+ str(self.state) + (" Score: ") + str(self.score) + (" Lives: ") + str(self.lives)
        debugMessage = "State: "+ str(self.state) + (" Score: ") + str(self.score) + (" Lives: ") + str(self.lives)
        if(debugMessage != self.oldDebugMessage):
            print(debugMessage)
            self.oldDebugMessage = debugMessage
        #reset the game if the resetswitch is pressed for 5 seconds
        if self.startResetSwitch.getState() == 1 and self.state > 1:
            self.resetSwitchDuration+=deltaTime
            if self.resetSwitchDuration>self.resetMaxDuration:
                self.state = -1
                self.resetSwitchDuration = 0.0

        else:
            self.resetSwitchDuration = 0.0

        #call the state function
        func = self.stateFunctionsDict[self.state]
        func(self, deltaTime)
        self.screenScore=self.score
        self.screenLives=self.lives
        #self.scoreChanger.changeScore(self.score, deltaTime)

       
    #def updateScoreReels(self, dt):
        #if self.state > 1:

            #if self.scoreChanger.active == False:
                #self.scoreChanger.changeScore(self.score)
        


        
class FullImage(Image):
    pass


class Highscore():
        
    def update(self,dt):
        self.clickerA# input om naam te schrijven
        self.clickerB# input om te bevestigen
        self.naam
        
    def getLetters():
        letter1 = 'a'
        letter2 = 'a'
        letter3 = 'a'
        naam = ' aaa '
        for i in range(o,3):
            if i ==0:
                letter1 = letter
            if i ==1:
                letter2 = letter
            if i ==2:
                letter3 = letter
                naam =(" ",letter1,letter2,letter3,"")
            for x in range(0,27):
                if clickerA == True:
                    x+=1
                if x==27:
                    x=0
                if clickerB == True:
                    letter=(chr(ord('a')+x))
                    i +=1
        return naam
    def setScores(x):
        
        plaats = x
        name = getLetters()
        score = FlipperGame.Score1
        theHighscore = (name+ str(score)+"\n")
        file=open("highscore.txt","r+")
        if plaats ==1:   
            file.write(theHighscore)
            file.write(FlipperGame.plaats1)
            file.write(FlipperGame.plaats2)
        if plaats == 2:
            file.write(FlipperGame.plaats1)
            file.write(theHighscore)
            file.write(FlipperGame.plaats2)
        if plaats == 3:
            file.write(FlipperGame.plaats1)
            file.write(FlipperGame.plaats2)
            file.write(theHighscore)
        file.close()
        return 1

    

class FlipperApp(App):
    def build(self):
        
        game = FlipperGame()
        img = FullImage(source = '/home/pi/Desktop/Ruben#/Test/space.png')   
        game.add_widget(img)            
        Clock.schedule_interval(game.update, 1.0/60)
        #Clock.schedule_interval(game.updateScoreReels, 1.0)
        return game
           
   
if __name__ == '__main__':
    try:
        
        FlipperApp().run()

        while True:
            sleep(1)

    finally:
        GPIO.cleanup()
    
    
