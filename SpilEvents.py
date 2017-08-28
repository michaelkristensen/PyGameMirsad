import pygame
import sys
import pygame.locals

pygame.init()

minVindue = pygame.display.set_mode((500, 200))



while (True):

    ############# Kun til at afslute PyGame ##################
    for event in pygame.event.get():
        print (event)
        if (event.type == pygame.locals.QUIT):
            pygame.quit()
            sys.exit()

        if (event.type == pygame.MOUSEMOTION):
            #mX , mY = pygame.mouse.get_pos()
            print('Mus')

        if (event.type == pygame.MOUSEBUTTONDOWN):
            musVenstre,musMidt, musHojre = pygame.mouse.get_pressed()
            print(musVenstre)


    ###########################################################

    pygame.display.update()