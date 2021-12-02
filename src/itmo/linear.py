from util import remove_gamma, luminance, change_luminance

def linear(img, k=100):
    img = remove_gamma(img)
    l = luminance(img)
    l_h = l * k
    img = change_luminance(img, l, l_h) 
    return img