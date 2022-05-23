import cv2
import numpy as np
import pytesseract

#img1 = cv2.imread('200_actual.jpg')
#img1 = cv2.imread('100_2.jpg')
img1 = cv2.imread('500_actual.jpg')

#img2 = cv2.imread('200_actual.jpg', 0)
#img2 = cv2.imread('100_2.jpg', 0)
img2 = cv2.imread('500_actual.jpg', 0)

img_median = cv2.medianBlur(img2, 5)
cv2.imshow('window_1',img_median)
cv2.imwrite('window_1_.jpg',img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()

wide = cv2.Canny(img_median, 240, 250)
cv2.imshow('window_2',wide)
cv2.imwrite('window_2_.jpg',wide)

img4 = cv2.imread('window_2_.jpg')

kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(img4, kernel, iterations=1)

cv2.imshow('Dilation' , img_dilation)
cv2.imwrite('Dilation2.jpg' , img_dilation)

print(wide.shape)

cropped = img_dilation[332:420, 898:1050]
cv2.imshow("cropped", cropped)
cv2.imwrite("cropped.jpg", cropped)

#img3 = cv2.resize(cropped, (600, 360))
#cv2.imshow("resized", img3)
#cv2.imwrite("resized.jpg", img3)

croppd = cv2.imread('icropped.jpg')

# configurations
config = ('-l eng --oem 1 --psm 3')

# pytessercat
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
text1 = pytesseract.image_to_string(croppd, config=config)

# print text
text2 = text1.split('\n')
print(text2)

cv2.waitKey(0)
cv2.destroyAllWindows()



