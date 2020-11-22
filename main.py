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
# infinite loop
path = 'OLDRADIOSHOWS'

files = os.listdir(path)
# directory = "OLDRADIOSHOWS/"
files.sort(key=lambda x: x.split(".")[1])
for f in files:
    print(f)
file1 = files[0]
player = vlc.MediaPlayer('OLDRADIOSHOWS/'+file1)
value = vlc.MediaPlayer().is_playing()
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

                if player != vlc.MediaPlayer('OLDRADIOSHOWS/'+file1):
                    player.stop()
                    player = vlc.MediaPlayer('OLDRADIOSHOWS/'+file1)
                    print("stopping and starting 1")
                    player.play()

                # if player == vlc.MediaPlayer('OLDRADIOSHOWS/'+file1) and value == True:
                #     player.pause()
                #     print("pause 1")
                # else:
                #     player.play()
                #     print(file1+"playing")
                else:
                    player.pause()
                    print("pause 1")

            elif event.key == K_ESCAPE:
                player.stop
                pygame.quit()
                exit(0)

        break
