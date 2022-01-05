from itmo.fhdr.test import test
from matplotlib import pyplot as plt

if __name__ == "__main__":
    psnr, ssim = test(f"itmo/fhdr/checkpoints/epoch_44.ckpt", "../datasets/testing_data_ours", "test_output/fhdr")
    print(f"PSNR: {psnr}, SSIM: {ssim}")