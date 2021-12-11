import cv2
import numpy as np

def _load_image(path):
    i = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if i is None:
        raise Exception("invalid path")
    i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    return i

def load_ldr_image(path):
    i = _load_image(path)
    return i / 255

def load_hdr_image(path):
    return _load_image(path).clip(0, None)

def _save_image(img, path):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, img)

def save_hdr_image(img, path):
    _save_image(img.astype(np.float32), path)

def save_ldr_image(img, path):
    _save_image((img * 255).astype(np.uint8), path)

def remove_gamma(img):
    return img ** 2.2

def apply_gamma(img):
    return img ** (1/2.2)

def luminance(img):
    """ luminance map of image """
    return 0.27*img[..., 0] + 0.67*img[..., 1] + 0.06*img[..., 2]

def change_luminance(img, old_l, new_l):
    """ change luminance of image given old and new luminance maps """
    img = img.copy()
    ratio = np.divide(new_l, old_l, out=np.zeros_like(new_l), where=(old_l != 0))
    for i in range(0, 3):
        img[..., i] = img[..., i] * ratio
    return img