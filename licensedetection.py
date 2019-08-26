import numpy as np
import cv2
import imutils
import sys
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread('C:/Users\Mohan\Desktop\LicenseDetection\json_photos\Car_Image212.jpeg')

image = imutils.resize(image, width=500) 

cv2.imshow("Original Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.bilateralFilter(gray, 11, 17, 17)

edged = cv2.Canny(gray, 170, 200)

cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
NumberPlateCnt = None 
print (NumberPlateCnt)
count = 0
for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        if len(approx) == 4:  
            NumberPlateCnt = approx 
            break
cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
cv2.imshow("Final Image With Number Plate Detected", image)

crop_img = image[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)

cv2.imwrite("final.jpg",crop_img )

final="final.jpg"
oc=pytesseract.image_to_string (final)
print(oc)

cv2.waitKey(0)
