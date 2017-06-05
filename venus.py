import pygame as p
from pygame.locals import* 
from sys import exit
from os import system
from classe import texto

p.init()


screen = p.display.set_mode((1200, 760))
p.display.set_caption('Vênus')
astronauta = p.image.load('animaok.gif').convert()
astronauta_position = [900, 20]


BLACK = (0,0,0)
WHITE = (255, 255, 255)



primeira_tela = p.image.load('venus.jpg')
segunda_tela = p.image.load('ceu_venus.jpg').convert()
terceira_tela = p.image.load('surface_venus.png').convert()
x = 1200
rect_branco = p.image.load('white_rect.png').convert()
robo = p.image.load('curiosity_png.png').convert_alpha()
rect_robo = robo.get_rect()
rect_robo.right = 600
rect_robo.top = 460
bigorna = p.image.load('bigorna.png').convert_alpha()
rect_bigorna = bigorna.get_rect()
rect_bigorna.top = 0
rect_bigorna.right = 500
fogo = p.image.load('fogo.png').convert()
rect_fogo = fogo.get_rect()
rect_fogo.top = 300
rect_fogo.right = 500


clock = p.time.Clock()

p.font.init()

fonte_padrao = p.font.get_default_font()
fonte_jogo = p.font.SysFont(fonte_padrao, 35)
fonte_ganhou = p.font.SysFont(fonte_padrao, 50)
fonte_perdeu = p.font.SysFont(fonte_padrao, 100)
fonte_novoperdeu = p.font.SysFont(fonte_padrao, 60)

para_frente = 20
para_tras = 5
para_cima = 10
para_baixo = 10
sem_pressionar = 5
pular = 30




events = p.event.get()

jogo = 0

