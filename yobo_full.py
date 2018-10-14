#import modules
import time
import RPi.GPIO as GPIO         #temp.sensor
from lib import disp		#display parameters and functions
from lib import prog
from itertools import cycle     #cycling loop tool
from gpiozero import Button

#pin definitions
ledR = 13                       #led lights
ledG = 6
ledB = 5
PWR  = 25                       #power switch
BT1  = 15                       #button
BT2  = 16                       #button
RST  = 24                       #display 

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(PWR,  GPIO.OUT)
GPIO.setup(BT1,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BT2,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#set initial LED states
GPIO.output(ledR, 0)
GPIO.output(ledG, 0)
GPIO.output(ledB, 0)

#GPIO.output(PWR, False)

butt1 = Button(BT1, pull_up=False,hold_repeat=False)
butt2 = Button(BT2, pull_up=False,hold_repeat=False)

#button functions
##b1 = 0
##b2 = 0
##def button_callback(channel):
##    global b1
##    b1 = b1 + 1
##    print("Button 1 was pushed!" + str(b1))
##    time.sleep(0.1)
##    
##def button_callback2(channel):
##    global b2
##    b2 += 1
##    print("Button 2 was pushed!" + str(b2))
##
##GPIO.add_event_detect(BT1,GPIO.RISING,callback=button_callback)
##GPIO.add_event_detect(BT2,GPIO.RISING,callback=button_callback2)

#menu options
lst = ['Yog', 'Other', 'Misc']
n_l = len(lst) 

#main loop
try:
    # first, select the cooking program from the choice menu.
    i = 0 
    print("The choice menu")
    disp.PRNT_MENU(1,str(lst[i]))
    print 'Current choice: 1'

    while butt2.is_pressed == False:
        if butt1.is_pressed:
            i = i+1
            if i >= n_l:
                i = 0   #revert counter to zero if going out of bounds
            ch_disp = i + 1
            print 'Current choice: ' + str(ch_disp)
            disp.PRNT_MENU(ch_disp,str(lst[i]))
            butt1.wait_for_release()
            
        time.sleep(0.1)

    #once the button 2 is pressed, execute the selected program.
        
    print 'lets doooooo it!'
    prog.cook(ch_disp)

    #for autostart on reboot, put this into cronwrap:
    #sudo python /home/pi/YOBO/yobo_full.py
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print ('Program Exited Cleanly')

#put 
