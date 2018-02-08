import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 12000))
mx = my = 0
direction = "se"

while True:
	message, address = serverSocket.recvfrom(1024)
	message = ""
	if direction == "se":
		mx += 10
		my +=10
		if mx >=1024:
			direction = "so"
		elif my>=568:
			direction = "ne"

	elif direction == "ne" :
		mx+=10
		my-=10
		if mx>=1024:
			direction = "no"
		elif my<=0:
			direction = "se"
	elif direction == "no":
		mx -=10
		my -=10
		if mx<=0:
			direction = "ne"
		elif my<=0:
			direction = "so"
	elif direction == "so":
		mx -=10
		my +=10
		if mx<=0:
			direction = "se"
		elif my>=568:
			direction = "no"
	#message = message.upper()
	message = str.encode(str(mx)+","+str(my)+","+direction)
	serverSocket.sendto(message, address)
