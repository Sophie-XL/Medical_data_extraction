# Create a function to preprocess images
import numpy as np
import cv2
from PIL import Image

def preprocess_image(img):
    # 1. Convert color images to grayscale
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    # 2. Enlarge the image to get better contrast: increase size by 1.5 times and use linear interpolation to fill in the gaps
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    # 3. Apply adaptive thresholding to enhance image contrast
    processed_image = cv2.adaptiveThreshold(
                    resized, 255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY,
                    61,
                    11
                    )
    return processed_image