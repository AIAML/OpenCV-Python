import cv2
import numpy as np

img = cv2.imread('c:/samples/shapes.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, trash = cv2.threshold(gray, 200, 255,cv2.THRESH_BINARY)

contors, _ = cv2.findContours(trash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for c in contors:
    approx = cv2.approxPolyDP(c,0.01 * cv2.arcLength(c,True),True)
    cv2.drawContours(img,[approx],0,(0,255,0),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv2.putText(img,"triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0))
    elif len(approx) == 4:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, "pentagone", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    else :
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
