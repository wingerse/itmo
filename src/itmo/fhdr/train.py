import time
import os

import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from .dataset import HDRDataset
from .model import FHDR
from .util import mu_tonemap, update_lr
from .vgg import VGGLoss

def train(
    checkpoint_path, dataset_path, batch_size=1, iteration_count=1, lr=0.0002, epochs=200, lr_decay_after=100,
    resume_epoch=1,
):
    """
    Train the FHDR model. 
    
    :param checkpoint_path: The checkpoint directory to save the checkpoint of every epoch. 
    :param dataset_path: Path of the training dataset.
    :param batch_size: The batch size, default 1.
    :param iteration_count: Number of FHDR iterations, default 1.
    :param lr: Learning rate, default 0.0002.
    :param epochs: Number of epochs, default 200.
    :param lr_decay_after: When to start decaying the learning rate, default 100.
    :resume_epoch: If training is interrupted, which epoch to resume from, default 1 (i.e. start from beginning)
    """

    # create checkpoints directory if not existing
    os.makedirs(checkpoint_path, exist_ok=True)

    assert torch.cuda.is_available()
    # use first GPU
    torch.cuda.set_device(0)

    dataset = HDRDataset(dataset_path, batch_size)
    # dataloader which shuffles for every epoch. Also use multiprocessing and pinned memory for extra performance.  
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True, 
        multiprocessing_context="spawn")

    model = FHDR(iteration_count)
    model.cuda()

    # we use l1 and perceptual loss
    l1 = torch.nn.L1Loss()
    perceptual_loss = VGGLoss()
    # with adam optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(0.9, 0.999))

    # if resuming from an interrupted training, load the last checkpoint
    if resume_epoch != 1:
        model.load_state_dict(torch.load(os.path.join(checkpoint_path, f"epoch_{resume_epoch-1}.ckpt")))
        start_epoch = resume_epoch
    else:
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
            # zero out the gradients
            optimizer.zero_grad()

            # get input and ground truth from dataloader
            input = data[0].cuda()
            gt_hdr = data[1].cuda()
            # tonemap before calculating loss
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

        # epoch loss is the average epoch loss for each batch. 
        epoch_loss /= len(dataset) / batch_size
        epoch_finish = time.time()
        time_taken = (epoch_finish - epoch_start) / 60

        print(f"End of epoch {epoch}. Time taken: {time_taken:.2f} minutes. Loss: {epoch_loss}")

        # save checkpoint for epoch
        torch.save(model.state_dict(), os.path.join(checkpoint_path, f"epoch_{epoch}.ckpt"))
    
    time_taken = (time.time() - start) / 60
    print(f"Done. Time taken: {time_taken:.2f} minutes")