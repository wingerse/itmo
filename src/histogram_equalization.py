# Code taken from https://github.com/samsudinng/cv_histogram_equalization/tree/master/demo_notebook and is bound to changes later


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


img_filename = 'Unequalized_Hawkes_Bay_NZ.jpg'
save_filename = 'Equalized_Hawkes_Bay_NZ.jpg'

#load file as pillow Image
img = Image.open(img_filename)

# convert to grayscale
imgray = img.convert(mode='L')

#convert to NumPy array
img_array = np.asarray(imgray)

#flatten image array and calculate histogram via binning
histogram_array = np.bincount(img_array.flatten(), minlength=256)

#normalize
num_pixels = np.sum(histogram_array)
histogram_array = histogram_array/num_pixels

#cumulative histogram
chistogram_array = np.cumsum(histogram_array)


# flatten image array into 1D list
img_list = list(img_array.flatten())

# transform pixel values to equalize
eq_img_list = [transform_map[p] for p in img_list]

# reshape and write back into img_array
eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)


# Let's plot the histograms

#histogram and cumulative histogram of original image has been calculated above
ori_cdf = chistogram_array
ori_pdf = histogram_array

#calculate histogram and cumulative histogram of equalized image
eq_histogram_array = np.bincount(eq_img_array.flatten(), minlength=256)
num_pixels = np.sum(eq_histogram_array)
eq_pdf = eq_histogram_array/num_pixels
eq_cdf = np.cumsum(eq_pdf)

#plot
plt.figure()
plt.plot(ori_pdf)
plt.plot(eq_pdf)
plt.xlabel('Pixel intensity')
plt.ylabel('Distribution')
plt.legend(['Original','Equalized'])
plt.figure()
plt.plot(ori_cdf)
plt.plot(eq_cdf)
plt.xlabel('Pixel intensity')
plt.ylabel('Distribution')
plt.legend(['Original','Equalized'])


eq_img = Image.fromarray(eq_img_array, mode='L')
eq_img.save(save_filename)

