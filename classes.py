import pygame
from pygame.locals import* 
from sys import exit
from os import system
from classe import texto

pygame.init()

WHITE = (255, 255, 255)

class Button:
	def __init__(self, tela, cor, posicao_x, posicao_y, largura, altura, nome_botao, fonte, cor_fonte):
		self.screen = tela
		self.cor = cor
		self.x = posicao_x
		self.y = posicao_y
		self.largura = largura
		self.altura = altura
		self.label = nome_botao
		self.fonte = fonte
		self.cor_fonte = cor_fonte
		#self.nova_tela = nova_tela


	def desenha_tela(self):
		pygame.draw.rect(self.screen, self.cor, (self.x, self.y, self.largura, self.altura))
		label = texto(self.label, self.x+8, self.y-20)
		label.novo_blit(self.fonte, self.cor_fonte, self.screen, 30)

	def play(self):
		p = pygame
		position = p.mouse.get_pos()
		if self.x+self.largura>position[0]>self.x and self.y+self.altura>position[1]>self.y:
			if self.x==800:
				import netuno.py
			if self.x==730:
				import testeurano.py
			if self.x==590:
				import saturno.py
			if self.x==470:
				import jupiter.py
			if self.x==360:
				import Marte.py
			if self.x==220:
				import venus.py
			if self.x==115:
				import mercurio.py


	"""def clique_botao(self):
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN:
				position=pygame.mouse.get_pos()
				print(position)
				if self.x+self.largura>position[0]>self.x and self.y+self.altura>position[1]>self.y:
					self.screen.fill((0,0,0))
					self.screen.blit(self.nova_tela, (0,0))"""




class Nova_tela:
	def __init__(self, tela, cor, fundo):
		self.screen = tela
		self.cor = cor
		self.imagem = imagem

	def limpa_tela(self):
		screen.fill(cor)
		screen.blit(fundo)

