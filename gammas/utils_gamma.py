import cv2
import numpy as np


def get_gamma_image(image, gamma, a, b):
    img = image
    new_a = float(a) 
    new_b = float(b)
    gm = float(gamma)
    im_gamma = (new_a * ((img/255)**gm) + new_b) * 255
    im_gamma = im_gamma.astype(np.uint8)
    return im_gamma