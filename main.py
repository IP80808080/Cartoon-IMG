import numpy as np
import cv2

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 5)

edge = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 10)

color = cv2.bilateralFilter(img, 4, 250, 250)

cartoon = cv2.bitwise_and(color, color, mask=edge)


cv2.imwrite('cartoon_image.jpg', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()