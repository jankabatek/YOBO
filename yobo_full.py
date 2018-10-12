#import modules
import time
import RPi.GPIO as GPIO         #temp.sensor
from lib import disp			#display parameters and functions
from itertools import cycle     #cycling loop tool

#pin definitions
ledR = 13                       #led lights
ledG = 6
ledB = 5
PWR  = 25                       #power switch
BTN  = 15                       #button
RST  = 24                       #display 

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(PWR,  GPIO.OUT)
GPIO.setup(BTN,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#set initial LED states
GPIO.output(ledR, 0)
GPIO.output(ledG, 0)
GPIO.output(ledB, 0)

GPIO.output(PWR, False)

lst = ['Yog', 'Other', 'Misc']
lst2 = [1,2,3]

i_list = [0,1,2]
i_pool = cycle(i_list)


#main loop
try:
    print("The choice menu")
    
    for i in i_pool:
        print lst[int(i)]
        raw_input("Press Enter to continue...")
        # input("Press Enter to continue...")
        j = int(i+1)    
        disp.PRNT_MENU(j,'Yog 6hrs')
    
    # while GPIO.input(BTN) == GPIO.LOW: # Run forever
        # time.sleep(0.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print ('Program Exited Cleanly')
