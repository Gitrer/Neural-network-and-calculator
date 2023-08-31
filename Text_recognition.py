import sys
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

Image_filename = sys.argv[1]
Image = Image.open(Image_filename)

bw_image = Image.convert('L')

string = pytesseract.image_to_string(bw_image, lang='eng')

print(string)
