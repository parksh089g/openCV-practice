# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:22:54 2020

@author: User
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/User/opencv/convex.png')
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1] # 1이 번개모양 주변의 contour
hull = cv2.convexHull(cnt)

cv2.drawContours(img1, [hull], 0,(0,255,0), 3)

titles = ['Original','Convex Hull']
images = [img, img1]

for i in range(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()