from itmo.fhdr.fhdr import fhdr
from util import load_image, save_hdr_image

generated, psnr, ssim = fhdr(
    load_image("./itmo/fhdr/dataset/test/LDR/ldr_ldr_184_data.jpg"), 
    load_image("./itmo/fhdr/dataset/test/HDR/real_ldr_184_data.hdr"),
    "./itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")

print(f"PSNR={psnr}, SSIM={ssim}")
print(generated.min(), generated.max())
save_hdr_image(generated, "gen.hdr")