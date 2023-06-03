from operator import truediv
from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates
from itertools import count
import shutil
import ocr
import os

# initialize the app and defining routes to the web app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# this one returns the html file
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# this is is the api endpoint which performs the ocr function
@app.post("/extract_text")
def perform_ocr(image: UploadFile = File(...)):
    # this function saves file to disk in path temp and names it temp
    temp_file = _save_file_to_disk(image, path="temp", save_as="temp") 
    text = ocr.read_image(temp_file) #this part performs the ocr execution. ocr liblary was defined in ocr.py
    with open("test.txt", "w") as f:
        for texts in text:
            f.write(texts)
    #this is the logic part for processing the extracted file to find the document type
    fh =open("test.txt", "r")
    pas = "PASSPORT"
    iden = "IDENTIFICATION CARD"
    ret = "Invalid"
    s = " "
    while (s):
        s= fh.readline()
        l=s.split()
        if "PASSPORT" in l:
            return {"filename": image.filename, "text": pas}
        elif "Passport" in l:
            return {"filename": image.filename, "text": pas}
        elif "JAMHURI" in l:
            return {"filename": image.filename, "text": iden}

# this function saves the file to the local machine
def _save_file_to_disk(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return temp_file

