
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
import os
import cv2
import numpy as np

from fyp.src import util

def luminanceConversion(R, G, B):
    luminance = format(0.27*R + 0.67*G + 0.06*B, '.12g')
    return luminance

def logPSNR(testImageArray, referenceImageArray):
    Lmin =0
    # print(referenceImage)

    testImageLuminance = np.max(testImageArray,Lmin)
    # print(testImageLuminance, "bef")
    for i in range(len(testImageLuminance)):
        logVal=log10(testImageLuminance[i])
        testImageLuminance[i] = logVal
    # print(testImageLuminance, "aft")

    referenceImageLuminance = np.max(referenceImageArray, Lmin)
    # print(referenceImageLuminance, "befref")

    for i in range(len(referenceImageLuminance)):
        logVal=log10(referenceImageLuminance[i])
        referenceImageLuminance[i] = logVal
    # print(referenceImageLuminance, "aftref")
    # print(referenceImageLuminance, "referenceluminance")
    mse = np.mean((testImageLuminance -referenceImageLuminance) ** 2)
    if (mse == 0):  # means that no noise present, logPSNR serves no importance here
        return 100
    Lmax = 10000     # as most HDR displays will not exceed this value.(according to Kai Linn's thesis)
    logPsnr = 10 * log10(log10(Lmax)/mse)
    return logPsnr

def main():
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # Loading images (original image and compressed image)
    # original = cv2.imread(os.path.join(dir_path, 'original_image.png'))
    # print()
    # contrast = cv2.imread(os.path.join(dir_path, 'compressed_image.png'), 1)


    testImage = util.load_hdr_image('./generated_hdr_b_0_0.hdr')
    # print(testImage.shape[0])
    testImageArray = np.zeros([testImage.shape[0], testImage.shape[1]])
    # print('array',testImageArray)
    for h in range(len(testImage)):
        for w in range(len(testImage[h])):
            # print(testImage[h][w])
            # print(testImage[h][w])
            testImageArray[h][w] = luminanceConversion(testImage[h][w][0], testImage[h][w][1], testImage[h][w][2])
            # print(array[h][w])

        # print(testImage[h])
    # for h in testImage:
    #     for w in h:
    #         array[h][w] = luminanceConversion(testImage[h][w][0],testImage[h][w][1], testImage[h][w][2])
    # print(testImageArray)

    # print(np.mean(testImageArray))
    referenceImage = util.load_hdr_image('./gt_hdr_b_0_0.hdr')
    referenceImageArray = np.zeros([referenceImage.shape[0], referenceImage.shape[1]])
    # print('array', referenceImageArray)
    for h in range(len(referenceImage)):
        for w in range(len(referenceImage[h])):
            # print(testImage[h][w])
            # print(testImage[h][w])
            referenceImageArray[h][w] = luminanceConversion(referenceImage[h][w][0], referenceImage[h][w][1], referenceImage[h][w][2])
            # print(array[h][w]
    # print(referenceImageArray)

    # Value expected: 29.73dB
    # print("-- First Test --")
    print(f"log PSNR value is {logPSNR(testImageArray, referenceImageArray)} dB")


    # # Value expected: 31.53dB (Wikipedia Example)
    # print("\n-- Second Test --")
    # print(f"PSNR value is {psnr(original2, contrast2)} dB")


if __name__ == '__main__':
    main()