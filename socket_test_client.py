import socket

s = socket.socket()
host = '192.168.2.122'
port = 12348
s.connect((host, port))

rec = s.recv(1024)
#rec = rec.decode()
print(rec['x'])
s.close()
