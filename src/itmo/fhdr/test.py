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
    """
    Test the FHDR model on the testing dataset.

    :param checkpoint_path: Path of the checkpoint to use.
    :param dataset_path: The testing dataset path.
    :param output_path: Where to output the generated images + ldr and ground truth.
    :batch_size: The batch size, default 1.
    :iteration_count: Number of FHDR iterations, default 1.
    :return: Tuple of average (PSNR, SSIM).
    """

    assert torch.cuda.is_available()
    torch.cuda.set_device(0)

    dataset = HDRDataset(dataset_path, batch_size)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = FHDR(iteration_count)
    model.cuda()
    # load checkpoint
    model.load_state_dict(torch.load(checkpoint_path))

    # create the output directories if not present
    os.makedirs(path.join(output_path, "ldr"), exist_ok=True)
    os.makedirs(path.join(output_path, "hdr"), exist_ok=True)
    os.makedirs(path.join(output_path, "gt_hdr"), exist_ok=True)

    mse_loss = nn.MSELoss()
    psnr = 0
    ssim = 0

    with torch.no_grad():
        for batch, data in enumerate(tqdm(data_loader, desc="Testing %")):
            input = data[0].cuda()
            gt_hdr = data[1].cuda()
            # tonemap the ground truth for calculating psnr
            gt_t = mu_tonemap(gt_hdr)

            # take last iteration
            output = model(input)[-1]

            # for each image in the batch
            for batch_i in range(len(output)):
                # get image number
                n = data[2][batch_i]

                # get the input ldr, generated output and ground truth, and unprocess them
                input_u = unpreprocess_ldr(input[batch_i])
                output_u = unpreprocess_hdr(output[batch_i])
                gt_hdr_u = unpreprocess_hdr(gt_hdr[batch_i])

                save_ldr_image(input_u, path.join(output_path, "ldr", f"{n}.png"))
                save_hdr_image(output_u, path.join(output_path, "hdr", f"{n}.hdr"))
                save_hdr_image(gt_hdr_u, path.join(output_path, "gt_hdr", f"{n}.hdr"))

                # calculating PSNR score
                mse = mse_loss(mu_tonemap(output[batch_i]), gt_t[batch_i])
                psnr += 10 * np.log10(1 / mse.item())

                # calculating SSIM score
                ssim += structural_similarity(output_u, gt_hdr_u, channel_axis=2)
    
    # take averages
    psnr /= len(dataset)
    ssim /= len(dataset)

    return (psnr, ssim)