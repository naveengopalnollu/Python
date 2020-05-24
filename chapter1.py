#cv2 = computer vison
import cv2
"""
#Code for reading and viewing an image using python
print('package Imported')
img = cv2.imread("Resources/text3.jpeg")#reading an image
cv2.imshow("Output",img) #Showing an Image
cv2.waitKey(5000) #waiting for milliseconds
"""
"""
#Code for reading and viewing Video
cap = cv2.VideoCapture("Resources/testvideo1.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""
#Code for reading and viewing WebCam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,1000)
while True:
    success, img = cap.read()
    cv2.imshow("",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break







