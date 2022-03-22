import cv2
import numpy as np
import pytesseract
import os

from django.conf import settings
full_path = str(settings.BASE_DIR)
from images.models import UserImage

def text_detection(img_url):

    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    path = "E:/7th sem project/OCR_django"+img_url
    print(path)
    img_r = cv2.imread(path)
    text = pytesseract.image_to_string(img_r)
    return text