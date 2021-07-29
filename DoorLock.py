import DoorLockClass
import RPi.GPIO as IoPort
import time
import threading
import cv2
import numpy as np
import os
import imagezmq
import socket
from imutils.video import VideoStream

def Nunber_ONE(c):
    data=1
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()
    
def Nunber_TWO(c):
    data=2
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()
    
def Nunber_THREE(c):
    data=3
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()
    
def Nunber_FOUR(c):
    data=4
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()
    
def Nunber_FIVE(c):
    data=5
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()

def Nunber_SIX(c):
    data=6
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()

def Nunber_SEVEN(c):
    data=7
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()

def Nunber_EIGHT(c):
    data=8
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()

def Nunber_NINE(c):
    data=9
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()

def Nunber_STAR(c):
    data='Q'
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()

def Nunber_ZERO(c):
    data=0
    clsDoor.NumberLock(data)
    clsDoor.BuzzerNumber()

def Nunber_SHOP(c):
    clsDoor.BuzzerNumber()
    face=threading.Thread(target=face_recognition,args=())    
    face.start()
    
def END(c):
    global end
    end=1

def face_recognition():
    print("face_recognition program Start!!")
    recognizer= cv2.face.createLBPHFaceRecognizer()
    recognizer.load('trainer/trainer.yml')
    cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    global x
    global y
    global h
    global confidence
    id = 0    
    names = ['None', 'minsu']   
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) 
    cam.set(4, 480) 

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    count=0
    count2=0
    end=0
    while True:
        ret, img =cam.read()
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
            if (confidence < 80):
               
                count=count+1
                    
                id = names[1]
                confidence = "  {0}%".format(round(80 - confidence))
                
                if(count==20):
                    print("The door is open")
                    clsDoor.BuzzerOpen()
                    end=1
                    break
            else:
                id = "unknown"
                count2=count2+1
                if(count2==20):
                    print("UnKnown user!!")
                    end=1
                    clsDoor.BuzzerClose()
                    break
                
                confidence = "  {0}%".format(round(80 - confidence))
        if(end==1):
            break
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, "Client", (x+150,y+150), font, 1, (255,100,100), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        
    
        cv2.imshow('Cliant',img) 
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    print("Face recognition program was finished")
    cam.release()
    cv2.destroyAllWindows()    
 
'''      
def realtime_cctv():
    global stop_thread
    print("Real Time CCTV Start!!")
    sender = imagezmq.ImageSender(connect_to='tcp://127.0.0.1:5555')
    rpi_name = socket.gethostname()
    picam = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    
    while True:
        if stop_thread:
            print("Real Time CCTV END")
            break
        image = picam.read()
        sender.send_image(rpi_name, image)
'''      

IoPort.setwarnings(False)
sw=[2,3,4,17,27,22,10,9,11,13,19,26,15]
IoPort.setmode(IoPort.BCM)
IoPort.setup(sw[0], IoPort.IN)
IoPort.setup(sw[1], IoPort.IN)
IoPort.setup(sw[2], IoPort.IN)
IoPort.setup(sw[3], IoPort.IN)
IoPort.setup(sw[4], IoPort.IN)
IoPort.setup(sw[5], IoPort.IN)
IoPort.setup(sw[6], IoPort.IN)
IoPort.setup(sw[7], IoPort.IN)
IoPort.setup(sw[8], IoPort.IN)
IoPort.setup(sw[9], IoPort.IN) #*
IoPort.setup(sw[10], IoPort.IN)
IoPort.setup(sw[11], IoPort.IN) ##
IoPort.setup(sw[12], IoPort.IN) #end

print("Start!!")
number=int(input("Please enter initial password: "))

clsDoor = DoorLockClass.doorlock()
clsDoor.NumberProcessing(number)

IoPort.add_event_detect(sw[0],IoPort.FALLING,callback=Nunber_ONE,bouncetime=200)
IoPort.add_event_detect(sw[1],IoPort.FALLING,callback=Nunber_TWO,bouncetime=200)
IoPort.add_event_detect(sw[2],IoPort.FALLING,callback=Nunber_THREE,bouncetime=200)
IoPort.add_event_detect(sw[3],IoPort.FALLING,callback=Nunber_FOUR,bouncetime=200)
IoPort.add_event_detect(sw[4],IoPort.FALLING,callback=Nunber_FIVE,bouncetime=200)
IoPort.add_event_detect(sw[5],IoPort.FALLING,callback=Nunber_SIX,bouncetime=200)
IoPort.add_event_detect(sw[6],IoPort.FALLING,callback=Nunber_SEVEN,bouncetime=200)
IoPort.add_event_detect(sw[7],IoPort.FALLING,callback=Nunber_EIGHT,bouncetime=200)
IoPort.add_event_detect(sw[8],IoPort.FALLING,callback=Nunber_NINE,bouncetime=200)
IoPort.add_event_detect(sw[9],IoPort.FALLING,callback=Nunber_STAR,bouncetime=200) #*
IoPort.add_event_detect(sw[10],IoPort.FALLING,callback=Nunber_ZERO,bouncetime=200)
IoPort.add_event_detect(sw[11],IoPort.FALLING,callback=Nunber_SHOP,bouncetime=200) ##
IoPort.add_event_detect(sw[12],IoPort.FALLING,callback=END,bouncetime=200) #end

end=0
x=0
y=0
h=0
confidence=0
stop_thread=False

#sender = imagezmq.ImageSender(connect_to='tcp://127.0.0.1:5555')
#rpi_name = socket.gethostname()
#picam = VideoStream(usePiCamera=True).start()
#cctv=threading.Thread(target=realtime_cctv,args=())    
#cctv.start()
while True:
    if(end==1):
        #stop_thread=True
        break
    #print("tset")
    #image = picam.read()
    #sender.send_image(rpi_name, image)
    
print("END")
IoPort.cleanup()