import imagezmq
import socket
import time
from imutils.video import VideoStream

sender = imagezmq.ImageSender(connect_to='tcp://127.0.0.1:5555')
rpi_name = socket.gethostname()
picam = VideoStream(usePiCamera=True).start()
print("Start")
time.sleep(2.0)

while True:
    image = picam.read()
    sender.send_image(rpi_name,image)