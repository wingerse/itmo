import include_parent_path
from itmo import fhdr
from util import load_ldr_image, load_hdr_image, save_ldr_image
from tmo import reinhard

if __name__ == "__main__":
    ldr = load_ldr_image("test_images/ldr_test3.jpg")
    hdr = load_hdr_image("test_images/hdr_test3.hdr")

    generated, psnr, ssim = fhdr(
        ldr, 
        hdr,
        "src/itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")

    print(generated.min(), generated.max())
    print(f"PSNR={psnr}, SSIM={ssim}")
    save_ldr_image(reinhard(generated), "test_outputs/gen_fhdr.png")
