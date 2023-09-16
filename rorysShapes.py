import numpy as np
import cv2 
img = cv2.imread('pills/white_circle.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh = cv2.threshold(img,127,255,0)
mask_red = cv2.inRange(hsv, lower_red, upper_red)
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(cnt)
print( M )