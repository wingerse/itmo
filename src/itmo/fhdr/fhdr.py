from .model import FHDR
import torch
from torch import nn
from skimage.metrics import structural_similarity
import numpy as np
from .util import mu_tonemap, preprocess_ldr, preprocess_hdr, unpreprocess_hdr

def fhdr(ldr, gt_hdr, ckpt_path, iteration_count=1):
    model = FHDR(iteration_count)
    torch.cuda.set_device(0)
    model.cuda()

    mse_loss = nn.MSELoss()
    model.load_state_dict(torch.load(ckpt_path))

    ldr = preprocess_ldr(ldr)
    gt_hdr = preprocess_hdr(gt_hdr)

    with torch.no_grad():
        input = ldr.unsqueeze(0)
        output = model(input)

        output = output[-1][0]

        # calculating PSNR score
        mse = mse_loss(mu_tonemap(output), mu_tonemap(gt_hdr))
        psnr = 10 * np.log10(1 / mse.item())

        generated = unpreprocess_hdr(output)
        real = unpreprocess_hdr(gt_hdr)

        # calculating SSIM score
        ssim = structural_similarity(generated, real, multichannel=True)

        return (generated, psnr, ssim)

