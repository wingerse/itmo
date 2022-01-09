"""
usage: split_dataset.py [-h] [--aug_dataset_path AUG_DATASET_PATH] [--training_data_path TRAINING_DATA_PATH]
                        [--testing_data_path TESTING_DATA_PATH] [--training_data_size TRAINING_DATA_SIZE]

Split augmented dataset into training and testing set

optional arguments:
  -h, --help            show this help message and exit
  --aug_dataset_path AUG_DATASET_PATH
                        Path of augmented dataset (default: datasets/aug_dataset)
  --training_data_path TRAINING_DATA_PATH
                        Path of training dataset (default: datasets/training_data_ours)
  --testing_data_path TESTING_DATA_PATH
                        Path of testing dataset (default: datasets/testing_data_ours)
  --training_data_size TRAINING_DATA_SIZE
                        Size of training data, rest is testing data (default: 10000)
"""

import argparse
import include_parent_path
import os
from os import path
import random
import shutil
import argparse

p = argparse.ArgumentParser(description="Split augmented dataset into training and testing set", 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("--aug_dataset_path", default="datasets/aug_dataset", help="Path of augmented dataset")
p.add_argument("--training_data_path", default="datasets/training_data_ours", help="Path of training dataset")
p.add_argument("--testing_data_path", default="datasets/testing_data_ours", help="Path of testing dataset")
p.add_argument("--training_data_size", type=int, default=10000, help="Size of training data, rest is testing data")

args = p.parse_args()

ldr_path = path.join(args.aug_dataset_path, "ldr")
hdr_path = path.join(args.aug_dataset_path, "hdr")

# get all ldr and hdr images, pair them and shuffle them
ldrs = sorted(map(lambda x: path.join(ldr_path, x), os.listdir(ldr_path)))
hdrs = sorted(map(lambda x: path.join(hdr_path, x), os.listdir(hdr_path)))
pairs = list(zip(ldrs, hdrs))

if len(pairs) < args.training_data_size:
    print("Error: training_data_size exceeds aug dataset size")
    os._exit(1)

random.shuffle(pairs)

training_data_ldr_path = path.join(args.training_data_path, "ldr")
training_data_hdr_path = path.join(args.training_data_path, "hdr")
testing_data_ldr_path = path.join(args.testing_data_path, "ldr")
testing_data_hdr_path = path.join(args.testing_data_path, "hdr")

# make required output directories
os.makedirs(training_data_ldr_path, exist_ok=True)
os.makedirs(training_data_hdr_path, exist_ok=True)
os.makedirs(testing_data_ldr_path, exist_ok=True)
os.makedirs(testing_data_hdr_path, exist_ok=True)

# then take first args.training_data_size as training pairs, rest as testing pairs

training = pairs[:args.training_data_size]
testing = pairs[args.training_data_size:]

# save the resulting images. 

for ldr, hdr in training:
    ldr_filename = path.basename(ldr)
    hdr_filename = path.basename(hdr)
    shutil.copy(ldr, path.join(training_data_ldr_path, ldr_filename))
    shutil.copy(hdr, path.join(training_data_hdr_path, hdr_filename))

for ldr, hdr in testing:
    ldr_filename = path.basename(ldr)
    hdr_filename = path.basename(hdr)
    shutil.copy(ldr, path.join(testing_data_ldr_path, ldr_filename))
    shutil.copy(hdr, path.join(testing_data_hdr_path, hdr_filename))