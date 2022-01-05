from itmo import linear, fhdr
from tmo import drago
from tmo.reinhard import reinhard
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np

ldr = load_ldr_image("../datasets/testing_data_ours/ldr/126.jpg")

hdr = fhdr(ldr, f"itmo/fhdr/checkpoints/ours_l1.ckpt")
save_hdr_image(hdr, "test_output/fhdr.hdr")

hdr_t = reinhard(hdr)
save_ldr_image(hdr_t, "test_output/fhdr.png")