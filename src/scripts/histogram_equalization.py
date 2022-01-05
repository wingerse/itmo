# Code taken from https://github.com/samsudinng/cv_histogram_equalization/tree/master/demo_notebook and is bound to changes later


# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
#
#
# img_filename = 'Unequalized_Hawkes_Bay_NZ.jpg'
# save_filename = 'Equalized_Hawkes_Bay_NZ.jpg'
#
# #load file as pillow Image
# img = Image.open(img_filename)
#
# # convert to grayscale
# imgray = img.convert(mode='L')
#
# #convert to NumPy array
# img_array = np.asarray(imgray)
#
# #flatten image array and calculate histogram via binning
# histogram_array = np.bincount(img_array.flatten(), minlength=256)
#
# #normalize
# num_pixels = np.sum(histogram_array)
# histogram_array = histogram_array/num_pixels
#
# #cumulative histogram
# chistogram_array = np.cumsum(histogram_array)
# transform_map = np.floor(255 * chistogram_array).astype(np.uint8)
#
# # flatten image array into 1D list
# img_list = list(img_array.flatten())
#
# # transform pixel values to equalize
# eq_img_list = [transform_map[p] for p in img_list]
#
# # reshape and write back into img_array
# eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)
#
#
# # Let's plot the histograms
#
# #histogram and cumulative histogram of original image has been calculated above
# ori_cdf = chistogram_array
# ori_pdf = histogram_array
#
# #calculate histogram and cumulative histogram of equalized image
# eq_histogram_array = np.bincount(eq_img_array.flatten(), minlength=256)
# num_pixels = np.sum(eq_histogram_array)
# eq_pdf = eq_histogram_array/num_pixels
# eq_cdf = np.cumsum(eq_pdf)
#
# #plot
# plt.figure()
# plt.plot(ori_pdf)
# plt.plot(eq_pdf)
# plt.xlabel('Pixel intensity')
# plt.ylabel('Distribution')
# plt.legend(['Original','Equalized'])
# plt.figure()
# plt.plot(ori_cdf)
# plt.plot(eq_cdf)
# plt.xlabel('Pixel intensity')
# plt.ylabel('Distribution')
# plt.legend(['Original','Equalized'])
#
#
# eq_img = Image.fromarray(eq_img_array, mode='L')
# eq_img.save(save_filename)
#
#

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def histogram_equalization(img):
    img = cv.imread(img)
    img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:, :, 0] = cv.equalizeHist(img_yuv[:, :, 0])

    # convert the YUV image back to RGB format
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)

    show_image_comparison(img, img_output)
    show_plot(img)
    show_plot(img_output)
    return img

def show_plot(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()
    return

def show_image_comparison(img, img_output):
    cv.imshow('Color input image', img)
    cv.imshow('Histogram equalized', img_output)
    # cv.imshow("equalizeHist", np.hstack((img, img_output)))
    return

if __name__ == "__main__":
    histogram_equalization('test_images/ldr_test3.jpg')