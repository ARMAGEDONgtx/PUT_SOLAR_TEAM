import socket

TCP_IP = '192.168.0.110' #aders tego kompa - serwera 
TCP_PORT = 5005
BUFFER_SIZE = 20 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept() #akcpetujemy kazde polaczenie
print ('Connection address:', addr)
i = 0
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data.decode())
    conn.send(str(i).encode()) #przesylamy jakias zmienna
    i = i + 1

conn.close()