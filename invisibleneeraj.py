###################### Neeraj##################################


########################################

import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
#allowing the system to sleep for 3 seconds before the webcam fires up !
time.sleep(3)
count = 0
background = 0
#taking thee image of background
for i in range(60):
    ret,background = cap.read()
background = np.flip(background,axis=1)
while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    count+=1
    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,120,70])# here red 
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask1 = mask1+mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
    mask2 = cv2.bitwise_not(mask1)

    pic = cv2.imread('34.jpg')

    res1 = cv2.bitwise_and(background,background,mask=mask1)
    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('hsv',hsv)
    #cv2.imshow("Invisible Neeraj",res1)
    #cv2.imshow("Invisible Neeraj",res2)
    cv2.imshow("Invisible Neeraj",final_output)
    
    k = cv2.waitKey(10)
    if k == 27:
        break
