# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:47:16 2018

@author: dhruv_dzb8kxe
"""
#importing OPEN CV 
import cv2
#Picking up the Image
image = cv2.imread('n.jpg')
#displaying image
cv2.imshow('Original',image)

#Convert the image to GRAYSCALE
grey_image = cv2.cvtColor(image,cv2.COLOR_BAYER_BG2GRAY)
cv2.imshow('Grayscale',grey_image)
cv2.waitKey()
#Destroy Windows
cv2.destroyAllWindows()
 
