from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def ocr_engine(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text
