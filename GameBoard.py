import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os
from Dice import RandomDice
import Move
from Questions import questions
from Finish import EndGame
class Peao:
    def __init__(self,x,y,house,color) -> None:
        self.x =x
        self.y =y
        self.house = house
        self.color = color 

Peao1 = Peao(50,750,0,"Black")
#Peao2 = Peao(50,800,0,"Amarelo")
#Peao3 = Peao(200,750,0,"Azul")
#Peao4 = Peao(200,800,0,"Branco")
Peao5 = Peao(125,775,0,"Red")
pygame.init()

#<-- absolute dir the script is in
abs_file_path =os.getcwd() + "\\imgs\\"

pygame.mixer.music.load('a-hero-of-the-80s-126684.mp3')

pygame.mixer.music.play(0,0,2500) 

pygame.mixer.music.queue('hero-80s-127027.mp3')
pygame.mixer.music.queue('lady-of-the-80x27s-128379.mp3')
pygame.mixer.music.queue('stranger-things-124008.mp3')
pygame.mixer.music.queue('to-the-death-159171.mp3')
pygame.mixer.music.queue('hero-80s-127027.mp3')
pygame.mixer.music.queue('lady-of-the-80x27s-128379.mp3')
pygame.mixer.music.queue('stranger-things-124008.mp3')
pygame.mixer.music.queue('to-the-death-159171.mp3')




IMAGEM_BACK = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Start.png')),(1920,1080))
Finish = pygame.image.load(os.path.join(abs_file_path,'Finish.png'))

PEAO_PRETO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Black.png')),(150,150))
PEAO_AMARELO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Yellow.png')),(150,150))
PEAO_AZUL = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Blue.png')),(150,150))
PEAO_BRANCO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-White.png')),(150,150))
PEAO_VERMELHO = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,'Peao-Grow-Red.png')),(150,150))
SIXSIDESDICE = pygame.image.load(os.path.join(abs_file_path,'dice-six-faces-six.png'))
ROLLDICE = pygame.image.load(os.path.join(abs_file_path,'RollDice.png'))


JaFeitas =[]



pontos = 0
fonte = pygame.font.SysFont('comicsansms', 60, bold=True)

infoObject = pygame.display.Info()
#tela = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
tela = pygame.display.set_mode((1920, 1080))
altura = infoObject.current_h/2
largura = infoObject.current_w/2
print("largura",infoObject.current_w,"Altura",infoObject.current_h)


tela.blit(IMAGEM_BACK, (0, 0))


tela.blit(PEAO_PRETO, (50, 750))

tela.blit(PEAO_VERMELHO, (125, 775))

pygame.display.set_caption('ClaudioEnglish Game Board')
relogio = pygame.time.Clock()
ListDice = []



largura_Centro = int((infoObject.current_w/2)-256)
altura_Centro = int((infoObject.current_h/2)-256)

def RollDice(player):
    ImagemDice,ListDice,Number = RandomDice()
    loop = 0
    while loop < 6:
        for item in ListDice:
            tela.blit(pygame.image.load(os.path.join("",item)), (largura_Centro, altura_Centro))
            pygame.time.delay(100)
            
            pygame.display.update()
        loop+=1            
    tela.blit(ImagemDice, (largura_Centro, altura_Centro))   
    DiceNumber = fonte.render(f"Player {player}, your number is: {Number}", True, (255,255,255))
    DiceNumberLargura = DiceNumber.get_width()/2
    print(Number)
    tela.blit(DiceNumber, (largura-DiceNumberLargura, altura - 350))  
    pygame.display.update()
    pygame.time.delay(1000)
    return Number
     


Players = [Peao1,Peao5]
End = False
Ordem =["Black","Red"]
ListaNumber=0
while True:
    
    for Player in Players:
        
        if End == True:
            EndGame(StringWin)
        if ListaNumber == 2:
            ListaNumber = 0      
        if Ordem[ListaNumber] == Player.color:
            
            PhraseWin = fonte.render(f"You WON !!!! Player: {Player.color}", True, (0,0,0))
            NewTurn = fonte.render(f"Your turn player: {Player.color}", True, (0,0,0))
            LarguraPalavra = NewTurn.get_width()/2
            
            tela.blit(NewTurn, (largura-LarguraPalavra, altura-340))
            pygame.display.update()
            pygame.time.delay(1500)
            
            tela.blit(SIXSIDESDICE, (largura_Centro, altura_Centro))  
            
            tela.blit(ROLLDICE, (largura-296, altura_Centro+550))  


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Resp,JaFeitas = questions(JaFeitas)
                print(f"Resposta: {Resp},Perguntas ja feitas {JaFeitas}")
                
               
                
                if Resp == "Correto":
                    tela.blit(IMAGEM_BACK, (0, 0))
                    tela.blit(ROLLDICE, (largura-296, altura_Centro+550)) 
                    SumHouses = RollDice(Player.color)
                    
                    #pygame.time.delay(3000)
                    Soma = (Player.house + SumHouses)
                   
                    Player.x,Player.y,Player.house = Move.MoveTo(Player.x,Player.y,(Soma),Player.color)
                    if Player.house > 28:
                        print("Color", Player.color)
                        pygame.mixer.music.load('Victory.mp3')
                        pygame.mixer.music.play(0,0,0)
                        win = pygame.image.load(os.path.join(abs_file_path,f'{Player.color}Win.png'))

                        tela.blit(win, (1920,1080))
                        StringWin = Player.color
                        print(win)
                        pygame.display.update()
                        End = True
                tela.blit(IMAGEM_BACK, (0, 0))
                for P in Players:
                    
                    if P.house == 5 or P.house == 15 or P.house == 25:
                        peao = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,f'Peao-Grow-{P.color}.png')),(150,150))
                        peao = pygame.transform.rotate(peao,180)
                        tela.blit(peao, (P.x, P.y))
                        
                    else:
                        peao = pygame.transform.scale(pygame.image.load(os.path.join(abs_file_path,f'Peao-Grow-{P.color}.png')),(150,150))
                        peao = pygame.transform.rotate(peao,0)
                        tela.blit(peao, (P.x, P.y))
                ListaNumber+=1 
                #pygame.time.delay(3000)
               
                                      
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
        pygame.display.update()