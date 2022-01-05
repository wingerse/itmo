import cv2
from random import random, uniform, randrange
import numpy as np
from util import apply_gamma, luminance

MIN_FRAC = 0.2 # minimum fraction of the image to crop
MAX_FRAC = 0.6 # maximum fraction of the image to crop
MIN_LOSS = 0.05 # minimum fraction of the image to lose information
MAX_LOSS = 0.1 # maximum fraction of the image to lose information

def change_exposure(img, bright):
    """
    Change exposure of the image such that there is over-saturation or undersaturation and information is lost. 
    :param img: The image.
    :param bright: Whether to oversaturate. If false, undersaturate. 
    :return: The resulting image.  
    """
    
    # calculate histogram of the image
    hist, edges = np.histogram(img, bins=img.size)

    # find a random fraction to lose information
    loss = uniform(MIN_LOSS, MAX_LOSS)

    pixel_count = 0
    edge = None
    # if oversaturation, start from the end of histogram, else start from the beginning
    rng = range(len(hist)-1, -1, -1) if bright else range(0, len(hist))
    # find the first pixel value (edge) such that the fraction of pixels which have 
    # values >= to this value is >= loss. 
    for i in rng:
        edge = edges[i] if bright else edges[i+1]
        pixel_count += hist[i]
        if pixel_count/img.size >= loss:
            break

    if bright:
        # if oversaturating, scale up the image such that the edge becomes 1
        img = img / edge
        img = img.clip(0, 1)
    else:
        # if undersaturating, shift the image such that edge becomes 0 and then scale it back so that values are 0-1
        img = img - edge
        img = img.clip(0, None)
        img /= img.max()
    return img

def crf(img):
    """
    Apply a random camera response function to the image. 
    """

    n_mean = 0.9
    n_std = 0.1
    a_mean = 0.6
    a_std = 0.1

    n = np.clip(np.random.normal(n_mean, n_std), 0.2, 2.5)
    a = np.clip(np.random.normal(a_mean, a_std), 0.0, 5.0)
    p = img ** n
    img = (1 + a) * (p / (p + a))
    return img

def augment(img, size):
    """
    Synthesize a random LDR-HDR crop from the image with a given square image size (eg: 256). 
    """

    # do a random crop of the image between MIN_FRAC and MAX_FRAC
    frac = uniform(MIN_FRAC, MAX_FRAC)
    scene_size = int(frac * min(img.shape[0], img.shape[1]))
    pos_y = randrange(0, img.shape[0]-scene_size)
    pos_x = randrange(0, img.shape[1]-scene_size)
    img = img[pos_y:pos_y+scene_size, pos_x:pos_x+scene_size]

    # resize the image according to the given size
    hdr = cv2.resize(img, (size, size), interpolation=cv2.INTER_LINEAR)

    # randomly flip
    if random() <= 0.5:
        hdr = cv2.flip(hdr, 1)

    # randomly oversaturate or undersaturate. 
    bright = random() <= 0.5
    ldr = change_exposure(hdr, bright)
    # apply camera response function
    ldr = crf(ldr)
    # apply gamma curve
    ldr = apply_gamma(ldr)
    return ldr, hdr

def augment_images(img, count_per_mp, size):
    """
    Augment many images from a single image. 
    :param img: The source image.  
    :param count_per_mp: How many images to augment per mega pixel.  
    :param size: Size of synthesized images.  
    :return: Generator of augmented images.  
    """

    n = int((img.shape[0]*img.shape[1]) / 1e6 * count_per_mp)
    return (augment(img, size) for _ in range(n))
