import cv2
import numpy as np
import pytesseract

img1 = cv2.imread('100_1.png')
#img1 = cv2.imread('100_2.jpg')
#img1 = cv2.imread('500_1.jpg')

img2 = cv2.imread('100_1.png', 0)
#img2 = cv2.imread('100_2.jpg', 0)
#img2 = cv2.imread('500_1.jpg', 0)



img_median = cv2.medianBlur(img2, 5)
cv2.imshow('window_1',img_median)
cv2.imwrite('window_1.jpg',img_median)
cv2.waitKey(0)
cv2.destroyAllWindows()

wide = cv2.Canny(img_median, 240, 250)
cv2.imshow('window_2',wide)
cv2.imwrite('window_2.jpg',wide)

img4 = cv2.imread('window_2.jpg')

kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(img4, kernel, iterations=1)
cv2.imshow('Dilation' , img_dilation)
cv2.imwrite('Dilation.jpg' , img_dilation)


print(wide.shape)

cropped = wide[186:240, 472:550]
cv2.imshow("cropped", cropped)
cv2.imwrite("cropped.jpg", cropped)

#img3 = cv2.resize(cropped, (600, 360))
#cv2.imshow("resized", img3)
#cv2.imwrite("resized.jpg", img3)

img4 = cv2.imread('resized.jpg')

# configurations
config = ('-l eng --oem 1 --psm 3')

# pytessercat
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(cropped, config=config)

# print text
text = text.split('\n')
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()



