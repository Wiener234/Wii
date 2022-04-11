import cwiid
from time import sleep
import sys

btn_up = 2048
btn_down = 1024
btn_right = 512
btn_left = 256

btn_b = 4
btn_a = 8

btn_plus = 4069
btn_minus = 16
btn_home = 128

btn_1 = 2
btn_2 = 1


#connect wii-mote

wm = None 
bal = None
i=2

# while not wm: 
#   print("Press 1+2 now to connect...")
#   try:
#     wm=cwiid.Wiimote("00:25:A0:D1:B2:F4")
#     wm.rumble = 1
#     wm.led = 1
#     sleep(0.5)
#     wm.rumble = 0
#     print("Wii-Mote Connected...")
#   except RuntimeError: 
#     if (i>10): 
#       quit() 
#       break 
#     print ("Error opening wiimote connection" )
#     print ("attempt " + str(i) )
#     i +=1





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

bal.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_BALANCE | cwiid.RPT_NUNCHUK
#wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_IR | cwiid.RPT_NUNCHUK | cwiid.RPT_BALANCE

#print('Battery: ' + str(wm.state['battery']))

while True:
    sleep(2)

    #buttons = wm.state['buttons']
    buttons_bal = bal.state['buttons']

    # if buttons == btn_1 + btn_2:
    #     exit()

    if buttons_bal == 8:
      exit()


    # if wm.state['ir_src'][0] != None:
    #     print(type(wm.state['ir_src'][0]['size']))
    print(bal.state)




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


