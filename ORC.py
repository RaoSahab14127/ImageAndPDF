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


#from PIL import Image

#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Engr. Rao Hammad Ali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#def image_to_text(image_path):
   # img = Image.open(image_path)
  #  text = pytesseract.image_to_string(img)
 #   return text

#image_path = './R.png'
#extracted_image_text = image_to_text(image_path)
#print("Extracted text from image:")
#print(extracted_image_text)

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Engr. Rao Hammad Ali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

from PIL import Image

# Load the image containing the lab report
image = Image.open('./R.png')

# Use OCR to extract text from the image
text = pytesseract.image_to_string(image)

# Perform formatting and filtering on the extracted text
formatted_text = ""

# Split the text into paragraphs based on consecutive newline characters
paragraphs = text.split('\n\n')

# Process each paragraph and apply formatting as needed
for paragraph in paragraphs:
    # Remove leading/trailing whitespace
    paragraph = paragraph.strip()
    
    # Skip empty paragraphs
    if not paragraph:
        continue
    
    # Split the paragraph into lines
    lines = paragraph.split('\n')
    
    # Filter out empty lines and remove leading/trailing whitespace
    lines = [line.strip() for line in lines if line.strip()]
    
    # Process each line and apply formatting as needed
    for line in lines:
        # Example formatting: Add a prefix to each line
        formatted_line = "Line: " + line
        
        # Append the formatted line to the result
        formatted_text += formatted_line + '\n'
    
    # Add a space between paragraphs
    formatted_text += '\n'

# Print the formatted text or save it to a file
print(formatted_text)

# Or save the formatted text to a file
with open('formatted_lab_report.txt', 'w') as file:
    file.write(formatted_text)
