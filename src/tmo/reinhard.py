from .util import logmean
from util import apply_gamma, luminance, change_luminance

def reinhard(img, a=0.18):
    """
    Do reinhard global tonemapping operation on image. 
    """

    # find luminance map
    l = luminance(img)
    # then find key of image
    key = logmean(l)
    # scale such that the key is equal to a
    scaled = a/key * l
    # apply the curve
    l_d = scaled / (1 + scaled)
    # change the luminance of image and apply gamma
    img_t = change_luminance(img, l, l_d)
    img_t /= img_t.max()
    return apply_gamma(img_t)