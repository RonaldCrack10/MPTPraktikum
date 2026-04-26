import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('cannot access to the camera')
    exit()
while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    cv2.imshow('Camera', gray_frame)
    if cv2.waitKey(1) == ord('q'):
        break

def drawHistogram(gray_image):
    pass