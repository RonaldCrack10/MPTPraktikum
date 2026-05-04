import cv2
import numpy as np
from scipy import signal


def processImage(frame):
    """
    Process the provided image (3-channel BGR) and calculate
    gradients in X and Y direction as well as the gradient magnitude.

    gx and gy shall contain the gradient direction image with values between -1 and +1
    grad shall contain the gradient magnitude image with values between 0 and 1

    :param frame: 3-channel BGR image (np.array)
    :return: 3-tupel (gx, gy, grad) containing the gradient image in X and Y direction as well as the gradient magnitude image (1-channel np.float32 images each).
    """
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_norm = np.float32(gray_frame / 255.0)
    gx = cv2.Sobel(gray_frame_norm, cv2.CV_32F, 1, 0, ksize = 3) / 4  # 1 to 0 because we want the gradient in x direction, ksize is the size of the kernel. y direction is 0 because we don't want the gradient in y direction
    # The division by 4 is necessary to scale the gradient values to be between -1 and +1, since the maximum possible value of the Sobel operator with a kernel size of 3 is 4.
    gy = cv2.Sobel(gray_frame_norm, cv2.CV_32F, 0, 1, ksize = 3) / 4 # 0 to 1 because we want the gradient in y direction, ksize is the size of the kernel. x direction is 0 because we don't want the gradient in x direction
    # grad = np.sqrt(gx ** 2 + gy ** 2) / np.sqrt(2)

    # Den Strukturtensor M vorbereiten
    Ix2 = gx ** 2
    Iy2 = gy ** 2
    Ix_Iy = gx * gy
    
    N = 7
    Ix2  = signal.convolve2d(Ix2, np.ones((N,N))) / (N**2)
    Iy2  = signal.convolve2d(Iy2, np.ones((N,N))) / (N**2)
    Ix_Iy = signal.convolve2d(Ix_Iy, np.ones((N,N))) / (N**2)

    kappa = 0.04
    det_M = Ix2 * Iy2 - Ix_Iy ** 2
    trace = Ix2  + Iy2
    strength = det_M - kappa * trace ** 2 
    strength /= np.max(strength)

    corners = np.zeros_like(strength)
    corners[strength > 0.1] = 1.0

    cv2.imshow("Harris Corner Strength", strength)
    cv2.imshow("Harris Corners", corners)
   


def displayImage(gx, gy, grad):
    """
    Apply appropriate scaling and display the provided images.

    :param gx: Gradient image in X-Direction (np.float32 image with values between -1 and +1)
    :param gy: Gradient image in Y-Direction (np.float32 image with values between -1 and +1)
    :param grad: Gradient magnitude image (np.float32 image with values between 0 and 1)
    """
    cv2.imshow('Gradient X', 0.5 * gx + 0.5)  # Scale the gradient in x direction to be between 0 and 1
    cv2.imshow('Gradient Y', 0.5 * gy + 0.5)  # Scale the gradient in y direction to be between 0 and 1
    cv2.imshow('Gradient Magnitude', grad) # The gradient magnitude is already between 0 and 1, so we can display it directly



def mainLoop():

    """
    The main loop of this program
    """
    # TODO: Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # TODO: Read next image from camera 
        
        ret, frame = cap.read()
        # TODO: Call processImage to retrieve properly scaled gradient direction and magnitude images
        processImage(frame= frame)

        # TODO: Call displayImage to display the images
        # displayImage(gx, gy, grad)
        # TODO: Also display the original camera image in color
        cv2.imshow('Camera', frame)
        # TODO: Break the infinite loop when the users presses ESCAPE (27)
        if cv2.waitKey(1) == 27:
             break
        

    # TODO: Release the capture and writer objects
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    mainLoop()

