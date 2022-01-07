import math
from math import log10, sqrt
import imageio
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "../"))
from util import change_luminance, luminance, save_hdr_image, save_ldr_image, load_ldr_image, load_hdr_image, remove_gamma, apply_gamma,_save_image,_load_image
from quality import evaluation_metric



def main():
    test_image_hdr = load_hdr_image("test_images/generated_hdr.hdr")
    test_image_hdr_luminance = luminance(test_image_hdr)



    reference_image_hdr = load_hdr_image('test_images/gt_hdr.hdr')
    reference_image_hdr_luminance = luminance(reference_image_hdr)

    print(f"log PSNR value is {evaluation_metric.log_psnr(test_image_hdr_luminance, reference_image_hdr_luminance)} dB")

    # test_image_tonemapped = load_ldr_image('C:/Users/ASus/Documents/Final Year Project/latest fyp codes 5-01-21/fyp/test_images/generated_tmo.jpg')
    test_image_tonemapped = load_ldr_image('test_images/generated_tmo.jpg')
    # testImageTonemappedLuminance = util.luminance(testImageTonemapped)

    # reference_image_tonemapped = load_ldr_image('C:/Users/ASus/Documents/Final Year Project/latest fyp codes 5-01-21/fyp/test_images/gt_tmo.jpg')
    reference_image_tonemapped = load_ldr_image('test_images/gt_tmo.jpg')

    # referenceImageTonemappedLuminance = util.luminance(referenceImageTonemapped)
    #

    print(f" SSIM value is {evaluation_metric.ssim(test_image_tonemapped, reference_image_tonemapped)} ")
    print(f" PSNR value is {evaluation_metric.psnr(test_image_tonemapped, reference_image_tonemapped)} dB")



if __name__ == '__main__':
    main()