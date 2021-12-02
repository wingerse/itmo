from itmo import fhdr
from util import load_ldr_image, load_hdr_image, save_ldr_image
from tmo import reinhard

ldr = load_ldr_image("../images/ldr_test3.jpg")
hdr = load_hdr_image("../images/hdr_test3.hdr")

generated, psnr, ssim = fhdr(
    ldr, 
    hdr,
    "./itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")

print(generated.min(), generated.max())
print(f"PSNR={psnr}, SSIM={ssim}")
save_ldr_image(reinhard(generated), "gen_fhdr.png")
