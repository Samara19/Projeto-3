import pygame as p
from pygame.locals import* 
from sys import exit
from os import system
from classe import texto
from classes import Button
from classe_texto1 import texto1
from classe_texto import texto

p.init()

screen = p.display.set_mode((1000, 663), 0, 32)
p.display.set_caption('Space Trek')

"""som_foguete=p.mixer.Sound("somfoguete.wav")
som_netuno=p.mixer.Sound("netuno.wav")"""

PRETO= (0,0,0)
BRANCO= (255,255,255)
VERDE= (0,255,0)
VERMELHO= (255,0,0)
AZUL=(0,0,255)

"""fonte = p.font.Font(None, 30)


screen = p.display.set_mode((1000, 663), 0, 32)
p.display.set_caption('Space Trek')"""


primeira_tela = p.image.load('fundo2.png')
"""background_filename = 'fundo2.png'
background = p.image.load(background_filename).convert()
background_filename0 = 'fundo0.jpg'
background0 = p.image.load(background_filename0).convert()
logo=p.image.load("logo.png")
ImagemNave=p.image.load("fog.png")
rect=ImagemNave.get_rect()"""


clock = p.time.Clock()

p.font.init()

fonte_padrao = p.font.get_default_font()
fonte_jogo = p.font.SysFont(fonte_padrao, 30)
fonte_menor = p.font.SysFont(fonte_padrao, 20)
fonte_ganhou = p.font.SysFont(fonte_padrao, 50)
fonte_perdeu = p.font.SysFont(fonte_padrao, 100)
fonte_novoperdeu = p.font.SysFont(fonte_padrao, 60)

"""texto_aviso=fonte.render("Aperte enter para continuar",1,BRANCO)
texto_cria=fonte.render("Criadoras:Ana,Samara e Tainara",1,BRANCO)




som_inicio=p.mixer.Sound("inicio.wav")


textos11=["Olá viajante!","Precisamos que você nos traga informações importantes sobre o espaço,","passe por cada um dos planetas complete os desafios para coletar informações!","Contamos com você!"]
textosposnept=["Bom trabalho viajante!","Demos sorte de conseguir entrar na chuva de diamantes de netuno!","Pronto para o próximo planeta?!"]
textosposurano=["Bom trabalho viajante!","A atmosfera de urano é mesmo interessante! ","Pronto para o próximo planeta?!"]
textospossaturno=["Bom trabalho viajante!","Descobrimos muitas coisas sobre saturno!","Pronto para o próximo planeta?!"]
textospojupiter=["Bom trabalho viajante!","Sobrevivemos a uma gravidade igual 2,4 vezes a da Terra  " ,"Pronto para o próximo planeta?!"]
textospomarte=["Bom trabalho viajante!","O drone coletou informações preciosas! " ,"Pronto para o próximo planeta?!"]
textospovenus=["Bom trabalho viajante!","Vênus é um planeta muito curioso! " ,"Pronto para o próximo planeta?!"]
textospoterra=["Bom trabalho viajante!","Os dados coletados são extremamente úteis!","Pode retornar para  Terra! Até outra viajem!" ]

screen.blit((background0),(0, 0))
som_inicio.play(2)
p.display.update()
p.time.wait(6000)
screen.blit(logo,(230,250))
p.display.update()
p.time.wait(4000)
screen.blit((texto_cria),(230,500))


p.display.update()
p.time.wait(2000)
screen.fill(PRETO)

screen.blit(ImagemNave,(900,100))

screen.blit((background),(0, 0))
screen.blit((texto_aviso),(700,400))
p.display.update()






contador=0



clock = p.time.Clock()
while True:
    
    for event in p.event.get():
        if event.type == QUIT:
             som_inicio.stop()
             p.display.quit()
             exit()
             
            
        tecla=p.key.get_pressed()
        if event.type==KEYDOWN:
            if tecla[K_RETURN]:
               
                if contador<4:
                    te=[textos11[contador]]
                    novos_textos=texto1(te,0,500)
                    novos_textos.novo_blit1(fonte,BRANCO,screen,20,contador)
                    p.display.update()
                    time_passed = clock.tick(30)
                    contador=contador+1
                    
                elif contador==4:
                    som_foguete.play(1)
                    p.time.wait(1000)
                    screen.fill(PRETO)
                    numero=range(10)
                    repeticao=[]
                    
                    
                    for a in numero:
                        repeticao.append((900-8*a,100-10*a))
                    for i in repeticao:
    
                        screen.blit((background),(0, 0))
                        screen.blit((texto_aviso),(700,400))

                        screen.blit(ImagemNave,i)
                        p.display.update()
                        ultima_posicao=i
                        time_passed = clock.tick(30)
                    som_foguete.stop()    
                    print(i)
                    textos=["Vamos primeiramente para Netuno!"]
                    novos_textos=texto1(textos,0,500)
                    novos_textos.novo_blit1(fonte,BRANCO,screen,10,0)
                    p.display.update()
                    time_passed = clock.tick(30)
                    contador=contador+1
                elif contador==5:
                    som_inicio.stop()"""


events = p.event.get()

andamento = 0

while andamento == 0:
    for event in events:
        if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.display.quit()
    screen.blit(primeira_tela, (0, 0)) #coloca a imagem no display
    planeta1 = ["Netuno"]
    planeta2 = ["Urano"]
    planeta3 = ["Saturno"]
    planeta4 = ["Júpiter"]
    planeta5 = ["Marte"]
    planeta6 = ["Vênus"]
    planeta7 = ["Mercúrio"]
    planeta8 = ["Terra"]
    netuno = Button(screen, PRETO, 800, 75, 85, 36, planeta1, fonte_jogo, BRANCO)
    netuno.desenha_tela()
    urano = Button(screen, PRETO, 730, 130, 73, 36, planeta2, fonte_jogo, BRANCO)
    urano.desenha_tela()
    saturno = Button(screen, PRETO, 590, 190, 93, 36, planeta3, fonte_jogo, BRANCO)
    saturno.desenha_tela()
    jupiter = Button(screen, PRETO, 470, 260, 85, 36, planeta4, fonte_jogo, BRANCO)
    jupiter.desenha_tela()
    marte = Button(screen, PRETO, 360, 205, 70, 36, planeta5, fonte_jogo, BRANCO)
    marte.desenha_tela()
    venus = Button(screen, PRETO, 220, 295, 80, 36, planeta6, fonte_jogo, BRANCO)
    venus.desenha_tela()
    mercurio = Button(screen, PRETO, 115, 320, 100, 36, planeta7, fonte_jogo, BRANCO)
    mercurio.desenha_tela()
    terra = Button(screen, PRETO, 300, 255, 50, 36, planeta8, fonte_jogo, BRANCO)
    terra.desenha_tela()


 


    

    p.display.update()
    time_passed = clock.tick(30)
    
    
    while True:
        events = p.event.get()
        for event in events:
            if andamento==0:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        p.display.quit()
                if event.type == p.MOUSEBUTTONDOWN:
                    netuno.play()
                    urano.play()
                    saturno.play()
                    jupiter.play()
                    marte.play()
                    venus.play()
                    mercurio.play()
                    