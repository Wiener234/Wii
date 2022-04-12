import cwiid
from time import sleep
import socket


# define Wiimote buttons

btn_up = 2048
btn_down = 1024
btn_right = 512
btn_left = 256

btn_b = 4
btn_a = 8

btn_plus = 4096
btn_minus = 16
btn_home = 128

btn_1 = 2
btn_2 = 1



#set up socket to send data
s = socket.socket()
host = '192.168.2.122'
print(host)
port = 12346
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print("Got connection from", addr)

wm = None
i = 2

while not wm:
    print('Press 1+2 now to connect Wiimote...')
    sleep(2)
    try:
        wm = cwiid.Wiimote('00:25:A0:D1:B2:F4')
        wm.led = 1
        wm.rumble = 1
        sleep(0.5)
        wm.rumble = 0
        print('Wiimote connected...')
    except:
        if i > 10:
            quit()
            break
        print('Error opening wiimote connection.')
        print('attempt' + str(i))
        i += 1

# set Wiimote report mode
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK

while True:
    buttons = wm.state['buttons']

    # exit socket and script
    if buttons == btn_1 + btn_2:
        c.send('exit'.encode())
        s.close()
        print('Exiting...')
        sleep(1)
        exit()
    
    if buttons == btn_right:
        print('next')
        c.send('next'.encode())
        sleep(0.5)

    if buttons == btn_left:
        print('prev')
        c.send('prev'.encode())
        sleep(0.5)

    if buttons == btn_up:
        print('pag_down')
        c.send('pag_down'.encode())
        sleep(0.5)

    if buttons == btn_down:
        print('pag_up')
        c.send('pag_up'.encode())
        sleep(0.5)

    if buttons == btn_plus:
        print('F5')
        c.send('f5'.encode())
        sleep(0.5)
    
    if buttons == btn_plus + btn_b:
        print('shift + f5')
        c.send('shift + f5'.encode())
        sleep(0.5)

    if buttons == btn_minus:
        print('Esc')
        c.send('esc'.encode())
        sleep(0.5)