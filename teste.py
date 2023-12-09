'''
Casas de 1 a 4

Subtrai 175 no eixo y (0,-175)

tela.blit(PEAO_PRETO, (50, 750))
tela.blit(PEAO_AMARELO, (50, 800))
tela.blit(PEAO_AZUL, (200, 750))
tela.blit(PEAO_BRANCO, (200, 800))
tela.blit(PEAO_VERMELHO, (125, 775))

Casas de 11 a 14

Subtrai 175 no eixo y (0,-175)


tela.blit(PEAO_PRETO, (650, 575))
tela.blit(PEAO_AMARELO, (650, 625))
tela.blit(PEAO_AZUL, (800, 575))
tela.blit(PEAO_BRANCO, (800, 625))
tela.blit(PEAO_VERMELHO, (725, 600))

Casas de 21 a 24

Subtrai 175 no eixo y (0,-175)

tela.blit(PEAO_PRETO, (1235, 575))
tela.blit(PEAO_AMARELO, (1235, 625))
tela.blit(PEAO_AZUL, (1385, 575))
tela.blit(PEAO_BRANCO, (1385, 625))
tela.blit(PEAO_VERMELHO, (1310, 600))


Casa 5

primeiro peao começa em X = 130 e vai somando 70.
eixo y= 0 e rotate 180º.
tela.blit(PEAO_PRETO, (130, 0))
tela.blit(PEAO_AMARELO, (200, 0))
tela.blit(PEAO_AZUL, (270, 0))
tela.blit(PEAO_BRANCO, (340, 0))
tela.blit(PEAO_VERMELHO, (410, 0))

Casas 16 a 19

Soma 175 no eixo x (+175,0)

tela.blit(PEAO_PRETO, (940, 75))
tela.blit(PEAO_AMARELO, (940, 125))
tela.blit(PEAO_AZUL, (1090, 75))
tela.blit(PEAO_BRANCO, (1090, 125))
tela.blit(PEAO_VERMELHO, (1015, 100))

Casas 26 a END

Soma 175 no eixo x (+175,0)

tela.blit(PEAO_PRETO, (1540, 75))
tela.blit(PEAO_AMARELO, (1540, 125))
tela.blit(PEAO_AZUL, (1690, 75))
tela.blit(PEAO_BRANCO, (1690, 125))
tela.blit(PEAO_VERMELHO, (1615, 100))

Casas 6 a 9

Soma 175 no eixo x (+175,0)

tela.blit(PEAO_PRETO, (350, 75))
tela.blit(PEAO_AMARELO, (350, 125))
tela.blit(PEAO_AZUL, (500, 75))
tela.blit(PEAO_BRANCO, (500, 125))
tela.blit(PEAO_VERMELHO, (425, 100))

Casas 10

tela.blit(PEAO_PRETO, (400, 800))
tela.blit(PEAO_AMARELO, (470, 800))
tela.blit(PEAO_AZUL, (540, 800))
tela.blit(PEAO_BRANCO, (610, 800))
tela.blit(PEAO_VERMELHO, (680, 800))


Casas 20

tela.blit(PEAO_PRETO, (1025, 800))
tela.blit(PEAO_AMARELO, (1095, 800))
tela.blit(PEAO_AZUL, (1165, 800))
tela.blit(PEAO_BRANCO, (1235, 800))
tela.blit(PEAO_VERMELHO, (1305, 800))



Casa 15
tela.blit(PEAO_PRETO, (710, 0))
tela.blit(PEAO_AMARELO, (780, 0))
tela.blit(PEAO_AZUL, (850, 0))
tela.blit(PEAO_BRANCO, (920, 0))
tela.blit(PEAO_VERMELHO, (990, 0))

Casa 25

tela.blit(PEAO_PRETO, (1300, 0))
tela.blit(PEAO_AMARELO, (1370, 0))
tela.blit(PEAO_AZUL, (1440, 0))
tela.blit(PEAO_BRANCO, (1510, 0))
tela.blit(PEAO_VERMELHO, (1580, 0))



'''
import pygame
import os
from pygame.locals import *
pygame.init()

infoObject = pygame.display.Info()
tela = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
altura = infoObject.current_h/2
largura = infoObject.current_w/2

IMAGEM_BACK = pygame.image.load(os.path.join('imgs','Start.png'))

