from .model import FHDR
import torch
from .util import preprocess_ldr, unpreprocess_hdr

def fhdr(ldr, ckpt_path="src/itmo/fhdr/checkpoints/ours.ckpt", iteration_count=1):
    """
    Run the FHDR model on a given ldr image. 

    :param ldr: The ldr image numpy array.
    :param ckpt_path: The saved checkpoint.
    :iteration_count: number of FHDR iterations to do, default is 1. 
    :return: generated hdr image as a numpy array
    """
    # use first gpu
    torch.cuda.set_device(0) 

    model = FHDR(iteration_count)
    model.cuda()

    # load weights and biases from the checkpoint
    model.load_state_dict(torch.load(ckpt_path)) 

    ldr = preprocess_ldr(ldr).cuda()

    with torch.no_grad():
        # create batch of only 1 image
        input = ldr.unsqueeze(0) 
        output = model(input)

        # we take the last iteration
        output = output[-1][0] 
        output = unpreprocess_hdr(output)
        return output