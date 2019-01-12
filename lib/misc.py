#################################
#LED PINS
import RPi.GPIO as GPIO
import time

ledR = 24                       #led lights
ledG = 10 
ledB = 25

GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
 
def LED_OFF():
    GPIO.output(ledR, 0)
    GPIO.output(ledG, 0)
    GPIO.output(ledB, 0)
 
def LED_FLICK():
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

def LED_RED():
    GPIO.output(ledR, 1)
    GPIO.output(ledG, 0)
    GPIO.output(ledB, 0)

def LED_GRE():
    GPIO.output(ledR, 0)
    GPIO.output(ledG, 1)
    GPIO.output(ledB, 0)

def LED_BLU():
    GPIO.output(ledR, 0)
    GPIO.output(ledG, 0)
    GPIO.output(ledB, 1)
 #################################
 # MISC - move to another python script.
def LED_FLICK():
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
    GPIO.output(ledR, 0)
    GPIO.output(ledG, 1)
    GPIO.output(ledB, 0)
    time.sleep(0.5)

def LED_RED():
    GPIO.output(ledR, 1)
    GPIO.output(ledG, 0)
    GPIO.output(ledB, 0)

def LED_GRE():
    GPIO.output(ledR, 0)
    GPIO.output(ledG, 1)
    GPIO.output(ledB, 0)

def LED_BLU():
    GPIO.output(ledR, 0)
    GPIO.output(ledG, 0)
    GPIO.output(ledB, 1)


