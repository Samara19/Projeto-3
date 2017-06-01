import pygame as p
from pygame.locals import* 
from sys import exit
from os import system
from classe import texto

p.init()


screen = p.display.set_mode((950, 712))
p.display.set_caption('Saturno')
astronauta = p.image.load('animaok.gif').convert()
astronauta_position = [680, 20]



background = p.image.load('saturn.jpg').convert()


clock = p.time.Clock()

p.font.init()

fonte_padrao = p.font.get_default_font()
fonte_jogo = p.font.SysFont(fonte_padrao, 30)

fonte_perdeu = p.font.SysFont(fonte_padrao, 100)

BLACK = (0,0,0)
WHITE = (255, 255, 255)


events = p.event.get()

jogo = 0

while jogo == 0:
    for event in events:
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0)) #coloca a imagem no display
    screen.blit(astronauta, (astronauta_position))
    #criando textos
    tela_1 = ["Olá, astronauta! Seja bem vindo...", "...ao segundo maior planeta do Sistema Solar!", "Para conseguir passar por mim,", "você terá de provar ser muito bom ou boa em Matemática!", "E olha que não é fácil não, hein?", "Está preparado para começar?", "Se sim, pressione ENTER para avançar!"] 
    tela_2 = ["Pois bem, vamos começar:", "Diga-me, quanto é 15 X 4?", "Poooxa, é fácil, vamos lá, eu acredito em você!", "Digite 1 para 50", "Digite 2 para 45", "Digite 3 para 90", "Ou 4 para 60"]
    ganhou = ["UOOOOOOOU", "É ISSO AÍ AMIGÃO/AMIGONA!", "VOCÊ CONSEGUIU ESCAPAR DO MEU CAMPO MAGNÉTICO MONSTRUOSO!", "E VOLTAR PARA A SEGURANÇA DA SUA NAVE!" "MISSÃO CUMPRIDA COM SUCESSO!"]
    perdeu = ["GAME OVER!"]
   
   #inserindo textos no display
    entrada = texto(tela_1,95, 20)
    entrada.novo_blit(fonte_jogo, WHITE, screen, 40)
    #entrada_2 = texto(instructions, 95, 200)
    #entrada_2.novo_blit(fonte_jogo, WHITE, screen, 40)

    

    p.display.update()
    time_passed = clock.tick(30)
    
    
    while True:
        events = p.event.get()
        for event in events:
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    jogo = 1
                    p.display.quit()
                if event.key == p.K_RETURN:
                    screen.fill(BLACK)
                    screen.blit(segunda_tela, (0,0))
                    screen.blit(astronauta, rect_astronauta)
                    p.display.update()
                    time_passed = clock.tick(30)
                    jogo=1
            if jogo==1:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
                    if event.key==p.K_SPACE:
                        screen.fill(BLACK)
                        screen.blit(segunda_tela, (0,0))
                        rect_astronauta.top-=para_cima
                        screen.blit(astronauta, rect_astronauta)
                        p.display.update()
                        time_passed = clock.tick(30)
                    if event.key==p.K_LEFT:
                        screen.fill(BLACK)
                        screen.blit(segunda_tela, (0,0))
                        rect_astronauta.right-=para_frente
                        screen.blit(astronauta, rect_astronauta)
                        p.display.update()
                        time_passed = clock.tick(30)

        if jogo==1:
            screen.fill(BLACK)
            screen.blit(segunda_tela, (0,0))
            rect_astronauta.top+=sem_pressionar
            screen.blit(astronauta, rect_astronauta)
            p.display.update()
            time_passed = clock.tick(30)
            p.display.update()
            time_passed = clock.tick(30)
            if rect_astronauta.top<5:
                jogo=2
            if rect_astronauta.top>400:
                jogo=2
            if rect_astronauta.left>150:
                jogo=3


        if jogo==2:
            screen.blit(astronauta, rect_astronauta)
            entrada = texto(perdeu,255, 320)
            entrada.novo_blit(fonte_perdeu, WHITE, screen, 0)
            p.display.update()
            time_passed = clock.tick(30)

        if jogo==3:
            screen.blit(astronauta, rect_astronauta)
            entrada = texto(ganhou,255, 320)
            entrada.novo_blit(fonte_jogo, WHITE, screen, 0)
            p.display.update()
            time_passed = clock.tick(30)



            