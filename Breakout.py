
import pygame,sys
import math
import time
import random
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,150,0)
orange = (255,69,0)
gold = (255,215,0)
blue = (25,25,112)
pink = (255,20,147)




#Power_Up Variables
BonusCounter = 0

#Gold Block level 4
Bonus1_x = 15
Bonus1_y = 120

#Second Gold Block Level 4
Bonus2_x = 325
Bonus2_y = 550

#Uplist level 4
Bonus3_x = 45
Bonus3_y = 400

#Uplist Level 5
Bonus4_x = 190
Bonus4_y = 400

#Uplift 2 Level 5
Bonus5_x = 605
Bonus5_y = 400

#Downlift LeveL 5
Bonus6_x = 750
Bonus6_y = 150


#Moving Gold Block Level 3
Bonus7_change_x = -.5
Bonus7_x = 250
Bonus7_y = 450

Bonus8_change_x = .5
Bonus8_x = 250
Bonus8_y = 250

#Time
Clock = pygame.time.Clock()
TimeCount = 0

#Random Variable
Random = random.randrange(1,2)

#Time Reset Variables (Captures ticks then subtract to get time)
Timereset1 = 0
Timereset2 = 0
Timereset3 = 0
Timereset4 = 0
Timereset5 = 0
Timereset6 = 0
Timereset7 = 0
Timereset8 = 0
Timereset9 = 0
Timereset10 = 0
Timereset11 = 0



#Counter to freeze the screen temporarily
#8 = 5
#6 = 4
#4 = 3
#2 = 2
#0 = 1
FreezeCounter = 0
#

#Life Color Variables
Live1_color = blue
Live2_color = blue
Live3_color = blue

#Counter for Game Over
LifeCounter = 0

#Score
Score = 0


#Surface
GameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breakout!!!!")
#pygame.display.flip()
GameExit = False

#Paddle Settings
lead_x = 300
lead_y = 580
lead_x_change = 0

#Ball Settings
lead_ball_x = 350
lead_ball_y = 150
lead_ball_change = 0
lead_ball_x_change = 0

#Ball Physics Variable
Vector = -.5

#Level 2 ball settings


#Brick x Values

Brick1_x = 5
Brick2_x = 120
Brick3_x = 235
Brick4_x = 350
Brick5_x = 465
Brick6_x = 580
Brick7_x = 695

Brick8_x = 5
Brick9_x = 120
Brick10_x = 235
Brick11_x = 350
Brick12_x = 465
Brick13_x = 580
Brick14_x = 695

Brick15_x = 5
Brick16_x = 120
Brick17_x = 235
Brick18_x = 350
Brick19_x = 465
Brick20_x = 580
Brick21_x = 695


#List of Brick_x Values
Brick_x_List = []
         
Brick_x_List.append(Brick1_x)
Brick_x_List.append(Brick2_x)
Brick_x_List.append(Brick3_x)
Brick_x_List.append(Brick4_x)
Brick_x_List.append(Brick5_x)
Brick_x_List.append(Brick6_x)
Brick_x_List.append(Brick7_x)



#Life x Values
Live1_x = 665
Live2_x = 700
Live3_x = 735

#Introduction Message

font = pygame.font.SysFont(None,50)
def Begin_Game(text,color,xPosition,yPosition):
    Game_Text = font.render(text, True, color)
    GameDisplay.blit(Game_Text, [xPosition,yPosition])



#Score Variables

ScoreOpen = open("C:\\Users\\Will\\Desktop\\BreakScores.txt","r")
ScoreCounter = 0
Scorelist = []


for i in ScoreOpen:
    Scorelist.append(i.strip())
print(Scorelist)

Score1 = Scorelist[0]
Score2 = Scorelist[1]
Score3 = Scorelist[2]
Score4 = Scorelist[3]
Score5 = Scorelist[4]
Score6 = Scorelist[5]
Score7 = Scorelist[6]
Score8 = Scorelist[7]
Score9 = Scorelist[8]
Score10 = Scorelist[9]

#Begin_Game("Press the left or right arrow keys to start!",red) 
  
#time.sleep(2)


x=1
#Start Screen Loop
while x == 1:
    Begin_Game("Press Space to Begin or Backspace to Exit",gold,40,300)
    Begin_Game("INSTRUCTIONS" , orange,250,100)
    Begin_Game("<- and -> arrow keys to move paddle",white,65,150)
    Begin_Game("Hit the top of the Screen to Win",white,115,220)
    Begin_Game("Press S to view Scores",red,190,420)


    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            GameExit == True
            sys.exit()

        


        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                x = False
                print(1)
            elif event.key == pygame.K_BACKSPACE:
                sys.exit()
            elif event.key == pygame.K_s:
                x = 3

while x == 3:
    GameDisplay.fill(pink)
    Begin_Game("Scores",gold,0,0)
    Begin_Game("1 {0} {1}".format("TRM",Score1),black,0,100)
    Begin_Game("2 {0} {1}".format("ABG",Score2),green,0,150)
    Begin_Game("3 {0} {1}".format("TOW",Score3),green,0,200)
    Begin_Game("4 {0} {1}".format("GLA",Score4),green,0,250)
    Begin_Game("5 {0} {1}".format("SME",Score5),green,0,300)
    Begin_Game("6 {0} {1}".format("IRW",Score6),green,0,350)
    Begin_Game("7 {0} {1}".format("PAO",Score7),green,0,400)
    Begin_Game("8 {0} {1}".format("PWF",Score8),green,0,450)
    Begin_Game("9 {0} {1}".format("WPA",Score9),green,0,500)
    Begin_Game("10 {0} {1}".format("JRS",Score10),green,0,550)
    
    pygame.display.update()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            GameExit == True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = 4
    
        #elif x == False:
         #   print(1)
          #  break
        

