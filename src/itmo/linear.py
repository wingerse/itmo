from util import remove_gamma, luminance, change_luminance

def linear(img, k=100):
    """
    Linear ITMO. 

    :param img: LDR image.  
    :param k: How much to stretch, default 100.
    :return: HDR image.  
    """

    img = remove_gamma(img)
    l = luminance(img)
    l_h = l * k
    img = change_luminance(img, l, l_h) 
    return img