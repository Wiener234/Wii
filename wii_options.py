import cwiid
from time import sleep
import sys

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


#connect wii-mote

wm = None 
bal = None
i=2



if sys.argv[1] == 'wiimote' or sys.argv[1] == 'both':
  while not wm: 
    print("Press 1+2 now to connect...")
    try:
      wm=cwiid.Wiimote("00:25:A0:D1:B2:F4")
      # wm.enable(cwiid.FLAG_MESG_IFC | cwiid.FLAG_MOTIONPLUS)
      wm.enable(cwiid.FLAG_MOTIONPLUS)
      wm.rpt_mode = cwiid.RPT_MOTIONPLUS | cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_IR | cwiid.RPT_NUNCHUK | cwiid.RPT_BALANCE
      wm.rumble = 1
      wm.led = 1
      sleep(0.5)
      wm.rumble = 0
      print("Wiimote Connected...")
    except RuntimeError: 
      if (i>10): 
        quit() 
        break 
      print ("Error opening wiimote connection" )
      print ("attempt " + str(i) )
      i +=1




if sys.argv[1] == 'balance' or sys.argv[1] == 'both':
  while not bal:
    print("Press the red button now to connect...")
    sleep(2)
    try:  
      bal = cwiid.Wiimote("78:A2:A0:25:8E:5D")
      bal.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_BALANCE | cwiid.RPT_NUNCHUK
      print("Board Connected...")
    except RuntimeError: 
      if (i>10): 
        quit() 
        break 
      print ("Error opening wiimote connection" )
      print ("attempt " + str(i) )
      i +=1 


#print('Battery: ' + str(wm.state['battery']))

if sys.argv[1] == 'wiimote':
  while True:
      sleep(0.5)

      buttons = wm.state['buttons']


      if buttons == btn_1 + btn_2:
         exit()
        
      print(wm.state)



if sys.argv[1] == 'balance':
  while True:
      #sleep(2)
  

      buttons_bal = bal.state['buttons']

      if buttons_bal == 8:
        exit()
      try:
        print(bal.state['balance'])
      except:
        pass
  


if sys.argv[1] == 'both':
  while True:
      sleep(2)
  
      buttons = wm.state['buttons']
      buttons_bal = bal.state['buttons']
  
      if buttons == btn_1 + btn_2:
          exit()
  
      if buttons_bal == 8:
        exit()
  









#wm.state = dict

#wm.state['acc'] = tuple

#wm.state['buttons'] = int

#wm.state['ir_src'] = list
#wm.state['ir_src'][0] (empty) = NoneType 
#wm.state['ir_src'][x] = dict 
#wm.state['ir_src'][x]['pos'] = tuple
#wm.state['ir_src'][x]['pos'][x] = int
#wm.state['ir_src'][x]['size'] = int

#wm.state['nunchuk'] = dict
#wm.state['nunchuk']['stick'] = tuple
#wm.state['nunchuk']['acc'] = tuple
#wm.state['nunchuk']['buttons'] = int


# acc = 1 tilt left an rigth | 2 tilt for and back | 3 on top or not

# angle and stuff https://stackoverflow.com/questions/63939618/pitch-and-yaw-from-a-wiimote-motion-plus-using-cwiid-python
