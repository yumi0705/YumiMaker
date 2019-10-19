import cv2
import numpy as np
import pyautogui as pg
import time
pic=pg.screenshot()
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
template = cv2.imread('xb.PNG')
(h, w )= template.shape[:2]
pg.moveTo(50,250)
pg.click()
time.sleep(1)
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.3
x=0
y=0
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    x=pt[0]
    y=pt[1]
print(x,y)
pg.moveTo(x+15,y+120)
time.sleep(1)
pg.mouseDown()
pg.moveTo(x-200,y+100)
pg.mouseUp()
#resimg=cv2.resize(img,(300,200))
#cv2.imshow("img",resimg)
cv2.waitKey()
cv2.destroyAllWindows()
