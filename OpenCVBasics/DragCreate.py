

import cv2 
import numpy as np 


# Variables 

drawing = False  # it will become True till Mouse  button will clicked & it will turn to false when button is not pressed 
ix = -1
iy = -1 
## for tracking 

# -----------------------------------Function ----------------------------


def draw_Rectange(event,x,y,flags,params):
    global ix,iy,drawing 

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True 
        ix,iy = x,y 

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,25,25),thickness = -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,0),thickness = -1)


# As their are 2 points that we have to track  1st Point Where we have Clicked the Mouse Button that is our ix & iy 
# & 2nd point is where we have ended up pressing the Mouse Button that is our x & y the cursor spot.





# ----------------------------------------Showing the image --------------------------------

img = np.zeros((512,512,3))

cv2.namedWindow(winname='drag_create')


cv2.setMouseCallback('drag_create',draw_Rectange)


while True:
    cv2.imshow('drag_create',img)

    if cv2.waitKey(1) & 0xFF == 27 :
        break 

cv2.destroyAllWindows() 