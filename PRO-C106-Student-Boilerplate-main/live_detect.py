import cv2
facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera =cv2.VideoCapture(0)
while True:
    ret, frame=camera.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(grayscale,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1)==32):
        break