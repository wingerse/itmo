import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class FHDR(nn.Module):
    """
    The FHDR model as described in the paper. For more information, read the paper.
    """

    def __init__(self, iteration_count):
        super().__init__()

        self.iteration_count = iteration_count

        self.reflect_pad = nn.ReflectionPad2d(1)
        self.feb1 = nn.Conv2d(3, 64, kernel_size=3, padding=0)
        self.feb2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)

        self.feedback_block = FeedbackBlock()

        self.hrb1 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.hrb2 = nn.Conv2d(64, 3, kernel_size=3, padding=0)

        self.tanh = nn.Tanh()

    def forward(self, input):

        outs = []

        feb1 = F.relu(self.feb1(self.reflect_pad(input)))
        feb2 = F.relu(self.feb2(feb1))

        for i in range(self.iteration_count):
            fb_out = self.feedback_block(feb2)

            FDF = fb_out + feb1

            hrb1 = F.relu(self.hrb1(FDF))
            del FDF
            out = self.hrb2(self.reflect_pad(hrb1))
            out = self.tanh(out)
            outs.append(out)

        return outs


class FeedbackBlock(nn.Module):
    def __init__(self):
        super().__init__()

        self.compress_in = nn.Conv2d(128, 64, kernel_size=1, padding=0)
        self.DRDB1 = DilatedResidualDenseBlock()
        self.DRDB2 = DilatedResidualDenseBlock()
        self.DRDB3 = DilatedResidualDenseBlock()
        self.last_hidden = None

        self.GFF_3x3 = nn.Conv2d(64, 64, kernel_size=3, padding=1, bias=True)
        self.should_reset = True

    def forward(self, x):
        if self.should_reset:
            self.last_hidden = torch.zeros(x.size(), device=torch.device("cuda:0"))
            self.last_hidden.copy_(x)
            self.should_reset = False

        # hidden layer is concatenated with input, doubling its size, i.e. 128
        out = torch.cat((x, self.last_hidden), dim=1)
        # it is then compressed back to 64
        out = self.compress_in(out)

        out = self.DRDB1(out)
        out = self.DRDB2(out)
        out = self.DRDB3(out)

        out = F.relu(self.GFF_3x3(out))
        self.last_hidden = out
        self.last_hidden = Variable(self.last_hidden.data)

        return out


class DilatedResidualDenseBlock(nn.Module):
    def __init__(self, nDenselayer=4, growthRate=32):
        super().__init__()

        nChannels_ = 64
        modules = []

        # since each layer is connected to layers after it, the channel size grows 
        for i in range(nDenselayer):
            modules.append(make_dense(nChannels_, growthRate))
            nChannels_ += growthRate
        # then each layer is fed sequentially. Dense connections is achieved by concatenating input of each layer
        # with output of it.
        self.dense_layers = nn.Sequential(*modules)
        self.should_reset = True

        self.compress = nn.Conv2d(128, 64, kernel_size=1, stride=1, padding=0)
        self.conv_1x1 = nn.Conv2d(nChannels_, 64, kernel_size=1, padding=0, bias=False)

    def forward(self, x):
        if self.should_reset:
            self.last_hidden = torch.zeros(x.size()).cuda()
            self.last_hidden.copy_(x)
            self.should_reset = False

        # hidden layer is concatenated with input doubling its size, i.e. 128
        out = torch.cat((x, self.last_hidden), dim=1)

        # it is then compressed to 64
        out = self.compress(out)
        out = self.dense_layers(out)
        out = self.conv_1x1(out)

        self.last_hidden = out
        self.last_hidden = Variable(out.data)

        return out


class make_dense(nn.Module):
    def __init__(self, nChannels, growthRate, kernel_size=3):
        super().__init__()
        self.conv = nn.Conv2d(
            nChannels,
            growthRate,
            kernel_size=kernel_size,
            padding=(kernel_size - 1),
            bias=False,
            dilation=2,
        )

    def forward(self, x):
        out = F.relu(self.conv(x))
        # output of each layer is its input concat with output, this allows later layers to consume the 
        # output of this layer as well previous layers.
        out = torch.cat((x, out), 1)
        return out
