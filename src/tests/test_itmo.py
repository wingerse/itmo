import include_parent_path
from itmo import linear, fhdr
from tmo import drago
from tmo.reinhard import reinhard
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np
import pytest

def test_itmo():
    ldr = load_ldr_image("datasets/testing_data_ours/ldr/144.jpg")

    hdr = fhdr(ldr, f"src/itmo/fhdr/checkpoints/epoch_44.ckpt")
    save_hdr_image(hdr, "test_outputs/fhdr.hdr")

    hdr_t = reinhard(hdr)
    save_ldr_image(hdr_t, "test_outputs/fhdr.png")