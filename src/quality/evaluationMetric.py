
# import cv2
# from math import log10
# import numpy as np
#
#
# def luminanceConversion(R, G, B):
#     luminance = 0.27*R + 0.67*G + 0.06*B
#     return luminance
#
#
# # def findLuminance(testImageTriplets, referenceImageTriplets):
# #     testImage = luminanceConversion(testImageTriplets[0], testImageTriplets[1], testImageTriplets[2])
# #     referenceImage = luminanceConversion(referenceImageTriplets[0], referenceImageTriplets[1], referenceImageTriplets[2])
# #     return testimage ,referenceimage
#
#
# def logPSNR(testImageTriplets, referenceImageTriplets):
# #     testImage = luminanceConversion(testImageTriplets[0], testImageTriplets[1], testImageTriplets[2])
# #     referenceImage = luminanceConversion(referenceImageTriplets[0], referenceImageTriplets[1], referenceImageTriplets[2])
#     Lmin =0
#     testImageLuminance = max(testImage,Lmin)
#     referenceImageLuminance = max(referenceImage, Lmin)
#     mse = np.mean(( log10(testImageLuminance)- log10(referenceImageLuminance)) ** 2)
#     if (mse == 0):  # means that no noise present, logPSNR serves no importance here
#         return 100
#     Lmax = 1000     # as most HDR displays will not exceed this value.(according to Kai Linn's thesis)
#     logPsnr = 10 * log10(log10(Lmax)/mse)
#     return logPsnr
#
#
#
# def main():
#     testImage = cv2.imread("test_image.png")
#     referenceImage = cv2.imread("reference_image.png", 1)
#     value = logPSNR(testImage, referenceImage)
#     print(f"logPSNR value is {value} dB")
#     if __name__ == "__main__":
#         main()



from math import log10
import imageio
import cv2
import numpy as np

from fyp.src import util

def logPSNR(testImage, referenceImage):
    Lmin =0
    # print(referenceImage)
    testImageLuminance = max(testImage,Lmin)
    referenceImageLuminance = max(referenceImage, Lmin)
    mse = np.mean((log10(testImageLuminance)- log10(referenceImageLuminance)) ** 2)
    if (mse == 0):  # means that no noise present, logPSNR serves no importance here
        return 100
    Lmax = 10000     # as most HDR displays will not exceed this value.(according to Kai Linn's thesis)
    logPsnr = 10 * log10(log10(Lmax)/mse)
    return logPsnr

def main():
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # Loading images (original image and compressed image)
    # original = cv2.imread(os.path.join(dir_path, 'original_image.png'))
    # contrast = cv2.imread(os.path.join(dir_path, 'compressed_image.png'), 1)

    testImage = util.load_hdr('./generated_hdr_b_0_0.hdr')
    print(testImage)
    referenceImage = util.load_hdr('./gt_hdr_b_0_0.hdr')


    # Value expected: 29.73dB
    print("-- First Test --")
    print(f"PSNR value is {logPSNR(testImage, referenceImage)} dB")


    # # Value expected: 31.53dB (Wikipedia Example)
    # print("\n-- Second Test --")
    # print(f"PSNR value is {psnr(original2, contrast2)} dB")


if __name__ == '__main__':
    main()