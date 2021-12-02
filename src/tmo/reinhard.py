from .util import logmean
from util import apply_gamma, luminance, change_luminance
import numpy as np

def reinhard(img, a=0.18):
    l = luminance(img)
    key = logmean(l)
    scaled = a/key * l
    l_d = scaled / (1 + scaled)
    img_t = change_luminance(img, l, l_d)
    img_t /= img_t.max()
    return apply_gamma(img_t)