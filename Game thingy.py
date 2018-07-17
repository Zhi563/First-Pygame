#=====Imports=====#
import random
import time
import pygame
pygame.init()
#=====Variables=====#
x = 250
y = 250
speed = 1.5
width = 10
height = 10
pointCounter = 0
#***Colours***#
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
#***Apples***#
awidth = 10
aheight = 10
appX = []
appY = []
numOfApp = 0
#***Obstacles***#
obwidth = 10
obheight = 10
obX = []
obY = []
numOfOb = 0
#*****Movement*****#
left = False
right = False
up = False
down = False
#=====Functions=====#
#***APPLES***#
def randomApple():
    global appX,appY,numOfApp,speed
    if len(appX) == 0:
        numOfApp += 1
        obX.clear()
        obY.clear()
        for i in range(8 +(numOfApp*2)):
            appX.append(random.randint(16,475))
            appY.append(random.randint(16,475))            
def spawnApple():
        for i in range (0,len(appX)):
            pygame.draw.rect(screen,green,(appX[i],appY[i],awidth,aheight),0)
            c1 = screen.get_at(((appX[i]-1),(appY[i])-1))
            c2 = screen.get_at(((appX[i]-1),(appY[i]+11)))
            c3 = screen.get_at(((appX[i]+11),(appY[i]-1)))
            c4 = screen.get_at(((appX[i]+11),(appY[i]+11)))
            if c1 == green or c2 == green or c3 == green or c4 == green or c1 == red or c2 == red or c3 == red or c4 == red:
                del (appX[i])
                del (appY[i])
                appX.append(random.randint(16,475))
                appY.append(random.randint(16,475))
def apple():
    # check if eat apple
    global appX,appY,pointCounter
    t = 0
    while t < (len(appX)):
#   check for collision
        if (appX[t] - 10 < x < appX[t] + 10) and (appY[t] - 10 < y < appY[t] + 10):
            del(appX[t])
            del(appY[t])
            pointCounter += 1
        t += 1    
#***OBSTACLES***#
def randomObstacle():#generate obstacles locations
    global obX,obY,numOfOb
    if len(obX) == 0:
        numOfOb += 1
        for i in range(3 +(numOfOb*2)):
            obX.append(random.randint(16,475))
            obY.append(random.randint(16,475))
def spawnObstacle():#spawns all obstacles in list
        for i in range (0,len(obX)):
            pygame.draw.rect(screen,red,(obX[i],obY[i],obwidth,obheight),0)
            c1 = screen.get_at(((obX[i]-1),(obY[i])-1))
            c2 = screen.get_at(((obX[i]-1),(obY[i]+11)))
            c3 = screen.get_at(((obX[i]+11),(obY[i]-1)))
            c4 = screen.get_at(((obX[i]+11),(obY[i]+11)))
            if c1 == red or c2 == red or c3 == red or c4 == red:
                del (obX[i])
                del (obY[i])
                obX.append(random.randint(16,475))
                obY.append(random.randint(16,475))
            if c1 == green or c2 == green or c3 == green or c4 == green:
                del (obX[i])
                del (obY[i])
                obX.append(random.randint(16,475))
                obY.append(random.randint(16,475))
            if c1 != red or c2 != red or c3 != red or c4 != red or c1 != green or c2 != green or c3 != green or c4 != green :
                r = False
def obstacle(): #checks if white touches obstacles
    global q
    c1 = screen.get_at((int(x),int(y)))
    c2 = screen.get_at((int(x+width),int(y+height)))
    c3 = screen.get_at((int(x+width),int(y)))
    c4 = screen.get_at((int(x),int(y+height)))
    if c1 == red or c2 == red or c3 == red or c4 == red:
        q = False
#***Writing***#
def levelOverlay():
    if len(appX) == 0:
        screen.fill(yellow)
        font = pygame.font.SysFont("comicsansms",50,True)
        count = font.render("Level: " +str(numOfApp+1),1,black)
        screen.blit(count,(275,200))
        pygame.display.update()
        pygame.time.delay(1000)
def printThings():
    font = pygame.font.SysFont("comicsansms",20,True)
    totalScore = font.render("Total Score: "+str(pointCounter),1,yellow)
    screen.blit(totalScore,(510,0))
    level = font.render("Level: " +str(numOfApp),1,yellow)
    screen.blit(level,(510,50))
    remaining = font.render("Remaining Cubes: " +str(len(appX)),1,yellow)
    screen.blit(remaining,(510,100))
    collect = font.render("Collect the GREEN",1,green)
    screen.blit(collect,(510,150))
    avoid = font.render("AVOID THE RED",1,red)
    screen.blit(avoid,(510,200))
    instructions = font.render("Use arrow keys to move",1,yellow)
    screen.blit(instructions,(505,300))
#=====Screen=====#
size = (750,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Thing")
#=====Clock=====#
clock = pygame.time.Clock()
#=====Main Loop=====#
q = True
while q:
#=====Borders=====#
    screen.fill(black)
    pygame.draw.rect(screen,red,(0,0,500,500),30)
    pygame.draw.rect(screen,black,(500,0,550,500),0)
    pygame.draw.rect(screen,black,(0,500,500,550),0)
    #Apple Functions
    randomApple()
    spawnApple()
    apple()
    #Obstacle Functions
    randomObstacle()
    spawnObstacle()
    obstacle()

    levelOverlay()
    
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = False
#=====Score and Print=====#
    printThings()
#=====Movement=====#
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_LEFT]:
        left = True
        right = False
        up = False
        down = False
    if keyboard[pygame.K_RIGHT]:
        left = False
        right = True
        up = False
        down = False
    if keyboard[pygame.K_UP]:
        left = False
        right = False
        up = True
        down = False
    if keyboard[pygame.K_DOWN]:
        left = False
        right = False
        up = False
        down = True
    if left:
        x-=speed
    if right:
        x+=speed
    if up:
        y-=speed      
    if down:
        y+=speed
    if len(appX) == 0:
        left = False
        right = False
        up = False
        down = False
#=====Updateing=====#
    pygame.draw.rect(screen,white,(x,y,width,height),0)
    pygame.display.update()
pygame.quit()
print("Your score: ", pointCounter)
print("Your level: ", numOfApp)
