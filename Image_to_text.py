import cv2
import pytesseract

img = cv2.imread(r"C:\Users\DEVASISH\OneDrive\Pictures\Screenshots\Screenshot 2024-07-09 221108.png")
cv2.imshow("Image", img)

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img)

print(text)
