import pygame
from pygame.locals import *
from sys import exit
from classe_texto import texto

 
pygame.init()

PRETO= (0,0,0)
BRANCO= (255,255,255)
VERDE= (0,255,0)
VERMELHO= (255,0,0)
AZUL=(0,0,255)

t1=["Olá astronauta!","Você deve levar um drone até o alto do monte olimpo!","Ele é um vulcã inativo de Marte,","maoir que o Everest","Seu drone esta funcionando mas seu controle remoto esta quebrado","para controla-lo será necessário apertar as setas de acordo"," com a sequência que será mostrada","Boa sorte viajante!"]




fonte = pygame.font.Font(None, 30)
fonte2 = pygame.font.Font(None, 80)

screen=pygame.display.set_mode((1019, 600), 0, 32)
pygame.display.set_caption('Space Trek')
background_filename = 'vulcao.jpg'
background = pygame.image.load(background_filename).convert()
ship_filename = 'drone3.png'
ship = pygame.image.load(ship_filename).convert_alpha()
ship_filenamedois = 'dronedois.png'
shipdois = pygame.image.load(ship_filenamedois).convert_alpha()
setas_nome='setas.png'
setas = pygame.image.load(setas_nome).convert_alpha()
grade_nome='grade.png'
grade= pygame.image.load(grade_nome).convert_alpha()
clock=pygame.time.Clock()
vitoria=fonte2.render("Parabéns você venceu!",1000,PRETO)
perda=fonte2.render("Você errou,vamos começar denovo!",1000,PRETO)
fundo2=pygame.image.load("marte.jpg").convert()
o=True
vit=0
nave=(100,390)
screen.blit(shipdois,(0,0))
screen.blit(fundo2,(200,100))
entrada_2 = texto(t1, 95, 50)
entrada_2.novo_blit(fonte, BRANCO, screen, 60)
pygame.display.update()
pygame.time.wait(4000)


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(ship,nave)
    screen.blit(setas, (0, 0))
    pygame.display.update()
    time_passed=clock.tick(30)
    screen.fill(PRETO)
    numero=range(2000)
    repeticao=[]
    lista=[]
    certo=[1]
    if vit==1:
        screen.blit(background,(0,0))
        screen.blit(ship, nave )
        screen.blit(setas, (0, 0))
        screen.blit(vitoria,(5,300))
        pygame.display.update()
        time_passed = clock.tick(60)
        screen.blit((background),(0, 0))
        screen.blit(ImagemNave,ultima_posicao)
        screen.blit((texto_aviso),(400,400))
        pygame.display.update()
        contador=0
        clock = pygame.time.Clock()
    if vit==2:
        screen.blit(background,(0,0))
        screen.blit(ship, nave)
        screen.blit(setas, (0, 0))
        
        screen.blit(perda,(5,300))
        pygame.display.update()
        time_passed = clock.tick(60)
        pygame.time.wait(5000)
        o=True
      
                                                
                                


        
    seta=0
    tempo=0
        
    while o==True:
        direita=K_RIGHT
        esquerda=K_LEFT
        cima=K_UP
        baixo=K_DOWN
        sequencia=[baixo,esquerda,cima,direita,cima,cima,direita,esquerda,direita,cima,baixo,direita,direita,cima,direita,cima,esquerda,direita,cima,esquerda,cima,cima,baixo,baixo,direita,direita,esquerda,baixo,esquerda,cima,direita,cima]
        lista=[]
        lista2=[]
        l=390
        k=100
        listanave=[]
        for a in numero:
            repeticao.append((500-4*a,0*a))
        for y in list(range(40)):
                listanave.append((140+10*y,290+2*y))
        
        for i in repeticao:
            screen.fill(PRETO)
            screen.blit(background,(0,0))
        
            screen.blit(setas, (i))
            screen.blit(ship,nave)
            pygame.display.update()
            time_passed = clock.tick(60)
            j=1
            for event in pygame.event.get():
                if j==1:
                    if event.type==KEYDOWN:
                        while seta<=32:
                            if nave in listanave:
                                if event.key==sequencia[seta] :
                                
                                    lista.append(sequencia[seta])
                                    screen.fill(PRETO)
                                    screen.blit(background,(0,0))
                                 
                                    screen.blit(setas, (i))
                                    nave=(k+10,l+2)
                                    screen.blit(ship,nave)
                                    print(nave)
                                    j=0
                                    k=k+10
                                    l=l+2
                                    seta=seta+1
                                    pygame.display.update()
                                    time_passed = clock.tick(60)
                                    
                                       
                                elif j==1 :
                                    lista.append(0)
                                    screen.fill(PRETO)
                                    screen.blit(background,(0,0))
                                    print(nave)
                                  
                                    screen.blit(setas, (i))
                                    screen.blit(ship, nave)
                                    nave=(k-2, l-2)
                                    k=k-2
                                    l=l-2
                                    
                                    j=0
                                    seta=seta+1
                                    pygame.display.update()
                                    time_passed = clock.tick(60)
                                    seta=10000
                                
                            else:    
                                if event.key==sequencia[seta]:
                                    lista.append(sequencia[seta])
                                    screen.fill(PRETO)
                                    screen.blit(background,(0,0))
                                   
                                    screen.blit(setas, (i))
                                    nave=(k+2,l-5)
                                    screen.blit(ship,nave)
                                    j=0
                                    k=k+2
                                    l=l-5
                                    seta=seta+1
                                    pygame.display.update()
                                    time_passed = clock.tick(60)
                                    print(nave)

                                       
                                elif j==1 :
                                    screen.fill(PRETO)
                                    screen.blit(background,(0,0))
                                    screen.blit(setas, (i))
                                    screen.blit(ship, nave)
                                    print(nave)
                                    nave=(k-50, l)
                                    k=k-50
                                    j=0
                                    seta=seta+1
                                    pygame.display.update()
                                    time_passed = clock.tick(60)
                                    seta=10000
                            break       
                      
                            
            if lista==sequencia:
                vit=1
                o=False
                
            if seta==10000:
                vit=2
                o=False
                break    
                    
                    
                
            
            
     
    
    


