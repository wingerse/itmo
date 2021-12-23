from itmo import linear, fhdr
from tmo import drago
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
from matplotlib import pyplot as plt

ldr = load_ldr_image("../datasets/testing_data_ours/ldr/984.jpg")
gt = load_hdr_image("../datasets/testing_data_ours/hdr/984.hdr")

hdr, psnr, ssim = fhdr(ldr, gt, f"itmo/fhdr/checkpoints/FHDR-iter-1.ckpt", iteration_count=1)
hdr_t = drago(hdr)
save_ldr_image(hdr_t, "test_output/fhdr.png")
print(psnr, ssim)