import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
 #   cv2.imshow("frame",frame)
    
    flower_img = frame
    hsv_img=cv2.cvtColor(flower_img,cv2.COLOR_BGR2HSV)
#hsv_img[0:30,0:30]=hsv_img[370:400,370:400]
#    print(hsv_img[0:30,0:30])
    lower_red=np.array([110,100,0])
    upper_red=np.array([210,200,255])
    mask=cv2.inRange(hsv_img,lower_red,upper_red)
    mask=~mask
#cv2.imshow('mask',mask)
    kernel = np.ones((6,6),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    kernel = np.ones((20,20),np.uint8)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    cv2.imshow('yumi',dilation)
    
    contours,h = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    print(contours)
    frame = cv2.drawContours(frame, contours, -1, (255,255,0), 3)
    cnt = contours[0]
    M = cv2.moments(cnt)
    print(M)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print(cx,cy)
    cv2.circle(frame,(cx,cy),5,(255,0,0),-1)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()

