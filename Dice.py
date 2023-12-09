from random import randint
import pygame
import os

import pathlib
pygame.init()
infoObject = pygame.display.Info()
tela = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
largura = (infoObject.current_w/2) -256
altura = (infoObject.current_h/2) -256
abs_file_path =os.getcwd() + "\\imgs\\"
def RandomDice():
    NumberDice = randint(1, 6)
 


    ListDice=[]
    imgs = pathlib.Path(abs_file_path)
    for item in imgs.iterdir():
        if "dice" in str(item):
            
            ListDice.append(item)
            
            #tela.blit(pygame.image.load(os.path.join("",item)),(largura, altura))
            #pygame.time.delay(900)
    
    if NumberDice == 1:
        DICE = pygame.image.load(os.path.join(abs_file_path,'dice-six-faces-one.png'))
    elif NumberDice == 2:
        DICE = pygame.image.load(os.path.join(abs_file_path,'dice-six-faces-two.png'))
    elif NumberDice == 3:
        DICE = pygame.image.load(os.path.join(abs_file_path,'dice-six-faces-three.png'))
    elif NumberDice == 4:
        DICE = pygame.image.load(os.path.join(abs_file_path,'dice-six-faces-four.png'))
    elif NumberDice == 5:
        DICE = pygame.image.load(os.path.join(abs_file_path,'dice-six-faces-five.png'))
    else:
        DICE = pygame.image.load(os.path.join(abs_file_path,'dice-six-faces-six.png'))
    
    
    
    return DICE,ListDice,NumberDice