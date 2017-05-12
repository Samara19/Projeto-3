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



screen = pygame.display.set_mode((805, 700), 0, 32)

background_filename = 'fundo1.jpg'
background = pygame.image.load(background_filename).convert()
caixa_texto=pygame.draw.rect(screen,BRANCO,[0,200,600,500])
fonte = pygame.font.Font(None, 22)
texto1 = fonte.render("Olá viajante!", 1, PRETO)
texto2=fonte.render("Precisamos que você nos traga informações importantes sobre o espaço,",1,PRETO)
texto3=fonte.render("passe por cada um dos planetas complete os desafios para coletar informações!",1,PRETO)
texto4=fonte.render("Contamos com você!",1,PRETO)
texto_aviso=fonte.render("Aperte enter para continuar",1,BRANCO)
screen.blit((texto1),(0,400))
screen.blit((texto2),(0,605))
screen.blit((texto3),(0,620))
screen.blit((texto4),(0,635))
screen.blit((texto_aviso),(600,600))






pygame.display.set_caption('Space Trek')
pygame.display.flip()

contador=0

clock = pygame.time.Clock()
while True:
    screen.blit((background),(0, 0))
    pygame.display.update()
    time_passed = clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        tecla=pygame.key.get_pressed()
        if event.type==KEYDOWN:
            if tecla[K_BACKSPACE]:
                if contador==0:
                    print("oi")
                    contador=+1
                    textos=["Vamos primeiramente para Plutão!"]
                    novos_textos=texto(textos,0,640)
                    novos_textos.novo_blit(fonte,PRETO,screen)
                    screen.blit((background,caixa_texto,bolinha_continuar),(0, 0))
                    pygame.display.update()
                    time_passed = clock.tick(30)
                
            
                
                
         
       

