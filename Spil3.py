import pygame
import random

breddePaaVinduet = 1000
hoejdePaaVinduet = 500
roedBaggrund = 0
groenBaggrund = 255
blaaBaggrund = 0
roedCirkel = 255
groenCirkel = 0
blaaCirkel = 0
xCirkel = 50
yCirkel = 250
radiusCirkel = 5
tykkelseCirkel = 0
speedx = 1
speedy = 0

pygame.init()
minVindue = pygame.display.set_mode((breddePaaVinduet, hoejdePaaVinduet))

spilletErIgang = True

while (spilletErIgang):

    minVindue.fill((roedBaggrund , groenBaggrund , blaaBaggrund))

    pygame.draw.circle(minVindue , (roedCirkel , groenCirkel , blaaCirkel) , (xCirkel , yCirkel) , radiusCirkel , tykkelseCirkel)



    xCirkel = xCirkel + speedx
    yCirkel = yCirkel + speedy

    pygame.display.update()