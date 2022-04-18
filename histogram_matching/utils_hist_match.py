import cv2
import numpy as np
from skimage.exposure import cumulative_distribution
# cdf
def cdf(im):
    c, b = cumulative_distribution(im)
    for i in range(b[0]):
        c = np.insert(c, 0, 0)
    for i in range(b[-1]+1, 256):
        c = np.append(c, 1)
    return c

# matching
def hist_matching(c, c_t, im):
    b = np.interp(c, c_t, np.arange(256))
    pix_repl = {i:b[i] for i in range(256)}
    mp = np.arange(0, 256)
    for (k, v) in pix_repl.items():
        mp[k] = v
    s = im.shape
    im = np.reshape(mp[im.ravel()], im.shape)
    im = np.reshape(im, s)
    return im.astype(np.uint8)

def get_historgram_matching(main_image, sub_image):
    
    ###### resize img for matching
    # get main img height, width
    main_img = main_image
    sub_img = sub_image
    main_height = main_img.shape[0]
    main_width = main_img.shape[1]
    sub_resized = cv2.resize(sub_img, (main_height, main_width))
   
    # calculate cdf of each color channel
    cdf_main_r = cdf(main_img[:, :, 0])
    cdf_main_g = cdf(main_img[:, :, 1])
    cdf_main_b = cdf(main_img[:, :, 2])

    cdf_sub_r = cdf(sub_resized[:, :, 0])
    cdf_sub_g = cdf(sub_resized[:, :, 1])
    cdf_sub_b = cdf(sub_resized[:, :, 2])

    # matching histogram of each color channel
    img_result = np.zeros((main_height, main_width, 3), dtype=np.uint8) 

    img_result[:,:,0] = hist_matching(cdf_main_r, cdf_sub_r, main_img[:, :, 0])
    img_result[:,:,1] = hist_matching(cdf_main_g, cdf_sub_g, main_img[:, :, 1])
    img_result[:,:,2] = hist_matching(cdf_main_b, cdf_sub_b, main_img[:, :, 2])   

    return img_result