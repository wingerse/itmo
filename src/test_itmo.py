from itmo import linear, fhdr
from tmo import drago
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np

ldr = load_ldr_image("../images/ldr_test3.jpg")
gt = load_hdr_image("../images/hdr_test3.hdr")
hdr, psnr, ssim = fhdr(ldr, gt, "itmo/fhdr/checkpoints/latest.ckpt", iteration_count=2)
save_hdr_image(hdr, "test_output/fhdr.hdr")
hdr_t = drago(hdr)
save_ldr_image(hdr_t, "test_output/fhdr.jpg")
print(psnr, ssim)