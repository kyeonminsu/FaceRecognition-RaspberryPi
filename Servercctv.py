import cv2
import imagezmq
import numpy as np
import os

image_hub = imagezmq.ImageHub()
recognizer= cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None', 'minsu']
cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
print("Start!!")

while True:
    rpi_name,img = image_hub.recv_image()
    img = cv2.flip(img, 1) # Flip vertically
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            id = names[1]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow(rpi_name, img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    
    image_hub.send_reply(b'OK')
    
print("END")
cam.release()
cv2.destroyAllWindows()