import math

import pygame


def findTrekantOmkreds(): #Lead: Yusuf, team: Hadi
    a + b + c
    return [a,b,c]

def trekantSider(x1, x2, x3, y1, y2, y3): #Closed. Lead: Bjørn, Rasmus E, Nick
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    return [a, b, c]

def findTrekantAreal(sider, vinkler): #Lead: Rasmus W, team: Jakob
    # sider = findTrekantSidelængde, vinkler = findTrekantVinkler
    areal = (1 / 2) * sider[0] * sider[1] * math.sin(math.radians(vinkler[2]))
    return areal

def findTrekantVinkler(a,b,c): #Lead: Said, team: Omar
    vinkelSum = 180
    taellerA = (b ** 2 + c ** 2 - a ** 2)
    naevnerA = (2 * b * c)
    Av = math.acos(taellerA / naevnerA)
    A = math.degrees(Av)

    taellerB = (a ** 2 + c ** 2 - b ** 2)
    naevnerB = (2 * a * c)
    Bv = math.acos(taellerB / naevnerB)
    B = math.degrees(Bv)

    C = vinkelSum - A - B

    return (A, B, C)

def findTrekantOmskrevneCirkelsRadius(a,b,c): #Lead: Gwion, team: Frederik L, Frederik H
    s = (a + b + c) / 2
    aAT = math.sqrt(s * (s - a) * (s - b) * (s - c))
    rAC1 = (a * b * c) / (aAT * 4)

    print('---')
    print('Radius Af Din Cirkel Er: ', rAC1)
    print('---')

def findTrekantOmskrevneCirkelsKordinater(): #Lead: Magnus, team: Christoffer, Liam
    return 0

def findTrekantIndskrevneCirkelsRadius(areal, omkreds): #Lead: Michael, team: Alexander
    r = areal / (omkreds * 2)
    return 0

def findTrekantIndskrevneCirkelsKordinater(): #Lead: Gabriel, team: Allan, Daniel
    return 0

def tegnTrekant(): #Lead: Yusuf, team: Hadi
    while True:
        mitVindue = pygame.display.set_mode((1000, 1000))
        mitVindue.fill((255, 255, 255))
        pygame.display.update()
        return [pygame.draw.polygon(mitVindue, (0, 0, 0), ((x_1, y_1),(x_2,y_2),(x_3,y_3)), 0)]

def skrivResultater(): #Lead: Gwion, team: Frederik L, Frederik H
    return 0
