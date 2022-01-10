import include_parent_path
from itmo import linear, fhdr
from tmo import drago
from tmo.reinhard import reinhard
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np
import pytest
import os
from quality import metrics


# This file will test the whole algorithm together without the UI.

def test_whole_algorithm_together():
    """
    This function will load a valid ldr image, fhdr itmo with the latest checkpoint is being applied on that ldr image.
    Once the transformation is done, a generated hdr image is obtained.
    The generated hdr image is tone mapped to an ldr format to be able to display on a normal screen.
    Then we check if the coresponding files are created properly and then we calculate the psnr and ssim score
    to make sure that our generated model is better than the ldr image.
    """


    ldr = load_ldr_image("test_images/ldr_test.png")

    hdr = fhdr(ldr)    # applying fhdr itmo with latest checkpoint
    save_hdr_image(hdr, "test_outputs/fhdr.hdr")

    hdr_t = reinhard(hdr)
    save_ldr_image(hdr_t, "test_outputs/fhdr.png")
    assert os.path.isfile("test_outputs/fhdr.hdr") == True
    assert os.path.isfile("test_outputs/fhdr.png") == True

    gt_hdr = load_hdr_image("test_images/hdr_test.hdr")
    ground_truth_tmo = reinhard(gt_hdr)

    # checking if the tone mapped generated hdr image gives better scores than the original ldr image
    assert metrics.psnr(hdr_t, ground_truth_tmo) > metrics.psnr(ldr, ground_truth_tmo)
    assert metrics.ssim(hdr_t, ground_truth_tmo) > metrics.ssim(ldr, ground_truth_tmo)