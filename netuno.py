import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

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

clock = pygame.time.Clock()

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


while True:

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
            screen.blit(t5,(90,250))
            pygame.display.update()
            time_passed = clock.tick(30)
            break

        if contador >= 5:
            screen.fill((0,0,0))
            screen.blit(planeta,(0,0))
            t6 = fonte_fim.render("Parábens, você venceu!",1,(255,255,255))
            t7 = fonte_esc.render("Pressione esc para sair.",1,(255,255,255))
            pressed_keys = pygame.key.get_pressed()
            events = pygame.event.get()
            screen.blit(t6,(70,250))
            screen.blit(t7,(320,350))
            pygame.display.update()
            time_passed = clock.tick(30)
            print('antes')

            while True:
                for event in pygame.event.get():
                    print(event)
                    if event.type == QUIT:
                        print("quit")
                        pygame.display.quit() 
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            print("esc")
                            
                
            break
        
        
        

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
