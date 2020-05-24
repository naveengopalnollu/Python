import cv2
import numpy as np
img = cv2.imread("Resources/text3.jpeg")
kernal = np.ones((5,5),np.uint8)
"""
#COnverting image to Grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)
cv2.waitKey(0)
"""
#Converting image to Blur
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img,150,200)
imgDilation = cv2.dilate(imgCanny,kernal,iterations=1)
imgErode = cv2.erode(imgDilation,kernal,iterations=1)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilation Image",imgDilation)
cv2.imshow("Eroded Image",imgErode)
cv2.waitKey(0)

