import cv2 
import numpy as np 

# read an image 
img = cv2.imread("image/fruits.jpg")

# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img)

img[:,:,2]=0

cv2.imshow("window",img)
# cv2.imshow("window",img_gray)

cv2.waitKey(0)