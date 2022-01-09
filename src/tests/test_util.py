import include_parent_path
from tmo.util import logmean
from util import apply_gamma, change_luminance, load_hdr_image, remove_gamma, save_hdr_image, save_ldr_image, load_ldr_image, luminance, _load_image, _save_image
from quality import evaluation_metric
import numpy as np
import pytest
from itmo.fhdr.util import preprocess_hdr, preprocess_ldr, unpreprocess_hdr, unpreprocess_ldr
import torch

# test luminance
def test_one_pixel_luminance():
    assert luminance(np.array([[[0.1,0.2,0.3]]])) == [[0.179]]
    assert luminance(np.array([[[0.2, 0.3, 0.4]]])) == [[0.279]]


def test_four_pixel_luminance():
    # testing on (2,2,3) dimension
    assert (luminance(np.array([[[0.1, 0.2, 0.3],[0.1, 0.2, 0.3]],[[0.1, 0.2, 0.3],[0.1, 0.2, 0.3]]])) == [[0.179, 0.179],[0.179, 0.179]]).all() == True


# test loading image
def test_load_existing_ldr_image():

    ldr_img_path = "test_images/ldr_test.png"
    img =load_ldr_image(ldr_img_path)
    assert (0 <= img).all() and (img<= 1).all()



def test_load_non_existing_ldr_image():

    ldr_img_path = "test_images/ldr_tst.png"
    try:
        load_ldr_image(ldr_img_path)
    except Exception as e:
        assert str(e) == f"invalid path: {ldr_img_path}"


def test_load_existing_hdr_image():
    hdr_img_path = "test_images/hdr_test.hdr"
    img =load_hdr_image(hdr_img_path)
    assert (img>=0).all()
    # assert os.path.isfile("../images/hdr_test.hdr") == True


def test_load_non_existing_hdr_image():
    hdr_img_path = "test_images/hdr_tst.hdr"
    try:
        load_hdr_image(hdr_img_path)
    except Exception as e:
        assert str(e) == f"invalid path: {hdr_img_path}"

def test_equal_save_image():
    """
    Testing if the np array values of the original image and saved copy of same image is the same. Assert statement should return True
    :return:None
    """

    img_path = "test_images/hdr_test.hdr"
    frst_image = _load_image(img_path)
    _save_image(frst_image,"test_images/test_save_function.hdr")
    saved_img = _load_image ("test_images/test_save_function.hdr")
    assert (np.array(frst_image) == np.array(saved_img)).all() ==True


# test saving image
def test_unequal_saved_image():
    """
    Testing if the np array values of the original image and saved copy of a different image is the same. Assert statement should return false
    :return:None
    """

    img_path = "test_images/hdr_test2.hdr"
    frst_image = _load_image(img_path)
    _save_image(frst_image,"test_images/test2_save_function.hdr")
    saved_img = _load_image ("test_images/test2_save_function.hdr")
    unequal_img_path = "test_images/hdr_test.hdr"
    unequal_img = _load_image(unequal_img_path)
    assert (np.array(unequal_img) == np.array(saved_img)).all() ==False

def test_logmean():
    l = np.array([
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 100.0],
    ])

    l = logmean(l)
    # calculate logmean by hand and check if its the same
    assert l == 2.682825957054137

def test_apply_gamma():
    # 0.0 is the smallest, 0.5 is the middle, 1.0 is the max, covering all values
    ldr = np.array([[[0.0, 0.5, 1.0]]])
    ldr = apply_gamma(ldr)
    assert ldr[0, 0, 0] == 0.0
    # is close enough
    assert ldr[0, 0, 1] - 0.72974005284072 <= 0.00000000000001
    assert ldr[0, 0, 2] == 1.0

def test_remove_gamma():
    # 0.0 is the smallest, 0.5 is the middle, 1.0 is the max, covering all values
    ldr = np.array([[[0.0, 0.5, 1.0]]])
    ldr = remove_gamma(ldr)
    assert ldr[0, 0, 0] == 0.0
    # is close enough
    assert ldr[0, 0, 1] - 0.21763764082403 <= 0.00000000000001
    assert ldr[0, 0, 2] == 1.0

def test_preprocess_ldr():
    # 0 is the smallest, 0.5 is the middle and 1.0 is the maximum
    # covering all cases
    ldr = np.array([[[0.0, 0.5, 1.0]]])
    ldr = apply_gamma(ldr)
    ldr_p = preprocess_ldr(ldr)
    # is a tensor
    assert type(ldr_p) == torch.Tensor
    # is properly scaled and color channel is the first dimension
    assert ldr_p[0, 0, 0].item() == -1.0
    # this scaling is a result of quantizing 0.5 * 255 to uint8
    assert ldr_p[1, 0, 0].item() - -0.003921568 <= 0.00000001
    assert ldr_p[2, 0, 0].item() == 1.0

def test_unpreprocess_ldr():
    # -1 is the smallest, 0.0 is the middle and 1.0 is the maximum
    # covering all cases
    ldr = torch.tensor([[[-1.0]], [[0.0]], [[1.0]]])
    ldr = unpreprocess_ldr(ldr)
    ldr = remove_gamma(ldr)

    # is a numpy array
    assert type(ldr) == np.ndarray
    # and is scaled properly
    assert ldr[0, 0, 0] == 0.0
    assert ldr[0, 0, 1] - 0.5 <= 0.0000001
    assert ldr[0, 0, 2] == 1.0

def test_preprocess_hdr():
    # 0 is the smallest, 0.5 is the middle and 1.0 is the maximum
    # covering all cases
    hdr = np.array([[[0.0, 0.5, 1.0]]])
    hdr = preprocess_hdr(hdr)

    # is a tensor
    assert type(hdr) == torch.Tensor
    # is scaled properly and color channel is the first dimension
    assert hdr[0, 0, 0] == -1.0
    assert hdr[1, 0, 0] == 0.0
    assert hdr[2, 0, 0] == 1.0

def test_unpreprocess_hdr():
    # -1.0 is the smallest, 0.0 is the middle and 1.0 is the maximum
    # covering all cases
    hdr = torch.tensor([[[-1.0]], [[0.0]], [[1.0]]])
    hdr = unpreprocess_hdr(hdr)

    # is a numpy array
    assert type(hdr) == np.ndarray
    # and is scaled properly
    assert hdr[0, 0, 0] == 0.0
    assert hdr[0, 0, 1] == 0.5
    assert hdr[0, 0, 2] == 1.0

def test_change_luminance():
    # change luminance and check if luminance is infact equal to what we changed it to
    img = np.array([[[0.0, 0.5, 1.0]]])
    l_old = luminance(img)
    l_new = np.array([[0.69420]])
    img = change_luminance(img, l_old, l_new)
    assert luminance(img)[0, 0] == 0.69420