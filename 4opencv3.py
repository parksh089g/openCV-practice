# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:26:04 2020

@author: User
"""

import cv2
import numpy as np

img = cv2.imread('C:/Users/User/opencv/4/chessboard.png')
img_original = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize=3)

lines = cv2.HoughLines(edges,1,np.pi/180,130)

for i in range(len(lines)):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 -1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

res = np.vstack((img_original,img))
cv2.imshow('img.thresholding50',res)
cv2.waitKey(0)
cv2.destroyAllWindows()