from ocr import *
import os
import cv2
import numpy as np 
from PIL import Image
import scipy.misc

input_img = cv2.imread("pills/orange_circle.jpg")
imgtest = 255 - input_img
img = cv2.resize(input_img, (640, 480))
cv2.imshow('image', img)
input_img_cpy = img.copy()
cv2.waitKey(0)

def test_ocr():
    # Provide the path to the image you want to analyze

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = 'pills/white_circle.jpg'
    abs_file_path = os.path.join(script_dir, rel_path)
    img = cv2.resize(input_img, (640, 480))

    # Perform OCR on the image
    result = perform_ocr(abs_file_path)

    # Print the extracted text
    print("Extracted Text: " + result)

    cv2.waitKey()

if __name__ == "__main__":
    test_ocr()