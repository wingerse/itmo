import include_parent_path
from itmo import linear, fhdr
from tmo import drago
from tmo.reinhard import reinhard
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
from skimage.metrics import structural_similarity
import numpy as np
import pytest

# 661, 993
def test_fhdr():
    ldr = load_ldr_image("datasets/testing_data_ours/ldr/355.jpg")
    gt = load_hdr_image("datasets/testing_data_ours/hdr/355.hdr")
    hdr = fhdr(ldr, f"src/itmo/fhdr/checkpoints/ours_l1.ckpt")

    save_ldr_image(ldr, "test_outputs/fhdr_ldr.png")
    save_ldr_image(drago(gt), "test_outputs/fhdr_gt.png")
    save_ldr_image(drago(hdr), "test_outputs/fhdr_hdr.png")

    ssim = structural_similarity(hdr, gt, channel_axis=2)
    print(ssim)