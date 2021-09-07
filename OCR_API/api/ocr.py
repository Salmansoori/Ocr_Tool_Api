from PIL import Image
import pytesseract
import os
import sys
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 


## function that extract the text content from image

def read_image(img):
    try:
        openImage=Image.open(img)
        return pytesseract.image_to_string(openImage)
    except:
        return "Unable to process file"
