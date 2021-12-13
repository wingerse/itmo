import os
from os import path
import numpy as np
import torch
import torch.nn as nn
from skimage.metrics import structural_similarity
from torch.utils.data import DataLoader
from tqdm import tqdm

from .dataset import HDRDataset
from .model import FHDR
from .util import mu_tonemap, unpreprocess_hdr, unpreprocess_ldr
from util import save_ldr_image, save_hdr_image

def test(checkpoint_path, dataset_path, output_path, batch_size=1, iteration_count=1):
    dataset = HDRDataset(dataset_path, batch_size)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = FHDR(iteration_count)

    assert torch.cuda.is_available()
    torch.cuda.set_device(0)

    model.cuda()
    model.load_state_dict(torch.load(checkpoint_path))

    os.makedirs(path.join(output_path, "ldr"), exist_ok=True)
    os.makedirs(path.join(output_path, "hdr"), exist_ok=True)
    os.makedirs(path.join(output_path, "gt_hdr"), exist_ok=True)

    mse_loss = nn.MSELoss()
    psnr = 0
    ssim = 0

    with torch.no_grad():
        for batch, data in enumerate(tqdm(data_loader, desc="Testing %")):
            input = data[0]
            gt_hdr = data[1]
            gt_t = mu_tonemap(gt_hdr)

            output = model(input)[-1]

            for batch_i in range(len(output)):
                i = batch * batch_size + batch_i

                input_u = unpreprocess_ldr(input[batch_i])
                output_u = unpreprocess_hdr(output[batch_i])
                gt_hdr_u = unpreprocess_hdr(gt_hdr[batch_i])

                save_ldr_image(input_u, path.join(output_path, "ldr", f"{i}.png"))
                save_hdr_image(output_u, path.join(output_path, "hdr", f"{i}.hdr"))
                save_hdr_image(gt_hdr_u, path.join(output_path, "gt_hdr", f"{i}.hdr"))

                # calculating PSNR score
                mse = mse_loss(mu_tonemap(output[batch_i]), gt_t[batch_i])
                psnr += 10 * np.log10(1 / mse.item())

                # calculating SSIM score
                ssim += structural_similarity(output_u, gt_hdr_u, channel_axis=2)
    
    psnr /= len(dataset)
    ssim /= len(dataset)

    return (psnr, ssim)