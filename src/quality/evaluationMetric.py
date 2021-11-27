import cv2
from math import log10
import numpy as np


def logPSNR(testimage, referenceimage):
    Lmin =0
    testimageluminance = max(testimage,Lmin)
    referenceimageluminance = max(referenceimage, Lmin)
    mse = np.mean(( testimageluminance- referenceimageluminance) ** 2)
    if (mse == 0):  # means thatno noise present, logPSNR serves no importance here
        return 100
    Lmax = 1000     # as most HDR displays will not exceed this value.(according to Kai Linn's thesis)
    logpsnr = 10 * log10(log10(Lmax)/mse)
    return logpsnr



def main():
    testimage = cv2.imread("test_image.png")
    referenceimage = cv2.imread("reference_image.png", 1)
    value = logPSNR(testimage, referenceimage)
    print(f"logPSNR value is {value} dB")
    if __name__ == "__main__":
        main()