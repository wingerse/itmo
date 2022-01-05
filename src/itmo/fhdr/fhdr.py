from .model import FHDR
import torch
from torch import nn
import numpy as np
from .util import preprocess_ldr, unpreprocess_hdr

def fhdr(ldr, ckpt_path, iteration_count=1):
    model = FHDR(iteration_count)
    torch.cuda.set_device(0)
    model.cuda()

    model.load_state_dict(torch.load(ckpt_path))

    ldr = preprocess_ldr(ldr).cuda()

    with torch.no_grad():
        input = ldr.unsqueeze(0)
        output = model(input)

        output = output[-1][0]
        output = unpreprocess_hdr(output)
        return output