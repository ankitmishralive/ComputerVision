

import cv2 
import numpy as np 

# -----------------------------------Function ----------------------------


def draw_Rectange(event,x,y,flags,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,center=(x,y),radius=100,color=(0,0,255),thickness=5)



# ----------------------------------------Showing the image --------------------------------

img = cv2.imread("../image/dog_backpack.jpg")

cv2.namedWindow(winname='dog')


cv2.setMouseCallback('dog',draw_Rectange)


while True:
    cv2.imshow('dog',img)

    if cv2.waitKey(1) & 0xFF == 27 :
        break 

cv2.destroyAllWindows() 