import os
from os import path
import random
import shutil

aug_dataset_path = "../datasets/aug_dataset"
ldr_path = path.join(aug_dataset_path, "ldr")
hdr_path = path.join(aug_dataset_path, "hdr")

ldrs = sorted(map(lambda x: path.join(ldr_path, x), os.listdir(ldr_path)))
hdrs = sorted(map(lambda x: path.join(hdr_path, x), os.listdir(hdr_path)))
pairs = list(zip(ldrs, hdrs))
random.shuffle(pairs)

os.makedirs("../datasets/training_data2/ldr", exist_ok=True)
os.makedirs("../datasets/training_data2/hdr", exist_ok=True)
os.makedirs("../datasets/testing_data2/ldr", exist_ok=True)
os.makedirs("../datasets/testing_data2/hdr", exist_ok=True)

training = pairs[:10000]
testing = pairs[10000:]

for ldr, hdr in training:
    ldr_filename = path.basename(ldr)
    hdr_filename = path.basename(hdr)
    shutil.copy(ldr, path.join("../datasets/training_data2/ldr/", ldr_filename))
    shutil.copy(hdr, path.join("../datasets/training_data2/hdr/", hdr_filename))

for ldr, hdr in testing:
    ldr_filename = path.basename(ldr)
    hdr_filename = path.basename(hdr)
    shutil.copy(ldr, path.join("../datasets/testing_data2/ldr/", ldr_filename))
    shutil.copy(hdr, path.join("../datasets/testing_data2/hdr/", hdr_filename))