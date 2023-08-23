import cv2 


img = cv2.imread("../image/00-puppy.jpg")


while True:
   cv2.imshow("Puppy",img)

   # if we waited at least 1 milisecond  & we pressed the escape key
   if cv2.waitKey(1) & 0xFF==27:
      break 

# cv2.waitKey()
cv2.destroyAllWindows()