import numpy as np

def drago(img, max_output_lumi=100, bias=0.85, lwa=None, b_warning=1):
    check_13_color(img)
    check_negative(img)

    lumi = lum(img)

    if lwa is None:
        lwa = log_mean(lumi)

    lwa = lwa / ((1 + bias - 0.85) ^ 5)

    l_max = np.amax(lumi.flatten())

    l_s = lumi / lwa
    l_max_s = l_max / lwa

    c = np.log(bias) / np.log(0.5)
    p1 = (max_output_lumi / 100) / (np.log10(1 + l_max_s))
    p2 = np.log(1 + l_s) / np.log(2 + 8 * ((l_s / l_max_s) ** c))
    new_lumi = p1 * p2

    img_out = change_luminance(img, lumi, new_lumi)

    return img_out

def log_mean(img):
    """
    This function computes the geometric mean
    :param img:
    :return:
    """
    delta = np.exp(-6)
    img_delta = np.log(img + delta)
    l_mean = np.exp(np.mean(img_delta.flatten()))

    # delta = exp(-6)
    # img_delta = [0] * len(img)
    # for i in range(len(img)):
    #     row = [0] * len(img[i])
    #     for j in range(len(img[i])):
    #         row[j] = log(img[i][j] + delta)
    #     img_delta[i] = row
    #
    # count = 0
    # total = 0
    # for i in range(len(img_delta)):
    #     for j in range(len(img_delta[i])):
    #         total += img_delta[i][j]
    #         count += 1
    #
    # mean = total / count
    #
    # l_mean = exp(mean)

    return l_mean

def remove_specials(img, clamping_value=0):
    """
    This function is used to remove inf or NaN values
    :param img: array of floating values
    :param clamping_value:
    :return: array of floating values without special values
    """
    img[~np.isfinite(img)] = clamping_value

    # without numpy
    # for i in range(len(img)):
    #     for j in range(len(img[i])):
    #         if img[i][j] == inf or img[i][j] is None:
    #             img[i][j] = clamping_value
    return img

def check_13_color(img):
    """
    This function is used to ensure image is either 1 or 3 color channels image
    :param img:
    :return:
    """
    n = 3
    col = img.shape[n-1]
    if col != 3 and col != 1:
        # raise Exception("The image has to be an RGB or luminance image")
        return False
    else:
        return True

def check_negative(img):
    """
    This function is used to check if img contains any negative values
    :param img:
    :return:
    """
    return np.any(img < 0)

def lum(img):
    # This function calculates the luminance
    # img: an RGB image
    # return luminance as XYZ color

    n = 3
    col = img.shape[n-1]

    if col == 1:
        lumi = img
    elif col == 3:
        lumi = 0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]
    else:
        lumi = np.mean(img, 3)

    return lumi

def change_luminance(img, lumi, new_lumi):
    n = 3
    col = img.shape[n - 1]
    col_new = new_lumi.shape[n - 1]

    img_out = np.zeros(img.shape)

    if col_new == 1:
        for i in range(col):
            img_out[:, :, i] = (img_out[:, :, i] * new_lumi) / lumi
    elif col_new == 3:
        if col == col_new:
            for i in range(col):
                img_out[:, :, i] = (img_out[:, :, i] * new_lumi[:, :, i]) / lumi
        else:
            new_lumi = lum(new_lumi)
            for i in range(col):
                img_out[:, :, i] = (img_out[:, :, i] * new_lumi) / lumi
    else:
        new_lumi = lum(new_lumi)
        for i in range(col):
            img_out[:, :, i] = (img_out[:, :, i] * new_lumi) / lumi

    img_out = remove_specials(img_out)
    return img_out