#Game Loop
#Ball Movement
#Paddle Movement
while not GameExit:
    #print(lead_ball_y)
    #Lives Statement
    Random = random.randrange(1,3)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            GameExit == True
            sys.exit()
     
        


       

        if event.type == pygame.KEYDOWN:
            if FreezeCounter < 4:
                if event.key == pygame.K_SPACE:
                    print(Random)
                    if Random == 1:
                        lead_ball_change = .5
                        lead_ball_x_change = .5
                    elif Random == 2:
                        lead_ball_change = .5
                        lead_ball_x_change = -.5
                elif event.key == pygame.K_LEFT:
                        lead_x_change = -.8
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = .8
            elif FreezeCounter == 4:
                if event.key == pygame.K_SPACE:
                    if Random == 1:
                        lead_ball_change = .7
                        lead_ball_x_change = .7
                    elif Random == 2:
                        lead_ball_change = .7
                        lead_ball_x_change = -.7
                elif event.key == pygame.K_LEFT:
                        lead_x_change = -.8
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = .8
            elif FreezeCounter == 6:
                if event.key == pygame.K_SPACE:
                    if Random == 1:
                        lead_ball_change = .3
                        lead_ball_x_change = .3
                    elif Random == 2:
                        lead_ball_change = .3
                        lead_ball_x_change = -.3
                elif event.key == pygame.K_LEFT:
                        lead_x_change = -.8
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = .8

            elif FreezeCounter == 8:
                if event.key == pygame.K_SPACE:
                    if Random == 1:
                        lead_ball_change = .3
                        lead_ball_x_change = .3
                    elif Random == 2:
                        lead_ball_change = .3
                        lead_ball_x_change = -.3
                elif event.key == pygame.K_LEFT:
                        lead_x_change = -.8
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = .8
                

   

        
        
        
            

   




    #Paddle Boundary
    if lead_x > 670:
      lead_x = 670
    
    elif lead_x < 0:
        lead_x = 0

    #Paddle Collision
    if lead_ball_y <= 600 and lead_ball_y >= 570:
        if lead_ball_x <= lead_x + 130 and lead_ball_x > lead_x:
            lead_ball_change = -.5

    #Ball Side Boundary "No Physics Yet"
    if lead_ball_x > 790:
        if FreezeCounter < 4:
            lead_ball_x_change  = -.5
        elif FreezeCounter == 4:
            lead_ball_x_change = -.7
        elif FreezeCounter == 6:
            lead_ball_x_change = -.8
        elif FreezeCounter == 8:
            lead_ball_x_change = -.8

    elif lead_ball_x < 0:
        if FreezeCounter < 4:
            lead_ball_x_change = .5
        elif FreezeCounter == 4:
            lead_ball_x_change = .7
        elif FreezeCounter == 6:
            lead_ball_x_change = .8
        elif FreezeCounter == 8:
            lead_ball_x_change = .8
    
    #Ball Bottom Screen "boundary"
    #if lead_ball_y > 590:
     #   lead_ball_y = 590


   


    #Physics
    #if lead_ball == lead_x:
        

    #Brick Break


    #Movement
    lead_x += lead_x_change
    lead_ball_y += lead_ball_change
    lead_ball_x += lead_ball_x_change



    #Background
    GameDisplay.fill(green)

    #TODO: Ball Top Screen Win Logic

    

    #Level 2
    if lead_ball_y < 0:
        
        if FreezeCounter == 0:  
            
            Begin_Game("You Win!",white,300,125)
            Begin_Game("Preparing Level 2...",white,220,300)
            lead_ball_y = 150
            lead_ball_x = 350
            lead_ball_change = 0
            lead_ball_x_change = 0
            pygame.display.update()
            time.sleep(2)
            FreezeCounter += 1
        
            
       
          
        #lead_ball_y = 350
        #lead_ball_change = 0
                                                                             
               #Replacing first row of bricks for level 2
    if FreezeCounter == 1:
        Brick1_x = 5
        Brick2_x = 120
        Brick3_x = 235
        Brick4_x = 350
        Brick5_x = 465
        Brick6_x = 580
        Brick7_x = 695
        Brick8_x = 5
        Brick9_x = 120
        Brick10_x = 235
        Brick11_x = 350
        Brick12_x = 465
        Brick13_x = 580
        Brick14_x = 695
        FreezeCounter += 1
        print(50000)
  
        print(100000)
        
    
        
        
        
               
    
        
   
    
    #Level 3
    if lead_ball_y < 0:
        if FreezeCounter == 2:
            Begin_Game("You Win!",white,300,125)
            Begin_Game("Preparing Level 3...",white,220,300)
            lead_ball_y = 150
            lead_ball_x = 350
            lead_ball_change = 0
            lead_ball_x_change = 0
            pygame.display.update()
            time.sleep(2)
            FreezeCounter += 1

        if FreezeCounter == 3:
            Brick1_x = 5
            Brick2_x = 120
            Brick3_x = 235
            Brick4_x = 350
            Brick5_x = 465
            Brick6_x = 580
            Brick7_x = 695
            Brick8_x = 5
            Brick9_x = 120
            Brick10_x = 235
            Brick11_x = 350
            Brick12_x = 465
            Brick13_x = 580
            Brick14_x = 695
            FreezeCounter += 1
       

           
    #Level 4
    if lead_ball_y < 0:
        if FreezeCounter == 4:
            Begin_Game("You Win!",white,300,125)
            Begin_Game("Preparing Level 4...",white,220,300)
            lead_ball_y = 150
            lead_ball_x = 350
            lead_ball_change = 0
            lead_ball_x_change = 0
            pygame.display.update()
            time.sleep(2)
            FreezeCounter += 1
        if FreezeCounter == 5:
            Brick1_x = 5
            Brick2_x = 120
            Brick3_x = 235
            Brick4_x = 350
            Brick5_x = 465
            Brick6_x = 580
            Brick7_x = 695
            Brick8_x = 5
            Brick9_x = 120
            Brick10_x = 235
            Brick11_x = 350
            Brick12_x = 465
            Brick13_x = 580
            Brick14_x = 695
            FreezeCounter += 1

    #Level 5
    if lead_ball_y < 0:


        if FreezeCounter == 6:
            Begin_Game("You Win!",white,300,125)
            Begin_Game("Preparing Final Level!",red,220,300)
            lead_ball_y = 350
            lead_ball_x = 350
            lead_ball_change = 0
            lead_ball_x_change = 0
            pygame.display.update()
            time.sleep(2)
            FreezeCounter += 1

        if FreezeCounter == 7:
            Brick1_x = 5
            Brick2_x = 120
            Brick3_x = 235
            Brick4_x = 350
            Brick5_x = 465
            Brick6_x = 580
            Brick7_x = 695
            Brick8_x = 5
            Brick9_x = 120
            Brick10_x = 235
            Brick11_x = 350
            Brick12_x = 465
            Brick13_x = 580
            Brick14_x = 695
            FreezeCounter += 1

                                
        

            
    #Score Text
    Begin_Game("Score {0}".format(Score),blue,20,560)


    #Timer
   
    Timer = pygame.time.get_ticks()
    

 
    
    if TimeCount == 0:
        Begin_Game("Time {0}".format(round((Timer)/1000)),white,20,520)
        Timereset1 = int(pygame.time.get_ticks())
    

    if TimeCount == 1:
        Begin_Game("Time {0}".format(round((Timer - Timereset1)/1000)),white,20,520)
        Timereset2 = int(pygame.time.get_ticks())

    if TimeCount == 2:
        Begin_Game("Time {0}".format(round((Timer - Timereset2)/1000)),white,20,520)
        Timereset3 = int(pygame.time.get_ticks())

    if TimeCount == 3:
        Begin_Game("Time {0}".format(round((Timer - Timereset3)/1000)),white,20,520)
        Timereset4 = int(pygame.time.get_ticks())

    if TimeCount == 4:
        Begin_Game("Time {0}".format(round((Timer - Timereset4)/1000)),white,20,520)
        Timereset5 = int(pygame.time.get_ticks())

    if TimeCount == 5:
        Begin_Game("Time {0}".format(round((Timer - Timereset5)/1000)),white,20,520)
        Timereset6 = int(pygame.time.get_ticks())

    if TimeCount == 6:
        Begin_Game("Time {0}".format(round((Timer - Timereset6)/1000)),white,20,520)
        Timereset7 = int(pygame.time.get_ticks())

    if TimeCount == 7:
        Begin_Game("Time {0}".format(round((Timer - Timereset7)/1000)),white,20,520)
        Timereset8 = int(pygame.time.get_ticks())

    if TimeCount == 8:
        Begin_Game("Time {0}".format(round((Timer - Timereset8)/1000)),white,20,520)
        Timereset9 = int(pygame.time.get_ticks())

    if TimeCount == 9:
        Begin_Game("Time {0}".format(round((Timer - Timereset9)/1000)),white,20,520)
        Timereset10 = int(pygame.time.get_ticks())

    if TimeCount == 10:
        Begin_Game("Time {0}".format(round((Timer - Timereset10)/1000)),white,20,520)
        Timereset11 = int(pygame.time.get_ticks())
        
       
 

  

    
    #pygame.time.get_ticks
    
     

    #Lives Text

    Begin_Game("LIVES",blue,550,560)

    #Live Object


    Live1 = pygame.draw.rect(GameDisplay,Live1_color,[Live1_x,565,25,25])
    Live2 = pygame.draw.rect(GameDisplay,Live2_color,[Live2_x,565,25,25])
    Live3 = pygame.draw.rect(GameDisplay,Live3_color,[Live3_x,565,25,25])

    

    #Life Lost and GameOver Logic
    if LifeCounter == 0:
        if lead_ball_y > 595:
            Live1_x = 10000
            lead_ball_y = 150
            lead_ball_x = 350
            lead_ball_change = 0
            lead_ball_x_change = 0
            LifeCounter += 1
            print(1)
    elif LifeCounter == 1:
        if lead_ball_y > 595:
            Live2_x = 10000
            lead_ball_y = 150
            lead_ball_x = 350
            lead_ball_change = 0
            lead_ball_x_change = 0
            LifeCounter += 1
            print(1)
    elif LifeCounter == 2:
        if lead_ball_y > 595:
            Live3_x = 10000
            lead_ball_y = 250
            lead_ball_x = 350
            lead_ball_change = 0
            lead_ball_x_change = 0
            LifeCounter += 1
            #while x == False:
            #pygame.display.flip()
            #time.sleep(2)
            if Live1_x == 10000 and Live2_x == 10000 and Live3_x == 10000:
                TimeCount += 1
                while Live1_x == 10000:
                    GameDisplay.fill(black)
                    Begin_Game("Game Over!",white,275,125)
                    Begin_Game("Your Score is {0}!".format(Score - (round(Timer/1000))),white,230,225)
                    Begin_Game("Press space to try again",gold,190,325)
                    Begin_Game("Press backspace to exit",gold,190,425)
                    lead_x = 10000
                    lead_ball_x = 10000
                    
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                
                                Live1_x = 665
                                Live2_x = 700
                                Live3_x = 735
                                lead_ball_x = 350
                                lead_ball_x_change = 0
                                lead_x = 350
                                Score = 0
                                LifeCounter = 0
                                FreezeCounter = 0
                                Brick1_x = 5
                                Brick2_x = 120
                                Brick3_x = 235
                                Brick4_x = 350
                                Brick5_x = 465
                                Brick6_x = 580
                                Brick7_x = 695
                                pygame.display.flip()
 

                            elif event.key == pygame.K_BACKSPACE:
                                sys.exit()
        
 

    #Where I draw,color, x location, y location, width,height
    #Replace x cord with leadx to move left and right
    #Paddle
    pygame.draw.rect(GameDisplay,red,[lead_x,580,130,30])

    #Ball
    pygame.draw.rect(GameDisplay,white,[lead_ball_x,lead_ball_y,10,10])
    


    #Bricks
    Brick1 = pygame.draw.rect(GameDisplay,black,[Brick1_x,5,100,30])
    Brick2 = pygame.draw.rect(GameDisplay,black,[Brick2_x,5,100,30])
    Brick3 = pygame.draw.rect(GameDisplay,black,[Brick3_x,5,100,30])
    Brick4 = pygame.draw.rect(GameDisplay,black,[Brick4_x,5,100,30])
    Brick5 = pygame.draw.rect(GameDisplay,black,[Brick5_x,5,100,30])
    Brick6 = pygame.draw.rect(GameDisplay,black,[Brick6_x,5,100,30])
    Brick7 =pygame.draw.rect(GameDisplay,black,[Brick7_x,5,100,30])
    if FreezeCounter == 2 or FreezeCounter == 4 or FreezeCounter == 6:
        Brick8 =  pygame.draw.rect(GameDisplay,red,[Brick8_x,55,100,30])
        Brick9 =  pygame.draw.rect(GameDisplay,red,[Brick9_x,55,100,30])
        Brick10 = pygame.draw.rect(GameDisplay,red,[Brick10_x,55,100,30])
        Brick11 = pygame.draw.rect(GameDisplay,red,[Brick11_x,55,100,30])
        Brick12 = pygame.draw.rect(GameDisplay,red,[Brick12_x,55,100,30])
        Brick13 = pygame.draw.rect(GameDisplay,red,[Brick13_x,55,100,30])
        Brick14 = pygame.draw.rect(GameDisplay,red,[Brick14_x,55,100,30])

    elif FreezeCounter == 8:
        Brick8 =  pygame.draw.rect(GameDisplay,red,[Brick8_x,55,100,30])
        Brick9 =  pygame.draw.rect(GameDisplay,red,[Brick9_x,55,100,30])
        Brick10 = pygame.draw.rect(GameDisplay,red,[Brick10_x,55,100,30])
        Brick11 = pygame.draw.rect(GameDisplay,red,[Brick11_x,55,100,30])
        Brick12 = pygame.draw.rect(GameDisplay,red,[Brick12_x,55,100,30])
        Brick13 = pygame.draw.rect(GameDisplay,red,[Brick13_x,55,100,30])
        Brick14 = pygame.draw.rect(GameDisplay,red,[Brick14_x,55,100,30])
        Brick15 = pygame.draw.rect(GameDisplay,gold,[Brick15_x,105,100,30])
        Brick16 = pygame.draw.rect(GameDisplay,gold,[Brick16_x,105,100,30])
        Brick17 = pygame.draw.rect(GameDisplay,gold,[Brick17_x,105,100,30])
        Brick18 = pygame.draw.rect(GameDisplay,gold,[Brick18_x,105,100,30])
        Brick19 = pygame.draw.rect(GameDisplay,gold,[Brick19_x,105,100,30])
        Brick20 = pygame.draw.rect(GameDisplay,gold,[Brick20_x,105,100,30])
        Brick21 = pygame.draw.rect(GameDisplay,gold,[Brick21_x,105,100,30])
        

 #Brick Break
    #if lead_ball_y == Brick4[0] and lead_ball_y == Brick4[1]:

