from tmo.reinhard import reinhard
from util import load_hdr_image, save_ldr_image

hdr = load_hdr_image("../images/Oxford_Church.hdr")
print(hdr.min(), hdr.max())
ldr = reinhard(hdr, 0.18)
save_ldr_image(ldr, "tmo.jpg")