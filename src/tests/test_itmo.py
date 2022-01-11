import include_parent_path
from itmo import linear, fhdr
from itmo.fhdr.test import test
from tmo import drago, mu_tonemap
from tmo.reinhard import reinhard
from util import apply_gamma, load_hdr_image, luminance, save_hdr_image, save_ldr_image, load_ldr_image
from skimage.metrics import structural_similarity
from quality import metrics
import numpy as np
import os

def test_linear_itmo():
    ldr = np.array([[[0.0, 0.5, 1.0]]])
    l = luminance(ldr)
    ldr = apply_gamma(ldr)
    hdr = linear(ldr, k=100)

    # check if luminance is scaled to 100
    assert luminance(hdr) - 100 * l <= 0.0000000001
    # has correct shape
    assert hdr.shape == ldr.shape

def _test_fhdr(img_number):
    # load ldr images and do linear and fhdr itmos
    ldr = load_ldr_image(f"datasets/testing_data_ours/ldr/{img_number}.jpg")
    gt = load_hdr_image(f"datasets/testing_data_ours/hdr/{img_number}.hdr")
    hdr = fhdr(ldr)
    hdr_linear = linear(ldr)

    gt_t = mu_tonemap(gt)
    hdr_t = mu_tonemap(hdr)
    hdr_linear_t = mu_tonemap(hdr_linear)

    # correct dimensions
    assert hdr.shape == gt.shape
    # generated hdr gives higher scores than ldr
    assert metrics.psnr(hdr_t, gt_t) > metrics.psnr(ldr, gt_t)
    # is better than linear itmo
    assert metrics.psnr(hdr_t, gt_t) > metrics.psnr(hdr_linear_t, gt_t)

    n_unique_hdr = len(np.unique(hdr))
    n_unique_gt = len(np.unique(gt))
    n_unique_ldr = len(np.unique(ldr))

    # number of unique pixel values (dynamic range) have increased
    assert n_unique_hdr > n_unique_ldr

    # number of unique pixel values (dynamic range) of hdr is closer to ground truth than the ldr
    assert abs(n_unique_hdr - n_unique_gt) < abs(n_unique_hdr - n_unique_ldr)

def test_fhdr_10_images():
    # test bright images
    _test_fhdr("27")   # fence and ground
    _test_fhdr("1207") # house and yard
    _test_fhdr("1951") # tree and wall
    _test_fhdr("3552") # sky
    _test_fhdr("3899") # building, sky and tree trunk
    # test dark images
    _test_fhdr("461")  # beach and water
    _test_fhdr("1313") # table leg and chair
    _test_fhdr("2353") # cars on a road
    _test_fhdr("2966") # person indoors
    _test_fhdr("3479") # sky, road, trees

def test_fhdr_test_difficult_image():
    _test_fhdr("4992") # a very dark image

def test_fhdr_all_images():
    imgs = os.listdir("datasets/testing_data_ours/ldr")
    fails = 0
    for img in imgs:
        try:
            _test_fhdr(img.split('.')[0])
        # only assertion failures are counted
        except AssertionError:
            print(img)
            fails += 1
    
    fail_percent = fails / len(imgs) * 100
    assert fail_percent <= 6

def test_fhdr_works_on_all_black():
    ldr = load_ldr_image("test_images/black.png")
    hdr = fhdr(ldr)

    save_ldr_image(drago(hdr), "test_outputs/black_hdr.jpg")

    # correct dimensions
    assert hdr.shape == ldr.shape

def test_fhdr_works_on_all_white():
    ldr = load_ldr_image("test_images/white.png")
    hdr = fhdr(ldr)

    save_ldr_image(drago(hdr), "test_outputs/white_hdr.jpg")

    # correct dimensions
    assert hdr.shape == ldr.shape

def test_fhdr_scores():
    psnr, ssim = test("src/itmo/fhdr/checkpoints/ours.ckpt", "datasets/testing_data_ours", "test_outputs/fhdr")
    # assert that scores are better than most existing non-machine learning itmos
    # and definitely better than score without itmo
    assert psnr > 20
    assert ssim > 0.60