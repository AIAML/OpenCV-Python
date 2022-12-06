import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#out = cv2.VideoWriter("output.avi",fourcc,20,(1280,528))
#set width video
cap.set(3,720)
#set height video
cap.set(4,720)

# it must be noted that original size of video must be written correctly because it is not shown in video player
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Test",gray)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()




