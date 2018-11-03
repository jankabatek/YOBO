#import modules
import time
import RPi.GPIO as GPIO         #temp.sensor
from lib import disp		#display parameters and functions
from lib import prog
from itertools import cycle     #cycling loop tool
from gpiozero import Button

import gaugette.gpio
import gaugette.rotary_encoder
import gaugette.switch

#GPIO pin definitions for  standard routines
ledR = 10                       #led lights
ledG = 24
ledB = 25
PWR  = 27                      #power switch
RST  = 12                      #display 

#WPi pin definitions for the rotary encoder (gaugette lib)
A_PIN = 0
B_PIN = 1
SW_PIN = 3
   
#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(PWR,  GPIO.OUT)
#GPIO.setup(BT1,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(BT2,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#set initial LED states
GPIO.output(ledR, 0)
GPIO.output(ledG, 0)
GPIO.output(ledB, 0)

#GPIO.output(PWR, False)
#butt1 = Button(BT1, pull_up=False,hold_repeat=False)
#butt2 = Button(BT2, pull_up=False,hold_repeat=False)

#Rotary initialization
gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder(gpio, A_PIN, B_PIN) #encoder 
encoder.start()
sw = gaugette.switch.Switch(gpio, SW_PIN) #built-in button press 


#menu options
lst = ['Yoghurt 6hrs', 'Other', 'Misc']
n_l = len(lst) 

#main loop
try:
    # first, select the cooking program from the choice menu.
    disp.PRNT_LOGO()
    time.sleep(2)
    i = 0
    butt_state = 0
    print("The choice menu")
    disp.PRNT_MENU(1,str(lst[i]))
    print ('Current choice: 1')

    while butt_state == 0:
        delta = encoder.get_cycles()
        butt_state = sw.get_state()
        if delta!=0:
            i = i+delta
            if i >= n_l:
                i = 0   #revert counter to zero if going out of upper bound
            if i <0 :
                i = n_l-1   #revert counter to the last if going out of lower bound  
                
            ch_disp = i + 1
            print ('Current choice: ' + str(ch_disp))
            disp.PRNT_MENU(ch_disp,str(lst[i]))
            
            
        time.sleep(0.1)

    #once the button 2 is pressed, execute the selected program.
        
    print ('lets doooooo it!')
    prog.cook(ch_disp)

    #for autostart on reboot, put this into cronwrap:
    #sudo python /home/pi/YOBO/yobo_full.py
        
except KeyboardInterrupt:
    GPIO.cleanup()
    disp.PRNT_LOGO()
    print ('Program Exited Cleanly')

#put 
