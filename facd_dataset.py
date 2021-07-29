import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
face_id=input('input user id: ')
print("wait")
count=0
while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count +=1
        #Save the captured image into the dataset folder
        cv2.imwrite("dataset/User."+str(face_id)+'.'+str(count)+".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)
        print(count)
        
    k = cv2.waitKey(100) & 0xff
    
    if k == 27:
        break
    elif count>=100:
        break

print("END")
cam.release()
cv2.destroyAllWindows()


