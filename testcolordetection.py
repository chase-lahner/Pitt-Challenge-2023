import cv2
import numpy as np 
input_img = cv2.imread("pills/lightgreen_circle.jpg")
input_img2 = cv2.imread("pills/green_capsule.jpg")
img = cv2.resize(input_img, (640, 480))
img2 = cv2.resize(input_img2, (640, 480))
#cv2.imshow('image', img)
input_img_cpy = img.copy()
input_img_cpy2 = img2.copy()



# Convert RGB/ BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)

#green
lower_green = np.array([60, 20, 50])
upper_green = np.array([90, 255, 255])
mask_green = cv2.inRange(hsv,lower_green,upper_green)
mask_green2 = cv2.inRange(hsv2,lower_green,upper_green)



#turqoise
lower_turqoise = np.array([190, 100, 100])
upper_turqoise = np.array([170, 255, 255])
mask_turqoise = cv2.inRange(hsv,lower_turqoise ,upper_turqoise )


#blue
lower_blue = np.array ([100, 50, 50])
upper_blue = np.array([130, 255, 255])
mask_blue = cv2.inRange(hsv,lower_blue ,upper_blue )

#grey
lower_grey = np.array([0, 100, 100])
upper_grey = np.array([10, 255, 255])
mask_grey = cv2.inRange(hsv,lower_grey ,upper_grey )

 
# Display filtered image
#cv2.imshow('mask_green', mask_green)
#cv2.imshow('mask_green2', mask_green2)



# find contours in the red mask
#contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Draw detected contour in input image
#contour_red_cap = cv2.drawContours(input_img_cpy, contours_red, -1, (255, 0, 255), 3)

# find contours in the green mask
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Draw detected contour in green image
contour_green_cap = cv2.drawContours(input_img_cpy, contours_green, -1, (255, 0, 255), 3)

contours_green2, _ = cv2.findContours(mask_green2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_green_cap2 = cv2.drawContours(input_img_cpy2, contours_green2, -1, (255, 0, 255), 3)


# find contours in the red mask
#contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Draw detected contour in input image
#contour_blue_cap = cv2.drawContours(input_img_cpy, contours_blue, -1, (255, 0, 255), 3)
 
# Dispay contour
cv2.imshow('contour_green_cap', contour_green_cap)
cv2.imshow('contour_green_cap2', contour_green_cap2)

cv2.waitKey(0)
