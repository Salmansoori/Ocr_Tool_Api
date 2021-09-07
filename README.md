# Ocr_Tool_Api
A simple ocr tool api using python FastAPI and tesseract that extract the text content from images.

# Setup 

1.Create Python virtual environment:

pip install pipenv (if not install)

cd to your project directory

pipenv shell

2. then install tesseract

On Windows

download file from https://github.com/UB-Mannheim/tesseract/wiki then add 

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your ocr script.

On Linux

sudo apt-get update

sudo apt-get install libleptonica-dev 

sudo apt-get install tesseract-ocr tesseract-ocr-dev

sudo apt-get install libtesseract-dev

On Mac

brew install tesseract

3.Then you should install the python package using pip:

pip install -r requirements.txt


# Starting a local server:

cd api

now run 

uvicorn main:app --reload