#Brick 1
    if lead_ball_y <= 35 and lead_ball_y >= 5:
        if lead_ball_x >= Brick1_x and lead_ball_x <= 120:
            Brick1_x = 10000
            
            Score += 10

            if FreezeCounter < 4:
                lead_ball_change = .5
            elif FreezeCounter == 4:
                lead_ball_change = .7
            elif FreezeCounter == 6:
                lead_ball_change = .8
            elif FreezeCounter == 8:
                lead_ball_change = .8

            if FreezeCounter == 8:
                LifeCounter = 2
                Live1_x = 10000
                Live2_x = 10000
                Live3_x = 10000
                lead_ball_y = 600



#Brick 2
    if lead_ball_y <= 35 and lead_ball_y >= 5:
        if lead_ball_x >= Brick2_x and lead_ball_x <= 235:
            Brick2_x = 10000
            lead_ball_change = .5
            Score += 10
            if FreezeCounter < 4:
                lead_ball_change = .5
            elif FreezeCounter == 4:
                lead_ball_change = .7
            elif FreezeCounter == 6:
                lead_ball_change = .8
            elif FreezeCounter == 8:
                lead_ball_change = .8
            


#Brick 3
    if lead_ball_y <= 35 and lead_ball_y >= 5:
        if lead_ball_x >= Brick3_x and lead_ball_x <= 350:
            Brick3_x = 10000
            lead_ball_change = .5
            Score += 10
            if FreezeCounter < 4:
                lead_ball_change = .5
            elif FreezeCounter == 4:
                lead_ball_change = .7
            elif FreezeCounter == 6:
                lead_ball_change = .8
            elif FreezeCounter == 8:
                lead_ball_change = .8
