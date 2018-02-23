import picamera
from time import sleep
from subprocess import call
import RPi.GPIO as GPIO
import json
import subprocess
#from twython import Twython

# init settings
GPIO.setmode(GPIO.BOARD)
button1 = 3 # button 1 grund 6 
button2 = 13 # button 2 ground 20
button3 = 23 # button 3 ground 25
#led1 = 7 # go to green led
#led2 = 8 # go to yellow led

# when button1 is pushed, camera starts taking photos without any filters
# when button2 is pushed, camera starts taking photos with filters
def setEnv():
    # init components
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # no filter
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # filter 1
    GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # filter 2
    #GPIO.setup(led1, GPIO_OUT)
    #GPIO.setup(led2, GPIO_OUT)

# setup the camera
with picamera.PiCamera() as camera:

    while(button1==False and button2==False and button3==False):

         # hit button 1
        if(button1==True and button2 == False and button3 == False):
            # filter
            print("button1 on")
            print("no filter")

        # hit button 2
        if(button1==False and button2 == True and button3 == False):
            # set filter 1
            print("button2 on")
            camera.awb_mode = 'sunlight'
            camera.image_effect = 'watercolor'

        # hit button3
        if(button1==False and button2 == False and button3 == True):
            # set filter2
            print("button3 on")
            camera.awb_mode = 'flash'
            camera.exposure_mode = 'beach'
        # hit button1 and button2
        if(button1==True and button2==True):
        # filter3
            print("button1 & button2 on")
            camera.image_effect = 'colorswap'

        #hit button1 and button3
        if(button1==True and button2==False and button3==True):
            # filter4
            print("button1 & button3 on")
            camera.awb_mode = 'shade'
            camera.exposure_mode = 'spotlight'

        # hit button 2 and button3
        if(button1==False and button2==True and button3==True):
            # filter5
            print("button2 & button3 on")
            camera.image_effect = 'colorswap'
            camera.exposure_mode = 'flash'
        
        # hit all buttons
        if(button1 == True and button2==True and button3==True):
            # shut down
            print("button1 & button2 & button3 on")
            break
            
        # set effect
        #camera.awb_mode = 'sunlight'
        #camera.exposure_mode = 'beach'
        #camera.image_effect = 'watercolor'
        # start recording 5 sec
        #camera.start_recording("pythonVideo.h264")
        #sleep(5)
        # stop recording
        #camera.stop_recording() 

        # for i in range(0,30):
        #     camera.capture('output' + str(i) + '.png')

    # close the camera
    #print("finish recording")
    #cmd = "MP4Box -add pythonVideo.h264 output.mp4"
    #call([cmd], shell=True)
    #print("finish generating mp4")

    # generate gif
    #gifCmd = "ffmpeg -i output.mp4  -an -r 15  -pix_fmt rgb24 -f gif output.gif"

    # gifCmd = "ffmpeg -r 10 -f image2 -i output%d.png -pix_fmt rgb24 -f gif output.gif"
    # call([gifCmd], shell=True)
    # print("gif has been generated")

    # delete h264 and mp4
    #delCmd = "rm -f pythonVideo.h264 output.mp4"

    # delCmd = "rm -f *.png"
    # call([delCmd], shell=True)
    # print("Done all process")

