import numpy as np
import torch
from torchvision import transforms

from util import apply_gamma, remove_gamma

def mu_tonemap(img):
    """
    Tonemap the HDR image using μ-law before computing loss 

    :param img: HDR image (can also be in batches).
    :return: Tonemapped image(s)
    """

    MU = 5000.0
    return torch.log(1.0 + MU * (img + 1.0) / 2.0) / np.log(1.0 + MU)

def preprocess_ldr(ldr):
    """
    Preprocess LDR image for the model by removing gamma, converting to pytorch tensor and normalizing it.

    :param ldr: Unprocessed LDR image.
    :return: Processed LDR image.
    """

    ldr = remove_gamma(ldr)
    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])((ldr * 255).astype(np.uint8))

def unpreprocess_ldr(ldr):
    """
    Undo the preprocessing.
    
    :param ldr: Processed LDR image.
    :return: Unprocessed LDR image.
    """

    ldr = (ldr + 1) / 2
    ldr =  (ldr.permute(1, 2, 0)).cpu().numpy() 
    ldr = apply_gamma(ldr)
    return ldr

def preprocess_hdr(hdr):
    """
    Preprocess HDR image for the model by converting to pytorch tensor and normalizing it. 

    :param hdr: Unprocessed HDR image.
    :return: Processed HDR image.
    """

    hdr = torch.from_numpy(hdr).permute(2, 0, 1)
    return transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(hdr)

def unpreprocess_hdr(hdr):
    """
    Undo the preprocessing.

    :param hdr: Processed HDR image.
    :return: Unprocessed HDR image.
    """

    hdr = (hdr * 0.5 + 0.5)
    return hdr.permute(1, 2, 0).cpu().numpy()

def update_lr(optimizer, epoch, epochs, lr, lr_decay_after):
    """
    Linearly decay the model learning rate.
    :param optimizer: The optimizer used by the model.
    :param epoch: The current epoch.
    :param epochs: The total number of epochs.
    :param lr: Learning rate. 
    :param: lr_decay_after: Which epoch to start decaying after. 
    """

    lr -= lr*(epoch - lr_decay_after)/(epochs - lr_decay_after)

    for param_group in optimizer.param_groups:
        param_group["lr"] = lr
