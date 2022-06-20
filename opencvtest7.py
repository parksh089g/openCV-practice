# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:16:07 2020

@author: User
"""

import cv2
import numpy as np

img1 = cv2.imread('C:/Users/User/opencv/star3.png',0)
img2 = cv2.imread('C:/Users/User/opencv/star4.png',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print("비교이미지와",ret,"일치")