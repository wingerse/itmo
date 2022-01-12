"""
usage: evaluate_fhdr.py [-h] [--ckpt_path CKPT_PATH] [--dataset_path DATASET_PATH] [--output_path OUTPUT_PATH]

Evaluate FHDR and print accuracy

optional arguments:
  -h, --help            show this help message and exit
  --ckpt_path CKPT_PATH
                        Checkpoint path (default: src/itmo/fhdr/checkpoints/ours.ckpt)
  --dataset_path DATASET_PATH
                        Testing dataset path (default: datasets/testing_data_ours)
  --output_path OUTPUT_PATH
                        Path for testing outputs/results (default: test_outputs/fhdr)
"""
import include_parent_path
from itmo.fhdr.test import test
from matplotlib import pyplot as plt
import argparse
from torch.cuda.memory import max_memory_allocated

p = argparse.ArgumentParser(description="Evaluate FHDR and print accuracy", 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("--ckpt_path", default="src/itmo/fhdr/checkpoints/ours.ckpt", help="Checkpoint path")
p.add_argument("--dataset_path", default="datasets/testing_data_ours", help="Testing dataset path")
p.add_argument("--output_path", default="test_outputs/fhdr", help="Path for testing outputs/results")

args = p.parse_args()

psnr, ssim = test(args.ckpt_path, args.dataset_path, args.output_path)
print(f"PSNR: {psnr}, SSIM: {ssim}")
max_memory = max_memory_allocated() / 1024 / 1024
print(f"Max memory: {max_memory}")
