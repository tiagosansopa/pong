#Pong de 4
#Redes Proyecto 1
import pygame,sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox


screen = pygame.display.set_mode((1024,568))
clock = pygame.time.Clock()
Tk().wm_withdraw()

class Meteoro(pygame.sprite.Sprite):

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.image =  pygame.image.load(image)
		w,h = self.image.get_size()
		scale = 0.25
		self.image = pygame.transform.scale(self.image, (int(w*scale), int(h*scale)))
		self.rect = self.image.get_rect()
		self.mx = 0
		self.my = 0
		self.direction = "se"
		
	def update(self,deltat):
		if self.direction == "se":
			self.mx += 10
			self.my +=10
			if self.mx >=1024:
				self.direction = "so"
			elif self.my>=568:
				self.direction = "ne"
				
		elif self.direction == "ne" :
			self.mx+=10
			self.my-=10
			if self.mx>=1024:
				self.direction = "no"
			elif self.my<=0:
				self.direction = "se"
		elif self.direction == "no":
			self.mx -=10
			self.my -=10
			if self.mx<=0:
				self.direction = "ne"
			elif self.my<=0:
				self.direction = "so"
		elif self.direction == "so":
			self.mx -=10
			self.my +=10
			if self.mx<=0:
				self.direction = "se"
			elif self.my>=568:
				self.direction = "no"
		
		self.rect = self.image.get_rect()
		self.rect.center = (self.mx, self.my)
		

class Jugador(pygame.sprite.Sprite):

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.image =  pygame.image.load(image)
		w,h = self.image.get_size()
		scale = 0.10
		self.image = pygame.transform.scale(self.image, (int(w*scale), int(h*scale)))
		self.rect = self.image.get_rect()
		self.mx = 0
		self.my = 530
		
	def update(self,deltat):
		self.rect = self.image.get_rect()
		self.rect.center = (self.mx, self.my)

rect = screen.get_rect()
meteoro = Meteoro('meteor.png',(0,0))
player1 = Jugador('plat.png',(0,0))
grupo = pygame.sprite.RenderPlain(player1,meteoro)
while True:
	deltat = clock.tick(30)
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		down = event.type == KEYDOWN
		if event.key == K_LEFT: player1.mx -= 20
		elif event.key == K_RIGHT: player1.mx += 20 
		elif event.key == K_DOWN: sys.exit(0)
	
	if meteoro.my == 530 and meteoro.mx +60 >= player1.mx >= meteoro.mx - 60 :
		if meteoro.direction == "se":
			meteoro.direction = "ne"
		elif meteoro.direction == "so":
			meteoro.directionn = "no"
		
	elif meteoro.my == 530 and not (meteoro.mx +60 >= player1.mx >= meteoro.mx - 60) :
		messagebox.showinfo('Perdiste','ok')
		meteoro.mx = 0
		meteoro.my = 0
	
	screen.fill((0,0,0))
	grupo.update(deltat)
	grupo.draw(screen)
	pygame.display.flip()

	