#import modules
import math
import time
import RPi.GPIO as GPIO         #temp.sensor
from lib import disp			#display parameters and functions 

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

#main loop
try:
    print("Waiting for the button to be pushed")
    disp.PRNT_BUTPRES()

    while GPIO.input(BTN) == GPIO.LOW: # Run forever
        time.sleep(0.5)
    
    #past the button push, do:
    time_init = time.time()
    time_dif  = 0		# duration counter
    time_cap  = 360 	# timer is set to 6 hours 

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

        if temperature < 44:	#change this value to adjust the 'too cold' threshold
            GPIO.output(ledR, 0)
            GPIO.output(ledG, 0)
            GPIO.output(ledB, 1)
            GPIO.output(PWR, True)

        if temperature > 44 and temperature < 45:	#change these values to adjust the 'comfortable' range
            GPIO.output(ledR, 0)
            GPIO.output(ledG, 1)
            GPIO.output(ledB, 0)
            GPIO.output(PWR, False)

        if temperature > 45:	#change this value to adjust the 'too hot' threshold
            GPIO.output(ledR, 1)
            GPIO.output(ledG, 0)
            GPIO.output(ledB, 0)
            GPIO.output(PWR, False)

        time.sleep(1)

    # post-countdown, do the following:   
    print ('The yoghurt is finished!')  
    disp.PRNT_BUTPRES()      
    GPIO.output(PWR, False) 

    while 1>0:
        GPIO.output(ledR, 0)
        GPIO.output(ledG, 0)
        GPIO.output(ledB, 1)
        time.sleep(0.5)
        GPIO.output(ledR, 0)
        GPIO.output(ledG, 1)
        GPIO.output(ledB, 0)
        time.sleep(0.5)
        GPIO.output(ledR, 1)
        GPIO.output(ledG, 0)
        GPIO.output(ledB, 0)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print ('Program Exited Cleanly')
