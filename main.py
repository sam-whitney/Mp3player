#!/usr/bin/env python
import playsound
import pygame
from pygame.locals import *
from pydub import AudioSegment
from pydub.playback import play




pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.

width, height = 64*10, 64*8
screen=pygame.display.set_mode((width, height))
# infinite loop

file1 = "OLDRADIOSHOWS/Abbott_&_Costello_42-10-15_Bank_Robbery.mp3"


while True:



    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_1:
                song = AudioSegment.from_mp3(file1)
                play(song)
            elif event.key==K_2:
                playsound("OLDRADIOSHOWS/Abbott_&_Costello_42-10-15_Bank_Robbery.mp3")

        break
