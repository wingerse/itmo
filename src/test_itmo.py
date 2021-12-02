from itmo import linear
from tmo import reinhard
from util import change_luminance, luminance, save_hdr_image, save_ldr_image, load_ldr_image, load_hdr_image, remove_gamma, apply_gamma
import numpy as np

ldr = load_ldr_image("../images/ldr_test3.jpg")
hdr = linear(ldr)
save_hdr_image(hdr, "gen_linear.hdr")
print(hdr.min(), hdr.max())

tmo = reinhard(hdr, 0.18)
save_ldr_image(tmo, "gen_linear.jpg")
