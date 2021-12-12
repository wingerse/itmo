from itmo import linear, fhdr
from tmo import reinhard
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np

ldr = load_ldr_image("../images/ldr_test.png")
gt = load_hdr_image("../images/hdr_test.hdr")
hdr, psnr, ssim = fhdr(ldr, gt, "itmo/fhdr/checkpoints/FHDR-iter-2.ckpt", iteration_count=2)
save_hdr_image(hdr, "test_output/fhdr.hdr")
hdr_t = reinhard(hdr)
save_ldr_image(hdr_t, "test_output/fhdr.jpg")
print(psnr, ssim)