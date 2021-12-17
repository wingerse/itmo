from itmo import linear, fhdr
from tmo import drago
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
from matplotlib import pyplot as plt

ldr = load_ldr_image("../datasets/aug_dataset_test/ldr/000009.jpg")
gt = load_hdr_image("../datasets/aug_dataset_test/hdr/000009.hdr")
hdr, psnr, ssim = fhdr(ldr, gt, f"itmo/fhdr/checkpoints/FHDR-iter-2.ckpt", iteration_count=2)
save_hdr_image(hdr, "test_output/fhdr.hdr")
hdr_t = drago(hdr)
save_ldr_image(hdr_t, "test_output/fhdr.jpg")
print(psnr, ssim)