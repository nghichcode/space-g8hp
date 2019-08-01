import cv2
import pytesseract

# image = cv2.imread("./Z12/BL_243_rowno_87_20190715-15-56-02.png")
image = cv2.imread("./Z11/BL_462_rowno_87_20190318-11-45-19.png")
gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("pppo1.png", gray1)

gray2 = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# gray2 = cv2.medianBlur(gray1, 3)
cv2.imwrite("pppo2.png", gray2)
 

# OCR
fwpa= open("OA1.txt","w+")

text1 = pytesseract.image_to_string(image)
fwpa.write("\n----\n"+text1)
text2 = pytesseract.image_to_string(gray1)
fwpa.write("\n----\n"+text2)
text3 = pytesseract.image_to_string(gray2)
fwpa.write("\n----\n"+text3)

fwpa.close()

