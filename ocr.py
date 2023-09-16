import pytesseract
import cv2

def perform_ocr(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    # Convert image to greyscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)
    # Gaussian blur
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    # cv2.imshow('blur', blur)
    # Otsu's threshold
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # cv2.imshow('thresh', thresh)

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    # cv2.imshow('kernel', kernel)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    # cv2.imshow('opening', opening)
    invert = 255 - opening
    cv2.imshow('invert', invert)

    # Perform OCR using Tesseract
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')

    return data;
