"""
usage: dataset_score.py [-h] [--dataset_path DATASET_PATH]

Calculate scores for ldr-hdr pairs (without any itmo)

optional arguments:
  -h, --help            show this help message and exit
  --dataset_path DATASET_PATH
                        Testing dataset path (default: datasets/testing_data_ours)
"""

import include_parent_path
from util import load_hdr_image, load_ldr_image
import os
from os import path
from tmo import mu_tonemap
from quality import metrics
import argparse

p = argparse.ArgumentParser(description="Calculate scores for ldr-hdr pairs (without any itmo)",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("--dataset_path", default="datasets/testing_data_ours", help="Testing dataset path")

args = p.parse_args()

ssim = 0
psnr = 0
images = os.listdir(path.join(args.dataset_path, "hdr"))
for image in images:
    a = load_ldr_image(path.join(args.dataset_path, "ldr", image.replace("hdr", "jpg")))
    b = load_hdr_image(path.join(args.dataset_path, "hdr", image))
    b_t = mu_tonemap(b)
    psnr += metrics.psnr(a, b_t)
    ssim += metrics.ssim(a, b)

# take averages
psnr /= len(images)
ssim /= len(images)

print(f"PSNR: {psnr}, SSIM: {ssim}")