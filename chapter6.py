import cv2
import numpy as np

img=cv2.imread("Resources/text3.jpeg")
img=cv2.resize(img,(300,200))
imgHor=np.hstack((img,img))
imgVer=np.vstack((img,img))
cv2.imshow("Horizontal",imgVer)

cv2.waitKey(0)