while jogo == 0:
    for event in events:
        if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.display.quit()
    screen.blit(primeira_tela, (0, 0)) #coloca a imagem no display
    screen.blit(astronauta, (astronauta_position))
    #criando textos
    tela_1 = ["Olá, astronauta! Meu nome é Vênus...", "...e eu sou o planeta mais quente do Sistema Solar...", "...além de ser um dos astros mais brilhantes...", "...no céu noturno aí da Terra!", "Só perco para a Lua!", "Para conseguir passar por mim,", "sua primeira missão é acertar quem sou eu no céu noturno!", "Pressione ENTER para avançar!"] 
    tela_2 = ["INSTRUÇÕES", "Clique sobre o ponto no céu...,", "...o qual você acredita ser o planeta Vênus!"]
    ganhou = ["É ISSO AÍ AMIGÃO/AMIGONA!"] 
    ganhou1 = ["ESTE SOU EU MESMO!"]
    ganhou2 = ["PRESTE MAIS ATENÇÃO EM MIM..."]
    ganhou3 = ["...DA PRÓXIMA VEZ QUE OLHAR PARA O CÉU!"] 
    ganhou4 = ["MISSÃO CUMPRIDA COM SUCESSO!"]
    perdeu1 = ["Este não sou eu!"]
    perdeu2 = ["Foi por pouco!!! Esta é a Lua, o satélite natural da Terra..."]
    perdeu2_continue = ["...e o astro mais luminoso do céu noturno!"]
    perdeu3 = ["Foi por pouco!!! Este é o planeta Júpiter!"]
    perdeu3_continue = ["Que, às vezes, pode ser visto da Terra a olho nu!"]
    perdeu0 = ["GAME OVER!"]
    #tela_redirecionamento = ["Você venceu a primeira etapa do jogo!", "Para passar por mim, ainda tem de cumprir mais uma etapa!", "Guie o robô..."]
   
   #inserindo textos no display
    entrada = texto(tela_1,120, 40)
    entrada.novo_blit(fonte_jogo, WHITE, screen, 44)
    #p.draw.rect(screen, WHITE, (150, 400, 100, 200))
    entrada_2 = texto(tela_2, 120, 400)
    entrada_2.novo_blit(fonte_jogo, WHITE, screen, 60)


    

    p.display.update()
    time_passed = clock.tick(30)

    jogo=0
    
    
    while True:
        events = p.event.get()
        for event in events:
            if jogo==0:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
                    if event.key == p.K_RETURN:
                        screen.fill(BLACK)
                        screen.blit(segunda_tela, (0,0))
                        rect_branco.set_alpha(0)
                        screen.blit(rect_branco, (840, 248))
                        screen.blit(rect_branco, (760, 303))
                        screen.blit(rect_branco, (800, 348))
                        p.display.update()
                        time_passed = clock.tick(30)
                if event.type == p.MOUSEBUTTONDOWN:
                    position = p.mouse.get_pos()
                    if 760+30>position[0]>760 and 303+30>position[1]>303:
                        entrada = texto(ganhou,350, 100)
                        entrada.novo_blit(fonte_ganhou, WHITE, screen, 40)
                        entrada = texto(ganhou1,403, 200)
                        entrada.novo_blit(fonte_ganhou, WHITE, screen, 40)
                        entrada = texto(ganhou2,320, 300)
                        entrada.novo_blit(fonte_ganhou, WHITE, screen, 40)
                        entrada = texto(ganhou3,230, 400)
                        entrada.novo_blit(fonte_ganhou, WHITE, screen, 40)
                        entrada = texto(ganhou4,290, 500)
                        entrada.novo_blit(fonte_ganhou, WHITE, screen, 40)
                        p.time.delay(5000)
                        #screen.fill(BLACK)
                        #screen.blit(primeira_tela, (0, 0))
                        #entrada = texto(tela_redirecionamento,95, 20)
                        #entrada.novo_blit(fonte_jogo, WHITE, screen, 40)
                        #p.time.delay(3000)
                        #jogo = 1
                        import jogo_integrado.py
                    elif 840+30>position[0]>840 and 248+30>position[1]>248:
                        entrada = texto(perdeu2,30, 100)
                        entrada.novo_blit(fonte_novoperdeu, WHITE, screen, 60)
                        entrada = texto(perdeu2_continue,150, 200)
                        entrada.novo_blit(fonte_novoperdeu, WHITE, screen, 60)
                        entrada = texto(perdeu0,350, 350)
                        entrada.novo_blit(fonte_perdeu, WHITE, screen, 40)
                        p.time.delay(4000)
                        import jogo_integrado.py
                    elif 800+30>position[0]>800 and 348+30>position[1]>348:
                        entrada = texto(perdeu3,170, 100)
                        entrada.novo_blit(fonte_novoperdeu, WHITE, screen, 60)
                        entrada = texto(perdeu3_continue,100, 200)
                        entrada.novo_blit(fonte_novoperdeu, WHITE, screen, 60)
                        entrada = texto(perdeu0,350, 350)
                        entrada.novo_blit(fonte_perdeu, WHITE, screen, 40)
                        p.time.delay(4000)
                        import jogo_integrado.py
                    else:
                        entrada = texto(perdeu1,305, 200)
                        entrada.novo_blit(fonte_perdeu, WHITE, screen, 40)
                        entrada = texto(perdeu0,350, 300)
                        entrada.novo_blit(fonte_perdeu, WHITE, screen, 40)
                        p.time.delay(4000)
                        import jogo_integrado.py

                        
            
                    #if position[0]==835 and position[1]==245:
                        #jogo=2
                        #jogo = 1
            if jogo==1:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
                    """if event.key == p.K_RIGHT:
                        screen.fill(BLACK)
                        screen.blit(terceira_tela, (0,0))
                        rect_robo.right-=para_tras
                        screen.blit(robo, rect_robo)
                        p.display.update()
                        time_passed = clock.tick(30)
                    if event.key == p.K_RIGHT:
                        screen.fill(BLACK)
                        screen.blit(terceira_tela, (0,0))
                        rect_robo.right+=para_frente
                        screen.blit(robo, rect_robo)
                        p.display.update()
                        time_passed = clock.tick(30)
                    if event.key == p.K_UP:
                        screen.fill(BLACK)
                        screen.blit(terceira_tela, (0,0))
                        if rect_robo.top>80:
                            rect_robo.top-=para_cima
                            screen.blit(robo, rect_robo)
                            p.display.update()
                            time_passed = clock.tick(30)
                    if event.key == p.K_DOWN:
                        screen.fill(BLACK)
                        screen.blit(terceira_tela, (0,0))
                        if rect_robo.top<330:
                            rect_robo.top+=para_baixo
                            screen.blit(robo, rect_robo)
                            p.display.update()
                            time_passed = clock.tick(30)
                    if event.key == p.K_SPACE:
                        screen.fill(BLACK)
                        screen.blit(terceira_tela, (0,0))
                        if rect_robo.top>80:
                            rect_robo.top-=pular
                            screen.blit(robo, rect_robo)
                            p.display.update()
                            time_passed = clock.tick(30)"""

        if jogo==1:
            screen.fill(BLACK)
            #rect_terceiratela.right-=sem_pressionar
            rel_x = x % terceira_tela.get_rect().width
            screen.blit(terceira_tela, (rel_x-terceira_tela.get_rect().width,398))
            if rel_x<1200:
                screen.blit(terceira_tela, (rel_x, 398))
            x-=sem_pressionar
            rect_bigorna.top+=sem_pressionar
            screen.blit(bigorna, rect_bigorna)
            screen.blit(fogo, rect_fogo)
            #if rect_terceiratela.right==20
            #rect_robo.right+=sem_pressionar
            screen.blit(robo, rect_robo)
            p.display.update()
            time_passed = clock.tick(30)
            if rect_robo.right>1240:
                screen.fill(BLACK)
                rect_robo.right = 550
                screen.blit(robo, rect_robo)


        if jogo==2:
            entrada = texto(ganhou,95, 20)
            entrada.novo_blit(fonte_jogo, WHITE, screen, 40)
                

            


            

        