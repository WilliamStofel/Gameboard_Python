import pygame
import os
from pygame.locals import *
from sys import exit
pygame.init() 
abs_file_path = os.getcwd() + "\\imgs\\"

print(abs_file_path)
tela = pygame.display.set_mode((1920, 1080))



def EndGame(color):

    Finish = pygame.image.load(os.path.join(abs_file_path,f'{color}Win.png'))
    tela.blit(Finish, (0, 0))

    while True:
        
    
    
        tela.blit(Finish, (0, 0))
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
