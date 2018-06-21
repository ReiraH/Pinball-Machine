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
from ScoreChanger import *

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
    print ("Creating Switches")
    lowerRightScoreSwitch = Switch("Lower Right Score Switch", CHIPONE, 0)
    upperRightScoreSwitch = Switch("Upper Right Score Switch", CHIPONE, 1)
    upperLeftScoreSwitch = Switch("Upper Left Score Switch", CHIPONE, 2)
    upperLeftBallGate = Switch("Upper Left Ball Gate", CHIPONE, 3)
    tiltSwitch = Switch("Tilt Switch", CHIPONE, 4)
    hPointsSwitch = Switch("100 Points Switch", CHIPONE, 11)
    upperRightBallGate = Switch("Upper Right Ball Gate", CHIPONE, 12)
    middleLeftScoreSwitch = Switch("Middle Left Score Switch", CHIPONE, 13)
    middleRightScoreSwitch = Switch("Middle Right Score Switch", CHIPONE, 14)
    lowerLeftScoreSwitch = Switch("Lower Left Score Switch", CHIPONE, 15)

    print ("Chip One Done")

    lowerRightBallGate = Switch("Lower Right Ball Gate", CHIPTWO, 0)
    ballLaunchBallGate = Switch("Ball Launch Ball Gate", CHIPTWO, 1)
    upperHoleSwitch = Switch("Upper Hole Ball Detection Switch", CHIPTWO, 2)
    rightHoleSwitch = Switch("Right Hole Ball Detection Switch", CHIPTWO, 3)
    lowerLeftBumperCoilEnabledSwitch = Switch("Lower Left Bumper Coil Enabled Switch", CHIPTWO, 4)
    upperRightBumperCoilEnabledSwitch = Switch("Upper Right Bumper Coil Enabled Switch", CHIPTWO, 5)
    lowerRightBumperCoilEnabledSwitch = Switch("Lower Right Bumper Coil Enabled Switch", CHIPTWO, 6)
    upperLeftBumperCoilEnabledSwitch = Switch("Upper Left Bumper Coil Enabled Switch", CHIPTWO, 7)
    upperLeftBumperBallDetectionSwitch = Switch("Upper Left Bumper Ball Detection Switch", CHIPTWO, 8)
    lowerRightBumperBallDetectionSwitch = Switch("Lower Right Bumper Ball Detection Switch", CHIPTWO, 9)
    upperRightBumperBallDetectionSwitch = Switch("Upper Right Bumper Ball Detection Switch", CHIPTWO, 10)
    lowerLeftBumperBallDetectionSwitch = Switch("Lower Left Bumper Ball Detection Switch", CHIPTWO, 11)
    leftHoleSwitch = Switch("Left Hole Ball Detection Switch", CHIPTWO, 12)
    scrubModePositionDetectionSwitch = Switch("Scrub Mode Position Detection Switch", CHIPTWO, 13)
    gameOverBallGate = Switch("Game Over Ball Gate", CHIPTWO, 14)
    lowerLeftBallGate = Switch("Lower Left Ball Gate", CHIPTWO, 15)

    print ("Chip Two Done")

    upperRightKickerBallDetectionSwitch = Switch("Upper Right Kicker Ball Detection Switch", CHIPTHREE, 2)
    lowerRightKickerBallDetectionSwitch = Switch("Lower Right Kicker Ball Detection Switch", CHIPTHREE, 3)
    rightKickerCoilEnabledSwitch = Switch("Right Kicker Coil Enabled Switch", CHIPTHREE, 4)
    upperLeftTarget = Switch("Upper Left Target", CHIPTHREE, 5)
    middleLeftTarget = Switch("Middle Left Target", CHIPTHREE, 6)
    lowerLeftTarget = Switch("Lower Left Target", CHIPTHREE, 7)
    lowerRightTarget = Switch("Lower Right Target", CHIPTHREE, 8)
    middleRightTarget = Switch("Middle Right Target", CHIPTHREE, 9)
    upperRightTarget = Switch("Upper Right Target", CHIPTHREE, 10)
    leftKickerCoilEnabledSwitch = Switch("Left Kicker Coil Enabled Switch", CHIPTHREE, 11)
    lowerLeftKickerBallDetectionSwitch = Switch("Lower Left Kicker Ball Detection Switch", CHIPTHREE, 12)
    upperLeftKickerBallDetectionSwitch = Switch("Upper Left Kicker Ball Detection Switch", CHIPTHREE, 13)
    startResetSwitch = Switch("Start Switch", CHIPTHREE, 15)
    leftFlipperSwitch = Switch("Left Flipper Switch", CHIPTHREE, 14)

    print ("Chip Three Done")

    #Coils Creation
    print ("Creating Coils" )
    
     #flippers
    GPIO.setup(6, GPIO.OUT,initial=LOW)
    
    #ball pusher
    GPIO.setup(24, GPIO.OUT,initial=LOW)
    
    middleHole = Hole("middleHole",19,upperHoleSwitch)
    GPIO.setup(middleHole.coilPin, GPIO.OUT,initial=LOW)

    rightHole = Hole("rightHole",18,rightHoleSwitch)
    GPIO.setup(rightHole.coilPin, GPIO.OUT,initial=LOW)

    leftHole = Hole("leftHole",17,leftHoleSwitch)
    GPIO.setup(leftHole.coilPin, GPIO.OUT,initial=LOW)

    rightKicker = Kicker("rightKicker",11,upperRightKickerBallDetectionSwitch,lowerRightKickerBallDetectionSwitch,rightKickerCoilEnabledSwitch)
    GPIO.setup(rightKicker.coilPin, GPIO.OUT,initial=LOW)

    leftKicker = Kicker("leftKicker",5,upperLeftKickerBallDetectionSwitch,lowerLeftKickerBallDetectionSwitch,leftKickerCoilEnabledSwitch)
    GPIO.setup(leftKicker.coilPin, GPIO.OUT,initial=LOW)

    lowerLeftBumper = Bumper("lowerLeftBumper",26,lowerLeftBumperBallDetectionSwitch,lowerLeftBumperCoilEnabledSwitch)
    GPIO.setup(lowerLeftBumper.coilPin, GPIO.OUT,initial=LOW)

    topLeftBumper = Bumper("topLeftBumper",13,upperLeftBumperBallDetectionSwitch,upperLeftBumperCoilEnabledSwitch)
    GPIO.setup(topLeftBumper.coilPin, GPIO.OUT,initial=LOW)

    lowerRightBumper = Bumper("lowerRightBumper",19,lowerRightBumperBallDetectionSwitch,lowerRightBumperCoilEnabledSwitch)
    GPIO.setup(lowerRightBumper.coilPin, GPIO.OUT,initial=LOW)

    topRightBumper = Bumper("topRightBumper",21,upperRightBumperBallDetectionSwitch,upperRightBumperCoilEnabledSwitch)
    GPIO.setup(topRightBumper.coilPin, GPIO.OUT,initial=LOW)

    scrubMode = Scrubmode("Scrubmode",10,9,lowerRightTarget,middleRightTarget,lowerLeftTarget,middleLeftTarget,scrubModePositionDetectionSwitch)
    GPIO.setup(scrubMode.coilPinOne, GPIO.OUT,initial=LOW)
    GPIO.setup(scrubMode.coilPinTwo, GPIO.OUT,initial=LOW)

    noobGate = Noobgate("Noobgate",12,lowerRightBallGate,ballLaunchBallGate)
    GPIO.setup(noobGate.coilPin, GPIO.OUT,initial=LOW)

    
    coilList = [rightKicker, leftKicker, lowerLeftBumper, topLeftBumper, lowerRightBumper, topRightBumper, middleHole, rightHole, leftHole]

    
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
            #print ("STATE 000000000000000000000000 iiiiiiiiiiiiffffffffffff statement")
            self.state = 1

    #state 1
    def Initialize(self, deltaTime):
        #print ("STATE 11111111111111111111")
        self.lives = 3
        self.score = 0 
        self.state = 2
        self.firstBall = True

        
        
    def disableCoils(self, disableFlippers):
        for x in self.coilList:
            #print ("disablecoils functie, for x in self.coilList:")
            x.disable()
        if disableFlippers == True:
            #print ("disablecoils functie, if disableFlippers == TRUE")
            #self.scrubMode.disable()
            #self.noobGate.disable()
            GPIO.output(6, self.LOW)

    #state 2
    def NewBall(self, deltaTime):
        #print ("STATE 2222222222222222222222222")
        self.disableCoils(True)
        if self.gameOverBallGate.getState() == 1:
            print ("eerste if is geactiveerd")
            if self.firstBall == False:
               self.lives-=1
               print ("tweede if is geactiveerd")
               if self.lives <= 0:
                   self.state = -1
                   print ("derde if is geactiveerd")
                   return
            print ("BALL PUSHER IS AAN")
            GPIO.output(24, self.HIGH)
            sleep(0.2)
            GPIO.output(24, self.LOW)
            sleep(0.5)

        
        if self.ballLaunchBallGate.getState() == 0:
           print ("ballLaunchBallGate is gelijk aan 0")
           self.state=3
           self.firstBall = False
           self.noobGate.reset()
           #GPIO.output(12, self.HIGH)
           #Turn on Flippers            
           GPIO.output(6, self.HIGH)

    def CheckOtherInputs(self):
        if(self.hPointsSwitch.getState() == 1 or self.upperLeftBallGate.getState() == 1 or self.upperRightBallGate.getState() == 1):
            if self.scoreActive == False:
                self.score += 100
            self.scoreActive == True;
        else:
            self.scoreActive = False
        if(self.lowerLeftScoreSwitch.getState() == 1 or self.lowerRightScoreSwitch.getState() == 1 or self.middleLeftScoreSwitch.getState() == 1 or self.middleRightScoreSwitch.getState() == 1 or self.upperLeftScoreSwitch.getState() == 1 or self.upperRightScoreSwitch.getState() == 1):
            if self.scoreActive == False:
                self.score += 2
                self.scoreActive == True;
        else:
            self.scoreActive = False 
        if(self.lowerLeftBallGate.getState() == 1 or self.lowerRightBallGate.getState() == 1):
            if self.scoreActive == False:
                self.score += 15
                self.scoreActive == True;
        else:
            self.scoreActive = False 

    #state 3
    def GameLogic(self, deltaTime):
        #print ("STATE 3333333333333333333333333333")

        for x in self.coilList:
            self.score += x.update(deltaTime)
        self.scrubMode.update(deltaTime)
        self.noobGate.update(deltaTime)
        self.CheckOtherInputs()
        if self.gameOverBallGate.getState() == 1:
            self.state = 2
        #elif self.tiltSwitch.getState() == 1:
            #self.state = 4
        


    #state 4
    def Tilt(self, deltaTime):
        #print ("STATE 4444444444444444444444")
        #Zet alle Coils even aan
        self.disableCoils(True)
        if self.gameOverBallGate.getState() == 1 or self.ballLaunchBallGate.getState() == 0:
            self.state = 2

    #state 5
    def GameOver(self, deltaTime):
        #print ("STATE 555555555555555555555555")
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
        #print ("STATE -------------11111111111111111111")
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
        
        plaats =x
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
    
    
