import socket
from time import sleep

#set up socket to send data
s = socket.socket()
host = '192.168.2.122'
print(host)
port = 12348
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print("Got connection from", addr)
