# This file carries out histogram equalization technique.
# The code was taken from https://medium.com/@kyawsawhtoon/a-tutorial-to-histogram-equalization-497600f270e2

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