#Brick 4 
    if lead_ball_y <= 35 and lead_ball_y >= 5:
        if lead_ball_x >= Brick4_x and lead_ball_x <= 445:
    
            Brick4_x = 10000

            lead_ball_change = .5
            Score += 10
            if FreezeCounter < 4:
                lead_ball_change = .5
            elif FreezeCounter == 4:
                lead_ball_change = .7
            elif FreezeCounter == 6:
                lead_ball_change = .8
            elif FreezeCounter == 8:
                lead_ball_change = .8

            if FreezeCounter == 8:
                FreezeCounter = 6
            
    
#Brick 5
    if lead_ball_y <= 35 and lead_ball_y >= 5:
        if lead_ball_x >= Brick5_x and lead_ball_x <= 560:
           lead_ball_change = .5
           Score += 10
           Brick5_x = 10000
           if FreezeCounter < 4:
                lead_ball_change = .5
           elif FreezeCounter == 4:
                lead_ball_change = .7
           elif FreezeCounter == 6:
                lead_ball_change = .8
           elif FreezeCounter == 8:
                lead_ball_change = .8
            
#Brick 6
    if lead_ball_y <= 35 and lead_ball_y >= 5:
        if lead_ball_x >= Brick6_x and lead_ball_x <= 675:
            lead_ball_change = .5
            Score += 10
            Brick6_x = 10000
            if FreezeCounter < 4:
                lead_ball_change = .5
            elif FreezeCounter == 4:
                lead_ball_change = .7
            elif FreezeCounter == 6:
                lead_ball_change = .8
            elif FreezeCounter == 8:
                lead_ball_change = .8
            
    
