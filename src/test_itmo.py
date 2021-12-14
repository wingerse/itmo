from itmo import linear, fhdr
from tmo import drago
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image

ldr = load_ldr_image("../images/ldr_test4.jpg")
gt = load_hdr_image("../images/hdr_test4.hdr")
hdr, psnr, ssim = fhdr(ldr, gt, "itmo/fhdr/checkpoints/3.ckpt", iteration_count=1)
save_hdr_image(hdr, "test_output/fhdr.hdr")
hdr_t = drago(hdr)
save_ldr_image(hdr_t, "test_output/fhdr.jpg")
print(psnr, ssim)