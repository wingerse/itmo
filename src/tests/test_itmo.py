import include_parent_path
from itmo import linear, fhdr
from tmo import drago
from tmo.reinhard import reinhard
from util import apply_gamma, load_hdr_image, luminance, save_hdr_image, save_ldr_image, load_ldr_image
from skimage.metrics import structural_similarity
import numpy as np
import pytest
import math

def test_linear_itmo():
    ldr = np.array([[[0.0, 0.5, 1.0]]])
    l = luminance(ldr)
    print(l)
    ldr = apply_gamma(ldr)
    hdr = linear(ldr, k=100)

    # check if luminance is scaled to 100
    assert luminance(hdr) - 100 * l <= 0.0000000001

# 661, 993
def test_fhdr_bright():
    # check bright image
    ldr = load_ldr_image("datasets/testing_data_ours/ldr/27.jpg")
    gt = load_hdr_image("datasets/testing_data_ours/hdr/27.hdr")
    print(gt.max())
    hdr = fhdr(ldr, f"src/itmo/fhdr/checkpoints/ours.ckpt")
    print(hdr.max())

    save_ldr_image(ldr, "test_outputs/fhdr_ldr.png")
    save_ldr_image(drago(gt), "test_outputs/fhdr_gt.png")
    save_ldr_image(drago(hdr), "test_outputs/fhdr_hdr.png")


    ssim = structural_similarity(hdr, gt, channel_axis=2)
    print(ssim)