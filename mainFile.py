import pygame.locals, trekantsFunktioner


pygame.init()

w = 1000
h = 800
isRunning = True
corners = [];

window = pygame.display.set_mode([w,h])
window.fill([255,255,255])

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.locals.MOUSEBUTTONUP:
            if len(corners) == 3:
                corners.clear()
                window.fill([255, 255, 255])
            corners.append(pygame.mouse.get_pos())
        elif event.type == pygame.locals.QUIT:
            exit()

    for corner in corners:
        x,y = corner
        pygame.draw.circle(window,[255,0,0],[x,y],5)

    if len(corners) == 3:
        pygame.draw.polygon(window,[0,0,255],corners,2)

    pygame.display.update()
