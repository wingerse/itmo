import include_parent_path
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image, luminance, _load_image, _save_image
from quality import evaluation_metric
import numpy as np
import pytest



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

