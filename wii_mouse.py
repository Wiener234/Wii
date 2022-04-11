import cwiid 
import time
#import pyautogui as pag
import socket
import pickle


#set up socket to send data
s = socket.socket()
host = '192.168.2.122'
print(host)
port = 12345
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print("Got connection from", addr)



#connecting to the Wiimote. This allows several attempts 
# as first few often fail. 
print ('Press 1+2 on your Wiimote now...' )
wm = None 
i=2 
while not wm: 
  try: 
    wm=cwiid.Wiimote() 
    print("Connected...")
  except RuntimeError: 
    if (i>10): 
      quit() 
      break 
    print ("Error opening wiimote connection" )
    print ("attempt " + str(i) )
    i +=1 

#set Wiimote to report button presses and accelerometer state 
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_IR
 
#turn on led to show connected 
wm.led = 1

xy = {'x': 0, 'y': 0, 'exit': 0, 'b': 0}

while True:
    button = wm.state['buttons']
    if button == 3:
        xy['exit'] = 1
        c.send(pickle.dumps(xy))
        s.close()
        exit(wm)
        quit()
    
    time.sleep(0.03)

    if button == 4:
      xy['b'] = 1
      c.send(pickle.dumps(xy))
    else:
      xy['b'] = 0
      c.send(pickle.dumps(xy))

    #error when pos none
    if wm.state['ir_src'][0] != None and wm.state['ir_src'][1] != None:

        #pos_val is value of "pos1" in dict and from type tuple
        x1 = wm.state['ir_src'][0]['pos'][0]
        y1 = wm.state['ir_src'][0]['pos'][1]

        x2 = wm.state['ir_src'][1]['pos'][0]
        y2 = wm.state['ir_src'][1]['pos'][1]


        # size for distanze to ir_source closer to source = less movement on screen
        #pos2_size = pos2['size']

        x = 1920 - (x1+x2)
        # y is overshooting 1080 on monitor
        y = (y1+y2)

        xy['x'] = x
        xy['y'] = y

        #xy = {'x': x, 'y': y, 'exit': 0}

        c.send(pickle.dumps(xy))

        #print(xy)


        # move Courser
        #pag.moveTo(x, y)



#wm.state['ir_src'] = list
#wm.state['ir_src'][0] (empty) = NoneType 
#wm.state['ir_src'][x] = dict 
#wm.state['ir_src'][x]['pos'] = tuple
#wm.state['ir_src'][x]['pos'][x] = int
#wm.state['ir_src'][x]['size'] = int