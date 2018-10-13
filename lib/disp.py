import Adafruit_GPIO.SPI as SPI #display
import Adafruit_SSD1306         #display

# image libraries
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# pin number
RST  = 24    

#define the display function
# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
#Load default font.
font = ImageFont.load_default()

#############################################################
# TEMPERATURE & TIME OUTPUT
def PRNT_MENU(num,text):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    # First define some constants to allow easy resizing of shapes.
    x = 4
    y = 2

    # Write output
    draw.text((x,y), 'Choose the program: ',  font=ImageFont.load_default(), fill=255)
    draw.text((x,y+14), '(' + str(num) +') ' + text ,  font=ImageFont.load_default(), fill=255)

    # Display image.
    disp.image(image)
    disp.display()


#############################################################
# TEMPERATURE & TIME OUTPUT
def PRNT_BUTPRES():
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    # First define some constants to allow easy resizing of shapes.
    x = 4
    y = 2
    
    # Write output
    draw.text((x,y), 'The time has come to ',  font=ImageFont.load_default(), fill=255)
    draw.text((x+10,y+14), '...push the button!',  font=ImageFont.load_default(), fill=255)

    # Display image.
    disp.image(image)
    disp.display()

#############################################################
# TEMPERATURE & TIME OUTPUT
def PRNT_TEMP(tem,tim):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    # First define some constants to allow easy resizing of shapes.
    x = 4
    y = 2
     
    # Write output
    draw.text((x, y),  '====( YOBO 2.0 )====',  font=font, fill=255)
    draw.text((x, y+10), 'Temperature:',  font=font, fill=255)
    draw.text((x, y+18), 'Rem. time:', font=font, fill=255)

    draw.text((x+80, y+10), str(tem) +'C',  font=font, fill=255)
    draw.text((x+80, y+18), str(tim) +' hrs', font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()


#############################################################
# FINISH SCREEN
def PRNT_FINISH():
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    # First define some constants to allow easy resizing of shapes.
    x = 4
    y = 4
     
    # Write output
    draw.text((x,y), 'Hora est.',  font=ImageFont.load_default(), fill=255)

    # Display image.
    disp.image(image)
    disp.display()

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
