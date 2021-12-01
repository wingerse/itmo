from .util import luminance, logmean, luminance, change_luminance
from util import apply_gamma

def reinhard(img, a=0.18):
    l = luminance(img)
    key = logmean(l)
    scaled = a/key * l
    l_d = scaled / (1 + scaled)
    return apply_gamma(change_luminance(img, l, l_d))