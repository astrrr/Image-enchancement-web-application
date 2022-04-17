import cv2
import numpy as np


def get_gamma_image(image, gamma):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    a = 1
    b = 0
    
    if gamma == '0.1':
        gm = 0.1
    elif gamma == '0.2':
        gm = 0.2
    elif gamma == '0.3':
        gm = 0.3
    elif gamma == '0.4':
        gm = 0.4
    elif gamma == '0.5':
        gm = 0.5
    elif gamma == '0.6':
        gm = 0.6
    elif gamma == '0.7':
        gm = 0.7
    elif gamma == '0.8':
        gm = 0.8
    elif gamma == '0.9':
        gm = 0.9
    elif gamma == '1.0':
        gm = 1.0
    im_gamma = (a * ((img/255)**gm) + b) * 255
    im_gamma = im_gamma.astype(np.uint8)
    return im_gamma