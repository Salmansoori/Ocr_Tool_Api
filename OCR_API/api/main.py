from fastapi import FastAPI
from fastapi import UploadFile, File
import ocr
import os

app=FastAPI()



documents=["sample_doc_1.png","sample_doc_2.png"]


## Home page
@app.get("/")
def home():
    return "welcome to ocr tool"


## route that will show all document_ids 

@app.get("/get_doc_list")
def ShowAllImages():
    return documents


## endpoint that extract the text from image that matched <document_id> of any of the documents passed in the url  

@app.get("/parse/{document_id}")
def ShowText(document_id: str):

    #check if document_id is in document list then return converted text
    if document_id in documents:
        file=document_id
        text =ocr.read_image(file)
        #print(text)
        return text

    return "No such file exists"    
   
## Upload new file if you want

@app.post("/uploadFile/")
async def UploadFile(file: UploadFile = File(...)):
    #append new image in documents
    documents.append(file.filename)

    return {"status":"FIle Uploaded successfully"}   
