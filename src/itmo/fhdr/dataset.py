import os

from torch.utils.data import Dataset
from .util import preprocess_hdr, preprocess_ldr

from util import load_hdr_image, load_ldr_image

class HDRDataset(Dataset):
    def __init__(self, path, batch_size):
        self.batch_size = batch_size

        ldr_path = os.path.join(path, "ldr")
        hdr_path = os.path.join(path, "hdr")

        self.ldr_paths = list(map(lambda p: os.path.join(ldr_path, p), sorted(os.listdir(ldr_path))))
        self.hdr_paths = list(map(lambda p: os.path.join(hdr_path, p), sorted(os.listdir(hdr_path))))

    def __getitem__(self, i):
        ldr = load_ldr_image(self.ldr_paths[i])
        ldr = preprocess_ldr(ldr)

        hdr = load_hdr_image(self.hdr_paths[i])
        hdr = preprocess_hdr(hdr)

        return (ldr, hdr)

    def __len__(self):
        return len(self.ldr_paths) // self.batch_size * self.batch_size
