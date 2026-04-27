# Helligkeit und Kontrast normalisieren
import cv2 
import numpy as np

def adjust_brightness(gray, brightness, contrast):

    mean, std = np.mean(gray), np.std(gray)
    normalized = brightness + contrast *(gray - mean) / std
    return np.clip(normalized, 0, 255).astype(np.uint8) # Clip the values to the valid range [0, 255] and convert to uint8 in order to display the image correctly else the image will be displayed as a black image    

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('cannot access to the camera')
    exit()

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    adjust_frame = adjust_brightness(gray_frame, brightness = 255, contrast= 5)
    cv2.imshow('Camera', adjust_frame)
    if cv2.waitKey(1) == ord('q'):

        break