#!/usr/bin/env python

import os
import vlc
from gpiozero import Button
from time import sleep


# initialize pygame for the test key presses
# pygame.init()
# pygame.font.init()

# width, height = 64*10, 64*8
# screen = pygame.display.set_mode((width, height))

# import files from folder
path = '/media/pi/MP3USB/radioshows'
files = os.listdir(path)

# sort files into the right order
files.sort(key=lambda x: x.split(".")[1])
for file in files:
    print(file)

filetriggers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

# Define Button variables for the GPIO pins
button1 = Button(8)
button2 = Button(9)
button3 = Button(10)
button4 = Button(11)
button5 = Button(12)
button6 = Button(13)
button7 = Button(14)
button8 = Button(15)
button9 = Button(16)
button10 = Button(17)
button11 = Button(18)
button12 = Button(19)
button13 = Button(20)
button14 = Button(21)
button15 = Button(22)
button16 = Button(23)
button17 = Button(24)
button18 = Button(25)
button19 = Button(26)
button20 = Button(27)

state1 = False
state2 = False

# Other variables for playback
player = vlc.MediaPlayer()
playing = 0
pause = False
stop = False

# Playback functions

# Play file
def playfile(number):
    global playing
    global pause
    media = '/media/pi/MP3USB/radioshows/'+files[number-1]

    if pause is True and playing == number:
        player.set_pause(0)
        print("resume:")
        pause = False
        return

    elif playing == number:
        player.set_pause(1)
        print("paused:")
        pause = True

    elif playing != number:
        player.set_media(vlc.Media(media))
        player.play()
        pause = False
        print("playing:")

    playing = number
    print(playing)
    return playing

def resumeplaying():
    if pause is True :
        player.set_pause(0)
        print("resume:")
        print(playing)
        pause = False
        return

    else:
        return
def pausefile():
    if pause is False:
        player.set_pause(1)
        print("paused")
        pause = True
        return
    else: 
        return
def volumeup():
    print("Volume Up")
    return

def volumedown():
    print("Volume Down")
    return
while True:
    
    
    
    if button1.is_pressed:
        playfile(1)
        sleep(0.5)
    elif button12.is_pressed:
        playfile(2)
        sleep(0.5)
    elif button3.is_pressed:
        playfile(3)
        sleep(0.5)
    elif button4.is_pressed:
        playfile(4)
        sleep(0.5)
    elif button5.is_pressed:
        playfile(5)
        sleep(0.5)
    elif button6.is_pressed:
        playfile(6)
        sleep(0.5)
    elif button7.is_pressed:
        playfile(7)
        sleep(0.5)
    elif button8.is_pressed:
        playfile(8)
        sleep(0.5)
    elif button9.is_pressed:
        playfile(9)
        sleep(0.5)
    elif button10.is_pressed:
        playfile(10)
        sleep(0.5)
    elif button11.is_pressed:
        playfile(11)
        sleep(0.5)
    elif button12.is_pressed:
        playfile(12)
        sleep(0.5)
    elif button13.is_pressed:
        playfile(13)
        sleep(0.5)
    elif button14.is_pressed:
        playfile(14)
        sleep(0.5)
    elif button15.is_pressed:
        playfile(15)
        sleep(0.5)
    elif button16.is_pressed:
        playfile(16)
        sleep(0.5)
    elif button17.is_pressed:
        resumeplaying()
        sleep(0.5)
    elif button18.is_pressed:
        pausefile()
        sleep(0.5)
    elif button19.is_pressed:
        volumedown()
        sleep(0.5)
    elif button20.is_pressed:
        volumeup()
        sleep(0.5)
    elif stop == True:
        break

    
