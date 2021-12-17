from itmo.fhdr.test import test
from matplotlib import pyplot as plt

if __name__ == "__main__":
    psnr, ssim = test(f"itmo/fhdr/checkpoints/FHDR-iter-2.ckpt", "../datasets/aug_dataset_test", "test_output/fhdr")
    print(psnr, ssim)