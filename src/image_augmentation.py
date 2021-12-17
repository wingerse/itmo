import cv2
from random import random, uniform, randrange
import numpy as np
from util import apply_gamma, luminance

def log_tonemap(l):
    return np.log(l + 1) / np.log(l.max() + 1)

def inverse_log_tonemap(l, max):
    return np.exp((l * np.log(max + 1))) - 1

MIN_FRAC = 0.2
MAX_FRAC = 0.6
MIN_LOSS = 0.05
MAX_LOSS = 0.1

def change_exposure(img):
    l = luminance(img)
    max_ = l.max()

    l_d = log_tonemap(l)
    hist, edges = np.histogram(l_d, bins=img.size)

    loss = uniform(MIN_LOSS, MAX_LOSS)
    bright = random() <= 0.5

    pixel_count = 0
    edge = None
    rng = range(len(hist)-1, -1, -1) if bright else range(0, len(hist))
    for i in rng:
        edge = edges[i] if bright else edges[i+1]
        pixel_count += hist[i]
        if pixel_count/l_d.size >= loss:
            break

    edge = inverse_log_tonemap(edge, max_)

    if bright:
        img = img / edge
        img = img.clip(0, 1)
    else:
        img = img - edge
        img = img.clip(0, None)
        img /= img.max()
    return img

def crf(img):
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
    frac = uniform(MIN_FRAC, MAX_FRAC)
    scene_size = int(frac * min(img.shape[0], img.shape[1]))
    pos_y = randrange(0, img.shape[0]-scene_size)
    pos_x = randrange(0, img.shape[1]-scene_size)

    img = img[pos_y:pos_y+scene_size, pos_x:pos_x+scene_size]
    hdr = cv2.resize(img, (size, size), interpolation=cv2.INTER_LINEAR)
    if random() <= 0.5:
        hdr = cv2.flip(hdr, 1)
    ldr = change_exposure(hdr)
    ldr = crf(ldr)
    ldr = apply_gamma(ldr)
    return ldr, hdr

def augment_images(img, count_per_mp, size):
    n = int((img.shape[0]*img.shape[1]) / 1e6 * count_per_mp)
    return (augment(img, size) for _ in range(n))
