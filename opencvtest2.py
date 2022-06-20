# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:30:21 2020

@author: User
"""
import cv2
import numpy as np

img = cv2.imread('C:/Users/User/opencv/ret.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.arcLength(cnt,True) #폐곡선 도형을 만들어 둘레길이 측정
M2 = cv2.arcLength(cnt,False) #시작점과 끝점을 연결하지 않고 둘레길이 측정

print(M)
print(M2)