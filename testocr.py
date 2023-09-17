from ocr import *
import os

def test_ocr():
    # Provide the path to the image you want to analyze

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = 'pills/green_semiCircle.jpg'
    abs_file_path = os.path.join(script_dir, rel_path)

    # Perform OCR on the image
    result = perform_ocr(abs_file_path)

    # Print the extracted text
    print("Extracted Text: " + result)

    cv2.waitKey()

if __name__ == "__main__":
    test_ocr()