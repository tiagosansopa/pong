import time
from socket import *

while True:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    message = b''
    addr = ("127.0.0.1", 12000)

    #start = time.time()
    clientSocket.sendto(message, addr)
    data, server = clientSocket.recvfrom(1024)
    mx,my,dire = data.decode("utf-8").split(",")
    print (mx,my,dire)
    #try:
        #data, server = clientSocket.recvfrom(1024)
        #end = time.time()
        #elapsed = end - start
        #print (data, pings, elapsed)
    #except timeout:
        #print ('REQUEST TIMED OUT')
