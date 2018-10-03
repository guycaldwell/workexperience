#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:01:27 2018

@author: guycaldwell
"""

import cv2

img = cv2.imread('soccer_photo.jpg')
img = cv2.resize(img, None, fx = 0.25, fy = 0.25)
    
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)


