import include_parent_path
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image, luminance
from quality import evaluation_metric
import numpy as np
import pytest


def test_one_pixel_luminance():
    assert luminance(np.array([[[0.1,0.2,0.3]]])) == [[0.179]]
    assert luminance(np.array([[[0.2, 0.3, 0.4]]])) == [[0.279]]


def test_four_pixel_luminance():
    # testing on (2,2,3) dimension
    assert (luminance(np.array([[[0.1, 0.2, 0.3],[0.1, 0.2, 0.3]],[[0.1, 0.2, 0.3],[0.1, 0.2, 0.3]]])) == [[0.179, 0.179],[0.179, 0.179]]).all() == True


def test_log_psnr():
    test_luminance = [[0.179]]
    reference_luminance = [[0.279]]
    assert evaluation_metric.log_psnr(test_luminance,reference_luminance) == 13.170629632605381

def test_log_psnr_same_images():
    test_luminance = [[0.179]]
    reference_luminance = [[0.179]]
    assert evaluation_metric.log_psnr(test_luminance,reference_luminance) == 100

def test_psnr():
    test_image = np.array([[[0.1,0.2,0.3]]])
    reference_image = np.array([[[0.2,0.3,0.4]]])
    assert evaluation_metric.psnr(test_image, reference_image) == 20

def test_psnr_same_images():
    test_image = np.array([[[0.1,0.2,0.3]]])
    reference_image = np.array([[[0.1,0.2,0.3]]])
    assert evaluation_metric.log_psnr(test_image, reference_image) == 100

def test_ssim():
    test_image = load_ldr_image("test_images/generated_tmo.jpg")
    reference_image = load_ldr_image("test_images/gt_tmo.jpg")
    assert evaluation_metric.ssim(test_image, reference_image) < 1 and evaluation_metric.ssim(test_image, reference_image) > 0

def test_ssim_same_image():
    test_image = load_ldr_image("test_images/gt_tmo.jpg")
    reference_image = load_ldr_image("test_images/gt_tmo.jpg")
    assert evaluation_metric.ssim(test_image, reference_image) == 1.0