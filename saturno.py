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
primeira_conta = p.image.load('primeira_conta.png').convert()
segunda_conta = p.image.load('segunda_conta.png').convert()
terceira_conta_1 = p.image.load('terceira_conta_1.png').convert()
terceira_conta_2 = p.image.load('terceira_conta_2.png').convert()
terceira_conta_3 = p.image.load('terceira_conta_3.png').convert()
fundo_estrelado = p.image.load('fundo_estrelado.jpg').convert()


clock = p.time.Clock()

p.font.init()

fonte_padrao = p.font.get_default_font()
fonte_jogo = p.font.SysFont(fonte_padrao, 35)

fonte_perdeu = p.font.SysFont(fonte_padrao, 100)
fonte_curiosidades = p.font.SysFont(fonte_padrao, 55)
BLACK = (0,0,0)
WHITE = (255, 255, 255)


events = p.event.get()

jogo = 0
pergunta = 0
respostas_certas = 0

while jogo == 0:
    for event in events:
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0)) #coloca a imagem no display
    screen.blit(astronauta, (astronauta_position))
    #criando textos
    entrada = ["BEM VINDO(A)..."]
    tela_1 = ["Olá, astronauta! Seja bem vindo...", "...ao segundo maior planeta do Sistema Solar!", "Para conseguir passar por mim,", "você terá de provar ser muito bom...", "ou boa em Matemática!", "E olha que não é fácil não, hein?", "Está preparado para começar?", "Se sim, pressione ENTER para avançar!"] 
    pergunta_1 = ["Pois bem, vamos começar:", "Diga-me, quanto é                      ?", "Poooxa, é fácil, vamos lá, eu acredito em você!", "", "", "Digite 1 para 50", "Digite 2 para 47", "Digite 3 para 90", "Ou 4 para 62"]
    titulo = ["CURIOSIDADES"]
    curiosidade_1 = ["Saturno possui 62 SATÉLITES NATURAIS!", "Imagine a Terra com 62 Luas!!!", "Pois é, bem vindo(a) à realidade de Saturno!", "Pressione ENTER para avançar!"]
    pergunta_2 = ["Segunda pergunta:", "Quanto é                    ?", "", "", "Digite 1 para 28,5", "Digite 2 para 29,5", "Digite 3 para 19,5", "Ou digite 4 para 30,5"]
    curiosidade_2 = ["1 ano de Saturno...", "...equivale a 29,5 anos terrestres!", "Imagine demorar 29,5 anos terrestres...", "...para completar um ano de vida!", "Animal!!!", "Pressione ENTER para avançar!"]
    pergunta_3 = ["Responda na sequência:", "", "", "Digite 1 para 10, 32 e 35, nesta ordem!", "Digite 2 para 32, 10 e 35, nesta ordem!", "Digite 3 para 100, 42 e 45, nesta ordem!", "Ou digite 4 para 10, 42 e 35, nesta ordem!"]
    curiosidade_3 = ["O dia de Saturno...", "...não possui 24 horas como o nosso!", "Possui apenas 10 horas,...", "...32 minutos e 35 segundos!", "O dia de Saturno termina antes...", "...que o nosso chegue à metade!"]
    acertou = ["Certa resposta!"]
    errou = ["Resposta incorreta!"]
    ganhou = ["Opa, é isso aí amiguinho(a)!", "Missão cumprida com sucesso!", "Já pode prosseguir viagem!", "Até mais!"]
    perdeu = ["GAME OVER!"]
    again = ["Infelizmente, não foi dessa vez!"]
    again_2 = ["Pressione ENTER para tentar novamente!"]
   
   #inserindo textos no display
    ini_title = texto(entrada,95, 50)
    apresentacao = texto(tela_1,95, 200)
    first_question = texto(pergunta_1,95, 50)
    second_question = texto(pergunta_2,95, 50)
    third_question = texto(pergunta_3,95, 50)
    curio_title = texto(titulo,95, 20)
    curio_1 = texto(curiosidade_1,95, 150)
    curio_2 = texto(curiosidade_2,95, 200)
    curio_3 = texto(curiosidade_3,95, 150)
    certo = texto(acertou,200, 250)
    errado = texto(errou,140, 250)
    ganha = texto(ganhou,95, 20)
    perde = texto(perdeu,250, 200)
    novamente = texto(again,285, 300)
    novamente_2 = texto(again_2, 230, 350)



    ini_title.novo_blit(fonte_perdeu, WHITE, screen, 40)
    apresentacao.novo_blit(fonte_jogo, WHITE, screen, 40)
  

    

    p.display.update()
    time_passed = clock.tick(30)
    
    
    while True:
        events = p.event.get()
        for event in events:
            if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
            if jogo==0:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        screen.fill(BLACK)
                        screen.blit(background, (0,0))
                        screen.blit(primeira_conta, (315, 145))
                        screen.blit(astronauta, astronauta_position)
                        first_question.novo_blit(fonte_jogo, WHITE, screen, 50)
                        pergunta=1
                        p.display.update()
                        time_passed = clock.tick(30)
                    if event.key == p.K_1:
                        jogo=4
                    if event.key == p.K_2:
                        jogo=4
                    if event.key == p.K_3:
                        jogo=4
                    if event.key == p.K_4:
                        respostas_certas+=1
                        print(respostas_certas)
                        jogo=3
            
            if jogo==1:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
                    if event.key == p.K_RETURN:
                        screen.fill(BLACK)
                        screen.blit(background, (0,0))
                        screen.blit(astronauta, astronauta_position)
                        screen.blit(segunda_conta, (220, 145))
                        second_question.novo_blit(fonte_jogo, WHITE, screen, 50)
                        pergunta=2
                        p.display.update()
                        time_passed = clock.tick(30)
                    if event.key == p.K_1:
                        jogo=4
                    if event.key == p.K_2:
                        respostas_certas+=1
                        jogo=3
                    if event.key == p.K_3:
                        jogo=4
                    if event.key == p.K_4:
                        jogo=4
            
            if jogo==2:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
                    if event.key == p.K_RETURN:
                        screen.fill(BLACK)
                        screen.blit(background, (0,0))
                        screen.blit(astronauta, astronauta_position)
                        screen.blit(terceira_conta_1, (95, 150))
                        screen.blit(terceira_conta_2, (260, 150))
                        screen.blit(terceira_conta_3, (360, 150))
                        third_question.novo_blit(fonte_jogo, WHITE, screen, 50)
                        pergunta=3
                        p.display.update()
                        time_passed = clock.tick(30)
                    if event.key == p.K_1:
                        respostas_certas+=1
                        jogo=3
                    if event.key == p.K_2:
                        jogo=4
                    if event.key == p.K_3:
                        jogo=4
                    if event.key == p.K_4:
                        jogo=4

            if jogo==3:
                screen.fill(BLACK)
                screen.blit(background, (0,0))
                screen.blit(astronauta, astronauta_position)
                certo.novo_blit(fonte_perdeu, WHITE, screen, 40)
                p.time.delay(3000)
                p.display.update()
                time_passed = clock.tick(30)
                if pergunta==1:
                    screen.blit(fundo_estrelado, (0, 0))
                    curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                    curio_1.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                    jogo=1
                elif pergunta==2:
                    screen.blit(fundo_estrelado, (0, 0))
                    curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                    curio_2.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                    jogo=2
                elif pergunta==3:
                    screen.blit(fundo_estrelado, (0, 0))
                    curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                    curio_3.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                    p.time.delay(3000)
                    if respostas_certas==3:
                        p.display.quit()
                        #screen.fill(BLACK)
                        #screen.blit(background, (0,0))
                        #screen.blit(astronauta, astronauta_position)
                        #ganha.novo_blit(fonte_jogo, WHITE, screen, 40)
                    else:
                        screen.fill(BLACK)
                        screen.blit(background, (0,0))
                        screen.blit(astronauta, astronauta_position)
                        perde.novo_blit(fonte_perdeu, WHITE, screen, 40)
                        novamente.novo_blit(fonte_jogo, WHITE, screen, 40)
                        novamente_2.novo_blit(fonte_jogo, WHITE, screen, 40)
                        jogo=0



            if jogo==4:   
                screen.fill(BLACK)
                screen.blit(background, (0,0))
                screen.blit(astronauta, astronauta_position)
                errado.novo_blit(fonte_perdeu, WHITE, screen, 40)
                p.time.delay(3000)
                p.display.update()
                time_passed = clock.tick(30)
                if pergunta==1:
                    screen.blit(fundo_estrelado, (0,0))
                    curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                    curio_1.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                    jogo=1
                elif pergunta==2:
                    screen.blit(fundo_estrelado, (0,0))
                    curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                    curio_2.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                    jogo=2
                elif pergunta==3:
                    screen.blit(fundo_estrelado, (0,0))
                    curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                    curio_3.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                    p.time.delay(7000)
                    screen.fill(BLACK)
                    screen.blit(background, (0,0))
                    screen.blit(astronauta, astronauta_position)
                    perde.novo_blit(fonte_perdeu, WHITE, screen, 40)
                    novamente.novo_blit(fonte_jogo, WHITE, screen, 40)
                    novamente_2.novo_blit(fonte_jogo, WHITE, screen, 40)
                    jogo=0





            