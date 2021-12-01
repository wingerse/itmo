import cv2

def load_image(path):
    i = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if i is None:
        raise Exception("invalid path")
    i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    return i

def save_image(img, path):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, img)

def save_hdr_image(img, path):
    save_image(img, path)

def save_ldr_image(img, path):
    save_image(img * 255, path)

def remove_gamma(img):
    return img ** 2.2

def apply_gamma(img):
    return img ** (1/2.2)