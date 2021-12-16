import time
import os

import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from .dataset import HDRDataset
from .model import FHDR
from .util import mu_tonemap, update_lr
from .vgg import VGGLoss

def weights_init(m):
    if isinstance(m, torch.nn.Conv2d):
        m.weight.data.normal_(0.0, 0.0)

def train(
    checkpoint_path, dataset_path, batch_size=1, iteration_count=1, lr=0.0002, epochs=200, lr_decay_after=100,
    resume_epoch=None,
):
    os.makedirs(checkpoint_path, exist_ok=True)

    dataset = HDRDataset(dataset_path, batch_size)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True, 
        multiprocessing_context="spawn")

    model = FHDR(iteration_count)

    assert torch.cuda.is_available()
    torch.cuda.set_device(0)

    model.cuda()

    l1 = torch.nn.L1Loss()
    perceptual_loss = VGGLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(0.9, 0.999))

    if resume_epoch is not None:
        model.load_state_dict(torch.load(os.path.join(checkpoint_path, f"epoch_{resume_epoch}.ckpt")))
        start_epoch = resume_epoch + 1
    else:
        model.apply(weights_init)
        start_epoch = 1

    start = time.time()

    for epoch in range(start_epoch, epochs+1):
        print(f"Epoch {epoch}")
        epoch_start = time.time()
        epoch_loss = 0

        # check whether LR needs to be updated
        if epoch > lr_decay_after:
            update_lr(optimizer, epoch, epochs, lr, lr_decay_after)

        for batch, data in enumerate(tqdm(data_loader, desc="Batch %")):
            optimizer.zero_grad(set_to_none=True)

            input = data[0].cuda()
            gt_hdr = data[1].cuda()
            gt_t = mu_tonemap(gt_hdr)

            # forward pass ->
            output = model(input)

            l1_loss = 0
            vgg_loss = 0

            # computing loss for n generated outputs (from n-iterations) ->
            for image in output:
                image_t = mu_tonemap(image)
                l1_loss += l1(image_t, gt_t)
                vgg_loss += perceptual_loss(image_t, gt_t)

            # averaged over n iterations
            l1_loss /= len(output)
            vgg_loss /= len(output)

            # averaged over batches
            l1_loss = torch.mean(l1_loss)
            vgg_loss = torch.mean(vgg_loss)

            # FHDR loss function
            loss = l1_loss + (vgg_loss * 10)
            epoch_loss += loss.item()

            # output is the final reconstructed image i.e. last in the array of outputs of n iterations
            output = output[-1]

            # backpropagate and step
            loss.backward()
            optimizer.step()

        epoch_loss /= len(dataset) / batch_size
        epoch_finish = time.time()
        time_taken = (epoch_finish - epoch_start) / 60

        print(f"End of epoch {epoch}. Time taken: {time_taken:.2} minutes. Loss: {epoch_loss}")

        torch.save(model.state_dict(), os.path.join(checkpoint_path, f"epoch_{epoch}.ckpt"))
    
    time_taken = (time.time() - start) / 60
    print(f"Done. Time taken: {time_taken:.2} minutes")