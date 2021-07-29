import cv2
import numpy as np
import imagezmq

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
image_hub = imagezmq.ImageHub()

print("Start!!")
while True:
    rpi_name,image = image_hub.recv_image()
    
    image = cv2.flip(image, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30,30)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=10,
            minSize=(5,5),
        )
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex + ew, ey + eh), (0,255,0), 2)
            
    cv2.putText(image, "Server", (30,30), font, 1, (255,100,100), 2)
    cv2.imshow(rpi_name, image)

    
    if cv2.waitKey(1) == ord('q'):
        break
    
    image_hub.send_reply(b'OK')

print("END")
cv2.destroyAllWindows()

