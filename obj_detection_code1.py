# sample code for object detection:
import cv2
from picamera2 import Picamera2

picam = Picamera2()
picam.start()
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'model.caffemodel')
