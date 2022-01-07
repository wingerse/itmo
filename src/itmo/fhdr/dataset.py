import os

from torch.utils.data import Dataset
from .util import preprocess_hdr, preprocess_ldr

from util import load_hdr_image, load_ldr_image
from pathlib import Path

class HDRDataset(Dataset):
    """
    Custom dataset that loads and pre-processes the LDR and HDR images for the model
    """

    def __init__(self, path, batch_size):
        self.batch_size = batch_size

        ldr_path = os.path.join(path, "ldr")
        hdr_path = os.path.join(path, "hdr")

        # sort the paths so ldr-hdr pairs are matching
        self.ldr_paths = list(map(lambda p: os.path.join(ldr_path, p), sorted(os.listdir(ldr_path))))
        self.hdr_paths = list(map(lambda p: os.path.join(hdr_path, p), sorted(os.listdir(hdr_path))))

    def __getitem__(self, i):
        ldr = load_ldr_image(self.ldr_paths[i])
        ldr = preprocess_ldr(ldr)

        hdr = load_hdr_image(self.hdr_paths[i])
        hdr = preprocess_hdr(hdr)

        # image filename without extension, i.e. image number
        n = Path(self.ldr_paths[i]).stem

        return (ldr, hdr, n)

    def __len__(self):
        # only multiples of batch sizes are returned, remainder is not processed
        return len(self.ldr_paths) // self.batch_size * self.batch_size
