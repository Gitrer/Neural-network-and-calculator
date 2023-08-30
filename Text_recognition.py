import sys
import pytesseract
from PIL import Image

Image_filename = sys.argv[1]
Image = Image.open(Image_filename)

string = pytesseract.image_to_string(Image, lang='eng')

print(string)
