import pygame
import random
import sys
import pygame.locals
import math



xVindueBrede = 1200
yVindueHoejde = 600

r1 = 5
r2 = 10
resultat = 0

pygame.init()

lydObjekt1 = pygame.mixer.Sound('lyd1.wav')
lydObjekt2 = pygame.mixer.Sound('lyd2.wav')

minVindue = pygame.display.set_mode((xVindueBrede , yVindueHoejde))

while True:  # main game loop

    flag = 0
    x = 0

    x1 = 0
    y1 = random.randint(0 , yVindueHoejde)
    x2 = xVindueBrede
    y2 = random.randint(0 , yVindueHoejde)

    a = (y2 - y1) / (x2 - x1)
    b = y1

    speed = random.randint(1 , 5)

    pygame.mixer.Sound.play(lydObjekt1)

    # largeText = pygame.font.Font('Freesansbold.ttf',115)

    for i in range(0 , xVindueBrede):

        ############# Kun til at afslute PyGame ##################
        for event in pygame.event.get():

            if (event.type == pygame.locals.QUIT):
                pygame.quit()

                sys.exit()

            if (event.type == pygame.MOUSEMOTION):
                mX , mY = pygame.mouse.get_pos()

        ###########################################################


        minVindue.fill((0 , 255 , 0))

        y = a * x + b  # funktion f(x)

        y = int(yVindueHoejde - y)  # Lav om på y koordinat
        pygame.draw.circle(minVindue , (255 , 0 , 0) , (x , y) , r1 , 0)
        x = x + speed

        pygame.draw.circle(minVindue , (255 , 100 , 90) , (xVindueBrede - 10 , mY) , r2 , 0)

        afstand = math.sqrt((xVindueBrede - x) * (xVindueBrede - x) + (mY - y) * (mY - y))

        if (afstand < (r1 + r2)) and (flag == 0):
            pygame.mixer.Sound.play(lydObjekt2)
            resultat = resultat + 1
            flag = 1

        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS' , 30)
        textsurface = myfont.render(str(resultat) , False , (0 , 0 , 200))
        minVindue.blit(textsurface , (10 , 10))

        pygame.display.update()
