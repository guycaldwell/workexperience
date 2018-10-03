#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:20:26 2018

@author: guycaldwell
"""
import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        cv2.imshow('image',img)
 
img = 0*np.ones((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)


cv2.imshow('image',img)
cv2.waitKey(0)
 
cv2.waitKey(1)       
cv2.destroyAllWindows()
cv2.waitKey(1)
