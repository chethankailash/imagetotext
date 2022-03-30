import cv2
import pytesseract
import sys

imgpath= sys.argv[1]

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
# here set your tesseract path with your tesseract path

img = cv2.imread(imgpath)
text = pytesseract.image_to_string(img)
print(text)