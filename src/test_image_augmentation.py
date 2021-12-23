from image_augmentation import change_exposure, crf
from tmo import drago
from util import apply_gamma, load_hdr_image, save_ldr_image
import numpy as np

hdr = load_hdr_image("../images/Apartment_float_o15C.hdr")
save_ldr_image(drago(hdr), "test_output/aug_reference.jpg")
ldr = change_exposure(hdr, True)
ldr = crf(ldr)
ldr = apply_gamma(ldr)
save_ldr_image(ldr, "test_output/aug_oversaturated.jpg")

ldr_bright_mask = ldr.copy()
ldr_bright_mask[np.all(ldr_bright_mask >= 1, axis=2)] = np.array([1, 0, 0]).astype(np.float32)
save_ldr_image(ldr_bright_mask, "test_output/aug_oversaturated_mask.jpg")

ldr = change_exposure(hdr, False)
ldr = crf(ldr)
ldr = apply_gamma(ldr)
save_ldr_image(ldr, "test_output/aug_undersaturated.jpg")

ldr_dark_mask = ldr.copy()
ldr_dark_mask[np.all(ldr_dark_mask <= 0, axis=2)] = np.array([1, 0, 0]).astype(np.float32)
save_ldr_image(ldr_dark_mask, "test_output/aug_undersaturated_mask.jpg")