pip install PyPDF2 pillow pytesseract
import PyPDF2
from PIL import Image
import pytesseract
def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page in range(num_pages):
            pdf_page = reader.getPage(page)
            text += pdf_page.extractText()
    return text
def image_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
pdf_path = 'path_to_your_pdf.pdf'
extracted_text = pdf_to_text(pdf_path)
print("Extracted text from PDF:")
print(extracted_text)

image_path = 'path_to_your_image.jpg'
extracted_image_text = image_to_text(image_path)
print("Extracted text from image:")
print(extracted_image_text)
