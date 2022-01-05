from itmo import linear, fhdr
from tmo import drago
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
from matplotlib import pyplot as plt

ldr = load_ldr_image("../images/ldr_test.png")
gt = load_hdr_image("../images/hdr_test.hdr")

hdr, psnr, ssim = fhdr(ldr, gt, f"itmo/fhdr/checkpoints/epoch_17.ckpt", iteration_count=1)

hdr_t = drago(hdr)
save_ldr_image(hdr_t, "test_output/fhdr.png")
print(psnr, ssim)