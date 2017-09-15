
import pygame


pygame.init()
pygame.font.init()
minVindue = pygame.display.set_mode((500, 200))
minVindue.fill((0, 255, 0))


while (True):


    pygame.draw.circle(minVindue , (255 , 0 , 0) , (50 , 200-10) , 10 , 0)
    minFont = pygame.font.SysFont('Comic Sans MS' , 70)
    minTekst = minFont.render('FUCK' , False , (200 , 0 , 200))
    minVindue.blit(minTekst , (100 , 30))
    pygame.display.update()
