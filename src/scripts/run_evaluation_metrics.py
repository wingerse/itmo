"""
usage: run_evaluation_metrics.py [-h] ldr_path gt_path

Calculate the PSNR, LogPSNR, SSIM scores for an LDR image that has gone through linear itmo and fhdr itmo

positional arguments:
  ldr_path    LDR image path
  gt_path     HDR ground truth image path

optional arguments:
  -h, --help  show this help message and exit
"""

import include_parent_path
from itmo.fhdr.fhdr import fhdr
from itmo.linear import linear
from tmo.reinhard import reinhard
from util import load_ldr_image, load_hdr_image
from quality import metrics
import argparse

p = argparse.ArgumentParser(description="Calculate the PSNR, LogPSNR, SSIM scores for an LDR image that has gone through\
 linear itmo and fhdr itmo")
p.add_argument("ldr_path", help="LDR image path")
p.add_argument("gt_path", help="HDR ground truth image path")

args = p.parse_args()

ldr = load_ldr_image(args.ldr_path)
gt = load_hdr_image(args.gt_path)
gt_tmo = reinhard(gt)

hdr_linear = linear(ldr)
hdr_linear_tmo = reinhard(hdr_linear)
hdr_fhdr = fhdr(ldr)
hdr_fhdr_tmo = reinhard(hdr_fhdr)

print("Metric scores for Linear itmo")

log_psnr_linear = metrics.log_psnr(hdr_linear, gt)
print(f"log PSNR value is {log_psnr_linear} dB")     #log psnr between  linear itmo image and reference image
ssim_linear = metrics.ssim(hdr_linear, gt)
print(f"SSIM value is {ssim_linear}")
psnr_linear = metrics.psnr(gt_tmo, hdr_linear_tmo)
print(f"PSNR value is {psnr_linear} dB")

print("------------")
print("Metric scores for fhdr itmo")

log_psnr_fhdr = metrics.log_psnr(hdr_fhdr, gt)
print(f"log PSNR value is {log_psnr_fhdr} dB")     #log psnr between  linear itmo image and reference image
ssim_fhdr = metrics.ssim(hdr_fhdr, gt)
print(f"SSIM value is {ssim_fhdr}")
psnr_fhdr = metrics.psnr(gt_tmo, hdr_fhdr_tmo)
print(f"PSNR value is {psnr_fhdr} dB")