import cv2
import pytesseract
from os import name
from pdf2image import convert_from_path
# import pandas as pd
# https://github.com/UB-Mannheim/tesseract/wiki





def pdfTotext(path, filename):
    custom_config = r'--oem 3 --psm 6'
    images = convert_from_path(path+filename, 500, poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')
    filename = filename.split(".")
    filename = filename[0]
    print(filename)
    for i, image in enumerate(images):
        fname = filename+'.png'
        image.save("upload_images/"+fname, "PNG")
    img = cv2.imread('upload_images/'+fname)
    p = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = p
    text = pytesseract.image_to_string(img, config=custom_config) 
    print(text)
    # img = cv2.resize(img, (680, 720))
    # cv2.imshow("window",img)
    # cv2.waitKey(0)
    return text