PEAO_PRETO = pygame.transform.scale(pygame.image.load(os.path.join('imgs','Peao-Grow-Black.png')),(150,150))
PEAO_AMARELO = pygame.transform.scale(pygame.image.load(os.path.join('imgs','Peao-Grow-Yellow.png')),(150,150))
PEAO_AZUL = pygame.transform.scale(pygame.image.load(os.path.join('imgs','Peao-Grow-Blue.png')),(150,150))
PEAO_BRANCO = pygame.transform.scale(pygame.image.load(os.path.join('imgs','Peao-Grow-White.png')),(150,150))
PEAO_VERMELHO = pygame.transform.scale(pygame.image.load(os.path.join('imgs','Peao-Grow-Red.png')),(150,150))
'''
PEAO_PRETO = pygame.transform.rotate(PEAO_PRETO,180)
PEAO_AMARELO = pygame.transform.rotate(PEAO_AMARELO,180)
PEAO_AZUL = pygame.transform.rotate(PEAO_AZUL,180)
PEAO_BRANCO = pygame.transform.rotate(PEAO_BRANCO,180)
PEAO_VERMELHO = pygame.transform.rotate(PEAO_VERMELHO,180)
'''
tela.blit(IMAGEM_BACK, (0, 0))

tela.blit(PEAO_PRETO, (50, 750))

house = 0
x,y = 50,750
qq =["Preto","Amarelo","Azul","Branco","Vermelho"]
while True:
    color = "Black"
    ValorDado =1

    soma = house + ValorDado
    
    
    house +=1 
    if soma == 5 or int(soma) ==15 or int(soma) == 25:
        PEAO_PRETO = pygame.transform.rotate(PEAO_PRETO,180)
        PEAO_AMARELO = pygame.transform.rotate(PEAO_AMARELO,180)
        PEAO_AZUL = pygame.transform.rotate(PEAO_AZUL,180)
        PEAO_BRANCO = pygame.transform.rotate(PEAO_BRANCO,180)
        PEAO_VERMELHO = pygame.transform.rotate(PEAO_VERMELHO,180)
    else:
        PEAO_PRETO = pygame.transform.rotate(PEAO_PRETO,0)
        PEAO_AMARELO = pygame.transform.rotate(PEAO_AMARELO,0)
        PEAO_AZUL = pygame.transform.rotate(PEAO_AZUL,0)
        PEAO_BRANCO = pygame.transform.rotate(PEAO_BRANCO,0)
        PEAO_VERMELHO = pygame.transform.rotate(PEAO_VERMELHO,0)

    if color == "Preto":
        Mult = 1
    elif color == "Amarelo":
        Mult = 2
    elif color == "Azul":
        Mult = 3
    elif color == "Branco":
        Mult = 4            
    elif color == "Vermelho":
        Mult = 5  
    soma = house + ValorDado  
    print(f"soma{soma},house {house} + ValorDado {ValorDado}")        
    if house < 5:
        if color == "Preto" or color =="Amarelo":
            x= 50
        elif color == "Branco" or color == "Azul":
            x = 200
        else:
            x = 125 
        y -=(175*ValorDado)
    elif house == 5:
        x += (70 * Mult)
        y=0
    elif house == 15:
        x += (70 * Mult)
        y=0
    elif house == 25:
        x += (70 * Mult)            
        y = 0
    elif house == 10: 
        x += (70 * Mult)
        y=800     
    elif house == 20:
        x += (70 * Mult)
        y=800                  
    elif house < 10:
        if color == "Preto" or color =="Amarelo":
            x= 350
        elif color == "Branco" or color == "Azul":
            x = 500
        else:
            x = 425            
        #ValorDado -= 5 
        print("CASA 6",soma)
        if (house) == 6:
            y += (130*ValorDado)
            
        else:
            y += (175*ValorDado)
    elif house < 15:
        if color == "Preto" or color =="Amarelo":
            x= 650
        elif color == "Branco" or color == "Azul":
            x = 800
        else:
            x = 725     
        #ValorDado-=10
        if (house) == 11:
            y -= (150*ValorDado)
        else:
            y -= (175*ValorDado)
        
    elif house < 20:
        if color == "Preto" or color =="Amarelo":
            x= 940
        elif color == "Branco" or color == "Azul":
            x = 1090
        else:
            x = 1015            
        #ValorDado-= 15
        if (house) == 16:

            y += (130*ValorDado)
        else:
            y += (175*ValorDado)
        
    elif house < 25:
        if color == "Preto" or color =="Amarelo":
            x= 1235
        elif color == "Branco" or color == "Azul":
            x = 1385
        else:
            x = 1310    
        #ValorDado -= 20
        if (house) == 21:
            y -= (150*ValorDado)
        else:
            y -= (175*ValorDado)        
    
    elif house < 29:
        if color == "Preto" or color =="Amarelo":
            x= 1540
        elif color == "Branco" or color == "Azul":
            x = 1690
        else:
            x = 1615    
        #ValorDado -=25
        if (house) == 26:
            y += (130*ValorDado)
        else:
            y += (175*ValorDado)        
        
    elif house > 28:
        y +=175 

    #print(f"valor de x = {x} ,valor de = {y},casa = {house}, cor {color} SOMA {soma}") 
    tela.blit(pygame.transform.scale(pygame.image.load(os.path.join('imgs',f'Peao-Grow-{color}.png')),(150,150)), (x, y))


    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    pygame.display.update()

#pygame.time.delay(5000)
