import numpy as np
import torch
from torchvision import transforms

from util import apply_gamma, remove_gamma

def mu_tonemap(img):
    """ tonemapping HDR images using μ-law before computing loss """

    MU = 5000.0
    return torch.log(1.0 + MU * (img + 1.0) / 2.0) / np.log(1.0 + MU)

def preprocess_ldr(ldr):
    ldr = remove_gamma(ldr)
    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])((ldr * 255).astype(np.uint8))

def unpreprocess_ldr(ldr):
    ldr = (ldr + 1) / 2
    ldr =  (ldr.permute(1, 2, 0)).cpu().numpy() 
    ldr = apply_gamma(ldr)
    return ldr

def preprocess_hdr(hdr):
    hdr = torch.from_numpy(hdr).permute(2, 0, 1)
    return transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(hdr)

def unpreprocess_hdr(hdr):
    hdr = (hdr * 0.5 + 0.5)
    return hdr.permute(1, 2, 0).cpu().numpy()

def update_lr(optimizer, epoch, epochs, lr, lr_decay_after):
    """ Linearly decaying model learning rate after specified lr_decay_after epochs """

    lr -= lr*(epoch - lr_decay_after)/(epochs - lr_decay_after)

    for param_group in optimizer.param_groups:
        param_group["lr"] = lr
