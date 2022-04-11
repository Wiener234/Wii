import socket
import pyautogui
import pickle

pyautogui.FAILSAFE = False

s = socket.socket()         # Create a socket object
host = '192.168.2.122'        # Get local machine name
port = 12345          # Reserve a port for your service.
s.connect((host, port))

while True:
    rec = s.recv(1024)
    rec = pickle.loads(rec)
    if rec['exit'] == 1:
        s.close()
        print('Exiting...')
        exit()

    pyautogui.moveTo(rec['x'], rec['y'])
