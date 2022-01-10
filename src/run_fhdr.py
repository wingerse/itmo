from itmo import fhdr
from tmo.drago import drago
from util import load_ldr_image, save_hdr_image, save_ldr_image

def run_fhdr(ldr_path, hdr_path):
    """
    Run FHDR on the image given, and output HDR image and tone mapped HDR image. 
    Tonemapped HDR image will be saved to the same output path but with jpg extension.
    :param ldr_path: Path of the ldr image.
    :param hdr_path: Path of the output HDR image. 
    """

    ldr = load_ldr_image(ldr_path)
    hdr = fhdr(ldr)
    hdr_tmo = drago(hdr)
    save_hdr_image(hdr, hdr_path)
    save_ldr_image(hdr_tmo, hdr_path.replace(".hdr", ".jpg"))
