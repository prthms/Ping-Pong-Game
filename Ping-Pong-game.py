import pygame
from random import randint
from pygame import mixer

pygame.init()
mixer.init()
music3 = mixer.music

screen_width = 800
screen_higth = 500

# Creating window
gameWindow = pygame.display.set_mode((screen_width,screen_higth))
pygame.display.set_caption("Ping Pong Game")

# background image
introimg = pygame.image.load("./Images/ping-pong-background.png")
introimg = pygame.transform.scale(introimg,(screen_width,screen_higth)).convert_alpha()
backimg = pygame.image.load("./Images/pong-computer-game645.jpg")
backimg = pygame.transform.scale(backimg,(screen_width,screen_higth)).convert_alpha()
clock = pygame.time.Clock()


# pygame fonts

yellow = (254, 253, 3)
font = pygame.font.SysFont("Segoe Print", 30)
def plot_text(text,color,x,y):
    screen_font = font.render(text, True,color)
    gameWindow.blit(screen_font, [x, y])

def plot_textas_size(text,color,x,y,size):
    font = pygame.font.SysFont("Segoe Print", size)
    screen_font = font.render(text, True,color)
    gameWindow.blit(screen_font, [x, y])


music1 = './sounds/tennisbackeffect.mp3'
music3.load(music1)

def playtennissound():
    music3.play()

def playmusic(songname):
    music3.load(songname)
    music3.play()



def gameloop():
    exit = True
    yellow = (254, 253, 3)
    white=(255,255,255)
    leftposi_x = 30
    leftposi_y = 200
    rightposi_x = 770
    rightposi_y = 200
    rightvel = 0
    leftvel = 0
    ballposi_x = 420
    ballposi_y = 200
    ballvelx =-2
    ballvely = 1
    leftscore =0
    rightscore =0
    music3.stop()

    while exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    rightvel = 3
                if event.key == pygame.K_z:
                    leftvel = 3
                if event.key == pygame.K_UP:
                    rightvel = -3
                if event.key == pygame.K_q:
                    leftvel = -3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    rightvel = 0
                if event.key == pygame.K_z:
                    leftvel =0
                if event.key == pygame.K_UP:
                    rightvel = 0
                if event.key == pygame.K_q:
                    leftvel = 0



        leftposi_y = abs(leftposi_y + leftvel)
        rightposi_y = abs(rightposi_y +rightvel)


        if leftposi_y <= 80 or leftposi_y >= 420:
            leftvel =0

        if rightposi_y <= 80 or rightposi_y >= 420:
            rightvel = 0

        # when ball get out from ground
        if ballposi_x > 795  :
            ballposi_x=420
            ballposi_y=200
            leftscore+=1
            playmusic('./sounds/pointout.mp3')


        if ballposi_x < 15:
            ballposi_x = 420
            ballposi_y = 200
            rightscore += 1
            playmusic('./sounds/pointout.mp3')


        if leftscore == 10:
            ballvelx =0
            ballvely=0
            gameover(leftscore,rightscore)
        if rightscore == 10:
            ballvelx = 0
            ballvely = 0
            gameover(leftscore,rightscore)

        # random no choise
        if ballposi_y <=85 :
            playmusic('./sounds/wall-hit.mp3')
            ballvely = randint(0, 3)

        if ballposi_y >=480 :
            playmusic('./sounds/wall-hit.mp3')
            ballvely = randint(-3, 0)

        if abs(rightposi_x-ballposi_x) <= 15 and abs(rightposi_y-ballposi_y) <= 45:
            playmusic('./sounds/hit.mp3')
            ballvelx = -2
            ballvely = randint(-1, 1)

        if abs(leftposi_x-ballposi_x) <= 15 and abs(leftposi_y-ballposi_y) <= 45:
            playmusic('./sounds/hit.mp3')
            ballvelx = 2
            ballvely = randint(-1, 1)



        ballposi_x += ballvelx
        ballposi_y += ballvely

        # screen objects
        gameWindow.blit(backimg, (0, 0))
        pygame.draw.rect(gameWindow, yellow, [leftposi_x,leftposi_y, 15, 60])
        pygame.draw.rect(gameWindow, yellow, [rightposi_x,rightposi_y, 15, 60])
        pygame.draw.rect(gameWindow, yellow, [ballposi_x,ballposi_y, 12, 12])
        plot_text(str(leftscore) ,white, 180,30)
        plot_text(str(rightscore) ,white, 580,30)
        plot_textas_size('Player A',white,160,6,20)
        plot_textas_size('Player B',white,550,6,20)

        pygame.display.update()

    pygame.quit()
    quit()

def gameover(lscore,rscore):
    exit =True
    white = (255, 255, 255)
    backimg1 = pygame.image.load("./Images/GAMEOVER01.png")
    backimg1 = pygame.transform.scale(backimg1, (screen_width, screen_higth)).convert_alpha()
    playmusic('./sounds/winning_sound.mp3')
    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_ESCAPE:
                    gameloop()
                    exit=False

        gameWindow.blit(backimg1, (0, 0))
        plot_text('Player A- '+str(lscore),white,15,15)
        plot_text('Player B- '+str(rscore),white,500,15)
        pygame.display.update()

def helps():
    helpimg = pygame.image.load("./Images/ping-pong-helpbox.jpg")
    helpimg = pygame.transform.scale(helpimg,(screen_width,screen_higth)).convert_alpha()
    exit = True
    while exit:
        gameWindow.blit(helpimg, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False

            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_ESCAPE:
                    Introscreen()
                    exit = False

def Introscreen():
    exit = True
    playmusic('./sounds/starting-sound.mp3')
    while exit:
        gameWindow.blit(introimg, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False

            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_h:
                    gameloop()
                    exit = False
                else:
                    helps()

Introscreen()

pygame.quit()
quit()