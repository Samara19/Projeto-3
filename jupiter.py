import pygame as p
from pygame.locals import* 
from sys import exit
from os import system
from classe import texto

p.init()


screen = p.display.set_mode((1050, 712))
p.display.set_caption('Júpiter')
astronauta = p.image.load('animaok.gif').convert()
astronauta_position = [680, 20]
para_cima = 150
para_frente = 15
sem_pressionar = 8

esquerda = p.image.load('seta_esquerda.jpg').convert()
espaço = p.image.load('space_bar.jpg').convert()

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
    instructions = ["INSTRUÇÕES:", "A sua missão é atravessar a minha superfície!", "MAS NÃO ENCOSTE NAS BORDAS SUPERIOR OU INFERIOR DA TELA!", "Utilize                   para conseguir voltar para a sua nave!", "E                                                         para se manter flutuando!", "ATENÇÃO: ACIMA DA LINHA VERMELHA, VOCÊ PODE PULAR MUITO ALTO!", "E ABAIXO, VOCÊ PODE NÃO CONSEGUIR SUBIR!", "Está preparado(a)? Se sim, pressione ENTER para avançar e boa sorte!"]
    ganhou = ["UOOOOOOOU", "É ISSO AÍ AMIGÃO/AMIGONA!", "VOCÊ CONSEGUIU ESCAPAR DO MEU CAMPO MAGNÉTICO MONSTRUOSO!", "E VOLTAR PARA A SEGURANÇA DA SUA NAVE!", "MISSÃO CUMPRIDA COM SUCESSO!"]
    perdeu = ["GAME OVER!"]

   #inserindo textos no display

    entrada = texto(tela_1,95, 20)
    entrada.novo_blit(fonte_jogo, WHITE, screen, 40)
    entrada_2 = texto(instructions, 95, 200)
    entrada_2.novo_blit(fonte_jogo, WHITE, screen, 60)
    screen.blit(esquerda, (180, 400))
    screen.blit(espaço, (120, 485))

    

    p.display.update()
    time_passed = clock.tick(30)
    
    
    while True:
        events = p.event.get()
        for event in events:
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.display.quit()
                if event.key == p.K_RETURN:
                    jogo=1
            if jogo==1:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
                    if event.key==p.K_SPACE:
                        screen.fill(BLACK)
                        screen.blit(segunda_tela, (0,0))
                        p.draw.line(screen, (255, 0, 0), (0, 356), (1050, 356), 5)
                        if rect_astronauta.top>250:
                            para_cima=50
                        rect_astronauta.top-=para_cima
                        screen.blit(astronauta, rect_astronauta)
                        p.display.update()
                        time_passed = clock.tick(30)
                    if event.key==p.K_LEFT:
                        screen.fill(BLACK)
                        screen.blit(segunda_tela, (0,0))
                        p.draw.line(screen, (255, 0, 0), (0, 356), (1050, 356), 5)
                        rect_astronauta.right-=para_frente
                        screen.blit(astronauta, rect_astronauta)
                        p.display.update()
                        time_passed = clock.tick(30)

        if jogo==1:
            screen.fill(BLACK)
            screen.blit(segunda_tela, (0,0))
            p.draw.line(screen, (255, 0, 0), (0, 356), (1050, 356), 5)
            rect_astronauta.top+=sem_pressionar
            screen.blit(astronauta, rect_astronauta)
            p.display.update()
            time_passed = clock.tick(30)
            if rect_astronauta.top<5:
                jogo=2
            if rect_astronauta.top>420:
                jogo=2
            if rect_astronauta.left<-270:
                jogo=3

        if jogo==2:
            screen.fill(BLACK)
            screen.blit(segunda_tela, (0,0))
            screen.blit(astronauta, rect_astronauta)
            entrada = texto(perdeu,280, 320)
            entrada.novo_blit(fonte_perdeu, WHITE, screen, 0)
            p.display.update()
            time_passed = clock.tick(30)
            p.time.delay(7000)
            import jogo_integrado.py

        if jogo==3:
            screen.fill(BLACK)
            screen.blit(segunda_tela, (0,0))
            screen.blit(astronauta, rect_astronauta)
            entrada = texto(ganhou,50, 230)
            entrada.novo_blit(fonte_jogo, WHITE, screen, 40)
            time_passed = clock.tick(30)
            p.time.delay(3000)
            import jogo_integrado.py
            
            
            
            



            