import pygame as p
from pygame.locals import* 
from sys import exit
from os import system
from classe import texto

p.init()


screen = p.display.set_mode((950, 712))
p.display.set_caption('Júpiter')
astronauta = p.image.load('animaok.gif').convert()
astronauta_position = [680, 20]
para_cima = 170
para_frente = 20
sem_pressionar = 8


primeira_tela = p.image.load('jupiter.jpg').convert()
segunda_tela = p.image.load('surface_jupiter.jpg').convert()

rect_astronauta = astronauta.get_rect()
rect_astronauta.right = 1000
rect_astronauta.top = 5

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
    screen.blit(primeira_tela, (0, 0)) #coloca a imagem no display
    screen.blit(astronauta, (astronauta_position))
    #criando textos
    tela_1 = ["Olá astronauta!", "Seja bem vindo(a) a Júpiter, o gigante do Sistema Solar!", "A minha gravidade é insana,", "então, prepare-se para flutuar por minha superfície!"]
    instructions = ["INSTRUÇÕES:", "A sua missão é atravessar a minha superífice", "sem encostar nas bordas superior e inferior da tela!", "Para isso, utilize a seta da esquerda para voltar para a sua nave!", "E a tecla de espaço para se manter flutuando, sem encostar nas bordas!", "Caso isso aconteça, GAME OVER!", "Está preparado(a)? Se sim, pressione ENTER para avançar e boa sorte!"]
    perdeu = ["GAME OVER!"]
   #inserindo textos no display
    entrada = texto(tela_1,95, 20)
    entrada.novo_blit(fonte_jogo, WHITE, screen, 40)
    entrada_2 = texto(instructions, 95, 200)
    entrada_2.novo_blit(fonte_jogo, WHITE, screen, 40)

    

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
            if rect_astronauta.top>390:
                jogo=2

        if jogo==2:
            screen.blit(astronauta, rect_astronauta)
            entrada = texto(perdeu,255, 320)
            entrada.novo_blit(fonte_perdeu, WHITE, screen, 0)
            p.display.update()
            time_passed = clock.tick(30)



            