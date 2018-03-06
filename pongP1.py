#Pong de 4
#Redes Proyecto 1
import pygame,sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
import socket


screen = pygame.display.set_mode((600,600))
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
			if self.mx >=568:
				self.direction = "so"
			elif self.my>=568:
				message = "01,ne"
				clientSocket.send(message.encode('utf-8'))
				self.direction = "ne"

		elif self.direction == "ne" :
			self.mx+=10
			self.my-=10
			if self.mx>=568:
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
				message = "01,no"
				clientSocket.send(message.encode('utf-8'))
				self.direction = "no"

		self.rect = self.image.get_rect()
		self.rect.center = (self.mx, self.my)


class Jugador(pygame.sprite.Sprite):

	def __init__(self, image, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image =  pygame.image.load(image)
		w,h = self.image.get_size()
		scale = 0.10
		self.image = pygame.transform.scale(self.image, (int(w*scale), int(h*scale)))
		self.rect = self.image.get_rect()
		self.mx = x
		self.my = y

	def update(self,deltat):
		self.rect = self.image.get_rect()
		self.rect.center = (self.mx, self.my)

rect = screen.get_rect()
meteoro = Meteoro('bola.png',(0,40))
player1 = Jugador('player1.png',35,590)
player2 = Jugador('player2.png',10,60)
player3 = Jugador('player3.png',590,35)
player4 = Jugador('player4.png',30,10)
grupo = pygame.sprite.RenderPlain(player1,player2,player3,player4,meteoro)
screen.fill((0,0,0))
grupo.draw(screen)
pygame.display.flip()
clientSocket = socket.socket()
clientSocket.connect(("127.0.0.1", 12000))
data = "p1ready"
clientSocket.send(data.encode('utf-8'))


while True:
	deltat = clock.tick(30)
	#data, server = clientSocket.recvfrom(1024)
	#mx,my,dire = data.decode("utf-8").split(",")
	
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		down = event.type == KEYDOWN
		if event.key == K_LEFT: 
			player1.mx -= 20
			m = "01,"+str(player1.mx)+","+str(player1.my)
			clientSocket.send(m.encode('utf-8'))
			
		elif event.key == K_RIGHT: 
			player1.mx += 20
			m = "01,"+str(player1.mx)+","+str(player1.my)
			clientSocket.send(m.encode('utf-8'))
		#elif event.key == K_UP: player2.my -= 20
		#elif event.key == K_DOWN: player2.my += 20
		#elif event.key == K_j: player4.mx -= 20
		#elif event.key == K_l: player4.mx += 20
		#elif event.key == K_i: player3.my -= 20
		#elif event.key == K_k: player3.my += 20
		elif event.key == K_SPACE: sys.exit(0)

	if meteoro.my == 568 and (meteoro.mx +618 >= player1.mx >= meteoro.mx) :
		if meteoro.direction == "se":
			meteoro.direction = "ne"
		elif meteoro.direction == "so":
			meteoro.directionn = "no"

	elif meteoro.my == 568 and not (meteoro.mx +618 >= player1.mx >= meteoro.mx) :
		messagebox.showinfo('Perdiste','ok')
		meteoro.mx = 0
		meteoro.my = 0

	screen.fill((0,0,0))
	grupo.update(deltat)
	grupo.draw(screen)
	pygame.display.flip()