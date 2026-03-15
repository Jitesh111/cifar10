#import socket
#import pickle
#import cv2
from os import path
import requests as req


#cap = cv2.VideoCapture(0)


#if (true):
#ret, frame = cap.read()
#cv2.imwrite('temp.jpg', frame)
url = 'http://localhost:5000/predict'
with open('truck.jpeg', 'rb') as f:
    files = {'image': f}
    r = req.post(url, files=files)
    print(r.text)