import socket
import pyautogui
import pickle
import subprocess
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK, VK_VOLUME_UP, VK_VOLUME_DOWN, KEYEVENTF_EXTENDEDKEY


x = 0

s = socket.socket()
host = '192.168.2.122'
port = 12344
s.connect((host, port))

while True:
    x += 1
    print(x)
    rec = s.recv(1024)
    rec = rec.decode()

    if rec == str('exit'):
        s.close()
        print('Exiting...')
        exit()
    if rec == str('right_top'):
        print('next')
        win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
    if rec == str('right_bottom'):
        print('lauter')
        win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
    if rec == str('left_bottom'):
        print('leiser')
        win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
    if rec == str('left_bottom & right_bottom'):
        print('play/pause')
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    if rec == str('left_top'):
        print('previous')
        win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
