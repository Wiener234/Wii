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
    try:
        rec = pickle.loads(rec)
    except:
        print('pickel Error')
        continue
    if rec['exit'] == 1:
        s.close()
        print('Exiting...')
        exit()

    if rec['b'] == 1:
        pyautogui.click()


    pyautogui.moveTo(rec['x'], rec['y'])
