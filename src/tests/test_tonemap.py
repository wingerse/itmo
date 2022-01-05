import include_parent_path
from tmo import reinhard, drago
from util import load_hdr_image, save_ldr_image

def test_tonemap():
    hdr = load_hdr_image("datasets/aug_dataset/hdr/100.hdr")
    print(hdr.min(), hdr.max())
    tmo_reinhard = reinhard(hdr)
    save_ldr_image(tmo_reinhard, "test_outputs/tmo_reinhard.jpg")
    tmo_drago = drago(hdr)
    save_ldr_image(tmo_drago, "test_outputs/tmo_drago.jpg")