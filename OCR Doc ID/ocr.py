import pytesseract
import os
import sys


def read_image(img_path, lang='eng'):
    """
    Performs OCR on the uploaded image

    recieves path to image file and converts it to english

    Returns converted text from image
    """

    try:
        return pytesseract.image_to_string(img_path, lang=lang)
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)

def _write_to_file(text, file_path):
    """
    Helper method to write text to a file
    """
    print("[INFO] Writing text to file: {0}".format(file_path))
    with open(file_path, 'w') as fp:
        fp.write(text)
