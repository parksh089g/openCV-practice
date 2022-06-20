# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:20:31 2020

@author: User
"""
import cv2
import numpy as np

img = cv2.imread('C:/Users/User/opencv/maps1.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(imgray,127,255,0)

#hierachy는 contours line의 계층 구조
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()