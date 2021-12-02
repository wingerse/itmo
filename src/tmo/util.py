import numpy as np

eps = np.nextafter(0, 1, dtype=np.float32)

def logmean(img):
    """ geometric mean (logmean) of image """
    return np.exp(np.mean(np.log(img + eps)))