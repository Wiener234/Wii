import socket

s = socket.socket()
host = '192.168.2.122'
port = 12348
s.connect((host, port))
