import include_parent_path
from tmo import reinhard, drago, mu_tonemap
from util import load_hdr_image, save_ldr_image
import numpy as np

THRESHOLD = 0.0001

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

    res_one_pixel = [[[1.0000, 1.0164, 1.0475]]]
    res_two_pixel = [[[1.0000, 1.0164, 1.0475], [1.0000, 1.0475, 1.0656]]]
    res_three_pixel = [[[1.0000, 1.0164, 1.0475], [1.0475, 1.0514, 1.0656], [1.0000, 1.0475, 1.0656]]]

    assert (one_pixel - res_one_pixel <= THRESHOLD).all()
    assert (two_pixel - res_two_pixel <= THRESHOLD).all()
    assert (three_pixel - res_three_pixel <= THRESHOLD).all()


def test_drago():
    one_pixel = np.array([[[1.0, 1.3, 2.0]]])
    two_pixel = np.array([[[1.0, 1.3, 2.0], [1.0, 2.0, 2.5]]])
    three_pixel = np.array([[[1.0, 1.3, 2.0], [2.0, 2.1, 2.5], [1.0, 2.0, 2.5]]])

    one_pixel = drago(one_pixel)
    two_pixel = drago(two_pixel)
    three_pixel = drago(three_pixel)

    res_one_pixel = [[[0.7297, 0.8221, 1.0000]]]
    res_two_pixel = [[[0.6964, 0.7846, 0.9543], [0.6593, 0.9035, 1.0000]]]
    res_three_pixel = [[[0.6945, 0.7825, 0.9517], [0.8763, 0.8960, 0.9699], [0.6593, 0.9035, 1.0000]]]

    assert (one_pixel - res_one_pixel <= THRESHOLD).all()
    assert (two_pixel - res_two_pixel <= THRESHOLD).all()
    assert (three_pixel - res_three_pixel <= THRESHOLD).all()

def test_reinhard():
    one_pixel = np.array([[[1.0, 1.3, 2.0]]])
    two_pixel = np.array([[[1.0, 1.3, 2.0], [1.0, 2.0, 2.5]]])
    three_pixel = np.array([[[1.0, 1.3, 2.0], [2.0, 2.1, 2.5], [1.0, 2.0, 2.5]]])

    one_pixel = reinhard(one_pixel)
    two_pixel = reinhard(two_pixel)
    three_pixel = reinhard(three_pixel)

    res_one_pixel = [[[0.7297, 0.8221, 1.0000]]]
    res_two_pixel = [[[0.6748, 0.7602, 0.9247], [0.6593, 0.9035, 1.0000]]]
    res_three_pixel = [[[0.6733, 0.7586, 0.9227], [0.8912, 0.9112, 0.9864], [0.6593, 0.9035, 1.0000]]]

    assert (one_pixel - res_one_pixel <= THRESHOLD).all()
    assert (two_pixel - res_two_pixel <= THRESHOLD).all()
    assert (three_pixel - res_three_pixel <= THRESHOLD).all()
