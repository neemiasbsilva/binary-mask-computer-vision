import numpy as np
import cv2

def binary_mask(path, r, g, b, k):
    # read the image
    img = cv2.imread(path)
    print(img.shape)
    # convert the channels of image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_binary = img[:,:,0] * r + img[:,:,1] * g + img[:,:,2] * b

    img_binary = img_binary > k

    img_binary = np.uint8(img_binary)
    img_binary *= 255

    return img, img_binary


