#import modules
import math
import time
import RPi.GPIO as GPIO         #temp.sensor
import disp                     #display parameters and functions 
import misc 

#pin definitions
PWR  = 25                       #power switch
BTN  = 15                       #button
RST  = 24                       #display 

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PWR,  GPIO.OUT)
GPIO.setup(BTN,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def cook(ch):
    time_init = time.time()
    time_dif  = 0		# duration counter

    #default presets:
    time_cap  = 360         # timer is set to 6 hours
    temp_tar  = 44
    pasteur   = False

    if ch ==1:
        time_cap  = 360  
        temp_tar  = 44
        pasteur   = False
        
    if ch==2:
        time_cap  = 360  
        temp_tar  = 44
        pasteur   = True

    print 'program lasting ' +str(time_cap) + ' minutes, at temp = ' + str(temp_tar)

    while time_dif<time_cap:
        tempStore = open("/sys/bus/w1/devices/28-0316a0fc70ff/w1_slave")	#change this number to the Device ID of your sensor
        data = tempStore.read()
        tempStore.close()
        tempData = data.split("\n")[1].split(" ")[9]
        temperature = float(tempData[2:])
        temperature = temperature/1000
        print (temperature)
        time_dif = (time.time() - time_init)/60
        print (time_dif)

        # display the output
        time_rem = math.ceil( (time_cap - time_dif)/6 )/10
        disp.PRNT_TEMP(temperature,time_rem)

        if temperature < temp_tar:	#change this value to adjust the 'too cold' threshold
            misc.LED_BLU()
            GPIO.output(PWR, True)

        if temperature > temp_tar and temperature < (temp_tar+1):	#change these values to adjust the 'comfortable' range
            misc.LED_GRE() 
            GPIO.output(PWR, False)

        if temperature > (temp_tar+1):	#change this value to adjust the 'too hot' threshold
            misc.LED_RED()
            GPIO.output(PWR, False)

        time.sleep(1)

    # post-countdown, do the following:   
    print ('The yoghurt is finished!')  
    disp.PRNT_BUTPRES()      
    GPIO.output(PWR, False) 

    while True:
        misc.LED_FLICK()
