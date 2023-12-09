import pygame
from pygame.locals import *
from ReloadImages import Reload


def MoveTo(x,y,house,color):
    if house == 1:
        if color =="Black":
            x,y = 50,650
        else:
            x,y = 200,650
    if house == 2:
        if color =="Black":
            x,y = 50,475
        else:
            x,y = 200,475
    if house == 3:
        if color =="Black":
            x,y = 50,250
        else:
            x,y = 200,250
    if house == 4:
        if color =="Black":
            x,y = 50,100
        else:
            x,y = 200,100
    if house == 5:
        if color =="Black":
            x,y = 200,0
        else:
            x,y = 300,0
    if house == 6:
        if color =="Black":
            x,y = 350,75
        else:
            x,y = 500,75
    if house == 7:
        if color =="Black":
            x,y = 350,250
        else:
            x,y = 500,250
    if house == 8:
        if color =="Black":
            x,y = 350,425
        else:
            x,y = 500,425
    if house == 9:
        if color =="Black":
            x,y = 350,600
        else:
            x,y = 500,600
    if house == 10:
        if color =="Black":
            x,y = 470,800
        else:
            x,y = 610,800
    if house == 11:
        if color =="Black":
            x,y = 650,625
        else:
            x,y = 800,625
    if house == 12:
        if color =="Black":
            x,y = 650,450
        else:
            x,y = 800,450
    if house == 13:
        if color =="Black":
            x,y = 650,275
        else:
            x,y = 800,275
    if house == 14:
        if color =="Black":
            x,y = 650,100
        else:
            x,y = 800,100
    if house == 15:
        if color =="Black":
            x,y = 780,0
        else:
            x,y = 920,0
    if house == 16:
        if color =="Black":
            x,y = 940,100
        else:
            x,y = 1090,100
    if house == 17:
        if color =="Black":
            x,y = 940,275
        else:
            x,y = 1090,275
    if house == 18:
        if color =="Black":
            x,y = 940,450
        else:
            x,y = 1090,450
    if house == 19:
        if color =="Black":
            x,y = 940,625
        else:
            x,y = 1090,625
    if house == 20:
        if color =="Black":
            x,y = 1095,800
        else:
            x,y = 1235,800
    if house == 21:
        if color =="Black":
            x,y = 1235,625
        else:
            x,y = 1385,625
    if house == 22:
        if color =="Black":
            x,y = 1235,450
        else:
            x,y = 1385,450
    if house == 23:
        if color =="Black":
            x,y = 1235,275
        else:
            x,y = 1385,275
    if house == 24:
        if color =="Black":
            x,y = 1235,100
        else:
            x,y = 1385,100
    if house == 25:
        if color =="Black":
            x,y = 1370,0
        else:
            x,y = 1510,0
    if house == 26:
        if color =="Black":
            x,y = 1540,100
        else:
            x,y = 1690,100
    if house == 27:
        if color =="Black":
            x,y = 1540,275
        else:
            x,y = 1690,275
    if house == 28:
        if color =="Black":
            x,y = 1540,450
        else: 
            x,y = 1690,450
    if house > 28:
        if color =="Black":
            x,y = 1540,625
        else: 
            x,y = 1690,625
    return x,y,house                   