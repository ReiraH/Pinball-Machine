from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.config import Config


class FlipperGame(Widget):
    Score1 = 7777
    Lives1 = 20
    score = NumericProperty(Score1)
    lives = NumericProperty(Lives1)
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
    highscore3 = 100
    

    def update(self, dt):
        if self.lives <=0:
            #self.lives =100
            print("haat piraat")
            if self.score >= FlipperGame.highscore3:
                high = Highscore()
                
                #Clock.schedule_interval(high.update, 1.0/60)
                if self.score >= FlipperGame.highscore2:
                    if self.score >= FlipperGame.highscore1:
                        print("plek 3 gekomen")
                        high.deplaats =1
                        high.setScores()
                        self.lives =100
                        return
                    else:
                        high.deplaats =2
                        print("plek 2 gekomen")
                        high.setScores()
                        self.lives =100
                        return
                else:
                    high.deplaats =3
                    print("plek 3 gekomen")
                    high.setScores()
                    self.lives =100
                    return
            
            return
                    
        self.score +=1
        self.lives -=1
        
class FullImage(Image):
        pass

class Highscore():
    print("werkt een iets meer?")
    naam = ' aaa '
    clickerA = True
    clickerB = True
    
    def update(self,dt):
        self.clickerA# input om naam te schrijven
        self.clickerB# input om te bevestigen
        self.naam
        
    def getLetters():
        letter1 = 'a'
        letter2 = 'a'
        letter3 = 'a'
        deplaats
        for i in range(o,3):
            if i ==0:
                letter1 = letter
            if i ==1:
                letter2 = letter
            if i ==2:
                letter3 = letter
                Highscore.naam =(" ",letter1,letter2,letter3,"")
                break
            for x in range(0,27):
                if Highscore.clickerA == True:
                    x+=1
                if x==27:
                    x=0
                if Highscore.clickerB == True:
                    letter=(chr(ord('a')+x))
                    i +=1
        Naam = Highscore.naam
        return naam
    def setScores():
        
        plaats =Highscore.deplaats
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
        return game
           
   
if __name__ == '__main__':   
        FlipperApp().run()
