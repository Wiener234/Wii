import cwiid
from time import sleep
import pickle
import socket



#set up socket to send data
s = socket.socket()
host = '192.168.2.122'
print(host)
port = 12344
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print("Got connection from", addr)





bal = None
i=2

while not bal:
  print("Press the red button now to connect...")
  sleep(2)
  try:  
    bal = cwiid.Wiimote("78:A2:A0:25:8E:5D")
    print("Board Connected...")
  except RuntimeError: 
    if (i>10): 
      quit() 
      break 
    print ("Error opening wiimote connection" )
    print ("attempt " + str(i) )
    i +=1 

sleep(5)
print('Ready set go...')

bal.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_BALANCE

while True:
    buttons = bal.state['buttons']
    
    sleep(0.03)

    if buttons == 8:
        c.send('exit'.encode())
        s.close()
        sleep(1)
        exit()
    
    right_top = bal.state['balance']['right_top']
    right_bottom = bal.state['balance']['right_bottom']
    left_top = bal.state['balance']['left_top']
    left_bottom = bal.state['balance']['left_bottom']


    

    if left_bottom > 3560 and right_bottom > 2930:
        print('pause')
        c.send('left_bottom & right_bottom'.encode())
        sleep(0.2)

    elif right_bottom > 2930:
        print(right_bottom)
        c.send('right_bottom'.encode())
        sleep(0.2)

    elif left_bottom > 3560:
        print(left_bottom)
        c.send('left_bottom'.encode())
        sleep(0.2)

    elif right_top > 18600:
        print(right_top)
        c.send('right_top'.encode())
        sleep(0.2)

    elif left_top > 2800:
        print(left_top)
        c.send('left_top'.encode())
        sleep(0.2)






#{'rpt_mode': 86, 'led': 0, 'rumble': 0, 'battery': 199, 'ext_type': 3, 'error': 0, 'buttons': 0, 'acc': (0, 0, 0),
#'balance': {'right_top': 18453, 'right_bottom': 2739, 'left_top': 2642, 'left_bottom': 3410}}