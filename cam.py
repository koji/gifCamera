import picamera
from time import sleep
from subprocess import call

# setup the camera
with picamera.PiCamera() as camera:
        # set effect
        camera.awb_mode = 'sunlight'
        #camera.exposure_mode = 'beach'
        camera.image_effect = 'watorcolor'
        # start recording 5 sec
        camera.start_recording("pythonVideo.h264")
        sleep(5)
        # stop recording
        camera.stop_recording()

# close the camera
print("finish recording")
cmd = "MP4Box -add pythonVideo.h264 output.mp4"
call([cmd], shell=True)
print("finish generating mp4")

# generate gif
gifCmd = "ffmpeg -i output.mp4  -an -r 15  -pix_fmt rgb24 -f gif output.gif"
call([gifCmd], shell=True)
print("gif has been generated")

# delete h264 and mp4
delCmd = "rm -f pythonVideo.h264 output.mp4"
call([delCmd], shell=True)
print("Done all process")

