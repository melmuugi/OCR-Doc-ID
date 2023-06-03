# OCR-Doc-ID

A simple AI and Optical Character Recognition Tool I made using FastAPI(Python)
and Tesseract to sort between a passport and an ID.

Setup

brew install tesseract
pip install -r requirements.txt

Starting a local server

cd src
uvicorn server:app --reload
