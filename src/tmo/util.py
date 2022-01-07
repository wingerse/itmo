import numpy as np

eps = np.nextafter(0, 1, dtype=np.float32)

def logmean(img):
    """ 
    Geometric mean (logmean) of image.
    :param img: An image. 
    :return: logmean.
    """

    return np.exp(np.mean(np.log(img + eps)))