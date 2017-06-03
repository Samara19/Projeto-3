import pygame
from pygame.locals import *
from sys import exit
from classe_texto1 import texto1
from classe_texto import texto

from random import randrange
 
pygame.init()

som_foguete=pygame.mixer.Sound("somfoguete.wav")
som_netuno=pygame.mixer.Sound("netuno.wav")

PRETO= (0,0,0)
BRANCO= (255,255,255)
VERDE= (0,255,0)
VERMELHO= (255,0,0)
AZUL=(0,0,255)

fonte = pygame.font.Font(None, 30)
p=pygame


screen = pygame.display.set_mode((1000, 663), 0, 32)
pygame.display.set_caption('Space Trek')


background_filename = 'fundo2.png'
background = pygame.image.load(background_filename).convert()
background_filename0 = 'fundo0.jpg'
background0 = pygame.image.load(background_filename0).convert()
logo=pygame.image.load("logo.png")
ImagemNave=pygame.image.load("fog.png")
rect=ImagemNave.get_rect()






texto_aviso=fonte.render("Aperte enter para continuar",1,BRANCO)
texto_cria=fonte.render("Criadoras:Ana,Samara e Tainara",1,BRANCO)




som_inicio=pygame.mixer.Sound("inicio.wav")


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
pygame.display.update()
pygame.time.wait(6000)
screen.blit(logo,(230,250))
pygame.display.update()
pygame.time.wait(4000)
screen.blit((texto_cria),(230,500))


pygame.display.update()
pygame.time.wait(2000)
screen.fill(PRETO)

screen.blit(ImagemNave,(900,100))

screen.blit((background),(0, 0))
screen.blit((texto_aviso),(700,400))
pygame.display.update()






contador=0



