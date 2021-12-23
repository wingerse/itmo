from itmo.fhdr.test import test
from matplotlib import pyplot as plt

if __name__ == "__main__":
    psnr, ssim = test(f"itmo/fhdr/checkpoints/FHDR-iter-1.ckpt", "../datasets/testing_data_authors", "test_output/authors_authors")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/FHDR-iter-1.ckpt", "../datasets/testing_data_ours", "test_output/authors_ours")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/FHDR-iter-1.ckpt", "../datasets/testing_data_virtualcamera", "test_output/authors_virtualcamera")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/epoch_128.ckpt", "../datasets/testing_data_authors", "test_output/ours_authors")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/epoch_128.ckpt", "../datasets/testing_data_ours", "test_output/ours_ours")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/epoch_128.ckpt", "../datasets/testing_data_virtualcamera", "test_output/ours_virtualcamera")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/virtualcamera.ckpt", "../datasets/testing_data_authors", "test_output/virtualcamera_authors")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/virtualcamera.ckpt", "../datasets/testing_data_ours", "test_output/virtualcamera_ours")
    print(psnr, ssim)
    psnr, ssim = test(f"itmo/fhdr/checkpoints/virtualcamera.ckpt", "../datasets/testing_data_virtualcamera", "test_output/virtualcamera_virtualcamera")
    print(psnr, ssim)