import cv2
img = cv2.imread("Resources/cars1.jpg")#reading an image

imgResize=cv2.resize(img,(300,200))

imgCrop = img[0:1050,0:1500]
cv2.imshow("Output crop",imgCrop) #Showing an Image
#cv2.imshow("Outpt",img) #Showing an Image
#cv2.imshow("Output",imgResize) #Showing an Image
cv2.waitKey(0) #waiting for milliseconds

#cropping an image
