import cv2

def get_historgram_equal(image):
    
    
    # split color channel
    B, G, R = cv2.split(image)

    # equalize image
    equalized_r = cv2.equalizeHist(R)
    equalized_g = cv2.equalizeHist(G)
    equalized_b = cv2.equalizeHist(B)

    # merge all channel
    equalized_image = cv2.merge((equalized_b, equalized_g, equalized_r))

    return equalized_image