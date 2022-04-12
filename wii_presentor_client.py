import socket
import pyautogui as pag

s = socket.socket()
host = '192.168.2.122'
port = 12346
s.connect((host, port))

while True:
    rec = s.recv(1024)
    rec = rec.decode()

    if rec == str('exit'):
        s.close()
        print('Exiting...')
        exit()

    if rec == str('next'):
        pag.press('right')

    if rec == str('prev'):
        pag.press('left')

    if rec == str('pag_up'):
        pag.press('pageup')

    if rec == str('pag_down'):
        pag.press('pagedown')

    if rec == str('f5'):
        pag.press('f5')

    if rec == str('shift + f5'):
        pag.hotkey('shift', 'f5')

    if rec == str('esc'):
        pag.press('esc')
