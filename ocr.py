import pytesseract
import cv2
# import the necessary packages
from google.oauth2 import service_account
from google.cloud import vision
import argparse
import cv2
import io

def perform_ocr(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    # Convert image to greyscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Gaussian blur
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    
    # Otsu's threshold
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    
    invert = 255 - opening
    
    # Show the greyscale image
    cv2.imshow('gray', gray)
    # Show the blurred image
    cv2.imshow('blur', blur)
    # Show the threshold image
    cv2.imshow('thresh', thresh)
    # Show the kernel image
    cv2.imshow('kernel', kernel)
    # Show the opening image
    cv2.imshow('opening', opening)
    # Show the invert image
    cv2.imshow('invert', invert)

    # Perform OCR using Tesseract
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')

    return data;

def draw_ocr_results(image, text, rect, color=(0, 255, 0)):
	# unpacking the bounding box rectangle and draw a bounding box
	# surrounding the text along with the OCR'd text itself
	(startX, startY, endX, endY) = rect
	cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
	cv2.putText(image, text, (startX, startY - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
	# return the output image
	return image

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image that we'll submit to Google Vision API")
ap.add_argument("-c", "--client", required=True,
	help="path to input client ID JSON configuration file")
args = vars(ap.parse_args())

# create the client interface to access the Google Cloud Vision API
credentials = service_account.Credentials.from_service_account_file(
	filename=args["client"],
	scopes=["https://www.googleapis.com/auth/cloud-platform"])
client = vision.ImageAnnotatorClient(credentials=credentials)
# load the input image as a raw binary file (this file will be
# submitted to the Google Cloud Vision API)
with io.open(args["image"], "rb") as f:
	byteImage = f.read()
	
    
       
# create an image object from the binary file and then make a request
# to the Google Cloud Vision API to OCR the input image
print("[INFO] making request to Google Cloud Vision API...")
image = vision.Image(content=byteImage)
response = client.text_detection(image=image)
# check to see if there was an error when making a request to the API
if response.error.message:
	raise Exception(
		"{}\nFor more info on errors, check:\n"
		"https://cloud.google.com/apis/design/errors".format(
			response.error.message))

# read the image again, this time in OpenCV format and make a copy of
# the input image for final output
image = cv2.imread(args["image"])
final = image.copy()
# loop over the Google Cloud Vision API OCR results
for text in response.text_annotations[1::]:
	# grab the OCR'd text and extract the bounding box coordinates of
	# the text region
	ocr = text.description
	startX = text.bounding_poly.vertices[0].x
	startY = text.bounding_poly.vertices[0].y
	endX = text.bounding_poly.vertices[1].x
	endY = text.bounding_poly.vertices[2].y
	# construct a bounding box rectangle from the box coordinates
	rect = (startX, startY, endX, endY)
	
	# draw the output OCR line-by-line
	output = image.copy()
	output = draw_ocr_results(output, ocr, rect)
	final = draw_ocr_results(final, ocr, rect)
	# show the output OCR'd line
	print(ocr)
	cv2.imshow("Output", output)
	cv2.waitKey(0)
# show the final output image
cv2.imshow("Final Output", final)
cv2.waitKey(0)