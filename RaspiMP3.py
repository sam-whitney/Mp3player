#!/usr/bin/env python

import os
import pygame
import vlc
from pygame.locals import *

# initialize pygame for the test key presses
pygame.init()
pygame.font.init()

width, height = 64*10, 64*8
screen = pygame.display.set_mode((width, height))


path = 'OLDRADIOSHOWS'

files = os.listdir(path)
states = [False, False, False, False, False,
         False, False, False, False, False,
        ]
files.sort(key=lambda x: x.split(".")[1])
for file in files:
    print(file)

player = vlc.MediaPlayer()
playing = 0
pause = False


def playfile(number):
    global playing
    global pause
    media = 'OLDRADIOSHOWS/'+files[number-1]

    if pause is True:
        player.set_pause(0)
        print("resume:")
        pause = False
        return

    if playing == number:
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


while True:

    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:

            if event.key == K_1:
                playfile(1)
            elif event.key == K_2:
                playfile(2)
            elif event.key == K_3:
                playfile(3)
            elif event.key == K_4:
                playfile(4)
            elif event.key == K_5:
                playfile(5)
            elif event.key == K_6:
                playfile(6)
            elif event.key == K_7:
                playfile(7)
            elif event.key == K_8:
                playfile(8)
            elif event.key == K_6:
                playfile(6)
            elif event.key == K_7:
                playfile(7)
            elif event.key == K_8:
                playfile(8)


            #     player.set_pause(0)
            #     player.set_media(vlc.Media('OLDRADIOSHOWS/'+files[0]))
            #     player.play()
            #     states[0] is True
            #     return states
            #
            #     print("1")
            # elif event.key == K_2:
            #     player.set_pause(0)
            #     player.set_media(vlc.Media('OLDRADIOSHOWS/'+files[1]))
            #     print("2")
            # elif event.key == K_3:
            #     print(states)

            if event.key == K_ESCAPE:
                player.stop
                pygame.quit()
                exit(0)

        break
