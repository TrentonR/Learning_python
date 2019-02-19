#Based on digital clock from b2cd

import time
import snaps
import pygame
cursor_char='_'

# Sets up window; requests format
snaps.setup(width=850, height=300, title='CLOCK WITH CHIME')
time_format=snaps.get_string('24 or 12 hr format:    ',cursor='_')
flag=isinstance(time_format,str)

while flag:
    try:
        integer_check=int(time_format)        
    except ValueError:
        time_format=snaps.get_string('Input must be an integer\n\nTry Again:    ')
        continue
    if int(time_format) != 12 and int(time_format) !=24:
        time_format=snaps.get_string('Invalid input\nMust be 12 or 24\n\nTry Again:    ')
        continue
    flag=False
#Loop ensures input is 12 or 24 in integer format

sound_var=pygame.mixer.Sound('Sniper_Fire_Reload-Mike_Koenig-1309646991.wav')
ding_dong=pygame.mixer.Sound('chime_big_ben_mod.wav')
ding_dong.set_volume(0.7)
#Creates sound objects for effects;

if time_format == '24':
    while True:
        current_time=time.localtime()
        hour_num=(current_time.tm_hour)
        minute_num=(current_time.tm_min)
        second_num=(current_time.tm_sec)
        
        if minute_num == 59 and second_num == 57:
            pygame.mixer.init()
        if minute_num == 0 and second_num == 0:
            ding_dong.play()
        if minute_num == 0 and second_num == 15:
            sound_var.play(loops=(hour_num-1), fade_ms=120)
#Provides sound effects at the top of the hour
        if minute_num <=9:
            minute_stng=('0'+str(current_time.tm_min))
        else:
            minute_stng=str(current_time.tm_min)
#Puts a zero in front of the minute when the minute is less than ten            
        second_stng=str(second_num)
        hour_stng=str(hour_num)
        clock_stng=(hour_stng+ ':' +minute_stng+ ':' +second_stng)
        snaps.display_message(clock_stng, size=200, color=(0,255,0))
        time.sleep(1)
#Lines up the string and displays it
#waits for a second before returning to the top of the loop
else:
    while True:
        current_time=time.localtime()
        hour_num=current_time.tm_hour
        minute_num=current_time.tm_min
        second_num=current_time.tm_sec
            
        if hour_num > 12:
            hour_num=hour_num-12
            hour_stng=str(hour_num)
            clock_sector='  PM'
        else:
            hour_stng=str(hour_num)
            clock_sector='  AM'
#Determines AM/PM and sets the variable to the appropriate string            
        if minute_num == 59 and second_num ==0:
            pygame.mixer.init()
        if minute_num == 0 and second_num == 0:
            ding_dong.play()
        if minute_num == 0 and second_num == 15:
            sound_var.play(loops=(hour_num-1), fade_ms=120)
#Provides sound effects at the top of the hour            
        if minute_num <=9:
            minute_stng=('0'+str(current_time.tm_min))
        else:
            minute_stng=str(current_time.tm_min)
#Puts a zero in front of the minute when the minute is less than ten            
        second_stng=str(current_time.tm_sec)
        clock_stng=(hour_stng+ ':' +minute_stng+ ':' +second_stng+ clock_sector)
        snaps.display_message(clock_stng, size=175, color=(255,0,0))
        time.sleep(1)
#Lines up the string and displays it
#waits for a second before returning to the top of the loop
