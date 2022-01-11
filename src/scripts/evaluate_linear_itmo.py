
"""
usage: evaluate_linear_itmo.py [-h] [--dataset_path DATASET_PATH]

Evaluate scores of linear ITMO

optional arguments:
  -h, --help            show this help message and exit
  --dataset_path DATASET_PATH
                        Path of testing dataset
"""

import include_parent_path
import numpy as np
from util import load_hdr_image, load_ldr_image
import os
from os import path
from tmo import mu_tonemap
from quality import metrics
import argparse
from pathlib import Path
from itmo import linear

p = argparse.ArgumentParser(description="Evaluate scores of linear ITMO")
p.add_argument("--dataset_path", default="datasets/testing_data_ours", help="Path of testing dataset")

args = p.parse_args()

ssim = 0
psnr = 0
ldr_files = os.listdir(path.join(args.dataset_path, "ldr"))
for ldr_file in ldr_files:
    ldr_path = path.join(args.dataset_path, "ldr", ldr_file)
    hdr_path = path.join(args.dataset_path, "hdr", Path(ldr_file).stem + ".hdr")

    # load ldr and hdr ground truth
    ldr = load_ldr_image(ldr_path)
    gt = load_hdr_image(hdr_path)
    hdr = linear(ldr)

    # find psnr and ssim for linear generated hdr and ground truth
    gt_t = mu_tonemap(gt)
    hdr_t = mu_tonemap(hdr)
    psnr += metrics.psnr(hdr_t, gt_t)
    ssim += metrics.ssim(hdr, gt)

# take averages
psnr /= len(ldr_files)
ssim /= len(ldr_files)

print(f"PSNR: {psnr}, SSIM: {ssim}")