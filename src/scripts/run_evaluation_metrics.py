# This file is used to calculate the PSNR, LogPSNR, SSIM scores for an LDR image that has gone through linear itmo and fhdr itmo


import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "../"))
from util import change_luminance, luminance, save_hdr_image, save_ldr_image, load_ldr_image, load_hdr_image, remove_gamma, apply_gamma,_save_image,_load_image
from quality import metrics



def main():
    """
    running the evaluation metric file
    :return: None
    """
    print("Metric scores for Linear itmo")
    reference_image_hdr = load_hdr_image('test_images/gt_hdr.hdr')        # reference hdr file
    reference_image_hdr_luminance = luminance(reference_image_hdr)         # luminance for refrence hdr file
    reference_image_tonemapped = load_ldr_image('test_images/gt_tmo.jpg')      # tone mapped reference image


    test_image_linear_hdr = load_hdr_image("test_images/generated_linear_itmo.hdr")      # generated linear itmo hdr file
    test_image_linear_luminance = luminance(test_image_linear_hdr)


    print(f"log PSNR value is {metrics.log_psnr(test_image_linear_luminance, reference_image_hdr_luminance)} dB")     #log psnr between  linear itmo image and reference image

    test_image_linear_tonemapped = load_ldr_image('test_images/generated_linear_tmo.jpg')      #  tone mapped test image


    print(f" SSIM value is {metrics.ssim(test_image_linear_hdr, reference_image_hdr)} ")
    print(f" PSNR value is {metrics.psnr(test_image_linear_tonemapped, reference_image_tonemapped)} dB")





    print("------------")
    print("Metric scores for fhdr itmo")
    test_image_fhdr = load_hdr_image("test_images/generated_hdr.hdr")      # generated fhdr itmo hdr file
    test_image_fhdr_luminance = luminance(test_image_fhdr)                   # calculating luminance

    print(f"log PSNR value is {metrics.log_psnr(test_image_fhdr_luminance, reference_image_hdr_luminance)} dB")     #log psnr between fhdr itmo test image and reference image

    test_image_fhdr_tonemapped = load_ldr_image('test_images/generated_tmo.jpg')      #  tone mapped test image




    print(f" SSIM value is {metrics.ssim(test_image_fhdr, reference_image_hdr)} ")
    print(f" PSNR value is {metrics.psnr(test_image_fhdr_tonemapped, reference_image_tonemapped)} dB")



if __name__ == '__main__':
    main()