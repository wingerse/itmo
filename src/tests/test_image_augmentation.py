import include_parent_path
from image_augmentation import augment, change_exposure, crf, MIN_LOSS, MAX_LOSS
from tmo import drago
from util import apply_gamma, load_hdr_image, luminance, save_ldr_image
import numpy as np

def test_change_exposure():
    hdr = load_hdr_image("test_images/Apartment_float_o15C.hdr")
    save_ldr_image(drago(hdr), "test_outputs/aug_reference.jpg")
    ldr = change_exposure(hdr, True)
    loss_frac = np.count_nonzero(ldr >= 1)/ldr.size
    # check if oversaturated image loses the required fraction of image (within +- 1%)
    assert (MIN_LOSS-0.01) <= loss_frac <= (MAX_LOSS+0.01)

    ldr = crf(ldr)
    ldr = apply_gamma(ldr)
    save_ldr_image(ldr, "test_outputs/aug_oversaturated.jpg")

    ldr_bright_mask = ldr.copy()
    ldr_bright_mask[np.all(ldr_bright_mask >= 1, axis=2)] = np.array([1, 0, 0]).astype(np.float32)
    save_ldr_image(ldr_bright_mask, "test_outputs/aug_oversaturated_mask.jpg")

    ldr = change_exposure(hdr, False)
    loss_frac = np.count_nonzero(ldr <= 0)/ldr.size
    # check if undersaturated image loses the required fraction of image (within +- 1%)
    assert (MIN_LOSS-0.01) <= loss_frac <= (MAX_LOSS+0.01)

    ldr = crf(ldr)
    ldr = apply_gamma(ldr)
    save_ldr_image(ldr, "test_outputs/aug_undersaturated.jpg")

    ldr_dark_mask = ldr.copy()
    ldr_dark_mask[np.all(ldr_dark_mask <= 0, axis=2)] = np.array([1, 0, 0]).astype(np.float32)
    save_ldr_image(ldr_dark_mask, "test_outputs/aug_undersaturated_mask.jpg")

def test_augment():
    hdr = load_hdr_image("test_images/Apartment_float_o15C.hdr")
    ldr, hdr = augment(hdr, 256)
    # correct size
    assert ldr.shape[0] == 256 and ldr.shape[1] == 256 and \
        hdr.shape[0] == 256 and hdr.shape[1] == 256
    # is an ldr image
    assert (0 <= ldr).all() and (ldr <= 1).all()