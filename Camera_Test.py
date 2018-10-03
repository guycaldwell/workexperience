
import numpy as np
import cv2
import sys


# Read image in colour
cap = cv2.VideoCapture(0)
 
# Read first frame
ok, frame = cap.read()
img = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

if not ok:
    print("Cannot read video file")
    sys.exit()
    
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.imshow('frame', img) 
cv2.waitKey(0)

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)

cap.release()

