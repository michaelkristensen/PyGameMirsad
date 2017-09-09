
import pygame


pygame.init()
minVindue = pygame.display.set_mode((500, 200))
minVindue.fill((0, 255, 0))


while (True):


    pygame.draw.circle(minVindue , (255 , 0 , 0) , (50 , 200-10) , 10 , 0)
    pygame.display.update()

    #HUSK clock