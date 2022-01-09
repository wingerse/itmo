import math
from math import log10
import numpy as np
from skimage.metrics import structural_similarity

def log_psnr(test_image_hdr_luminance, reference_image_hdr_luminance):
    """

    :param test_image_hdr_luminance: luminance of the test hdr image
    :param referenceImageHdr: luminance of HDR ground truth image to be compared with
    :return: logPSNR value denoting the quality of the test image compared to the reference image. The higher the logPSNR value,
             the closer is the test Image to the ground truth.
    Note: The formula for logPSNR was taken from Kai Linn's thesis chapter 2 page 34
    """
    Lmin =0
    test_image_hdr_max = np.max(test_image_hdr_luminance,Lmin)

    reference_image_hdr_max = np.max(reference_image_hdr_luminance, Lmin)

    mse = np.mean((np.log10(test_image_hdr_max) - np.log10(reference_image_hdr_max)) ** 2)
    if (mse == 0):  # means that no noise present, logPSNR serves no importance here
        return 100
    Lmax = 10000     # as most HDR displays will not exceed this value.(according to Kai Linn's thesis)
    log_psnr_value = 20 * log10(log10(Lmax)/math.sqrt(mse))
    return log_psnr_value


def ssim(test_image, reference_image):
    """
    This function computes the structural similarity difference between the test image and the reference image.
    It is a measure of the perceptual difference between the two images. The value ranges from 0 to 1 and the closer the value is to 1,
    the closer is the generated image from the ground truth image.
    :param testImageTonemapped: ldr format after tonemapping  the generated hdr image
    :param referenceImageTonemapped: ldr format after tonemapping  the ground truth hdr image
    :return: the SSIM score
    """
    return structural_similarity(test_image, reference_image, channel_axis=2)



def psnr(test_image_tonemapped, reference_image_tonemapped):
    """
    code adapted from https://github.com/jackfrued/Python-1/blob/master/analysis/compression_analysis/psnr.py

    This function computes the peak singnal-to-noise ratio of the tonemapped generated image and that of the tonemapped ground truth image.
    Used to measure the quality of the generated image compared to the ground truth. The higher the value, the better is the measurement.
    :param testImageTonemapped:ldr format after tonemapping  the generated hdr image
    :param referenceImageTonemapped: ldr format after tonemapping  the ground truth hdr image
    :return: the PSNR value
    """

    mse = np.mean((test_image_tonemapped - reference_image_tonemapped) ** 2)
    if (mse == 0):  # means that no noise present, PSNR serves no importance here
        return 100
    PIXEL_MAX = 1
    psnr_value = 10 * log10(PIXEL_MAX/(mse))
    return psnr_value