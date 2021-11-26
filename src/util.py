import torch
import cv2
import numpy as np
from torchvision import transforms

def load_ldr(path):
    i = cv2.imread(path)
    if i is None:
        raise Exception("invalid path")
    i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    return transforms.ToTensor()(i)

def preprocess_ldr(ldr):
    return transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(ldr)

def unpreprocess_ldr(ldr):
    return (ldr + 1) / 2

def save_ldr(ldr, path):
    ldr = (ldr.permute(1, 2, 0) * 255).cpu().numpy()
    ldr = cv2.cvtColor(ldr, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, ldr)

def load_hdr(path):
    i = cv2.imread(path, cv2.IMREAD_ANYDEPTH)
    if i is None:
        raise Exception("invalid path")
    i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    return torch.from_numpy(i).cuda().permute(2, 0, 1)

def preprocess_hdr(hdr):
    return transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(hdr).flip(0)

def unpreprocess_hdr(hdr):
    return ((hdr + 1) / 2).flip(0)

def save_hdr(hdr, path):
    hdr = hdr.permute(1, 2, 0).cpu().numpy()
    hdr = cv2.cvtColor(hdr, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, hdr)