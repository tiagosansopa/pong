#Pong de 4
#Redes Proyecto 1
import pygame,sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
import socket


screen = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()
Tk().wm_withdraw()

class Meteoro(pygame.sprite.Sprite):
	direction = "se"
	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.image =  pygame.image.load(image)
		w,h = self.image.get_size()
		scale = 0.25
		self.image = pygame.transform.scale(self.image, (int(w*scale), int(h*scale)))
		self.rect = self.image.get_rect()
		self.mx = 300
		self.my = 90
		self.direction = "se"

	def update(self,deltat):
		if self.direction == "se":
			self.mx += 10
			self.my +=10
			if self.mx >=868:
				self.direction = "so"
			elif self.my>=568:
				message = "02,ne"
				clientSocket.send(message.encode('utf-8'))
				self.direction = "ne"

		elif self.direction == "ne" :
			self.mx+=10
			self.my-=10
			if self.mx>=868:
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
				message = "02,no"
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
meteoro = Meteoro('bola.png',(50,90))
player1 = Jugador('player1.png',35,590)
player2 = Jugador('player2.png',10,60)
player4 = Jugador('player3.png',890,35)
player3 = Jugador('player4.png',30,10)
grupo = pygame.sprite.RenderPlain(player1,player2,player3,player4,meteoro)
screen.fill((0,0,0))
grupo.draw(screen)
pygame.display.flip()
clientSocket = socket.socket()
clientSocket.connect(("127.0.0.1", 12000))

while True:
	deltat = clock.tick(30)
	#data, server = clientSocket.recvfrom(1024)
	#mx,my,dire = data.decode("utf-8").split(",")
	
	m = "04,"+str(player4.mx)+","+str(player4.my)
	clientSocket.send(m.encode('utf-8'))
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		down = event.type == KEYDOWN
		#if event.key == K_LEFT: 
		#	player1.mx -= 20
		#	m = str.encode("01,"+str(player1.mx)+","+str(player1.my))
		#	clientSocket.sendto(m, addr)
		#	
		#elif event.key == K_RIGHT: 
		#	player1.mx += 20
		#	m = str.encode("01,"+str(player1.mx)+","+str(player1.my))
		#	clientSocket.sendto(m, addr)
		#if event.key == K_UP: 
		#	player2.my -= 20
		#	m = "02,"+str(player1.mx)+","+str(player1.my)
		#	clientSocket.send(m.encode('utf-8'))
		#elif event.key == K_DOWN: 
		#	player2.my += 20
		#	m = "02,"+str(player1.mx)+","+str(player1.my)
		#	clientSocket.send(m.encode('utf-8'))
		#elif event.key == K_j: player4.mx -= 20
		#elif event.key == K_l: player4.mx += 20
		if event.key == K_i: 
			player4.my -= 20
			
		elif event.key == K_k:
			player4.my += 20
			
		elif event.key == K_SPACE: sys.exit(0)

	if meteoro.mx == 860 and (meteoro.my +85 >= player4.my >= meteoro.my-85) :
		if meteoro.direction == "ne":
			meteoro.direction = "no"
			meteoro.my+=20
		elif meteoro.direction == "se":
			meteoro.directionn = "so"
			meteoro.my+=20

	elif meteoro.mx == 860 and not (meteoro.my +85 >= player4.my >= meteoro.my-85) :
		player4.mx = 0
		player4.my = 2000

	screen.fill((0,0,0))
	grupo.update(deltat)
	grupo.draw(screen)
	pygame.display.flip()
	update = clientSocket.recv(4096).decode('UTF-8').split("|")
	u=0
	for i in update:
		x = i .split(",")

		if len(x) == 2:
			if(u==0):
				player1.mx=int(x[0])
				player1.my=int(x[1])
			elif(u==1):
				player2.mx=int(x[0])
				player2.my=int(x[1])
			elif(u==2):
				player3.mx=int(x[0])
				player3.my=int(x[1])
		u+=1

