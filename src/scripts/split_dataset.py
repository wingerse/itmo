"""
Script to split the augmented dataset into training and testing set. 
"""

import include_parent_path
import os
from os import path
import random
import shutil

aug_dataset_path = "datasets/aug_dataset"
ldr_path = path.join(aug_dataset_path, "ldr")
hdr_path = path.join(aug_dataset_path, "hdr")

# get all ldr and hdr images, pair them and shuffle them
ldrs = sorted(map(lambda x: path.join(ldr_path, x), os.listdir(ldr_path)))
hdrs = sorted(map(lambda x: path.join(hdr_path, x), os.listdir(hdr_path)))
pairs = list(zip(ldrs, hdrs))
random.shuffle(pairs)

# make required output directories
os.makedirs("datasets/training_data_ours/ldr", exist_ok=True)
os.makedirs("datasets/training_data_ours/hdr", exist_ok=True)
os.makedirs("datasets/testing_data_ours/ldr", exist_ok=True)
os.makedirs("datasets/testing_data_ours/hdr", exist_ok=True)

# then take first 10000 as training pairs, rest as testing pairs

training = pairs[:10000]
testing = pairs[10000:]

# save the resulting images. 

for ldr, hdr in training:
    ldr_filename = path.basename(ldr)
    hdr_filename = path.basename(hdr)
    shutil.copy(ldr, path.join("datasets/training_data_ours/ldr/", ldr_filename))
    shutil.copy(hdr, path.join("datasets/training_data_ours/hdr/", hdr_filename))

for ldr, hdr in testing:
    ldr_filename = path.basename(ldr)
    hdr_filename = path.basename(hdr)
    shutil.copy(ldr, path.join("datasets/testing_data_ours/ldr/", ldr_filename))
    shutil.copy(hdr, path.join("datasets/testing_data_ours/hdr/", hdr_filename))