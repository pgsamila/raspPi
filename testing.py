#This is a comment

# importing libraries
import numpy as np
#import cv2
import serial 
#import RPi.GPIO as GPIO

#things setting up
ser = serial.Serial('/dev/ttyACM0', 9600)


ser.write('1')
#k = 'n'

while 1:
    print ser.readline() 
    
#close all windows open by the script

