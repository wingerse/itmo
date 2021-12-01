from itmo.fhdr.fhdr import fhdr
from util import load_image, save_ldr_image
from tmo.reinhard import reinhard

generated, psnr, ssim = fhdr(
    load_image("../images/ldr_test3.jpg"), 
    load_image("../images/hdr_test3.hdr"),
    "./itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")

print(f"PSNR={psnr}, SSIM={ssim}")
save_ldr_image(reinhard(generated), "gen.png")