from itmo import linear, fhdr
from tmo import drago
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
from matplotlib import pyplot as plt

ldr = load_ldr_image("../datasets/fhdr dataset/256/ldr/ldr_10_data.jpg")
gt = load_hdr_image("../datasets/fhdr dataset/256/hdr/groundtruth_10_data.hdr")
x = []
y_psnr = []
y_ssim = []
for i in list(range(1, 37+1)) + [61]:
    hdr, psnr, ssim = fhdr(ldr, gt, f"itmo/fhdr/checkpoints/epoch_{i}.ckpt", iteration_count=1)
    x.append(i)
    y_psnr.append(psnr)
    y_ssim.append(ssim)
    hdr_t = drago(hdr)
    save_ldr_image(hdr_t, f"test_output/fhdr_epoch_{i}.jpg")

plt.figure()
plt.plot(x, y_psnr)
plt.xticks(x)
plt.ylabel("PSNR")
plt.xlabel("Epochs")

plt.figure()
plt.plot(x, y_ssim)
plt.xticks(x)
plt.ylabel("SSIM")
plt.xlabel("Epochs")

plt.show()

#save_hdr_image(hdr, "test_output/fhdr.hdr")
#hdr_t = drago(hdr)
#save_ldr_image(hdr_t, "test_output/fhdr.jpg")
#print(psnr, ssim)