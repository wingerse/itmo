import cv2
import numpy as np

MAX_IMAGE_HEIGHT = 700
MAX_IMAGE_WIDTH = 600

def _load_image(path):
    """
    Load any kind of image from the path (without processing)
    """

    i = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if i is None:
        raise Exception(f"invalid path: {path}")
    i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    return i.astype(np.float32)

def load_ldr_image(path):
    """
    Load an LDR image from the path. Image values are in range [0, 1]
    """

    i = _load_image(path)
    return i / 255

def load_hdr_image(path):
    """
    Load an HDR image from the path. Image values are in range [0, ∞]
    """

    return _load_image(path).clip(0, None)

def _save_image(img, path):
    """
    Save any kind of image to the path.  
    """

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if not cv2.imwrite(path, img):
        raise Exception(f"count not save image to {path}")

def save_hdr_image(img, path):
    """
    Save an HDR image to the path. 
    """

    _save_image(img, path)

def save_ldr_image(img, path):
    """
    Save an LDR image to the path. 
    """

    _save_image((img * 255).astype(np.uint8), path)

def remove_gamma(img):
    """ 
    Remove gamma curve from the image.
    """

    return img ** 2.2

def apply_gamma(img):
    """
    Apply gamma curve to the image. 
    """

    return img ** (1/2.2)

def luminance(img):
    """ 
    Get luminance map of image 
    """

    return 0.27*img[..., 0] + 0.67*img[..., 1] + 0.06*img[..., 2]

def change_luminance(img, old_l, new_l):
    """ 
    change luminance of image given old and new luminance maps.
    """

    img = img.copy()
    ratio = np.divide(new_l, old_l, out=np.zeros_like(new_l), where=(old_l != 0))
    for i in range(0, 3):
        img[..., i] = img[..., i] * ratio
    return img

def scale_image(img, height, width):
    """
    Downscale an image if any of its dimensions exceed the limit or 
    upscale an image if both of its dimensions are under the limit.
    Aspect ratio is preserved.
    """
    # scale according to the dimension that is 
    # furthest away from the limit (when downscaling)
    # closest to the limit (when upscaling)
    if (MAX_IMAGE_HEIGHT / height) < (MAX_IMAGE_WIDTH / width):
        scale = MAX_IMAGE_HEIGHT / height
    else:           
        scale = MAX_IMAGE_WIDTH / width  
    
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dim = (width, height)

    # resize image
    scaled_image = cv2.resize(img, dim)
    return scaled_image, height, width