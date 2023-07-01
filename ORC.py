from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Engr. Rao Hammad Ali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

image_path = './R.png'
extracted_image_text = image_to_text(image_path)
print("Extracted text from image:")
print(extracted_image_text)
