# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:14:21 2018

@author: dhruv_dzb8kxe
"""

#importing OPEN CV 
import cv2
#Picking up the Image
image = cv2.imread('n.jpg')
#displaying image
cv2.imshow('Original',image)


hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV IMAGE',hsv_image)
cv2.waitKey(0)

cv2.imshow('HSV CHANNELL',hsv_image[:,:,0])
cv2.waitKey(0)

cv2.imshow('Saturation_channel',hsv_image[:,:,1])
cv2.waitKey(0)

cv2.imshow('Value Channel:',hsv_image[:,:,2])
cv2.waitKey(0)


cv2.destroyAllWindows()

