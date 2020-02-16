import numpy as np
import cv2

def binary_mask(path, r, g, b, k):
    # read the image
    img = cv2.imread(img)
    # convert the channels of image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_b = img[:,:,0] * r + img[:,:,1] * g + img[:,:,2] * b

    img_b = img_b > k

    img_b = np.uint8(img_b)
    img_b *= 255

    return img_b


