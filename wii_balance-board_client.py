import socket
import pyautogui
import pickle
import subprocess


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
        subprocess.run(["notify-send", "Balance-Board: next"])
        subprocess.run(["playerctl", "--ignore-player=Gwenview", "next"])
    if rec == str('right_bottom'):
        print('lauter')
        subprocess.run(["notify-send", "Balance-Board: volume up"])
        subprocess.run(["pactl", "set-sink-volume",
                       "alsa_output.pci-0000_00_1b.0.analog-stereo", "+2%"])
    if rec == str('left_bottom'):
        print('leiser')
        subprocess.run(["notify-send", "Balance-Board: volume down"])
        subprocess.run(["pactl", "set-sink-volume",
                       "alsa_output.pci-0000_00_1b.0.analog-stereo", "-2%"])
    if rec == str('left_bottom & right_bottom'):
        print('play/pause')
        subprocess.run(["notify-send", "Balance-Board: play-pause"])
        subprocess.run(["playerctl", "--ignore-player=Gwenview", "play-pause"])
    if rec == str('left_top'):
        print('previous')
        subprocess.run(["notify-send", "Balance-Board: previous"])
        subprocess.run(["playerctl", "--ignore-player=Gwenview", "previous"])
