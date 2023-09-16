import cv2
import numpy as np 
input_img = cv2.imread("redpillTest.JPG")
img = cv2.resize(input_img, (640, 480))
#cv2.imshow('image', img)
input_img_cpy = img.copy()
cv2.waitKey(0)


# Convert RGB/ BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

 #create a mask for red color
mask_red = cv2.inRange(hsv, lower_red, upper_red)
 
# Display filtered image
#cv2.imshow('mask_red', mask_red)
cv2.waitKey(0)

# find contours in the red mask
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
# Draw detected contour in input image
contour_red_cap = cv2.drawContours(input_img_cpy, contours_red, -1, (255, 0, 255), 3)
 
# Dispay contour
cv2.imshow('contour_red_cap', contour_red_cap)
cv2.waitKey(0)
