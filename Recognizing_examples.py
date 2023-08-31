import sys
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

Image_filename = sys.argv[1]

Image = Image.open(Image_filename)

bw_image = Image.convert('L')

string_rus = pytesseract.image_to_string(bw_image, lang='rus')

print(string_rus)
