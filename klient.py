import socket
import numpy as np
import matplotlib.pyplot as plt

TCP_IP = '192.168.0.110'
TCP_PORT = 5005
BUFFER_SIZE = 8
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


i = 0
while (i<100):
    s.send(MESSAGE.encode())
    data = s.recv(BUFFER_SIZE)
    plt.scatter(i, int(data.decode()))
    plt.pause(1)
    i = i + 1

#plt.show()
#s.send(MESSAGE.encode())
#data = s.recv(BUFFER_SIZE)
s.close()
#print ("received data:", data)