import time
import io
import picamera
import picamera.array
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import smbus
import numpy as np
from scipy import ndimage
bus = smbus.SMBus(1)
address = 0x04

def getCenter(image):
	return ndimage.measurements.center_of_mass(image)

def all():
    bus.write_block_data(address, 2, [0, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [1, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [2, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [3, 6, 148])
    time.sleep(0.2)

def zero():
    bus.write_block_data(address, 2, [0, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [1, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [2, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [3, 4, 0])
    time.sleep(0.2)

def up():
    bus.write_block_data(address, 2, [2, 4, 200])
    time.sleep(0.2)

def down():
    bus.write_block_data(address, 2, [2, 3, 50])
    time.sleep(0.2)

def forwards():
    bus.write_block_data(address, 2, [1, 4, 200])
    time.sleep(0.2)

def backwards():
    bus.write_block_data(address, 2, [1, 3, 50])
    time.sleep(0.2)

def right():
    bus.write_block_data(address, 2, [0, 4, 100])
    time.sleep(0.2)

def left():
    bus.write_block_data(address, 2, [0, 3, 50])
    time.sleep(0.2)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
time.sleep(2)
dst = (1024/2, 768/2)
e1 = 0
e2 = 0
while True:
    try:
        time.sleep(2)
        
        camera.capture(rawCapture, format="bgr")
        frame = rawCapture.array
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([100,50,50])
        upper_blue = np.array([120,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        #cv2.imshow('mask', mask)
        cv2.imshow('mask', frame)
        loc = getCenter(mask)
        cv2.waitKey(1)
        
        print('loc')
        print(loc)
        print('fb')
        print(dst[0]-loc[0])
        if(abs(dst[0]-loc[0]) > e1):
            if(dst[0] > loc[0]):
                print('f')
            else:
                print('b')
        time.sleep(2)
    except KeyboardInterrupt:
    	print('ctrl+c')
    	cv2.destroyAllWindows()
    	exit()
