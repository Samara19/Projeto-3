import pygame as p
from pygame.locals import* 
from sys import exit
from os import system

p.init()

screen = p.display.set_mode((950, 712), 0, 32)

p.display.set_caption('Mercúrio')

planeta_filename = 'mercurio.jpg'  #adiciona uma imagem ao programa
planeta = p.image.load(planeta_filename).convert()
anima_filename = 'animaok.gif'
anima = p.image.load(anima_filename).convert()

clock = p.time.Clock()

p.font.init()

fonte_padrao = p.font.get_default_font()
fonte_jogo = p.font.SysFont(fonte_padrao, 25)
fonte_fim = p.font.SysFont(fonte_padrao, 40)




x = 0
events = p.event.get()
pressed_keys = p.key.get_pressed()
while x==0:
    
            
    screen.blit(planeta, (0, 0)) #coloca a imagem no display
    screen.blit(anima, (680, 20))
    #criando textos
    texto = fonte_jogo.render('Olá Astronauta, você chegou em Mercúrio, o planeta mais próximo do Sol!',1,(255,255,255))
    t1 = fonte_jogo.render('Mercúrio é um pouco maior que a Lua da Terra,',1,(255,255,255))
    t2 = fonte_jogo.render('tem muitas crateras e não possui uma atmosfera significativa para impedir a entrada de meteoros.',1,(255,255,255))
    t3 = fonte_jogo.render('Existe uma parte do planeta que nunca recebe iluminação solar,',1,(255,255,255))
    t4 = fonte_jogo.render('onde ficam crateras com água congelada.',1,(255,255,255))
    
    screen.fill ((0,0,0))
    screen.blit(planeta, (0, 0)) #coloca a imagem no display
    screen.blit(anima, (680, 20))
    
    t5 = fonte_jogo.render('Para continuar, responda a seguinte pergunta:',1,(255,255,255))
    t6 = fonte_jogo.render('Quantos planetas existem no Sistema Solar?(lembre-se que Plutão não é considerado planeta.)',1,(255,255,255))
    t7 = fonte_jogo.render('Existe água em mercúrio?',1,(255,255,255))
    t8 = fonte_jogo.render('A atmosfera de Mercúrio permite a entrada de que objeto do espaço?',1,(255,255,255))
    t9 = fonte_jogo.render('1) 9 planetas, não, meteoros;',1,(255,255,255))
    t10 = fonte_jogo.render('2) 8 planetas, sim, astronautas;',1,(255,255,255))
    t11 = fonte_jogo.render('3) 8 planetas, sim, meteoros;',1,(255,255,255))    
    t12 = fonte_jogo.render('Parábens, aperte espaço para continuar!',1,(255,255,255))
    t13 = fonte_jogo.render('A resposta correta é a alternativa 3, aperte espaço para ir para a próxima questão!',1,(255,255,255))
    t14 = fonte_jogo.render('Pressione espaço para continuar.',1,(255,255,255))
    t15 = fonte_jogo.render('a) 9 planetas',1,(255,255,255))
    t16 = fonte_jogo.render('b) 8 planetas',1,(255,255,255))
    t17 = fonte_jogo.render('c) 7 planetas',1,(255,255,255))
    t18 = fonte_jogo.render('A resposta correta é a alternativa 2, aperte espaço para ir para a próxima questão!',1,(255,255,255))
    t19 = fonte_jogo.render('A resposta correta é a alternativa 1, aperte espaço para ir para a próxima questão!',1,(255,255,255))
    t20 = fonte_jogo.render('a) sim',1,(255,255,255))
    t21 = fonte_jogo.render('b) não',1,(255,255,255))
    t22 = fonte_jogo.render('c) talvez',1,(255,255,255))
    t23 = fonte_jogo.render('a) astronautas',1,(255,255,255))
    t24 = fonte_jogo.render('b) pássaros',1,(255,255,255))
    t25 = fonte_jogo.render('c) meteoros',1,(255,255,255))
    t26 = fonte_fim.render('Parabéns, Astronauta. Você completou a missão em Mercúrio!',1,(255,255,255))
    
   #inserindo textos no display
    screen.blit(texto, (100,20))
    screen.blit(t1, (100,50))
    screen.blit(t2, (100,70))
    screen.blit(t3, (100,90))
    screen.blit(t4, (100,110))
    screen.blit(t14, (100,130))
    
    

    p.display.update()
    time_passed = clock.tick(30)
    
    while x == 0:
        events = p.event.get()
        for event in events:
            if event.type == p.KEYDOWN:
                if event.key == p.K_3:
                    screen.blit(t12, (100,300))
                    screen.blit(t14, (100,340))
                    p.display.update()
                    time_passed = clock.tick(30)
                elif event.key == p.K_2 or event.key == p.K_1:
                    screen.blit(t13, (100,300))
                    screen.blit(t14, (100,340))
                    p.display.update()
                    time_passed = clock.tick(30)
                elif event.key == p.K_ESCAPE:
                    x = 1
                    p.display.quit()
                elif event.key == K_SPACE:
                    screen.fill((0,0,0))
                    screen.blit(planeta, (0,0))
                    screen.blit(anima, (680,20))
                    screen.blit(t5, (100,120))
                    screen.blit(t6, (100,160))
                    screen.blit(t15, (100,180))
                    screen.blit(t16, (100,200))
                    screen.blit(t17, (100,220))
                    p.display.update()
                    time_passed = clock.tick(30)
                    
                elif event.key == p.K_b:
                    screen.blit(t12, (100,300))
                    p.display.update()
                    time_passed = clock.tick(30)
                    x = 1
                elif event.key == p.K_a or p.K_c:
                    screen.blit(t18, (100,300))
                    p.display.update()
                    time_passed = clock.tick(30)
                    x = 1
                
                
    while x == 1:
        events = p.event.get()
        for event in events:
            if event.type == p.KEYDOWN:
                if event.key == K_SPACE:
                    screen.fill((0,0,0))
                    screen.blit(planeta, (0,0))
                    screen.blit(anima, (680,20))
                    screen.blit(t7, (100,120))
                    screen.blit(t20, (100,180))
                    screen.blit(t21, (100,200))
                    screen.blit(t22, (100,220))
                    p.display.update()
                    time_passed = clock.tick(30)
                elif event.key == p.K_a:
                    screen.blit(t12, (100,300))
                    p.display.update()
                    time_passed = clock.tick(30)
                    x = 2
                elif event.key == p.K_b or p.K_c:
                    screen.blit(t18, (100,300))
                    p.display.update()
                    time_passed = clock.tick(30)
                    x = 2
    while x == 2:
        events = p.event.get()
        for event in events:
            if event.type == p.KEYDOWN:
                if event.key == K_SPACE:
                    screen.fill((0,0,0))
                    screen.blit(planeta, (0,0))
                    screen.blit(anima, (680,20))
                    screen.blit(t8, (100,120))
                    screen.blit(t23, (100,180))
                    screen.blit(t24, (100,200))
                    screen.blit(t25, (100,220))
                    p.display.update()
                    time_passed = clock.tick(30)
                elif event.key == p.K_c:
                    screen.blit(t12, (100,300))
                    p.display.update()
                    time_passed = clock.tick(30)
                    x = 3
                elif event.key == p.K_b or p.K_a:
                    screen.blit(t18, (100,300))
                    p.display.update()
                    time_passed = clock.tick(30)
                    x = 3
    while x == 3:
        events = p.event.get()
        for event in events:
            if event.type == p.KEYDOWN:
                if event.key == K_SPACE:
                    screen.fill((0,0,0))
                    screen.blit(planeta, (0,0))
                    screen.blit(anima, (680,20))
                    screen.blit(t26, (25,300))
                    p.display.update()
                    time_passed = clock.tick(30)
                    import jogo_integrado.py
        



        
                
         
            
    
    






