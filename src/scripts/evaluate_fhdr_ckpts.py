import include_parent_path
from itmo.fhdr.test import test
from matplotlib import pyplot as plt

if __name__ == "__main__":
    x = []
    y_psnr = []
    y_ssim = []
    for i in range(92, 137+1):
        psnr, ssim = test(f"src/itmo/fhdr/checkpoints/epoch_{i}.ckpt", "datasets/testing_data_ours", "test_outputs/fhdr")
        x.append(i)
        y_psnr.append(psnr)
        y_ssim.append(ssim)
    
    print(x, y_psnr, y_ssim)

    x = range(1, len(y_ssim)+1)

    fig, ax = plt.subplots(1, 2)
    ax[0].plot(x, y_psnr)
    ax[0].set_ylabel("PSNR")
    ax[0].set_xlabel("Epochs")

    ax[1].plot(x, y_ssim)
    ax[1].set_ylabel("SSIM")
    ax[1].set_xlabel("Epochs")

    plt.show()