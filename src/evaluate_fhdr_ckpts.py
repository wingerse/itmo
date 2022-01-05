from itmo.fhdr.test import test
from matplotlib import pyplot as plt

if __name__ == "__main__":
    x = []
    y_psnr = []
    y_ssim = []
    for i in range(92, 137+1):
        psnr, ssim = test(f"itmo/fhdr/checkpoints/epoch_{i}.ckpt", "../datasets/testing_data_ours", "test_output/fhdr")
        x.append(i)
        y_psnr.append(psnr)
        y_ssim.append(ssim)
    
    print(x, y_psnr, y_ssim)

    plt.figure()
    plt.plot(x, y_psnr)
    plt.xticks(x)
    plt.ylabel("PSNR")
    plt.xlabel("Epochs")
    plt.savefig("psnr.png")

    plt.figure()
    plt.plot(x, y_ssim)
    plt.xticks(x)
    plt.ylabel("SSIM")
    plt.xlabel("Epochs")
    plt.savefig("ssim.png")

    plt.show()