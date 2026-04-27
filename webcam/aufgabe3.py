import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('cannot access to the camera')
    exit()
# while True:
#     ret, frame = cap.read()
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
#     cv2.imshow('Camera', gray_frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

def drawHistogram(gray_image):
    histogram = [0] * 256
    for i in range(gray_image.shape[0]): # Loop through each row of the image
        for j in range(gray_image.shape[1]): # Loop through each pixel in the image
            pixel_value = gray_image[i, j] # Get the pixel value (0-255)
            histogram[pixel_value] += 1 # Increment the count for this pixel value
    return histogram

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    histogram = drawHistogram(gray_frame)
    
    print(histogram)
    cv2.imshow('Camera', gray_frame)
    if cv2.waitKey(1) == ord('q'):
        break