#This is a comment

# importing libraries
import numpy as np
import cv2
import serial 
#import RPi.GPIO as GPIO

#things setting up
ser = serial.Serial('/dev/ttyACM0', 9600)
#GPIO.setmode(GPIO.BOARD) #use board pin numbering
#GPIO.setup(5, GPIO.OUT)  #set output pin 5
#GPIO.setup(26, GPIO.OUT) #set output pin 26
cap = cv2.VideoCapture(0)
#turn on/off bulbs
#GPIO.output(5,0) #turn off
#GPIO.output(26,1)#turn on

#ser.write('1')
#k = 'n'

while 1:
    
    if ser.readline() == 'G':
        #k = 'n'
        #GPIO.output(5,0)
        #GPIO.output(26,1)
    else:
        #k = 'n'
        #GPIO.output(5,1)
        #GPIO.output(26,0)
        #open the camera
        
        #read camera data
        ret, frame = cap.read()
        #convert to gray image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #view image on a window
        cv2.imshow('gray',gray)
        #close the camera
        cap.release()


#close all windows open by the script
cv2.distroyAllWindows()
