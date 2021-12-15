from itmo import linear, fhdr
from tmo import drago
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np

ldr = load_ldr_image("../images/ldr_test3.jpg")
hdr_linear = linear(ldr)
save_hdr_image(hdr_linear, "test_output/gen_linear.hdr")
gt = load_hdr_image("../images/hdr_test3.hdr")
hdr_fhdr, _, _ = fhdr(ldr, gt, "itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")
save_hdr_image(hdr_fhdr, "test_output/gen_fhdr.hdr")