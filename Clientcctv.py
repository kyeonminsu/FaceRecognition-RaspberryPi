import imagezmq
import socket
import time
from imutils.video import VideoStream
import cv2

sender = imagezmq.ImageSender(connect_to='tcp://127.0.0.1:5555')

rpi_name = socket.gethostname()
font = cv2.FONT_HERSHEY_SIMPLEX
picam = VideoStream(usePiCamera=True).start()
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
print("Start")
while True:
    image = picam.read()
    #ret,image= cap.read()
    image = cv2.flip(image, 1) # Flip camera vertically
    sender.send_image(rpi_name, image)
    
    cv2.putText(image, "Client", (30,30), font, 1, (255,100,100), 2)
    cv2.imshow(rpi_name, image)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    
print("END")
#cap.release()
cv2.destroyAllWindows()
