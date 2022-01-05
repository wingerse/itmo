import include_parent_path
from itmo.fhdr.test import test
from matplotlib import pyplot as plt

if __name__ == "__main__":
    psnr, ssim = test(f"src/itmo/fhdr/checkpoints/epoch_44.ckpt", "datasets/testing_data_ours", "test_outputs/fhdr")
    print(f"PSNR: {psnr}, SSIM: {ssim}")