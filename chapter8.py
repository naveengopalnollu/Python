import cv2
import numpy as np
import ImageStackfun as stfun

def getContours(img):
    countours,Hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area>200:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(len(approx))
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCorners ==3: ObjectType="Triangle"
            elif objCorners == 4:
                aspectRatio = w/float(h)
                if aspectRatio>0.95 and  aspectRatio<1.05:
                    ObjectType="Square"
                else:
                    ObjectType="Rectange"
            else : ObjectType="None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(imgContour,ObjectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)


path = 'Resources/shape1.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)
imgStack = stfun.stackImages(0.8,([img,imgGray,imgBlur],
                             [imgCanny,imgContour,imgBlank]))

cv2.imshow("Image",imgStack)
cv2.waitKey(0)