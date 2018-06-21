import RPi.GPIO as GPIO
from time import sleep
class ScoreChanger(object):
    HIGH = 0
    LOW = 1
    digitOnes = 24
    digitTens = 23
    digitHundreds = 15
    digitThousands = 18

    A = 0
    B = 0
    C = 0
    D = 0
        
    active = False
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(digitOnes, GPIO.OUT)
    GPIO.output(digitOnes, LOW)

    GPIO.setup(digitTens, GPIO.OUT)
    GPIO.output(digitTens, LOW)

    GPIO.setup(digitHundreds, GPIO.OUT)
    GPIO.output(digitHundreds, LOW)

    GPIO.setup(digitThousands, GPIO.OUT)
    GPIO.output(digitThousands, LOW)
    print "HI I AM A SCORECHANGER!!!!"
    state = 0
    coilActive = False
    timeEnabled = 0.0
    maxTimeEnabled = 0.07



    def changeScore(self,score, deltaTime):
        if self.state == 0:
            inputString = str(score)
            while(inputString.__len__() != 4):
                inputString = "0" + inputString    
            ScoreArray = list(inputString)
            self.newA = int(ScoreArray[0])
            self.atemp = self.newA
            self.newB = int(ScoreArray[1])
            self.btemp = self.newB
            self.newC = int(ScoreArray[2])
            self.ctemp = self.newC
            self.newD = int(ScoreArray[3])
            self.dtemp = self.newD
            print str(self.newD)
            if self.newA < self.A:
                self.newA += 10
            if self.newB < self.B:
                self.newB += 10
            if self.newC < self.C:
                self.newC += 10
            if self.newD < self.D:
                self.newD += 10
            self.state = 1

        elif self.state == 1:
            if self.coilActive == False:
                if self.newA > self.A:
                    self.timeEnabled+=deltaTime
                    if(self.timeEnabled>self.maxTimeEnabled):
                        GPIO.output(self.digitThousands, self.HIGH)
                        self.coilActive = True
                        self.timeEnabled = 0.0
                        self.newA-=1
                else:
                    self.state = 2
            else:
                self.timeEnabled += deltaTime
                if self.timeEnabled > self.maxTimeEnabled:
                    GPIO.output(self.digitThousands, self.LOW)
                    self.coilActive = False
                    self.timeEnabled = 0

        elif self.state == 2:
            if self.coilActive == False:
                if self.newB > self.B:
                    self.timeEnabled+=deltaTime
                    if(self.timeEnabled>self.maxTimeEnabled):
                        GPIO.output(self.digitHundreds, self.HIGH)
                        self.coilActive = True
                        self.timeEnabled = 0.0
                        self.newB-=1
                else:
                    self.state = 3
            else:
                self.timeEnabled += deltaTime
                if self.timeEnabled > self.maxTimeEnabled:
                    GPIO.output(self.digitHundreds, self.LOW)
                    self.coilActive = False
                    self.timeEnabled = 0


        elif self.state == 3:
            if self.coilActive == False:
                if self.newC > self.C:
                    self.timeEnabled+=deltaTime
                    if(self.timeEnabled>self.maxTimeEnabled):
                        GPIO.output(self.digitTens, self.HIGH)
                        self.coilActive = True
                        self.timeEnabled = 0.0
                        self.newC-=1
                else:
                    self.state = 4
            else:
                self.timeEnabled += deltaTime
                if self.timeEnabled > self.maxTimeEnabled:
                    GPIO.output(self.digitTens, self.LOW)
                    self.coilActive = False
                    self.timeEnabled = 0


        elif self.state == 4:
            if self.coilActive == False:
                if self.newD > self.D:
                    self.timeEnabled+=deltaTime
                    if(self.timeEnabled>self.maxTimeEnabled):
                        GPIO.output(self.digitOnes, self.HIGH)
                        self.coilActive = True
                        self.timeEnabled = 0.0
                        self.newD-=1
                else:
                    self.state = 5
            else:
                self.timeEnabled += deltaTime
                if self.timeEnabled > self.maxTimeEnabled:
                    GPIO.output(self.digitOnes, self.LOW)
                    self.coilActive = False
                    self.timeEnabled = 0


        elif self.state == 5:
            self.A = self.atemp
            self.B = self.btemp
            self.C = self.ctemp
            self.D = self.dtemp
            self.state = 0       


                



    def changeScoreOld(self,score):
        if self.active == False:
            self.active = True
            print "Program started"
        


            print "set input function"
            inputString = str(score)
            while(inputString.__len__() != 4):
                inputString = "0" + inputString    
            ScoreArray = list(inputString)
            newA = int(ScoreArray[0])
            atemp = newA
            newB = int(ScoreArray[1])
            btemp = newB
            newC = int(ScoreArray[2])
            ctemp = newC
            newD = int(ScoreArray[3])
            dtemp = newD
            print str(newD)
            if newA < self.A:
                newA += 10
            if newB < self.B:
                newB += 10
            if newC < self.C:
                newC += 10
            if newD < self.D:
                newD += 10
        
            print "HI I AM A SCORECHANGER!!!! Score: "+ inputString + "Last Score: " + str(self.A)+ str(self.B)+ str(self.C)+ str(self.D)

            while(newA  > self.A):
                    GPIO.output(self.digitThousands, self.HIGH)
                    sleep(0.15)
                    GPIO.output(self.digitThousands, self.LOW)
                    sleep(0.15)
                    newA-=1
            while(newB  > self.B):
                    GPIO.output(self.digitHundreds, self.HIGH)
                    sleep(0.15)
                    GPIO.output(self.digitHundreds, self.LOW)
                    sleep(0.15)
                    newB-=1
            while(newC > self.C):
                    GPIO.output(self.digitTens, self.HIGH)
                    sleep(0.15)
                    GPIO.output(self.digitTens, self.LOW)
                    sleep(0.15)
                    newC-=1
            while(newD  > self.D):
                    GPIO.output(self.digitOnes, self.HIGH)
                    sleep(0.15)
                    GPIO.output(self.digitOnes, self.LOW)
                    sleep(0.15)
                    newD-=1
            self.A = atemp
            self.B = btemp
            self.C = ctemp
            self.D = dtemp       
            self.active = False

    def resetScoreReels(self):
        oneAmount = 10 - self.D
        tenAmount = 10 - self.C
        hundredAmount = 10 - self.B
        thousandAmount = 10 - self.A
        if oneAmount != 10:
            for ones in range(0,oneAmount):
                GPIO.output(digitOnes, HIGH)
                sleep(0.1)
                GPIO.output(digitOnes, LOW)
                sleep(0.1)
        
        if tenAmount != 10:
            for tens in range(0,tenAmount):
                
                GPIO.output(digitTens, HIGH)
                sleep(0.1)
                GPIO.output(digitTens, LOW)
                sleep(0.1)
        
        if hundredAmount != 10:
            for hundreds in range(0,hundredAmount):
            
                GPIO.output(digitHundreds, HIGH)
                sleep(0.1)
                GPIO.output(digitHundreds, LOW)
                sleep(0.1)

        if thousandAmount != 10:          
            for thousands in range(0,thousandAmount):
         
                GPIO.output(digitThousands, HIGH)
                sleep(0.1)
                GPIO.output(digitThousands, LOW)
                sleep(0.1)
 