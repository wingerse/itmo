"""This file will test the whole algorithm together without the UI."""

import include_parent_path
from itmo import linear, fhdr
from tmo import drago
from tmo.reinhard import reinhard
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np
import pytest
import os
from quality import metrics


def run_whole_algorithm_testing_dataset(img_number):
    """
    This function will load a valid ldr image from the testing dataset, fhdr itmo is being applied on that ldr image.
    Once the transformation is done, a generated hdr image is obtained.
    The generated hdr image is tone mapped to an ldr format to be able to display on a normal screen.
    Then we check if the coresponding files are created properly and then we calculate the psnr and ssim score
    to make sure that our generated model is better than the ldr image.
    """


    ldr = load_ldr_image(f"datasets/testing_data_ours/ldr/{img_number}.jpg")

    hdr = fhdr(ldr)    # applying fhdr itmo with latest checkpoint
    save_hdr_image(hdr,f"test_outputs/fhdr_{img_number}.hdr")

    hdr_tmo = reinhard(hdr)
    save_ldr_image(hdr_tmo, f"test_outputs/fhdr_tmo_{img_number}.png")
    
    assert os.path.isfile(f"test_outputs/fhdr_{img_number}.hdr") == True
    assert os.path.isfile(f"test_outputs/fhdr_tmo_{img_number}.png") == True

    gt_hdr = load_hdr_image(f"datasets/testing_data_ours/hdr/{img_number}.hdr")
    ground_truth_tmo = reinhard(gt_hdr)

    # checking if the tone mapped generated hdr image gives better scores than the original ldr image
    assert metrics.psnr(hdr_tmo, ground_truth_tmo) > metrics.psnr(ldr, ground_truth_tmo)
    assert metrics.ssim(hdr_tmo, ground_truth_tmo) > metrics.ssim(ldr, ground_truth_tmo)


def test_10_images_testing_dataset():
    # test bright images
    run_whole_algorithm_testing_dataset("27")   # fence and ground
    run_whole_algorithm_testing_dataset("1207") # house and yard
    run_whole_algorithm_testing_dataset("1951") # tree and wall
    run_whole_algorithm_testing_dataset("3552") # sky
    run_whole_algorithm_testing_dataset("3899") # building, sky and tree trunk
    
    # test dark images
    run_whole_algorithm_testing_dataset("461")  # beach and water
    run_whole_algorithm_testing_dataset("1313") # table leg and chair
    run_whole_algorithm_testing_dataset("2353") # cars on a road
    run_whole_algorithm_testing_dataset("2966") # person indoors
    run_whole_algorithm_testing_dataset("3479") # sky, road, trees


def run_whole_algorithm_real_images(img_number):
    """
    This function will load a real image, fhdr itmo is being applied on that ldr image.
    Once the transformation is done, a generated hdr image is obtained.
    The generated hdr image is tone mapped to an ldr format to be able to display on a normal screen.
    Then we check if the coresponding files are created properly. Metric scores cannot be calculated because we do not have their reference hdr image 
    """


    ldr = load_ldr_image(f"test_images/{img_number}.jpg")

    hdr = fhdr(ldr)    # applying fhdr itmo with latest checkpoint
    save_hdr_image(hdr,f"test_outputs/fhdr_real_image_{img_number}.hdr")

    hdr_tmo = reinhard(hdr)
    save_ldr_image(hdr_tmo, f"test_outputs/fhdr_tmo_real_image_{img_number}.png")
    
    assert os.path.isfile(f"test_outputs/fhdr_real_image_{img_number}.hdr") == True
    assert os.path.isfile(f"test_outputs/fhdr_tmo_real_image_{img_number}.png") == True

def test_3_real_images():
    run_whole_algorithm_real_images("real_image_4")
    run_whole_algorithm_real_images("real_image_5")
    run_whole_algorithm_real_images("real_image_6")