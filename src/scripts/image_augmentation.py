"""
Script to generate augmented dataset from a high definition HDR dataset
"""
import include_parent_path
from image_augmentation import augment_images
from util import load_hdr_image, save_hdr_image, save_ldr_image
from tqdm import tqdm
import os

input_path = "datasets/full_dataset"
output_path = "datasets/aug_dataset"

if __name__ == "__main__":
    hdrs = os.listdir(input_path)
    # list of hdr images
    hdrs = list(map(lambda x: os.path.join(input_path, x), hdrs))
    # create output directories if not present
    os.makedirs(os.path.join(output_path, "ldr"), exist_ok=True)
    os.makedirs(os.path.join(output_path, "hdr"), exist_ok=True)
    count = 0
    for hdr_path in tqdm(hdrs):
        # for every hdr image, augment 1.6 images per megapixel and save the results. 
        hdr = load_hdr_image(hdr_path)
        aug = augment_images(hdr, 1.6, 256)
        for ldr, hdr in aug:
            count += 1
            save_ldr_image(ldr, os.path.join(output_path, "ldr", f"{count}.jpg"))
            save_hdr_image(hdr, os.path.join(output_path, "hdr", f"{count}.hdr"))