#Brick 7
    if lead_ball_y <= 35 and lead_ball_y >= 5:
        if lead_ball_x >= Brick7_x and lead_ball_x <= 790:
            lead_ball_change = .5
            Score += 10
            Brick7_x = 10000
            if FreezeCounter < 4:
                lead_ball_change = .5
            elif FreezeCounter == 4:
                lead_ball_change = .7
            elif FreezeCounter == 6:
                lead_ball_change = .8
            elif FreezeCounter == 8:
                #Instant Win
                lead_ball_change = -.8
                lead_ball_y = -50
            


#Brick 8
    if FreezeCounter >= 2:
        if lead_ball_y <= 80 and lead_ball_y >= 40:
            if lead_ball_x >= Brick8_x and lead_ball_x <= 120:
                Score += 10
                Brick8_x = 10000
                if FreezeCounter < 4:
                    lead_ball_change = .5
                elif FreezeCounter == 4:
                    lead_ball_change = .7
                elif FreezeCounter == 6:
                    lead_ball_change = .8
                elif FreezeCounter == 8:
                    lead_ball_change = .8

        #Brick 9
        if lead_ball_y <= 80 and lead_ball_y >= 40:
                if lead_ball_x >= Brick9_x and lead_ball_x <= 235:
                    Score += 10
                    Brick9_x = 10000   
                    if FreezeCounter < 4:
                        lead_ball_change = .5
                    elif FreezeCounter == 4:
                        lead_ball_change = .7
                    elif FreezeCounter == 6:
                        lead_ball_change = .8
                    elif FreezeCounter == 8:
                        lead_ball_change = .8

        #Brick 10

        if lead_ball_y <= 80 and lead_ball_y >= 40:
                if lead_ball_x >= Brick10_x and lead_ball_x <= 350:
                    Score += 10
                    Brick10_x = 10000
                    if FreezeCounter < 4:
                        lead_ball_change = .5
                    elif FreezeCounter == 4:
                        lead_ball_change = .7
                    elif FreezeCounter == 6:
                        lead_ball_change = .8
                    elif FreezeCounter == 8:
                        lead_ball_change = .8
        #Brick 11
        if lead_ball_y <= 80 and lead_ball_y >= 40:
                if lead_ball_x >= Brick11_x and lead_ball_x <= 445:
                    Score += 10
                    Brick11_x = 10000
                    if FreezeCounter < 4:
                        lead_ball_change = .5
                    elif FreezeCounter == 4:
                        lead_ball_change = .7
                    elif FreezeCounter == 6:
                        lead_ball_change = .8
                    elif FreezeCounter == 8:
                        lead_ball_change = .8

        #Brick 12
        if lead_ball_y <= 80 and lead_ball_y >= 40:
                if lead_ball_x >= Brick12_x and lead_ball_x <= 560:
                    Score += 10
                    Brick12_x = 10000
                    if FreezeCounter < 4:
                        lead_ball_change = .5
                    elif FreezeCounter == 4:
                        lead_ball_change = .7
                    elif FreezeCounter == 6:
                        lead_ball_change = .8
                    elif FreezeCounter == 8:
                        lead_ball_change = .8

        #Brick 13
        if lead_ball_y <= 80 and lead_ball_y >= 40:
                if lead_ball_x >= Brick13_x and lead_ball_x <= 675:
                    Score += 10
                    Brick13_x = 10000
                    if FreezeCounter < 4:
                        lead_ball_change = .5
                    elif FreezeCounter == 4:
                        lead_ball_change = .7
                    elif FreezeCounter == 6:
                        lead_ball_change = .8
                    elif FreezeCounter == 8:
                        lead_ball_change = .8

        #Brick 14
        if lead_ball_y <= 80 and lead_ball_y >= 40:
                if lead_ball_x >= Brick14_x and lead_ball_x <= 790:
                    Score += 10
                    Brick14_x = 10000
                    if FreezeCounter < 4:
                        lead_ball_change = .5
                    elif FreezeCounter == 4:
                        lead_ball_change = .7
                    elif FreezeCounter == 6:
                        lead_ball_change = .8
                    elif FreezeCounter == 8:
                        lead_ball_change = .8

        if FreezeCounter == 8:

        #Brick 15
            if lead_ball_y <= 125 and lead_ball_y >= 70:
                    if lead_ball_x >= Brick15_x and lead_ball_x <= 120:
                        Score += 10
                        Brick15_x = 10000
                        if FreezeCounter < 4:
                            lead_ball_change = .5
                        elif FreezeCounter == 4:
                            lead_ball_change = .7
                        elif FreezeCounter == 6:
                            lead_ball_change = .8
                        elif FreezeCounter == 8:
                            lead_ball_change = .8

            #Brick 16
            if lead_ball_y <= 125 and lead_ball_y >= 70:
                    if lead_ball_x >= Brick16_x and lead_ball_x <= 235:
                        Score += 10
                        Brick16_x = 10000
                        if FreezeCounter < 4:
                            lead_ball_change = .5
                        elif FreezeCounter == 4:
                            lead_ball_change = .7
                        elif FreezeCounter == 6:
                            lead_ball_change = .8
                        elif FreezeCounter == 8:
                            lead_ball_change = .8

            #Brick 17
            if lead_ball_y <= 125 and lead_ball_y >= 70:
                    if lead_ball_x >= Brick17_x and lead_ball_x <= 350:
                        Score += 10
                        Brick17_x = 10000
                        if FreezeCounter < 4:
                            lead_ball_change = .5
                        elif FreezeCounter == 4:
                            lead_ball_change = .7
                        elif FreezeCounter == 6:
                            lead_ball_change = .8
                        elif FreezeCounter == 8:
                            lead_ball_change = .8

            #Brick 18
            if lead_ball_y <= 125 and lead_ball_y >= 70:
                    if lead_ball_x >= Brick18_x and lead_ball_x <= 445:
                        Score += 10
                        Brick18_x = 10000
                        if FreezeCounter < 4:
                            lead_ball_change = .5
                        elif FreezeCounter == 4:
                            lead_ball_change = .7
                        elif FreezeCounter == 6:
                            lead_ball_change = .8
                        elif FreezeCounter == 8:
                            lead_ball_change = .8

            #Brick 19
            if lead_ball_y <= 125 and lead_ball_y >= 70:
                    if lead_ball_x >= Brick19_x and lead_ball_x <= 560:
                        Score += 10
                        Brick19_x = 10000
                        if FreezeCounter < 4:
                            lead_ball_change = .5
                        elif FreezeCounter == 4:
                            lead_ball_change = .7
                        elif FreezeCounter == 6:
                            lead_ball_change = .8
                        elif FreezeCounter == 8:
                            lead_ball_change = .8
    
            #Brick 20
            if lead_ball_y <= 125 and lead_ball_y >= 70:
                    if lead_ball_x >= Brick20_x and lead_ball_x <= 675:
                        Score += 10
                        Brick20_x = 10000  
                        if FreezeCounter < 4:
                            lead_ball_change = .5
                        elif FreezeCounter == 4:
                            lead_ball_change = .7
                        elif FreezeCounter == 6:
                            lead_ball_change = .8
                        elif FreezeCounter == 8:
                            lead_ball_change = .8

            #Brick 21
            if lead_ball_y <= 125 and lead_ball_y >= 70:
                    if lead_ball_x >= Brick21_x and lead_ball_x <= 790:
                        Score += 10
                        Brick21_x = 10000
                        if FreezeCounter < 4:
                            lead_ball_change = .5
                        elif FreezeCounter == 4:
                            lead_ball_change = .7
                        elif FreezeCounter == 6:
                            lead_ball_change = .8
                        elif FreezeCounter == 8:
                            lead_ball_change = .8



    #Powerup
    
    
    #Gold Blocks level 3
    if FreezeCounter == 4:
        Bonus7 = pygame.draw.rect(GameDisplay,gold,[Bonus7_x,Bonus7_y,20,20])
        Bonus8 = pygame.draw.rect(GameDisplay,gold,[Bonus8_x,Bonus8_y,20,20])
        #print(Bonus7_x)
        Bonus7_x += Bonus7_change_x
        Bonus8_x += Bonus8_change_x
        if Bonus7_x < 0:
            print(2)
            Bonus7_change_x = .5
            
        if Bonus7_x > 780:
            Bonus7_change_x = -.5

        if Bonus8_x < 0:
            Bonus8_change_x = .5

        if Bonus8_x > 780:
            Bonus8_change_x = -.5

        if lead_ball_y >= Bonus7_y and lead_ball_y <= Bonus7_y + 20:
            if lead_ball_x >= Bonus7_x and lead_ball_x <= Bonus7_x + 20:
                Bonus7_x = 10000
                Score+= 20

        if lead_ball_y >= Bonus8_y and lead_ball_y <= Bonus8_y + 20:
            if lead_ball_x >= Bonus8_x and lead_ball_x <= Bonus8_x + 20:
                Bonus8_x = 10000
               
                Score+= 20

        

        #if lead_ball_x >= Bonus7_x
            
    #Gold Block level 4 
    if FreezeCounter == 6:
        Bonus1 = pygame.draw.rect(GameDisplay,gold,[Bonus1_x,Bonus1_y,20,20])
        if lead_ball_y <= 140 and lead_ball_y >= Bonus1_y:
            if lead_ball_x >= Bonus1_x and lead_ball_x <= 35:
                Bonus1_x = 10000
                Score += 20
                BonusCounter += 1
                print("sdfnsdf")

        if BonusCounter == 1:
            Bonus2 = pygame.draw.rect(GameDisplay,gold,[Bonus2_x,Bonus2_y,20,20])
            if lead_ball_y <= 570 and lead_ball_y >= Bonus2_y:
                if lead_ball_x >= Bonus2_x and lead_ball_x <= 345:               
                    Score += 20
                    BonusCounter += 1
                    Bonus2_x = 10000
    #Pink Paddle Level 4
        if BonusCounter == 2:
            Bonus3 = pygame.draw.rect(GameDisplay,pink,[Bonus3_x,Bonus3_y,10,50])
            if lead_ball_x >= Bonus3_x and lead_ball_x <= 55:
                if lead_ball_y <= 450 and lead_ball_y >= Bonus3_y:
                    Score += 30
                    lead_ball_change = -2

       
                        
    #Pink and Black Bars Level 5
    if FreezeCounter == 8:
        Bonus4 = pygame.draw.rect(GameDisplay,pink,[Bonus4_x,Bonus4_y,10,50])
        if lead_ball_x >= Bonus4_x and lead_ball_x <= 200:
            if lead_ball_y <= 450 and lead_ball_y >= Bonus4_y: 
                lead_ball_change = -3

        Bonus5 = pygame.draw.rect(GameDisplay,pink,[Bonus5_x,Bonus5_y,10,50])
        if lead_ball_x >= Bonus5_x and lead_ball_x <= 625:
            if lead_ball_y <= 450 and lead_ball_y >= Bonus5_y: 
                lead_ball_change = -3

        Bonus6 = pygame.draw.rect(GameDisplay,black,[Bonus6_x,Bonus6_y,10,50])
        if lead_ball_x >= Bonus6_x and lead_ball_x <= 760:
            if lead_ball_y <= 200 and lead_ball_y >= Bonus6_y: 
                lead_ball_change = 5



    if FreezeCounter == 8:
        Begin_Game("Mark",pink,15,5)
        Begin_Game("    4",red,360,5)
        Begin_Game("Prof D", white,695,5)
   # print(lead_ball_y)

    
