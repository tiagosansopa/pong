import random
from socket import *
import time
import threading

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", 12000))
serverSocket.listen(1)
mx = my = 0
direction = "se"
seguir = False


def multiJugador(*args):
    conn = args[0]
    addr = args[1]
    player_position = (0,0)
    players_pos = [(0,0),(0,0),(0,0),(0,0)]
    try:
        print("conexion con {}.".format(addr))
        conn.send("Se conecto jugador nuevo".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print("recibido: {}".format(datos.decode('utf-8')))
                datos_decoded = datos.decode('utf-8')
                print("jugador "+str(addr))
                data_received = datos_decoded.split(',')
                print(data_received)
                if len(data_received) == 3 :
                    playerNumber = int(data_received[0])
                    players_pos[int(data_received[0])-1] = (int(data_received[1]),int(data_received[2]))
               

            else:
                print("prueba")
                break
    finally:
        conn.close()


while (seguir == False):
	con, address = serverSocket.accept()
	threading.Thread(target=multiJugador,args=(con,address)).start()
	#a = message.decode("utf-8").split(",")
	#print (str(a[0]))
	#serverSocket.sendto(message,address)
	
		
while True:
	#message, address = serverSocket.recvfrom(1024)
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
	print ("Something: \n",message.decode("utf-8"))

