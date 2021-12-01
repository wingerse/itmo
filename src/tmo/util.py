import numpy as np

def luminance(img):
    """ luminance map of image """
    return 0.27*img[..., 0] + 0.67*img[..., 1] + 0.06*img[..., 2]

def logmean(img):
    """ geometric mean (logmean) of image """
    eps = np.nextafter(0, 1)
    return np.exp(np.mean(np.log(img + eps)))

def change_luminance(img, old_l, new_l):
    """ change luminance of image given old and new luminance maps """
    img = img.copy()
    for i in range(0, 3):
        img[..., i] = img[..., i] / old_l * new_l
    return img
