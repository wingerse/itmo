import numpy as np

def mu_tonemap(img):
    """
    Tonemap the hdr image according to mu law
    """

    MU = 5000.0
    return np.log(1.0 + MU * (img + 1.0) / 2.0) / np.log(1.0 + MU)
