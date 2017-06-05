class texto:
    def __init__(self,textos,dimensoes1,dimensoes2):
        self.textos=textos
        self.dimensoes1=dimensoes1
        self.dimensoes2=dimensoes2
    def novo_blit(self,fonte,cor,screen,espaço):
        cont=0
        for texto in self.textos:
            import pygame
            cont=cont+espaço
            t=fonte.render(texto,1,cor)
            screen.blit((t),(self.dimensoes1,self.dimensoes2+cont))
            pygame.display.update()