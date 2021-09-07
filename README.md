# Ocr_Tool_Api
A simple ocr tool api that extract the text content from images using FastApi and tesseract ( Tesseract is an open source text recognition (OCR) Engine.It can be used directly, or (for programmers) using an API to extract printed text from images. It supports a wide variety of languages.Tesseract is compatible with many programming languages and frameworks through wrappers.)

# Setup 

1.Create Python virtual environment:

pip install pipenv (if not install)

cd to your project directory

pipenv shell

2.then install tesseract

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

now run following command

uvicorn main:app --reload