#Begin_Game("Press Space to Begin",white)
#time.sleep(2)

    #print(FreezeCounter)

    #Game Won
    if lead_ball_y < 0:
        if FreezeCounter == 8:
            
            GameDisplay.fill(black)
            Begin_Game("You have beaten the game!",white,150,150)
            Begin_Game("Your Score is {0}".format(Score),white,250,250)
            Begin_Game("Press space to play again or backspace to exit...",orange,0,350)
            
            #Score_Board

            if ScoreCounter == 0:
                if Score > int(Scorelist[-1]):
                    if Score > int(Scorelist[0]):
                        Scorelist[0] = Score
                        #Score1_Name = input("Congratulations! Enter your initials...")
                        Score1 = Score
                        ScoreCounter += 1

                    elif Score > int(Scorelist[1]):
                        Scorelist[1] = Score
                        #Score2_Name = input("Congratulations! Enter your initials...")
                        Score2 = Score
                        ScoreCounter += 1

                    elif Score > int(Scorelist[2]):
                        Scorelist[2] = Score
                        #Score3_Name = input("Congratulations! Enter your initials...")
                        Score3 = Score
                        ScoreCounter += 1

                    elif Score > int(Scorelist[3]):
                        Scorelist[3] = Score
                        #Score4_Name = input("Congratulations! Enter your initials...")
                        Score4 = Score
                        ScoreCounter += 1

                    elif Score > int(Scorelist[4]):
                        Scorelist[4] = Score
                        #Score5_Name = input("Congratulations! Enter your initials...")
                        Score5 = Score

                    elif Score > int(Scorelist[5]):
                        Scorelist[5] = Score
                        #Score6_Name = input("Congratulations! Enter your initials...")
                        Score6 = Score
                        ScoreCounter += 1
            
                    elif Score > int(Scorelist[6]):
                        Scorelist[6] = Score
                        #Score7_Name = input("Congratulations! Enter your initials...")
                        Score7 = Score
                        ScoreCounter += 1

                    elif Score > int(Scorelist[7]):
                        Scorelist[7] = Score
                        #Score8_Name = input("Congratulations! Enter your initials...")
                        Score8 = Score
                        ScoreCounter += 1

                    elif Score > int(Scorelist[8]):
                        Scorelist[8] = Score
                        #Score9_Name = input("Congratulations! Enter your initials...")
                        Score9 = Score
                        ScoreCounter += 1

                    elif Score > int(Scorelist[9]):
                        Scorelist[9] = Score
                        #Score10_Name = input("Congratulations! Enter your initials...")
                        Score10 = Score
                        ScoreCounter += 1

            ScoreWrite = open("C:\\Users\\Will\\Desktop\\BreakScores.txt","w")     
            ScoreWrite.write(str(Scorelist[0]) + "\n")             
            ScoreWrite.write(str(Scorelist[1]) + "\n")         
            ScoreWrite.write(str(Scorelist[2]) + "\n")         
            ScoreWrite.write(str(Scorelist[3]) + "\n")         
            ScoreWrite.write(str(Scorelist[4]) + "\n")         
            ScoreWrite.write(str(Scorelist[5]) + "\n")         
            ScoreWrite.write(str(Scorelist[6]) + "\n")         
            ScoreWrite.write(str(Scorelist[7]) + "\n")      
            ScoreWrite.write(str(Scorelist[8]) + "\n")         
            ScoreWrite.write(str(Scorelist[9]) + "\n")                  

        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            TimeCount += 1
                            FreezeCounter = 0
                            Live1_x = 665
                            Live2_x = 700
                            Live3_x = 735
                            Score = 0
                            ScoreCounter += 1
                            lead_ball_y = 150
                            lead_ball_x = 350
                            lead_ball_change = 0
                            lead_ball_x_change = 0
                            lead_x = 350
                            LifeCounter = 2
                            Brick1_x = 5
                            Brick2_x = 120
                            Brick3_x = 235
                            Brick4_x = 350
                            Brick5_x = 465
                            Brick6_x = 580
                            Brick7_x = 695
                            GameDisplay.fill(green)
                            pygame.display.flip()
 

                        elif event.key == pygame.K_BACKSPACE:
                            sys.exit()
        

    pygame.display.flip()
