"""
usage: evaluate_fhdr_ckpts.py [-h] [--dataset_path DATASET_PATH]

Evaluate FHDR checkpoints and plot graph of accuracy against epoch

optional arguments:
  -h, --help            show this help message and exit
  --dataset_path DATASET_PATH
                        Path of testing dataset (default: datasets/testing_data_ours)
"""

import include_parent_path
from itmo.fhdr.test import test
from matplotlib import pyplot as plt
import argparse

p = argparse.ArgumentParser(description="Evaluate FHDR checkpoints and plot graph of accuracy against epoch", 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("--dataset_path", default="datasets/testing_data_ours", help="Path of testing dataset")

args = p.parse_args()

x = []
y_psnr = []
y_ssim = []
for i in range(1, 200+1):
    psnr, ssim = test(f"src/itmo/fhdr/checkpoints/epoch_{i}.ckpt", args.dataset_path, "test_outputs/fhdr")
    x.append(i)
    y_psnr.append(psnr)
    y_ssim.append(ssim)

print(x, y_psnr, y_ssim)

x = range(1, len(y_ssim)+1)

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y_psnr)
ax[0].set_ylabel("PSNR")
ax[0].set_xlabel("Epochs")

ax[1].plot(x, y_ssim)
ax[1].set_ylabel("SSIM")
ax[1].set_xlabel("Epochs")

plt.show()