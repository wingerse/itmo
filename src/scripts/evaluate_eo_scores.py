"""
usage: evaluate_eo_scores.py

Script to calculate PSNR and SSIM scores for Expansion Operator results in the dataset
"""

import include_parent_path
import numpy as np
from util import load_hdr_image
from skimage.metrics import structural_similarity
import os
from os import path

def mu_tonemap(img):
    MU = 5000.0
    return np.log(1.0 + MU * (img + 1.0) / 2.0) / np.log(1.0 + MU)

def evaluate_eo_scores(eo):
    """
    For the given eo name, calculate the scores for all images
    """

    ssim = 0
    psnr = 0
    images = os.listdir("datasets/eo_results/hdr")
    for image in images:
        a = load_hdr_image(path.join("datasets/eo_results/hdr", image))
        b = load_hdr_image(path.join("datasets/eo_results/generated/", eo + image))
        a_t = mu_tonemap(a)
        b_t = mu_tonemap(b)
        mse = np.mean((a_t - b_t)**2)
        psnr += 10 * np.log10(1 / mse)
        ssim += structural_similarity(a, b, channel_axis=2)

    # take averages
    psnr /= len(images)
    ssim /= len(images)

    return (psnr, ssim)

# all eos in the dataset
eos = ["akyuz", "huo", "huophys", "kov", "kuo", "landis", "masia"]
for eo in eos:
    psnr, ssim = evaluate_eo_scores(eo)
    print(f"{eo}: PSNR: {psnr}, SSIM: {ssim}")