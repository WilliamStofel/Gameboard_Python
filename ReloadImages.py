import pygame
import os
from pygame.locals import *
pygame.init()

infoObject = pygame.display.Info()
tela = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
altura = infoObject.current_h/2
largura = infoObject.current_w/2

abs_file_path =os.getcwd() + "\\imgs\\"




IMAGEM_BACK = pygame.image.load(os.path.join(abs_file_path,'Start.png'))




def Reload(x,y,color):
    IMAGEM_BACK = pygame.image.load(os.path.join(abs_file_path,'Start.png'))
    tela.blit(IMAGEM_BACK, (0, 0))
    PEAO_PRETO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Preto.png')),(150,150))
    PEAO_AMARELO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Amarelo.png')),(150,150))
    PEAO_AZUL = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Azul.png')),(150,150))
    PEAO_BRANCO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Branco.png')),(150,150))
    PEAO_VERMELHO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Vermelho.png')),(150,150))
    if color == "Preto":
        tela.blit(PEAO_PRETO, (x, y))
    elif color == "Amarelo":
        tela.blit(PEAO_AMARELO, (x, y))
    elif color == "Azul":
        tela.blit(PEAO_AZUL, (x, y))
    elif color == "Branco":    
        tela.blit(PEAO_BRANCO, (x, y))
    elif color == "Vermelho":        
        tela.blit(PEAO_VERMELHO, (x, y))
