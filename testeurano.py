import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

fonte_padrao = pygame.font.get_default_font()
fonte_jogo = pygame.font.SysFont(fonte_padrao, 25)
fonte_over = pygame.font.SysFont(fonte_padrao, 180)
fonte_fim = pygame.font.SysFont(fonte_padrao, 100)
fonte_esc = pygame.font.SysFont(fonte_padrao, 30)

screen = pygame.display.set_mode((925, 800), 0, 32)

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
                t13 = fonte_jogo.render('Aperte a barra de espaço para continuar',1,(0,0,0))
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
            exit()
        
    pressed_keys = pygame.key.get_pressed()
    screen.blit(mesa, (0, 0))
    screen.blit(lixo['surface'], lixo['position'])
    screen.blit(mistura['surface'], mistura['position'])
    pygame.display.update()
    time_passed = clock.tick(30)
    
    if lista==listavence:
        print
        t1 = fonte_fim.render("Parábens, você venceu!",1,(255,0,0))
    else:
        t1 = fonte_over.render("GAME OVER!",1,(255,0,0))
    screen.blit(t1,(70,240))
    pygame.display.update()
    time_passed = clock.tick(30)
    pygame.time.delay(5000)
    import jogo_integrado.py



