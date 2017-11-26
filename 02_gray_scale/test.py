#This is a comment

# importing libraries
import numpy as np
import cv2

#open the camera
cap = cv2.VideoCapture(0)

#create infinite loop
while (True):
	#read camera data
	ret, frame = cap.read()
	#convert to gray image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#view image on a window
	cv2.imshow('gray',gray)
	#stop the script by pressing 'q' key on the keyboard
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#close the camera
cap.release()

#close all windows open by the script
cv2.distroyAllWindows()