pygame.quit()
quit()




'''

#ScoreWrite = open("C:\\Users\\Will\\Desktop\\BreakScores.txt","w")
Score = 75

#Score Code
ScoreOpen = open("C:\\Users\\Will\\Desktop\\BreakScores.txt","r")
#ScoreWrite = open("C:\\Users\\Will\\Desktop\\BreakScores.txt","w")
Scorelist = []

for i in ScoreOpen:
    Scorelist.append(i.strip())
print(Scorelist)

if Score > int(Scorelist[0]):
    Scorelist[0] = Score
    Score1 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[1]):
    Scorelist[1] = Score
    Score2 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[2]):
    Scorelist[2] = Score
    Score3 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[3]):
    Scorelist[3] = Score
    Score4 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[4]):
    Scorelist[4] = Score
    Score5 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[5]):
    Scorelist[5] = Score
    Score6 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[6]):
    Scorelist[6] = Score
    Score7 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[7]):
    Scorelist[7] = Score
    Score8 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[8]):
    Scorelist[8] = Score
    Score9 = input("Congratulations! Enter your initials...")

elif Score > int(Scorelist[9]):
    Scorelist[9] = Score
    Score10 = input("Congratulations! Enter your initials...")

print(Scorelist)

#Score Logic
            if Score > int(Scorelist[-1]):
                if Score > int(Scorelist[0]):
                    Scorelist[0] = Score
                    Score1_Name = input("Congratulations! Enter your initials...")
                    Score1 = Score

                elif Score > int(Scorelist[1]):
                    Scorelist[1] = Score
                    Score2_Name = input("Congratulations! Enter your initials...")
                    Score2 = Score

                elif Score > int(Scorelist[2]):
                    Scorelist[2] = Score
                    Score3_Name = input("Congratulations! Enter your initials...")
                    Score3 = Score


                elif Score > int(Scorelist[3]):
                    Scorelist[3] = Score
                    Score4_Name = input("Congratulations! Enter your initials...")
                    Score4 = Score

                elif Score > int(Scorelist[4]):
                    Scorelist[4] = Score
                    Score5_Name = input("Congratulations! Enter your initials...")
                    Score5 = Score

                elif Score > int(Scorelist[5]):
                    Scorelist[5] = Score
                    Score6_Name = input("Congratulations! Enter your initials...")
                    Score6 = Score
            
                elif Score > int(Scorelist[6]):
                    Scorelist[6] = Score
                    Score7_Name = input("Congratulations! Enter your initials...")
                    Score7 = Score

                elif Score > int(Scorelist[7]):
                    Scorelist[7] = Score
                    Score8_Name = input("Congratulations! Enter your initials...")
                    Score8 = Score

                elif Score > int(Scorelist[8]):
                    Scorelist[8] = Score
                    Score9_Name = input("Congratulations! Enter your initials...")
                    Score9 = Score

                elif Score > int(Scorelist[9]):
                    Scorelist[9] = Score
                    Score10_Name = input("Congratulations! Enter your initials...")
                    Score10 = Score
'''