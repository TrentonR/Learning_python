# 20190114 Trenton Rice
# Shipwreck for AWANA;

import snaps_shipwreck
import time
import random
import pygame
counter_max=int(input('Max Number of Instructions (Min is 2):   '))
min_delay=int(input('Min Delay:   '))
max_delay=int(input('Max Delay:   '))



snaps_shipwreck.display_image('shipwreck-wallpaper.jpg')
while True:
    begin_check=snaps_shipwreck.get_string('To Begin Press  ')
    if begin_check == '':
        break
    
pygame.mixer.Sound.play(pygame.mixer.Sound('Pacman_Introduction_Music.wav'))
time.sleep(4.5)
prev_command=0
loopy=True

while loopy:
    counter=0
    command_num=random.randint(2, counter_max)

    while counter <= command_num:
        command=random.randint(1, 6)
        pygame.mixer.init()
        tone=pygame.mixer.Sound('A-Tone.wav')
        bell=pygame.mixer.Sound('Ship_bell.wav')
        crash=pygame.mixer.Sound('Crash_Large.wav')
        if prev_command == command:
            continue
        if command == 1:
            tone.play(loops=1)
            snaps_shipwreck.display_message('PORT',color=(0,0,255))
        if command == 2:
            tone.play(loops=1)
            snaps_shipwreck.display_message('BOW',color=(255,0,0))
        if command == 3:
            bell.play()
            snaps_shipwreck.display_message('MAN OVERBOARD',color=(255,255,255))
        if command == 4:
            tone.play(loops=1)
            snaps_shipwreck.display_message('STARBOARD',color=(255,255,0))
        if command == 5:
            snaps_shipwreck.display_message('SHIPWRECK',color=(10,10,10))
            crash.play()
            time.sleep(1)
            crash.fadeout(800)
        if command == 6:
            tone.play(loops=1)
            snaps_shipwreck.display_message('STERN',color=(0,255,0))
        counter=counter+1
        prev_command=command
        delay=random.randint(5, 7)
        time.sleep((4*delay)/5)
        snaps_shipwreck.display_image('shipwreck-wallpaper.jpg')
        time.sleep(delay/5)

    loop_check=snaps_shipwreck.get_string('Start Next Round  ')
    snaps_shipwreck.display_image('shipwreck-wallpaper.jpg')
    if loop_check != '':
        snaps_shipwreck.display_image('Looney_themed_The_End.jpg')
        time.sleep(4)
        break
