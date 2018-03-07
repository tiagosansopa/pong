import random
from socket import *
import time



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", 12000))
serverSocket.listen(1)
players_pos = [(0,0),(0,0),(0,0),(0,0)]
conexiones = [(0,0),(0,0),(0,0),(0,0)]
contador_conexiones = 0 
number_of_players = 4
print("Server Running")
while contador_conexiones < number_of_players:
    con, address = serverSocket.accept()
    conexiones[contador_conexiones] = (con,address)
    contador_conexiones += 1
    print("Player %s connected",str(contador_conexiones))


print("Players connected")

for i in range(0,number_of_players):
    conn, address = conexiones[i]
    conn.send("All, players, ready, PLAY,".encode('UTF-8'))

print("Gaame !!!!!!!")

while True:
    for i in range(0,number_of_players):
        conn, address = conexiones[i]
        datos = conn.recv(4096)
        datos_decoded = datos.decode('utf-8')
        print (datos_decoded)
        data_received = datos_decoded.split(',')
        if len(data_received) == 3 :
            playerNumber = int(data_received[0])
            players_pos[int(data_received[0])-1] = (int(data_received[1]),int(data_received[2]))

    information_packet = ""
    for i in range(len(players_pos)):
        information_packet += str(players_pos[i][0]) +","+str(players_pos[i][1]) + "|"


    for i in range(0,number_of_players):
        conn, address = conexiones[i]
        conn.send(information_packet.encode('UTF-8'))
