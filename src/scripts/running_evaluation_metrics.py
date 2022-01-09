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
from quality import metrics



def main():
    """
    running the evaluation metric file
    :return: None
    """
    test_image_hdr = load_hdr_image("test_images/generated_hdr.hdr")      # generated itmo hdr file
    test_image_hdr_luminance = luminance(test_image_hdr)                   # calculating luminance



    reference_image_hdr = load_hdr_image('test_images/gt_hdr.hdr')        # reference hdr file
    reference_image_hdr_luminance = luminance(reference_image_hdr)         # luminance for hdr file

    print(f"log PSNR value is {metrics.log_psnr(test_image_hdr_luminance, reference_image_hdr_luminance)} dB")     #log psnr between test image and reference image

    test_image_tonemapped = load_ldr_image('test_images/generated_tmo.jpg')      #  tone mapped test image

    reference_image_tonemapped = load_ldr_image('test_images/gt_tmo.jpg')      # tone mapped reference image


    print(f" SSIM value is {metrics.ssim(test_image_hdr, reference_image_hdr)} ")
    print(f" PSNR value is {metrics.psnr(test_image_tonemapped, reference_image_tonemapped)} dB")



if __name__ == '__main__':
    main()