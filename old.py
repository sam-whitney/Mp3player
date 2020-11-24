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
media_player = vlc.MediaPlayer()
files = os.listdir(path)
files.sort(key=lambda x: x.split(".")[1])
for file in files:
    print(file)

file1 = files[0]
file2 = files[1]
player = vlc.MediaPlayer()
value = vlc.MediaPlayer().is_playing()
state = False
tick = True

def playaudio(key, file):

    # if player.set_pause(1):
    #     player.set_pause(0)
    #     print("resume")
    #
    state = True
    if event.key == key:
        track = vlc.Media('OLDRADIOSHOWS/'+file)
        print("Starting:"+file)
        player.set_media(track)
        player.play()
        state = True
    return state


def pause(key, player, tick):

    if event.key == key and tick is True:
        print("pause")
        player.set_pause(1)
        tick = False
        print(tick)
    return tick


def play(key, player, tick):
    if event.key == key and tick is False:
        print("play")
        player.set_pause(0)
        tick = True
        print(tick)
    return tick


while True:

    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            playaudio(K_1, file1)
            playaudio(K_2, file2)
            pause(K_8, player, tick)
            play(K_7, player, tick)

            # if event.key == K_1:
            #
            #     if player != vlc.MediaPlayer('OLDRADIOSHOWS/'+file1):
            #         player.stop()
            #         player = vlc.MediaPlayer('OLDRADIOSHOWS/'+file1)
            #         print("stopping and starting 1")
            #         player.play()
            #
            #     # if player == vlc.MediaPlayer('OLDRADIOSHOWS/'+file1) and value == True:
            #     #     player.pause()
            #     #     print("pause 1")
            #     # else:
            #     #     player.play()
            #     #     print(file1+"playing")
            #     else:
            #         player.pause()
            #         print("pause 1")

            if event.key == K_ESCAPE:
                player.stop
                pygame.quit()
                exit(0)

        break