clock = pygame.time.Clock()
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
             som_inicio.stop()
             p.display.quit()
             exit()
             
            
        tecla=pygame.key.get_pressed()
        if event.type==KEYDOWN:
            if tecla[K_RETURN]:
               
                if contador<4:
                    te=[textos11[contador]]
                    novos_textos=texto1(te,0,500)
                    novos_textos.novo_blit1(fonte,BRANCO,screen,20,contador)
                    pygame.display.update()
                    time_passed = clock.tick(30)
                    contador=contador+1
                    
                elif contador==4:
                    som_foguete.play(1)
                    pygame.time.wait(1000)
                    screen.fill(PRETO)
                    numero=range(10)
                    repeticao=[]
                    
                    
                    for a in numero:
                        repeticao.append((900-8*a,100-10*a))
                    for i in repeticao:
    
                        screen.blit((background),(0, 0))
                        screen.blit((texto_aviso),(700,400))

                        screen.blit(ImagemNave,i)
                        pygame.display.update()
                        ultima_posicao=i
                        time_passed = clock.tick(30)
                    som_foguete.stop()    
                    print(i)
                    textos=["Vamos primeiramente para Netuno!"]
                    novos_textos=texto1(textos,0,500)
                    novos_textos.novo_blit1(fonte,BRANCO,screen,10,0)
                    pygame.display.update()
                    time_passed = clock.tick(30)
                    contador=contador+1
                elif contador==5:
                    som_inicio.stop()
                    while True:
                        fonte_padrao = pygame.font.get_default_font()
                        fonte_jogo = pygame.font.SysFont(fonte_padrao, 25)
                        fonte_over = pygame.font.SysFont(fonte_padrao, 200)
                        fonte_fim = pygame.font.SysFont(fonte_padrao, 100)
                        fonte_esc = pygame.font.SysFont(fonte_padrao, 30)

                        screen = pygame.display.set_mode((1000, 650), 0, 32)

                        planeta_filename = 'netuno.jpg'
                        planeta = pygame.image.load(planeta_filename).convert()
                        nave = {'surface': pygame.image.load('nave.png').convert_alpha(),'position': [randrange(956), randrange(560)],'speed': {'x': 0,'y': 0}}


                        pygame.display.set_caption('Netuno')
                        t1 = fonte_jogo.render('Diamantes:',1,(255,255,255))
                        t3 = fonte_jogo.render('Vida:',1,(255,255,255))
                        t5 = fonte_jogo.render('Olá Astronauta, você chegou em Netuno',1,(255,255,255))
                        t6 = fonte_jogo.render('o planeta com os ventos mais velozes do Sistema Solar! Aqui em Netuno chove diamante (de verdade).',1,(255,255,255))
                        t7 = fonte_jogo.render('Porém, nosso planeta tem muitas nuvens de amoníco, que fazem mal para o ser humano!',1,(255,255,255))
                        t8 = fonte_jogo.render('Tome cuidado ao andar por aí e pegue diamantes para a sua missão!',1,(255,255,255))
                        t9 = fonte_jogo.render('Use as setas para pegar diamantes e para desviar das nuvens! ',1,(255,255,255))
                        t10 = fonte_jogo.render('Seu objetivo é conseguir 20 diamantes para ir para a próxima missão...',1,(255,255,255))
                        screen.blit(planeta, (0, 0))
                        screen.blit(t5, (100,50))
                        screen.blit(t6, (100,70))
                        screen.blit(t7, (100,90))
                        screen.blit(t8, (100,110))
                        screen.blit(t9, (100,130))
                        screen.blit(t10, (100,150))
                        pygame.display.update()
                        pygame.time.wait(4000)
                        

                        clock = pygame.time.Clock()
                        resul=0
                        def create_diamante():
                            return ({'surface': pygame.image.load('diamantep.png').convert_alpha(),'position': [randrange(1000), -64],'speed': randrange(1, 11)})

                        def create_nuvem():
                            return({'surface': pygame.image.load('nuvem.png').convert_alpha(),'position': [0, randrange(650)],'speed': randrange(2, 9)})
                            

                        ticks_to_diamante = 20
                        diamantes = []
                        ticks_to_nuvem = 40
                        nuvens = []

                        def move_diamantes():
                            for diamante in diamantes:
                                diamante['position'][1] += diamante['speed']

                        def move_nuvens():
                            for nuvem in nuvens:
                                nuvem['position'][0] += nuvem['speed']

                        def remove_used_diamantes():
                            for diamante in diamantes:
                                if diamante['position'][1] > 650:
                                    diamantes.remove(diamante)

                        def remove_used_nuvens():
                            for nuvem in nuvens:
                                if nuvem['position'][0] > 1000:
                                    nuvens.remove(nuvem)

                        def get_rect(obj):
                            return Rect(obj['position'][0],obj['position'][1],obj['surface'].get_width(),obj['surface'].get_height())

                        def nave_collided():
                            nave_rect = get_rect(nave)
                            for diamante in diamantes:
                                if nave_rect.colliderect(get_rect(diamante)):
                                    return True
                            return False

                        collided = False
                        contador = 0
                        vida = 10
                        jogo=0
                        collided = False
                        contador = 0
                        vida = 10
                        jogo=0


                        while jogo==0 :
                            
                            som_netuno.play()
                            if not ticks_to_diamante:
                                ticks_to_diamante = 20
                                diamantes.append(create_diamante())
                                
                            else:
                                ticks_to_diamante -= 1
                                
                            if not ticks_to_nuvem:
                                ticks_to_nuvem = 40
                                nuvens.append(create_nuvem())
                                    
                            else:
                                ticks_to_nuvem -= 1                
                               
                            nave['speed'] = {'x': 0,'y': 0}

                            for event in pygame.event.get():
                                if event.type == QUIT:
                                     som_inicio.stop()
                                     p.display.quit()
                                     exit()

                            pressed_keys = pygame.key.get_pressed()
                            
                            if pressed_keys[K_UP]:
                                nave['speed']['y'] = -5
                            elif pressed_keys[K_DOWN]:
                                nave['speed']['y'] = 5

                            if pressed_keys[K_LEFT]:
                                nave['speed']['x'] = -5
                            elif pressed_keys[K_RIGHT]:
                                nave['speed']['x'] = 5

                            screen.blit(planeta, (0, 0))

                            if not collided:
                                collided = nave_collided()
                                nave['position'][0] += nave['speed']['x']
                                nave['position'][1] += nave['speed']['y']

                                screen.blit(nave['surface'], nave['position'])
                            else:
                                for diamante in diamantes[:]:
                                    nave_rect = get_rect(nave)
                                    diamante_rect = get_rect(diamante)
                                    if nave_rect.colliderect(diamante_rect):
                                                diamantes.remove(diamante)        
                                                contador = contador + 1           
                                                a = str(contador)
                                                b = str(vida)
                                                t1 = fonte_jogo.render('Diamantes:',1,(255,255,255))
                                                t2 = fonte_jogo.render(a,1,(255,255,255))
                                                t3 = fonte_jogo.render('Vida',1,(255,255,255))
                                                t4 = fonte_jogo.render(b,1,(255,255,255))
                                                t5 = fonte_jogo.render("",1,(255,255,255))
                                    for nuvem in nuvens[:]:
                                            nave_rect = get_rect(nave)
                                            nuvem_rect = get_rect(nuvem)
                                            if nave_rect.colliderect(nuvem_rect):
                                                    nuvens.remove(nuvem)
                                                    vida = vida - 1
                                                    b = str(vida)
                                                    t3 = fonte_jogo.render('Vida',1,(255,255,255))
                                                    t4 = fonte_jogo.render(b,1,(255,255,255))
                                                    pygame.display.update()
                                                    time_passed = clock.tick(30)
                                
                                screen.blit(t1,(200,200))
                                screen.blit(t2,(200,220))
                                screen.blit(t3,(300,200))
                                screen.blit(t4,(300,220))
                                
                                nave['position'][0] += nave['speed']['x']
                                nave['position'][1] += nave['speed']['y']
                                screen.blit(nave['surface'], nave['position'])
                                

                                if vida<=0:
                                    screen.fill((0,0,0))
                                    screen.blit(planeta,(0,0))
                                    t5 = fonte_over.render("GAME OVER!",1,(255,0,0))
                                    t6= fonte_fim.render("Tente novamente",1,(255,0,0))
                                    
                                    screen.blit(t5,(90,250))
                                    screen.blit(t6,(200,400))
                                    
                                    
                                    pygame.display.update()
                                    time_passed = clock.tick(30)
                                    jogo=1
                                    pygame.time.wait(4000)
                                    
                                    
                                    
                                   
                                if contador >= 20 and jogo==0:
                                    
                                    screen.fill((0,0,0))
                                    screen.blit(planeta,(0,0))
                                    t6 = fonte_fim.render("Parábens, você venceu!",1,(255,255,255))
                                    screen.blit(t6,(70,250))
                                    pygame.display.update()
                                    time_passed = clock.tick(30)
                                    pygame.time.wait(2000 )
                                    print('antes')
                                    resul="ganhou"
                                if resul=="ganhou":
                                    som_netuno.stop()
                                   
                                    screen.blit((background),(0, 0))

                                    screen.blit(ImagemNave,ultima_posicao)


                                    screen.blit((texto_aviso),(700,400))

                                    pygame.display.update()


                                    contador=0

                                    clock = pygame.time.Clock()
                                    while True:
                                        som_inicio.play(3)
                                        for event in pygame.event.get():
                                            if event.type == QUIT:
                                                 som_inicio.stop()
                                                 p.display.quit()
                                                 exit()
                                            tecla=pygame.key.get_pressed()
                                            if event.type==KEYDOWN:
                                                if tecla[K_RETURN]:
                                                    
                                                    if contador<3:
                                                        te=[textosposnept[contador]]
                                                        novos_textos=texto1(te,0,500)
                                                        novos_textos.novo_blit1(fonte,BRANCO,screen,20,contador)
                                                        pygame.display.update()
                                                        time_passed = clock.tick(30)
                                                        contador=contador+1
                                                    elif contador==3:
                                                        som_foguete.play(1)
                                                        pygame.time.wait(1000)
                                                        screen.fill(PRETO)
                                                        numero=range(15)
                                                        repeticao=[]
                                                        
                                                        for a in numero:
                                                            repeticao.append((828-8*a,10+5*a-0.2*a))
                                                        for i in repeticao:
                                                            screen.blit((background),(0, 0))
                                                            screen.blit((texto_aviso),(700,400))

                                                            screen.blit(ImagemNave,i)
                                                            pygame.display.update()
                                                            ultima_posicao=i
                                                            time_passed = clock.tick(30)
                                                        som_foguete.stop()     
                                                        print(i)
                                                        textos=["Vamos para Urano!"]
                                                        novos_textos=texto1(textos,0,500)
                                                        novos_textos.novo_blit1(fonte,BRANCO,screen,10,0)
                                                        pygame.display.update()
                                                        time_passed = clock.tick(30)
                                                        contador=contador+1
                                                    elif contador==4:
                                                        fonte_padrao = pygame.font.get_default_font()
                                                        fonte_jogo = pygame.font.SysFont(fonte_padrao, 25)
                                                        fonte_over = pygame.font.SysFont(fonte_padrao, 180)
                                                        fonte_fim = pygame.font.SysFont(fonte_padrao, 100)
                                                        fonte_esc = pygame.font.SysFont(fonte_padrao, 30)



                                                        lista = []
                                                        listavence = [0,1,0,1,0,1]
                                                        listaperde = [1,0,1,0,1,0]

                                                        pygame.display.set_caption('Urano')
                                                        planeta_filename = 'urano.jpg'
                                                        planeta = pygame.image.load(planeta_filename).convert()
                                                        astro_filename = 'animaok.gif'
                                                        astro = pygame.image.load(astro_filename).convert()
                                                        lab_filename = 'lab.jpg'
                                                        lab = pygame.image.load(lab_filename).convert()
                                                        mesa_filename = 'mesa.jpg'
                                                        mesa = pygame.image.load(mesa_filename).convert()
                                                        prat_filename = 'prat.png'
                                                        prat = pygame.image.load(prat_filename).convert()
                                                        neonio_filename = 'neonio.png'
                                                        neonio = pygame.image.load(neonio_filename).convert_alpha()
                                                        helio_filename = 'helio.png'
                                                        helio = pygame.image.load(helio_filename).convert_alpha()
                                                        oxi_filename = 'oxi.png'
                                                        oxi = pygame.image.load(oxi_filename).convert_alpha()
                                                        metano_filename = 'metano.png'
                                                        metano = pygame.image.load(metano_filename).convert_alpha()
                                                        carbono_filename = 'carbono.png'
                                                        carbono = pygame.image.load(carbono_filename).convert_alpha()
                                                        hidro_filename = 'hidro.png'
                                                        hidro = pygame.image.load(hidro_filename).convert_alpha()
                                                        lixo_filename = 'lixo.png'
                                                        lixo = pygame.image.load(lixo_filename).convert_alpha()
                                                        mistura_filename = 'mistura.jpg'
                                                        mistura = pygame.image.load(mistura_filename).convert_alpha()
                                                        clock = pygame.time.Clock()

                                                        pygame.font.init()

                                                        x = 0
                                                        a=0

                                                        screen.blit(planeta, (0, 0)) #coloca a imagem no display
                                                        screen.blit(astro, (650, 20))
                                                        pygame.display.update()
                                                        time_passed = clock.tick(30)

                                                        lixo = {'surface': pygame.image.load('lixo.png').convert_alpha(),'position': [650, 300],'speed': {'x': 0,'y': 0}}
                                                        mistura = {'surface': pygame.image.load('mistura.jpg').convert_alpha(),'position': [190, 384],'speed': {'x': 0,'y': 0}}
                                                        neonio = {'surface': pygame.image.load('neonio.png').convert_alpha(),'position': [100,0],'speed': {'x': 0,'y': 0}}
                                                        helio = {'surface': pygame.image.load('helio.png').convert_alpha(),'position': [190, -18],'speed': {'x': 0,'y': 0}}
                                                        oxi = {'surface': pygame.image.load('oxi.png').convert_alpha(),'position': [320, 0],'speed': {'x': 0,'y': 0}}
                                                        metano = {'surface': pygame.image.load('metano.png').convert_alpha(),'position': [460, 0],'speed': {'x': 0,'y': 0}}
                                                        carbono = {'surface': pygame.image.load('carbono.png').convert_alpha(),'position': [600, 10],'speed': {'x': 0,'y': 0}}
                                                        hidro = {'surface': pygame.image.load('hidro.png').convert_alpha(),'position': [710, 10],'speed': {'x': 0,'y': 0}}

                                                        neonio['speed'] = {'x': 0,'y': 0}

                                                        655,200
                                                        def get_rect(obj):
                                                            return Rect(obj['position'][0],obj['position'][1],obj['surface'].get_width(),obj['surface'].get_height())

                                                        def neonio_collided():
                                                            neonio_rect = get_rect(neonio)
                                                            if neonio_rect.colliderect(get_rect(mistura)):
                                                                    return True
                                                            return False

                                                        while x == 0:
                                                            som_inicio.stop()
                                                            som_netuno.play()
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    exit()
                                                                screen.blit(planeta, (0, 0)) #coloca a imagem no display
                                                                screen.blit(astro, (650, 20))
                                                                t1 = fonte_jogo.render('Olá Astronauta, você chegou em Urano!',1,(255,255,255))
                                                                t2 = fonte_jogo.render('A atmosfera desse planete tem essa cor devido a mistura',1,(255,255,255))
                                                                t3 = fonte_jogo.render('de três gases principais: HIDROGÊNIO, HÉLIO e METANO!',1,(255,255,255))
                                                                t4 = fonte_jogo.render('Além disso, um ano aqui equivale a 84 anos na Terra!',1,(255,255,255))
                                                                t5 = fonte_jogo.render('Urano também tem 24 luas e 13 anéis!',1,(255,255,255))
                                                                t6 = fonte_jogo.render('Agora você irá para o Laborátório de Química...',1,(255,255,255))
                                                                t7 = fonte_jogo.render('Pressione a Barra de Espaço para continuar.',1,(255,255,255))
                                                                screen.blit(t1, (80,50))
                                                                screen.blit(t2, (80,70))
                                                                screen.blit(t3, (80,90))
                                                                screen.blit(t4, (80,110))
                                                                screen.blit(t5, (80,140))
                                                                screen.blit(t6, (80,160))
                                                                screen.blit(t7, (80,180))
                                                                
                                                                    
                                                                pygame.display.update()
                                                                if event.type==pygame.KEYDOWN:
                                                                    if event.key==pygame.K_SPACE:
                                                                        screen.fill((0,0,0))
                                                                        screen.blit(lab, (0, 0)) #coloca a imagem no display
                                                                        t8 = fonte_jogo.render('Seu objetivo nesse jogo é misturar os gases que',1,(0,0,0))
                                                                        t9 = fonte_jogo.render('formam a atmosfera de Urano!',1,(0,0,0))
                                                                        t10 = fonte_jogo.render('Os gases que você deseja misturar devem ser colocados no pote azul.',1,(0,0,0))
                                                                        t11 = fonte_jogo.render('Os gases que não fazem parte da atmosfera de Urano devem ir para o lixo.',1,(0,0,0))    
                                                                        t12 = fonte_jogo.render('As setas controlam o jogo.',1,(0,0,0))
                                                                        t13 = fonte_jogo.render('Asperte a barra de espaço para continuar',1,(0,0,0))
                                                                        screen.blit(t8, (100,100))
                                                                        screen.blit(t9, (100,120))
                                                                        screen.blit(t10, (100,140))
                                                                        screen.blit(t11, (100,160))
                                                                        screen.blit(t12, (100,180))
                                                                        screen.blit(t13, (100,200))
                                                                        pygame.display.update()
                                                                        pygame.time.delay(1000)
                                                                        time_passed = clock.tick(30)
                                                                        x = 1                  
                                                                                    
                                                        collided = True

                                                        while x==1:
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    som_netuno.stop()
                                                                    p.display.quit()
                                                                    exit()
                                                                
                                                            pressed_keys = pygame.key.get_pressed()
                                                            screen.blit(mesa, (0, 0))
                                                            screen.blit(lixo['surface'], lixo['position'])
                                                            screen.blit(mistura['surface'], mistura['position'])
                                                            screen.blit(helio['surface'], helio['position'])
                                                            screen.blit(oxi['surface'],oxi['position'])
                                                            screen.blit(metano['surface'], metano['position'])
                                                            screen.blit(carbono['surface'], carbono['position'])
                                                            screen.blit(hidro['surface'], hidro['position'])
                                                            neonio['speed'] = {'x': 0,'y': 0}          
                                                            if event.type==pygame.KEYDOWN:                
                                                                if pressed_keys[K_UP]:
                                                                    neonio['speed']['y'] = -5
                                                                elif pressed_keys[K_DOWN]:
                                                                    neonio['speed']['y'] = 5
                                                                if pressed_keys[K_LEFT]:
                                                                    neonio['speed']['x'] = -5
                                                                elif pressed_keys[K_RIGHT]:
                                                                    neonio['speed']['x'] = 5

                                                                screen.blit(mesa, (0, 0))
                                                                screen.blit(lixo['surface'], lixo['position'])
                                                                screen.blit(mistura['surface'], mistura['position'])
                                                                screen.blit(helio['surface'], helio['position'])
                                                                screen.blit(oxi['surface'],oxi['position'])
                                                                screen.blit(metano['surface'], metano['position'])
                                                                screen.blit(carbono['surface'], carbono['position'])
                                                                screen.blit(hidro['surface'], hidro['position'])

                                                                    
                                                                        
                                                                neonio['position'][0] += neonio['speed']['x']
                                                                neonio['position'][1] += neonio['speed']['y']
                                                                screen.blit(neonio['surface'], neonio['position'])
                                                                pygame.display.update()
                                                                time_passed = clock.tick(30)
                                                                
                                                            
                                                            
                                                                

                                                                screen.blit(neonio['surface'], neonio['position'])
                                                                
                                                                if True:
                                                                    neonio_rect = get_rect(neonio)
                                                                    mistura_rect = get_rect(mistura)
                                                                    if neonio_rect.colliderect(mistura_rect):
                                                                        a = 1
                                                                        lista.append(a)
                                                                        neonio['position'][0]=220
                                                                        neonio['position'][1]=237
                                                                        x = 2
                                                                        break
                                                                    lixo_rect = get_rect(lixo)
                                                                    if neonio_rect.colliderect(lixo_rect):
                                                                        a = 0
                                                                        lista.append(a)
                                                                        neonio['position'][0]=655
                                                                        neonio['position'][1]=200
                                                                        x = 2
                                                                        break                

                                                        x = 2

                                                        while x==2:
                                                            screen.fill((0,0,0))
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    som_netuno.stop()
                                                                    p.display.quit()
                                                                    exit()
                                                                    
                                                                
                                                            pressed_keys = pygame.key.get_pressed()
                                                            screen.blit(mesa, (0, 0))
                                                            screen.blit(lixo['surface'], lixo['position'])
                                                            screen.blit(mistura['surface'], mistura['position'])
                                                            screen.blit(oxi['surface'],oxi['position'])
                                                            screen.blit(metano['surface'], metano['position'])
                                                            screen.blit(carbono['surface'], carbono['position'])
                                                            screen.blit(hidro['surface'], hidro['position'])
                                                            helio['speed'] = {'x': 0,'y': 0}          
                                                            if event.type==pygame.KEYDOWN:                
                                                                if pressed_keys[K_UP]:
                                                                    helio['speed']['y'] = -5
                                                                elif pressed_keys[K_DOWN]:
                                                                    helio['speed']['y'] = 5
                                                                if pressed_keys[K_LEFT]:
                                                                    helio['speed']['x'] = -5
                                                                elif pressed_keys[K_RIGHT]:
                                                                    helio['speed']['x'] = 5
                                                                screen.blit(mesa, (0, 0))
                                                                screen.blit(lixo['surface'], lixo['position'])
                                                                screen.blit(mistura['surface'], mistura['position'])
                                                                screen.blit(oxi['surface'],oxi['position'])
                                                                screen.blit(metano['surface'], metano['position'])
                                                                screen.blit(carbono['surface'], carbono['position'])
                                                                screen.blit(hidro['surface'], hidro['position'])

                                                                    
                                                                        
                                                                helio['position'][0] += helio['speed']['x']
                                                                helio['position'][1] += helio['speed']['y']
                                                                screen.blit(helio['surface'], helio['position'])
                                                                pygame.display.update()
                                                                time_passed = clock.tick(30)
                                                                
                                                            
                                                            
                                                                

                                                                screen.blit(helio['surface'], helio['position'])
                                                                
                                                                if True:
                                                                    helio_rect = get_rect(helio)
                                                                    mistura_rect = get_rect(mistura)
                                                                    if helio_rect.colliderect(mistura_rect):
                                                                        a = 1
                                                                        lista.append(a)
                                                                        helio['position'][0]=150
                                                                        helio['position'][1]=220
                                                                        x = 3
                                                                        break
                                                                    lixo_rect = get_rect(lixo)
                                                                    if helio_rect.colliderect(lixo_rect):
                                                                        a = 0
                                                                        lista.append(a)
                                                                        helio['position'][0]=655
                                                                        helio['position'][1]=200
                                                                        x = 3
                                                                        break                

                                                        while x==3:
                                                            screen.fill((0,0,0))
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    som_netuno.stop()
                                                                    p.display.quit()
                                                                    exit()
                                                                
                                                            pressed_keys = pygame.key.get_pressed()
                                                            screen.blit(mesa, (0, 0))
                                                            screen.blit(lixo['surface'], lixo['position'])
                                                            screen.blit(mistura['surface'], mistura['position'])
                                                            screen.blit(metano['surface'], metano['position'])
                                                            screen.blit(carbono['surface'], carbono['position'])
                                                            screen.blit(hidro['surface'], hidro['position'])
                                                            oxi['speed'] = {'x': 0,'y': 0}          
                                                            if event.type==pygame.KEYDOWN:                
                                                                if pressed_keys[K_UP]:
                                                                    oxi['speed']['y'] = -5
                                                                elif pressed_keys[K_DOWN]:
                                                                    oxi['speed']['y'] = 5
                                                                if pressed_keys[K_LEFT]:
                                                                    oxi['speed']['x'] = -5
                                                                elif pressed_keys[K_RIGHT]:
                                                                    oxi['speed']['x'] = 5
                                                                screen.blit(mesa, (0, 0))
                                                                screen.blit(lixo['surface'], lixo['position'])
                                                                screen.blit(mistura['surface'], mistura['position'])
                                                                screen.blit(metano['surface'], metano['position'])
                                                                screen.blit(carbono['surface'], carbono['position'])
                                                                screen.blit(hidro['surface'], hidro['position'])

                                                                    
                                                                        
                                                                oxi['position'][0] += oxi['speed']['x']
                                                                oxi['position'][1] += oxi['speed']['y']
                                                                screen.blit(oxi['surface'], oxi['position'])
                                                                pygame.display.update()
                                                                time_passed = clock.tick(30)
                                                                
                                                            
                                                            
                                                                

                                                                screen.blit(oxi['surface'], oxi['position'])
                                                                
                                                                if True:
                                                                    oxi_rect = get_rect(oxi)
                                                                    mistura_rect = get_rect(mistura)
                                                                    if oxi_rect.colliderect(mistura_rect):
                                                                        a = 1
                                                                        lista.append(a)
                                                                        oxi['position'][0]=150
                                                                        oxi['position'][1]=220
                                                                        x = 4
                                                                        break
                                                                    lixo_rect = get_rect(lixo)
                                                                    if oxi_rect.colliderect(lixo_rect):
                                                                        a = 0
                                                                        lista.append(a)
                                                                        oxi['position'][0]=655
                                                                        oxi['position'][1]=200
                                                                        x = 4
                                                                        break 

                                                        while x==4:
                                                            screen.fill((0,0,0))
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    som_netuno.stop()
                                                                    p.display.quit()
                                                                    exit()
                                                                
                                                            pressed_keys = pygame.key.get_pressed()
                                                            screen.blit(mesa, (0, 0))
                                                            screen.blit(lixo['surface'], lixo['position'])
                                                            screen.blit(mistura['surface'], mistura['position'])
                                                            screen.blit(carbono['surface'], carbono['position'])
                                                            screen.blit(hidro['surface'], hidro['position'])
                                                            metano['speed'] = {'x': 0,'y': 0}          
                                                            if event.type==pygame.KEYDOWN:                
                                                                if pressed_keys[K_UP]:
                                                                    metano['speed']['y'] = -5
                                                                elif pressed_keys[K_DOWN]:
                                                                    metano['speed']['y'] = 5
                                                                if pressed_keys[K_LEFT]:
                                                                    metano['speed']['x'] = -5
                                                                elif pressed_keys[K_RIGHT]:
                                                                    metano['speed']['x'] = 5
                                                                screen.blit(mesa, (0, 0))
                                                                screen.blit(lixo['surface'], lixo['position'])
                                                                screen.blit(mistura['surface'], mistura['position'])
                                                                screen.blit(carbono['surface'], carbono['position'])
                                                                screen.blit(hidro['surface'], hidro['position'])
                                                                        
                                                                metano['position'][0] += metano['speed']['x']
                                                                metano['position'][1] += metano['speed']['y']
                                                                screen.blit(metano['surface'], metano['position'])
                                                                pygame.display.update()
                                                                time_passed = clock.tick(30)
                                                                
                                                            
                                                            
                                                                

                                                                screen.blit(metano['surface'], metano['position'])
                                                                
                                                                if True:
                                                                    metano_rect = get_rect(metano)
                                                                    mistura_rect = get_rect(mistura)
                                                                    if metano_rect.colliderect(mistura_rect):
                                                                        a = 1
                                                                        lista.append(a)
                                                                        metano['position'][0]=150
                                                                        metano['position'][1]=220
                                                                        x = 5
                                                                        break
                                                                    lixo_rect = get_rect(lixo)
                                                                    if metano_rect.colliderect(lixo_rect):
                                                                        a = 0
                                                                        lista.append(a)
                                                                        metano['position'][0]=655
                                                                        metano['position'][1]=200
                                                                        x = 5
                                                                        break

                                                        while x==5:
                                                            screen.fill((0,0,0))
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    som_netuno.stop()
                                                                    p.display.quit()
                                                                    exit()
                                                                
                                                            pressed_keys = pygame.key.get_pressed()
                                                            screen.blit(mesa, (0, 0))
                                                            screen.blit(lixo['surface'], lixo['position'])
                                                            screen.blit(mistura['surface'], mistura['position'])
                                                            screen.blit(hidro['surface'], hidro['position'])
                                                            carbono['speed'] = {'x': 0,'y': 0}          
                                                            if event.type==pygame.KEYDOWN:                
                                                                if pressed_keys[K_UP]:
                                                                    carbono['speed']['y'] = -5
                                                                elif pressed_keys[K_DOWN]:
                                                                    carbono['speed']['y'] = 5
                                                                if pressed_keys[K_LEFT]:
                                                                    carbono['speed']['x'] = -5
                                                                elif pressed_keys[K_RIGHT]:
                                                                    carbono['speed']['x'] = 5
                                                                screen.blit(mesa, (0, 0))
                                                                screen.blit(lixo['surface'], lixo['position'])
                                                                screen.blit(mistura['surface'], mistura['position'])
                                                                screen.blit(hidro['surface'], hidro['position'])
                                                                        
                                                                carbono['position'][0] += carbono['speed']['x']
                                                                carbono['position'][1] += carbono['speed']['y']
                                                                screen.blit(carbono['surface'], carbono['position'])
                                                                pygame.display.update()
                                                                time_passed = clock.tick(30)
                                                                
                                                            
                                                            
                                                                

                                                                screen.blit(carbono['surface'], carbono['position'])
                                                                
                                                                if True:
                                                                    carbono_rect = get_rect(carbono)
                                                                    mistura_rect = get_rect(mistura)
                                                                    if carbono_rect.colliderect(mistura_rect):
                                                                        a = 1
                                                                        lista.append(a)
                                                                        carbono['position'][0]=150
                                                                        carbono['position'][1]=220
                                                                        x = 6
                                                                        break
                                                                    lixo_rect = get_rect(lixo)
                                                                    if carbono_rect.colliderect(lixo_rect):
                                                                        a = 0
                                                                        lista.append(a)
                                                                        carbono['position'][0]=655
                                                                        carbono['position'][1]=200
                                                                        x = 6
                                                                        break

                                                            
                                                        while x==6:
                                                            screen.fill((0,0,0))
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    som_netuno.stop()
                                                                    p.display.quit()
                                                                    exit()
                                                                
                                                            pressed_keys = pygame.key.get_pressed()
                                                            screen.blit(mesa, (0, 0))
                                                            screen.blit(lixo['surface'], lixo['position'])
                                                            screen.blit(mistura['surface'], mistura['position'])
                                                            
                                                            hidro['speed'] = {'x': 0,'y': 0}          
                                                            if event.type==pygame.KEYDOWN:                
                                                                if pressed_keys[K_UP]:
                                                                    hidro['speed']['y'] = -5
                                                                elif pressed_keys[K_DOWN]:
                                                                    hidro['speed']['y'] = 5
                                                                if pressed_keys[K_LEFT]:
                                                                    hidro['speed']['x'] = -5
                                                                elif pressed_keys[K_RIGHT]:
                                                                    hidro['speed']['x'] = 5
                                                                screen.blit(mesa, (0, 0))
                                                                screen.blit(lixo['surface'], lixo['position'])
                                                                screen.blit(mistura['surface'], mistura['position'])

                                                                
                                                                        
                                                                hidro['position'][0] += hidro['speed']['x']
                                                                hidro['position'][1] += hidro['speed']['y']
                                                                screen.blit(hidro['surface'], hidro['position'])
                                                                pygame.display.update()
                                                                time_passed = clock.tick(30)
                                                                
                                                            
                                                            
                                                                

                                                                screen.blit(hidro['surface'], hidro['position'])
                                                                
                                                                if True:
                                                                    hidro_rect = get_rect(hidro)
                                                                    mistura_rect = get_rect(mistura)
                                                                    if hidro_rect.colliderect(mistura_rect):
                                                                        a = 1
                                                                        lista.append(a)
                                                                        hidro['position'][0]=150
                                                                        hidro['position'][1]=220
                                                                        x = 7
                                                                        break
                                                                    lixo_rect = get_rect(lixo)
                                                                    if hidro_rect.colliderect(lixo_rect):
                                                                        a = 0
                                                                        lista.append(a)
                                                                        hidro['position'][0]=150
                                                                        hidro['position'][1]=200
                                                                        x = 7
                                                                        break

                                                        while x==7:
                                                            screen.fill((0,0,0))
                                                            events = pygame.event.get()
                                                            for event in events:
                                                                if event.type == pygame.QUIT:
                                                                    som_netuno.stop()
                                                                    p.display.quit()
                                                                    exit()
                                                                
                                                            pressed_keys = pygame.key.get_pressed()
                                                            screen.blit(mesa, (0, 0))
                                                            screen.blit(lixo['surface'], lixo['position'])
                                                            screen.blit(mistura['surface'], mistura['position'])
                                                            pygame.display.update()
                                                            time_passed = clock.tick(30)
                                                            
                                                            if lista==listavence:
                                                               
                                                                t1 = fonte_fim.render("Parábens, você venceu!",1,(255,0,0))
                                                               
                                                                screen.blit(t1,(70,240))
                                                                
                                                                pygame.display.update()
                                                                pygame.time.wait(2000)
                                                                time_passed = clock.tick(30)
                                                                x=0
                                                                screen.blit((background),(0, 0))

                                                                screen.blit(ImagemNave,ultima_posicao)


                                                                screen.blit((texto_aviso),(700,400))

                                                                pygame.display.update()


                                                                contador=0

                                                                clock = pygame.time.Clock()
                                                                while True:
                                                                    som_netuno.stop()
                                                                    som_inicio.play(3)
                                                                    for event in pygame.event.get():
                                                                        if event.type == QUIT:
                                                                             som_inicio.stop()
                                                                             p.display.quit()
                                                                             exit()
                                                                        tecla=pygame.key.get_pressed()
                                                                        if event.type==KEYDOWN:
                                                                            if tecla[K_RETURN]:
                                                                               
                                                                                if contador<3:
                                                                                    te=[textosposurano[contador]]
                                                                                    novos_textos=texto1(te,0,500)
                                                                                    novos_textos.novo_blit1(fonte,BRANCO,screen,20,contador)
                                                                                    pygame.display.update()
                                                                                    time_passed = clock.tick(30)
                                                                                    contador=contador+1
                                                                                elif contador==3:
                                                                                    som_foguete.play(1)
                                                                                    pygame.time.wait(1000)
                                                                                    screen.fill(PRETO)
                                                                                    numero=range(15)
                                                                                    repeticao=[]
                                                                                    
                                                                                    for a in numero:
                                                                                        repeticao.append((716-2*a,77+5*a))
                                                                                    for i in repeticao:
                                                                                        screen.blit((background),(0, 0))
                                                                                        screen.blit((texto_aviso),(700,400))

                                                                                        screen.blit(ImagemNave,(i))
                                                                                        pygame.display.update()
                                                                                        ultima_posicao=i
                                                                                        time_passed = clock.tick(30)
                                                                                    som_foguete.stop()     
                                                                                    print(i)
                                                                                    textos=["Vamos para Saturno!"]
                                                                                    novos_textos=texto1(textos,0,500)
                                                                                    novos_textos.novo_blit1(fonte,BRANCO,screen,10,0)
                                                                                    pygame.display.update()
                                                                                    time_passed = clock.tick(30)
                                                                                    contador=contador+1
                                                                                elif contador==4:
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
                                                                                        curiosidade_1 = ["Saturno possui 62 SATÉLITES NATURAIS!", "Imagine a Terra com 62 Luas!!!", "Pois é, bem vindo(a) à realidade de Saturno!"]
                                                                                        pergunta_2 = ["Segunda pergunta:", "Quanto é                    ?", "", "", "Digite 1 para 28,5", "Digite 2 para 29,5", "Digite 3 para 19,5", "Ou digite 4 para 30,5"]
                                                                                        curiosidade_2 = ["1 ano de Saturno...", "...equivale a 29,5 anos terrestres!", "Imagine demorar 29,5 anos terrestres...", "...para completar um ano de vida!", "Animal!!!"]
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
                                                                                                            background_filename = 'fundo2.png'
                                                                                                            background = pygame.image.load(background_filename).convert()


                                                                                                            som_netuno.stop()
                                   
                                                                                                            screen.blit((background),(0, 0))

                                                                                                            screen.blit(ImagemNave,ultima_posicao)


                                                                                                            screen.blit((texto_aviso),(700,400))

                                                                                                            pygame.display.update()


                                                                                                            contador=0

                                                                                                            clock = pygame.time.Clock()
                                                                                                            while True:
                                                                                                                som_inicio.play(3)
                                                                                                                for event in pygame.event.get():
                                                                                                                    if event.type == QUIT:
                                                                                                                         som_inicio.stop()
                                                                                                                         p.display.quit()
                                                                                                                         exit()
                                                                                                                    tecla=pygame.key.get_pressed()
                                                                                                                    if event.type==KEYDOWN:
                                                                                                                        if tecla[K_RETURN]:
                                                                                                                           
                                                                                                                            if contador<3:
                                                                                                                                te=[textospossaturno[contador]]
                                                                                                                                novos_textos=texto1(te,0,500)
                                                                                                                                novos_textos.novo_blit1(fonte,BRANCO,screen,20,contador)
                                                                                                                                pygame.display.update()
                                                                                                                                time_passed = clock.tick(30)
                                                                                                                                contador=contador+1
                                                                                                                            elif contador==3:
                                                                                                                                som_foguete.play(1)
                                                                                                                                pygame.time.wait(1000)
                                                                                                                                screen.fill(PRETO)
                                                                                                                                numero=range(15)
                                                                                                                                repeticao=[]
                                                                                                                                
                                                                                                                                for a in numero:
                                                                                                                                    repeticao.append((688+1*a,147+2*a))
                                                                                                                                for i in repeticao:
                                                                                                                                    screen.blit((background),(0, 0))
                                                                                                                                    screen.blit((texto_aviso),(700,400))

                                                                                                                                    screen.blit(ImagemNave,i)
                                                                                                                                    pygame.display.update()
                                                                                                                                    ultima_posicao=i
                                                                                                                                    time_passed = clock.tick(30)
                                                                                                                                som_foguete.stop()     
                                                                                                                                print(i)
                                                                                                                                textos=["Vamos para Júpiter!"]
                                                                                                                                novos_textos=texto1(textos,0,500)
                                                                                                                                novos_textos.novo_blit1(fonte,BRANCO,screen,10,0)
                                                                                                                                pygame.display.update()
                                                                                                                                time_passed = clock.tick(30)
                                                                                                                                contador=contador+1
                                                                                                                            elif contador==4:
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
                                                                                                                                    instructions = ["INSTRUÇÕES:", "A sua missão é atravessar a minha superfície!", "MAS NÃO ENCOSTE NAS BORDAS SUPERIOR OU INFERIOR DA TELA!", "Utilize                   para conseguir voltar para a sua nave!", "E                                                         para se manter flutuando!", "Está preparado(a)? Se sim, pressione ENTER para avançar e boa sorte!"]
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
                                                                                                                                            p.time.delay(3000)
                                                                                                                                            p.display.quit()

                                                                                                                                        if jogo==3:
                                                                                                                                            screen.fill(BLACK)
                                                                                                                                            screen.blit(segunda_tela, (0,0))
                                                                                                                                            screen.blit(astronauta, rect_astronauta)
                                                                                                                                            entrada = texto(ganhou,50, 230)
                                                                                                                                            entrada.novo_blit(fonte_jogo, WHITE, screen, 40)
                                                                                                                                            p.display.update()
                                                                                                                                            time_passed = clock.tick(30)
                                                                                                                                            som_netuno.stop()
                                                                                                                                           
                                                                                                                                            screen.blit((background),(0, 0))

                                                                                                                                            screen.blit(ImagemNave,ultima_posicao)


                                                                                                                                            screen.blit((texto_aviso),(700,400))

                                                                                                                                            pygame.display.update()


                                                                                                                                            contador=0

                                                                                                                                            clock = pygame.time.Clock()
                                                                                                                                                                  
                                                                                                                                                                                                   
                                                                                                                                                                                
                                        

                                                                                                            
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


                                                                                        
                                                                                        
                                                                                                    

                                                            else:
                                                                t1 = fonte.render("GAME OVER!",1,(255,0,0))
                                                                
                                                                screen.blit(t1,(70,250))
                                                               
                                                                pygame.display.update()

                                                                screen.blit((background),(0, 0))

                                                                screen.blit(ImagemNave,ultima_posicao)


                                                                screen.blit((texto_aviso),(700,400))

                                                                pygame.display.update()


                                                                contador=0

                                                                clock = pygame.time.Clock()
                                                                while True:
                                                                    som_netuno.stop()
                                                                    som_inicio.play(3)
                                                                    for event in pygame.event.get():
                                                                        if event.type == QUIT:
                                                                             som_inicio.stop()
                                                                             p.display.quit()
                                                                             exit()
                                                                        tecla=pygame.key.get_pressed()
                                                                        if event.type==KEYDOWN:
                                                                            if tecla[K_RETURN]:
                                                                               
                                                                                if contador<3:
                                                                                    te=[textosposurano[contador]]
                                                                                    novos_textos=texto1(te,0,500)
                                                                                    novos_textos.novo_blit1(fonte,BRANCO,screen,20,contador)
                                                                                    pygame.display.update()
                                                                                    time_passed = clock.tick(30)
                                                                                    contador=contador+1
                                                                                elif contador==3:
                                                                                    som_foguete.play(1)
                                                                                    pygame.time.wait(1000)
                                                                                    screen.fill(PRETO)
                                                                                    numero=range(15)
                                                                                    repeticao=[]
                                                                                    
                                                                                    for a in numero:
                                                                                        repeticao.append((716-8*a,77,2+5*a))
                                                                                    for i in repeticao:
                                                                                        screen.blit((background),(0, 0))
                                                                                        screen.blit((texto_aviso),(700,400))

                                                                                        screen.blit(ImagemNave,i)
                                                                                        pygame.display.update()
                                                                                        ultima_posicao=i
                                                                                        time_passed = clock.tick(30)
                                                                                    som_foguete.stop()     
                                                                                    print(i)
                                                                                    textos=["Vamos para Saturno!"]
                                                                                    novos_textos=texto1(textos,0,500)
                                                                                    novos_textos.novo_blit1(fonte,BRANCO,screen,10,0)
                                                                                    pygame.display.update()
                                                                                    time_passed = clock.tick(30)
                                                                                    contador=contador+1
                                                                                elif contador==4:
                                                                                    p.display.set_caption('Saturno')
                                                                                    astronauta = p.image.load('animaok.gif').convert()
                                                                                    astronauta_position = [680, 20]



                                                                                    background = p.image.load('saturn.jpg').convert()
                                                                                    fundo_estrelado = p.image.load('fundo_estrelado.jpg').convert()


                                                                                    clock = p.time.Clock()

                                                                                    p.font.init()

                                                                                    fonte_padrao = p.font.get_default_font()
                                                                                    fonte_jogo = p.font.SysFont(fonte_padrao, 30)

                                                                                    fonte_perdeu = p.font.SysFont(fonte_padrao, 100)
                                                                                    fonte_curiosidades = p.font.SysFont(fonte_padrao, 45)
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
                                                                                        tela_1 = ["Olá, astronauta! Seja bem vindo...", "...ao segundo maior planeta do Sistema Solar!", "Para conseguir passar por mim,", "você terá de provar ser muito bom ou boa em Matemática!", "E olha que não é fácil não, hein?", "Está preparado para começar?", "Se sim, pressione ENTER para avançar!"] 
                                                                                        pergunta_1 = ["Pois bem, vamos começar:", "Diga-me, quanto é 15 x 4 + 2?", "Poooxa, é fácil, vamos lá, eu acredito em você!", "Digite 1 para 50", "Digite 2 para 47", "Digite 3 para 90", "Ou 4 para 62"]
                                                                                        titulo = ["CURIOSIDADES"]
                                                                                        curiosidade_1 = ["Saturno possui 62 SATÉLITES NATURAIS!", "Imagine a Terra com 62 Luas!", "Pois é, bem vindo(a) à realidade de Saturno!"]
                                                                                        pergunta_2 = ["Segunda pergunta:", "Quanto é 39 - 9,5?", "Digite 1 para 28,5", "Digite 2 para 29,5", "Digite 3 para 19,5", "Ou digite 4 para 30,5"]
                                                                                        curiosidade_2 = ["1 ano de Saturno equivale a 29,5 anos terrestres!", "Imagine demorar 29,5 anos terrestres,", "para completar um ano de vida!", "Animal!!!"]
                                                                                        pergunta_3 = ["Responda na sequência:", "1000 / 100?    8 x 4?      70/2?", "Digite 1 para 10, 32 e 35, nesta ordem!", "Digite 2 para 32, 10 e 35, nesta ordem!", "Digite 3 para 100, 42 e 45, nesta ordem!", "Ou digite 4 para 10, 42 e 35, nesta ordem!"]
                                                                                        curiosidade_3 = ["O dia de Saturno não possui 24 horas como o nosso!", "Possui apenas 10 horas, 32 minutos e 35 segundos!", "O dia de Saturno termina antes que"," o nosso chegue à metade!"]
                                                                                        acertou = ["Certa resposta!"]
                                                                                        errou = ["Resposta incorreta!"]
                                                                                        ganhou = ["Opa, é isso aí amiguinho(a)!", "Missão cumprida com sucesso!", "Já pode prosseguir viagem!", "Até mais!"]
                                                                                        perdeu = ["GAME OVER!"]
                                                                                       
                                                                                       #inserindo textos no display
                                                                                        apresentacao = texto(tela_1,95, 20)
                                                                                        first_question = texto(pergunta_1,95, 20)
                                                                                        second_question = texto(pergunta_2,95, 20)
                                                                                        third_question = texto(pergunta_3,95, 20)
                                                                                        curio_title = texto(titulo,95, 20)
                                                                                        curio_1 = texto(curiosidade_1,95, 150)
                                                                                        curio_2 = texto(curiosidade_2,95, 200)
                                                                                        curio_3 = texto(curiosidade_3,95, 150)
                                                                                        certo = texto(acertou,95, 20)
                                                                                        errado = texto(errou,95, 20)
                                                                                        ganha = texto(ganhou,95, 20)
                                                                                        perde = texto(perdeu,95, 20)


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
                                                                                                            screen.blit(astronauta, astronauta_position)
                                                                                                            first_question.novo_blit(fonte_jogo, WHITE, screen, 40)
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
                                                                                                            jogo=3
                                                                                                
                                                                                                if jogo==1:
                                                                                                    if event.type == p.KEYDOWN:
                                                                                                        if event.key == p.K_ESCAPE:
                                                                                                            p.display.quit()
                                                                                                        if event.key == p.K_RETURN:
                                                                                                            screen.fill(BLACK)
                                                                                                            screen.blit(background, (0,0))
                                                                                                            screen.blit(astronauta, astronauta_position)
                                                                                                            second_question.novo_blit(fonte_jogo, WHITE, screen, 40)
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
                                                                                                            third_question.novo_blit(fonte_jogo, WHITE, screen, 40)
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
                                                                                                    certo.novo_blit(fonte_jogo, WHITE, screen, 40)
                                                                                                    p.display.update()
                                                                                                    time_passed = clock.tick(30)
                                                                                                    if pergunta==1:
                                                                                                        screen.blit(fundo_estrelado, (0, 0))
                                                                                                        curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                                                                                                        curio_1.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                                                                                                        jogo=1
                                                                                                    elif pergunta==2:
                                                                                                        curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                                                                                                        curio_2.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                                                                                                        jogo=2
                                                                                                    elif pergunta==3:
                                                                                                        curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                                                                                                        curio_3.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                                                                                                        p.time.delay(3000)
                                                                                                        if respostas_certas==3:
                                                                                                            screen.fill(BLACK)
                                                                                                            screen.blit(background, (0,0))
                                                                                                            screen.blit(astronauta, astronauta_position)
                                                                                                            ganha.novo_blit(fonte_jogo, WHITE, screen, 40)
                                                                                                            p.time.delay(5000)
                                                                                                            som_netuno.stop()
                                                                                                           
                                                                                                            screen.blit((background),(0, 0))

                                                                                                            screen.blit(ImagemNave,ultima_posicao)


                                                                                                            screen.blit((texto_aviso),(700,400))

                                                                                                            pygame.display.update()


                                                                                                            contador=0

                                                                                                            clock = pygame.time.Clock()
                                                                                                                                        
                                                                                                            while True:
                                                                                                                som_inicio.play(3)
                                                                                                                for event in pygame.event.get():
                                                                                                                    if event.type == QUIT:
                                                                                                                         som_inicio.stop()
                                                                                                                         p.display.quit()
                                                                                                                         exit()
                                                                                                                    tecla=pygame.key.get_pressed()
                                                                                                                    if event.type==KEYDOWN:
                                                                                                                        if tecla[K_RETURN]:
                                                                                                                           
                                                                                                                            if contador<3:
                                                                                                                                te=[textospossaturno[contador]]
                                                                                                                                novos_textos=texto1(te,0,500)
                                                                                                                                novos_textos.novo_blit1(fonte,BRANCO,screen,20,contador)
                                                                                                                                pygame.display.update()
                                                                                                                                time_passed = clock.tick(30)
                                                                                                                                contador=contador+1
                                                                                                                            elif contador==3:
                                                                                                                                som_foguete.play(1)
                                                                                                                                pygame.time.wait(1000)
                                                                                                                                screen.fill(PRETO)
                                                                                                                                numero=range(15)
                                                                                                                                repeticao=[]
                                                                                                                                
                                                                                                                                for a in numero:
                                                                                                                                    repeticao.append((828-8*a,10+5*a-0.2*a))
                                                                                                                                for i in repeticao:
                                                                                                                                    screen.blit((background),(0, 0))
                                                                                                                                    screen.blit((texto_aviso),(700,400))

                                                                                                                                    screen.blit(ImagemNave,i)
                                                                                                                                    pygame.display.update()
                                                                                                                                    ultima_posicao=i
                                                                                                                                    time_passed = clock.tick(30)
                                                                                                                                som_foguete.stop()     
                                                                                                                                print(i)
                                                                                                                                textos=["Vamos para Júpiter!"]
                                                                                                                                novos_textos=texto1(textos,0,500)
                                                                                                                                novos_textos.novo_blit1(fonte,BRANCO,screen,10,0)
                                                                                                                                pygame.display.update()
                                                                                                                                time_passed = clock.tick(30)
                                                                                                                                contador=contador+1
                                                                                                                    
                                                                                                        else:
                                                                                                            screen.fill(BLACK)
                                                                                                            screen.blit(background, (0,0))
                                                                                                            screen.blit(astronauta, astronauta_position)
                                                                                                            perde.novo_blit(fonte_jogo, WHITE, screen, 40)
                                                                                                            jogo=0
                                                                                                        

                                                                                                                    
                                                                                                    if jogo==4:   
                                                                                                        screen.fill(BLACK)
                                                                                                        screen.blit(background, (0,0))
                                                                                                        screen.blit(astronauta, astronauta_position)
                                                                                                        errado.novo_blit(fonte_jogo, WHITE, screen, 40)
                                                                                                        p.display.update()
                                                                                                        time_passed = clock.tick(30)
                                                                                                        if pergunta==1:
                                                                                                            curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                                                                                                            curio_1.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                                                                                                            jogo=1
                                                                                                        elif pergunta==2:
                                                                                                            curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                                                                                                            curio_2.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                                                                                                            jogo=2
                                                                                                        elif pergunta==3:
                                                                                                            curio_title.novo_blit(fonte_perdeu, WHITE, screen, 50)
                                                                                                            curio_3.novo_blit(fonte_curiosidades, WHITE, screen, 60)
                                                                                                            p.time.delay(3000)
                                                                                                            screen.fill(BLACK)
                                                                                                            screen.blit(background, (0,0))
                                                                                                            screen.blit(astronauta, astronauta_position)
                                                                                                            perde.novo_blit(fonte_jogo, WHITE, screen, 40)
                                                                                                            jogo=ArithmeticError


                                                            
                                                                
                                                            
                                                                
                                                               
                                              
                                
                                
                                

                            move_diamantes()    
                            move_nuvens()
                            tempo = range(60)
                            for diamante in diamantes:
                                screen.blit(diamante['surface'], diamante['position'])

                            for nuvem in nuvens:
                                screen.blit(nuvem['surface'], nuvem['position'])

                            

                            pygame.display.update()
                            time_passed = clock.tick(30)

                            remove_used_diamantes()




                                    

                                            

                                           
                                                               
                                                   
                                                                                            
                                                                        
                                                                    
                                                                     
                                                                     

