from random import randint
from pygame.locals import *
import pygame
import os 
pygame.init()
infoObject = pygame.display.Info()
tela = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
Wrong = pygame.mixer.Sound('smb_mariodie.wav')
Correct = pygame.mixer.Sound('smb_1-up.wav')
abs_file_path =os.getcwd() + "\\imgs\\"
def questions(JaFeitas):

    tempo = 0
    NumberDice = randint(0, 27)
    if len(JaFeitas) == 28:
        JaFeitas= []
    for n in JaFeitas:
        if n != NumberDice:
            print(n)
        else:    
            NumberDice = randint(0, 27)
    JaFeitas.append(NumberDice)
               
    ListQuestions = ["B","A","B","C","D","A","D","B","C","D","B","C","B","A","B","B","D","A","A","B","B","C","D","D","A","B","B","C"]
    Pergunta = pygame.image.load(os.path.join(abs_file_path,f'q{NumberDice}.png'))
    tela.blit(Pergunta, (0, 0))
    while tempo < 120:
        tempo += 1
        pygame.display.update()
        pygame.time.delay(250)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
               
                if event.key == K_a and  ListQuestions[NumberDice] != "A":
                    Wrong.play()
                    return "Incorreto",JaFeitas
                if event.key == K_b and ListQuestions[NumberDice] != "B":
                    Wrong.play()
                    return "incorreto",JaFeitas
                if event.key == K_c and ListQuestions[NumberDice] != "C":
                    Wrong.play()
                    return "Incorreto",JaFeitas
                if event.key == K_d and ListQuestions[NumberDice] != "D":
                    Wrong.play()
                    return "Incorreto",JaFeitas        
                if event.key == K_a and  ListQuestions[NumberDice] == "A":
                    Correct.play()
                    return "Correto",JaFeitas
                if event.key == K_b and ListQuestions[NumberDice] == "B":
                    Correct.play()
                    return "Correto",JaFeitas
                if event.key == K_c and ListQuestions[NumberDice] == "C":
                    Correct.play()
                    return "Correto",JaFeitas
                if event.key == K_d and ListQuestions[NumberDice] == "D":
                    Correct.play()
                    return "Correto",JaFeitas      

    return "Incorreto",JaFeitas

   

