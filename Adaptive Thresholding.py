import cv2
import numpy as np

img = cv2.imread("c:/samples/sudoku.png")

_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th2 = cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);
th3 = cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2);


cv2.imshow("Image",img_grey)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()

