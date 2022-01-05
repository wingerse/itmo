import numpy as np
from math import log, log10
from util import luminance, change_luminance, apply_gamma
from .util import logmean

def bias(b, t):
    """
    The bias function described in the paper
    """

    return t ** (log(b)/log(0.5))

def drago(img, l_dmax=100, b=0.85):
    """
    Do drago tonemapping on image.
    """

    # find luminance
    l = luminance(img)
    l_old = l
    # find and scale world average
    l_wa = logmean(l)
    l_wa = l_wa / ((1 + b - 0.85) ** 5)
    l_max = np.max(l)

    # scale luminance such that world average is 1
    l = l / l_wa
    l_max = l_max / l_wa

    # apply the curve
    p1 = (l_dmax * 0.01) / (log10(l_max+1))
    p2 = np.log(l + 1) / np.log(2 + (bias(b, l / l_max)) * 8)
    l_d = p1 * p2
    l_d = np.clip(l_d, 0, 1)

    # change luminance of the image and apply gamma curve
    img_t = change_luminance(img, l_old, l_d)
    img_t /= img_t.max()
    img_t = apply_gamma(img_t)

    return img_t