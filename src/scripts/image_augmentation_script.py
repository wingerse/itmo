"""
usage: image_augmentation_script.py [-h] [--input_path INPUT_PATH] [--output_path OUTPUT_PATH] [--size SIZE]
                                    [--count_per_mp COUNT_PER_MP]

Generate augmented dataset from high definition HDR dataset

optional arguments:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH
                        Path of high definition HDR dataset (default: datasets/full_dataset)
  --output_path OUTPUT_PATH
                        Output path of augmentation (default: datasets/aug_dataset)
  --size SIZE           Size of augmented images (default: 256)
  --count_per_mp COUNT_PER_MP
                        Number of images per megapixel (default: 1.6)
"""
import include_parent_path
from image_augmentation import augment_images
from util import load_hdr_image, save_hdr_image, save_ldr_image
from tqdm import tqdm
import os
import argparse

p = argparse.ArgumentParser(description="Generate augmented dataset from high definition HDR dataset",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("--input_path", default="datasets/full_dataset", help="Path of high definition HDR dataset")
p.add_argument("--output_path", default="datasets/aug_dataset", help="Output path of augmentation")
p.add_argument("--size", type=int, default=256, help="Size of augmented images")
p.add_argument("--count_per_mp", type=float, default=1.6, help="Number of images per megapixel")

args = p.parse_args()

hdrs = os.listdir(args.input_path)
# list of hdr images
hdrs = list(map(lambda x: os.path.join(args.input_path, x), hdrs))
# create output directories if not present
os.makedirs(os.path.join(args.output_path, "ldr"), exist_ok=True)
os.makedirs(os.path.join(args.output_path, "hdr"), exist_ok=True)
count = 0
for hdr_path in tqdm(hdrs):
    # for every hdr image, augment 1 images per megapixel and save the results. 
    hdr = load_hdr_image(hdr_path)
    aug = augment_images(hdr, args.count_per_mp, args.size)
    for ldr, hdr in aug:
        count += 1
        save_ldr_image(ldr, os.path.join(args.output_path, "ldr", f"{count}.jpg"))
        save_hdr_image(hdr, os.path.join(args.output_path, "hdr", f"{count}.hdr"))