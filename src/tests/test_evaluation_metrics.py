import include_parent_path
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image, luminance
from quality import metrics
import numpy as np
import pytest



def test_log_psnr():
    # testing log_psnr on a single pixel luminance. The log_psnr is calculated manually and compared to the implementation in the algorithm
    test_luminance = [[0.179]]
    reference_luminance = [[0.279]]
    assert metrics.log_psnr(test_luminance,reference_luminance) == 26.341259265210763

def test_log_psnr_same_images():
    # for same images, that is, images with same luminance, the mean square error will be 0 and log_psnr will take maximum value which is 100
    test_luminance = [[0.179]]
    reference_luminance = [[0.179]]
    assert metrics.log_psnr(test_luminance,reference_luminance) == 100

def test_psnr():
    # calculating psnr manually using one pixel and comparing it with the implementation in the algorithm
    test_image = np.array([[[0.1,0.2,0.3]]])
    reference_image = np.array([[[0.2,0.3,0.4]]])
    assert metrics.psnr(test_image, reference_image) == 20

def test_psnr_same_images():
    # same images will have the same pixel and then the mean square error will be 0. Thus the value will be maximum which is 100
    test_image = np.array([[[0.1,0.2,0.3]]])
    reference_image = np.array([[[0.1,0.2,0.3]]])
    assert metrics.log_psnr(test_image, reference_image) == 100

def test_ssim():
    # blackbox testing to test if there is a value generated for the ssim between 0 and 1
    test_image = load_ldr_image("test_images/generated_tmo.jpg")
    reference_image = load_ldr_image("test_images/gt_tmo.jpg")
    assert metrics.ssim(test_image, reference_image) < 1 and metrics.ssim(test_image, reference_image) > 0

def test_ssim_same_image():
    # ssim score for 2 same images will be 1.0
    test_image = load_ldr_image("test_images/gt_tmo.jpg")
    reference_image = load_ldr_image("test_images/gt_tmo.jpg")
    assert metrics.ssim(test_image, reference_image) == 1.0