import include_parent_path
from matplotlib import pyplot as plt

psnr = [20.673043345416698, 20.251248793512637, 20.185508282318292, 20.295089503465334]
ssim = [0.6525370941069479, 0.6559128194919405, 0.6644402776945383, 0.6790879079870835]
memory = [229.18, 910.18, 2045.18, 3634]
time = [52, 203, 456, 882]

x = [256, 512, 768, 1024]

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, psnr)
ax[0, 0].set_ylabel("PSNR")
ax[0, 0].set_xlabel("Image size")

ax[0, 1].plot(x, ssim)
ax[0, 1].set_ylabel("SSIM")
ax[0, 1].set_xlabel("Image size")

ax[1, 0].plot(x, ssim)
ax[1, 0].set_ylabel("Time (ms)")
ax[1, 0].set_xlabel("Image size")

ax[1, 1].plot(x, ssim)
ax[1, 1].set_ylabel("Memory usage (MB) (without caching)")
ax[1, 1].set_xlabel("Image size")

plt.show()