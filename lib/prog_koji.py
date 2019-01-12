#import modules
import math
import time
import RPi.GPIO as GPIO         #temp.sensor
import disp                     #display parameters and functions 
import misc

import gaugette.gpio
import gaugette.rotary_encoder
import gaugette.switch

#pin definitions
PWR  = 22                       #power switch
HUM  = 23
RST  = 12                       #display

#WPi pin definitions for the rotary encoder (gaugette lib)
A_PIN = 0
B_PIN = 1
SW_PIN = 3

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PWR,  GPIO.OUT)
GPIO.setup(HUM,  GPIO.OUT)
#GPIO.setup(BTN,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Rotary initialization
gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder(gpio, A_PIN, B_PIN) #encoder 
encoder.start()
sw = gaugette.switch.Switch(gpio, SW_PIN) #built-in button press 


def cook(ch,tem,tim):
    time_init = time.time()
    time_dif  = 0		# duration counter
    abort = False

    #default presets:
    time_cap  = 360             # timer is set to 6 hours
    temp_tar  = 44
    humi_tar  = 74

    if ch ==1:
        time_cap  = 60*48  # 2 days incubation
        temp_tar  = 30
        humi_tar  = 74
        
    if ch==2:
        time_cap  = tim*60  
        temp_tar  = tem
        humi_tar  = 74

    if ch==3:
        time_cap  = 360  
        temp_tar  = 44

    if ch ==4:
        time_cap  = 660  
        temp_tar  = 44
        GPIO.output(PWR, False)
        time.sleep(60*60*4)
        time_init = time.time()
        

    print 'program lasting ' +str(time_cap) + ' minutes, at temp = ' + str(temp_tar)
    
    while time_dif<time_cap:
        tempStore = open("/sys/bus/w1/devices/28-0316a0fc70ff/w1_slave")	#change this number to the Device ID of your sensor
        data = tempStore.read()
        tempStore.close()
        tempData = data.split("\n")[1].split(" ")[9]
        temperature = float(tempData[2:])
        temperature = round(temperature/1000,2)
        print (temperature)
        time_dif = (time.time() - time_init)/60
        print (time_dif)

        if temperature < temp_tar:	#change this value to adjust the 'too cold' threshold
            GPIO.output(PWR, True)

        if temperature > temp_tar:	#change these values to adjust the 'comfortable' range
            GPIO.output(PWR, False)

        if humidity < humi_tar:	        #humidity control
            GPIO.setup(HUM,  GPIO.IN)
        if humidity > humi_tar:
            GPIO.setup(HUM,  GPIO.OUT)

        # display the output
        time_rem = math.ceil( (time_cap - time_dif)/6 )/10
        disp.PRNT_TEMP(temperature,time_rem)

        # more sensitive abort button with time.sleep(1) embedded into the routine
        mini_t = 0.0
        while mini_t < 1 and abort == False :
            mini_t += 0.1
            time.sleep(0.1)
            
            butt_state = sw.get_state()
            delta = encoder.get_cycles()
            if butt_state ==1 or delta !=0:
                butt_state ==0
                disp.PRNT_TEXT(' ','Hold button 3 secs', '    to abort.    ')
                time.sleep(4)
                butt_state = sw.get_state()
                if butt_state ==1:
                    time_dif = 10000000000000
                    abort = True

    if abort:
        disp.PRNT_TEXT(' ','Aborted!')
        GPIO.cleanup()
    else:
        # post-countdown, do the following:   
        print ('The yoghurt is finished!')  
        disp.PRNT_BUTPRES()      
        GPIO.output(PWR, False) 

        while True:
            misc.LED_FLICK()
