import cv2
import sys
# Load the cascade
#face_cascade = cv2.CascadeClassifier('..SET THE Correct Directory...../haarcascade_frontalface_alt2.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#out = cv2.VideoWriter("output.avi",fourcc,20,(1280,528))
# it must be noted that original size of video must be written correctly because it is not shown in video player
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 34), 1,1)


        cv2.imshow("Test",frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()




