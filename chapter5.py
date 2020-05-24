#cv2 = computer vison
import cv2
import numpy as np
#Code for reading and viewing an image using python

img = cv2.imread("Resources/cards1.png")#reading an image
width,height=250,350
pts1=np.float32([[111,219],[287,188],[54,182],[352,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
immgOut=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Output",immgOut ) #Showing an Image
cv2.waitKey(5000) #waiting for milliseconds







