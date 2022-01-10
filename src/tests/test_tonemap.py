import include_parent_path
from tmo import reinhard, drago, mu_tonemap
from util import load_hdr_image, save_ldr_image
import numpy as np

def test_tonemap():
    hdr = load_hdr_image("datasets/aug_dataset/hdr/100.hdr")
    print(hdr.min(), hdr.max())
    tmo_reinhard = reinhard(hdr)
    save_ldr_image(tmo_reinhard, "test_outputs/tmo_reinhard.jpg")
    tmo_drago = drago(hdr)
    save_ldr_image(tmo_drago, "test_outputs/tmo_drago.jpg")


def test_mu_tonemap():
    one_pixel = np.array([[[1.0, 1.3, 2.0]]])
    two_pixel = np.array([[[1.0, 1.3, 2.0], [1.0, 2.0, 2.5]]])
    three_pixel = np.array([[[1.0, 1.3, 2.0], [2.0, 2.1, 2.5], [1.0, 2.0, 2.5]]])

    one_pixel = mu_tonemap(one_pixel)
    two_pixel = mu_tonemap(two_pixel)
    three_pixel = mu_tonemap(three_pixel)

    res_one_pixel = [[[10000, 10164, 10475]]]
    res_two_pixel = [[[10000, 10164, 10475], [10000, 10475, 10656]]]
    res_three_pixel = [[[10000, 10164, 10475], [10475, 10514, 10656], [10000, 10475, 10656]]]

    for i in range(len(one_pixel)):
        for j in range(len(one_pixel[i])):
            for k in range(len(one_pixel[i][j])):
                assert int(one_pixel[i][j][k] * 10000) == res_one_pixel[i][j][k]

    for i in range(len(two_pixel)):
        for j in range(len(two_pixel[i])):
            for k in range(len(two_pixel[i][j])):
                assert int(two_pixel[i][j][k] * 10000) == res_two_pixel[i][j][k]

    for i in range(len(three_pixel)):
        for j in range(len(three_pixel[i])):
            for k in range(len(three_pixel[i][j])):
                assert int(three_pixel[i][j][k] * 10000) == res_three_pixel[i][j][k]


def test_drago():
    one_pixel = np.array([[[1.0, 1.3, 2.0]]])
    two_pixel = np.array([[[1.0, 1.3, 2.0], [1.0, 2.0, 2.5]]])
    three_pixel = np.array([[[1.0, 1.3, 2.0], [2.0, 2.1, 2.5], [1.0, 2.0, 2.5]]])

    one_pixel = drago(one_pixel)
    two_pixel = drago(two_pixel)
    three_pixel = drago(three_pixel)

    res_one_pixel = [[[7297, 8221, 10000]]]
    res_two_pixel = [[[6964, 7846, 9543], [6593, 9035, 10000]]]
    res_three_pixel = [[[6945, 7825, 9517], [8763, 8960, 9699], [6593, 9035, 10000]]]

    for i in range(len(one_pixel)):
        for j in range(len(one_pixel[i])):
            for k in range(len(one_pixel[i][j])):
                assert int(one_pixel[i][j][k] * 10000) == res_one_pixel[i][j][k]

    for i in range(len(two_pixel)):
        for j in range(len(two_pixel[i])):
            for k in range(len(two_pixel[i][j])):
                assert int(two_pixel[i][j][k] * 10000) == res_two_pixel[i][j][k]

    for i in range(len(three_pixel)):
        for j in range(len(three_pixel[i])):
            for k in range(len(three_pixel[i][j])):
                assert int(three_pixel[i][j][k] * 10000) == res_three_pixel[i][j][k]

def test_reinhard():
    one_pixel = np.array([[[1.0, 1.3, 2.0]]])
    two_pixel = np.array([[[1.0, 1.3, 2.0], [1.0, 2.0, 2.5]]])
    three_pixel = np.array([[[1.0, 1.3, 2.0], [2.0, 2.1, 2.5], [1.0, 2.0, 2.5]]])

    one_pixel = reinhard(one_pixel)
    two_pixel = reinhard(two_pixel)
    three_pixel = reinhard(three_pixel)

    res_one_pixel = [[[7297, 8221, 10000]]]
    res_two_pixel = [[[6748, 7602, 9247], [6593, 9035, 10000]]]
    res_three_pixel = [[[6733, 7586, 9227], [8912, 9112, 9864], [6593, 9035, 10000]]]

    for i in range(len(one_pixel)):
        for j in range(len(one_pixel[i])):
            for k in range(len(one_pixel[i][j])):
                assert int(one_pixel[i][j][k] * 10000) == res_one_pixel[i][j][k]

    for i in range(len(two_pixel)):
        for j in range(len(two_pixel[i])):
            for k in range(len(two_pixel[i][j])):
                assert int(two_pixel[i][j][k] * 10000) == res_two_pixel[i][j][k]

    for i in range(len(three_pixel)):
        for j in range(len(three_pixel[i])):
            for k in range(len(three_pixel[i][j])):
                assert int(three_pixel[i][j][k] * 10000) == res_three_pixel[i][j][k]
