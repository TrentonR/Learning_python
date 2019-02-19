# Steel the Bacon
# Trenton Rice 2019 01 16

import AWANA_snaps
import pygame
import random
import time
pygame.mixer.init()
num_max=int(input('Number of kids per team:   '))
AWANA_snaps.setup(width=1350, height=670, title='STEAL THE BACON')
sound_ob=pygame.mixer.Sound('A-Tone_mod.wav')
AWANA_snaps.get_key()
while True:
    num_str=str(random.randint(1, num_max))
    time.sleep(0.25)
    sound_ob.play()
    AWANA_snaps.display_message('Number\n'+num_str, vert='bottom', horiz='center',size=250,color=(255,255,255))
    AWANA_snaps.get_key()
    AWANA_snaps.display_message('The Next Number is...',vert='bottom', horiz='center',size=250,color=(125,175,175))
    delay=random.randint(2,6)/3
    time.sleep(delay)
