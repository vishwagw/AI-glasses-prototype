# sample code for object detection:
import cv2
from picamera2 import Picamera2

# Camera initialzation
picam = Picamera2()
picam.start()
# detection dataset model
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'model.caffemodel')

# while loop
while True:
    frame = picam.capture_array()
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype('int')
            label = f'Object: {confidence*100:.2f}%'
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, label, (startX, startY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
