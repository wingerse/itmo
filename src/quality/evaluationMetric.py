import math
from math import log10, sqrt
import imageio
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity

from fyp.src import util

def logPSNR(testImageHdrLuminance, referenceImageHdrLuminance):
    """

    :param testImageHdr: HDR image generated after passing an ldr image through the itmo algorithm
    :param referenceImageHdr: HDR ground truth image to be compared with
    :return: logPSNR value denoting the quality of the test image compared to the reference image. The higher the logPSNR value,
             the closer is the test Image to the ground truth.
    Note: The formula for logPSNR was taken from Kai Linn's thesis chapter 2 page 34
    """
    Lmin =0
    testImageHdrMax = np.max(testImageHdrLuminance,Lmin)

    referenceImageHdrMax = np.max(referenceImageHdrLuminance, Lmin)

    mse = np.mean((np.log10(testImageHdrMax) - np.log10(referenceImageHdrMax)) ** 2)
    if (mse == 0):  # means that no noise present, logPSNR serves no importance here
        return 100
    Lmax = 10000     # as most HDR displays will not exceed this value.(according to Kai Linn's thesis)
    logPsnr = 10 * log10(log10(Lmax)/math.sqrt(mse))
    return logPsnr


def SSIM(testImageTonemapped, referenceImageTonemapped):
    """
    This function computes the structural similarity difference between the test image and the reference image.
    It is a measure of the perceptual difference between the two images. The value ranges from 0 to 1 and the closer the value is to 1,
    the closer is the generated image from the ground truth image.
    :param testImageTonemapped: ldr format after tonemapping  the generated hdr image
    :param referenceImageTonemapped: ldr format after tonemapping  the ground truth hdr image
    :return: the SSIM score
    """
    return structural_similarity(testImageTonemapped,referenceImageTonemapped, multichannel=True)



def PSNR(testImageTonemapped, referenceImageTonemapped):
    """
    code adapted from https://github.com/jackfrued/Python-1/blob/master/analysis/compression_analysis/psnr.py

    This function computes the peak singnal-to-noise ratio of the tonemapped generated image and that of the tonemapped ground truth image.
    Used to measure the quality of the generated image compared to the ground truth. The higher the value, the better is the measurement.
    :param testImageTonemapped:ldr format after tonemapping  the generated hdr image
    :param referenceImageTonemapped: ldr format after tonemapping  the ground truth hdr image
    :return: the PSNR value
    """

    mse = np.mean((testImageTonemapped - referenceImageTonemapped) ** 2)
    if (mse == 0):  # means that no noise present, PSNR serves no importance here
        return 100
    PIXEL_MAX = 255.0
    Psnr = 20 * log10(PIXEL_MAX/sqrt(mse))
    return Psnr

def main():


    testImageHdr = util.load_hdr_image('./generated_hdr_b_0_0.hdr')
    testImageHdrLuminance = util.luminance(testImageHdr)


    referenceImageHdr = util.load_hdr_image('./gt_hdr_b_0_0.hdr')
    referenceImageHdrLuminance = util.luminance(referenceImageHdr)

    print(f"log PSNR value is {logPSNR(testImageHdrLuminance, referenceImageHdrLuminance)} dB")

    testImageTonemapped = util.load_hdr_image('./tmo_generated.jpg')
    # testImageTonemappedLuminance = util.luminance(testImageTonemapped)
    #
    referenceImageTonemapped = util.load_hdr_image('./tmo_gt.jpg')
    #
    # referenceImageTonemappedLuminance = util.luminance(referenceImageTonemapped)
    #

    print(f" SSIM value is {SSIM(testImageTonemapped, referenceImageTonemapped)} ")
    print(f" PSNR value is {PSNR(testImageTonemapped, referenceImageTonemapped)} dB")


if __name__ == '__main__':
    main()

