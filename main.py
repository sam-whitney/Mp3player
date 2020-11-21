#!/usr/bin/env python

import os
import pygame
from pygame.locals import *
from pydub import AudioSegment
from pydub.playback import play

# initialize pygame for the test key presses
pygame.init()
pygame.font.init()

width, height = 64*10, 64*8
screen = pygame.display.set_mode((width, height))
# infinite loop
path = 'OLDRADIOSHOWS'

files = os.listdir(path)
directory = "OLDRADIOSHOWS/"
for f in files:
    print(f)

file1 = files[1]


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
                song = AudioSegment.from_mp3(directory+files[0])
                play(song)
                print(files[0]+"playing")
            elif event.key == K_ESCAPE:
                pygame.quit()
                exit(0)

        break
