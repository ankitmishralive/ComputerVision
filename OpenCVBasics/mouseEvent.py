import cv2 
import numpy as np 

### Function 
def drawCircle(event,x,y,flags,param):
     if event ==cv2.EVENT_LBUTTONDOWN:
         cv2.circle(img,(x,y),radius=100,color=(255,0,0),thickness=-1)


     

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',drawCircle)


## Showing Images with OpenCV 
img= np.zeros((512,512,3))

while True:
    cv2.imshow('my_drawing',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break 

cv2.destroyAllWindows()


