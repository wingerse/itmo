import include_parent_path
from tmo import reinhard, drago, mu_tonemap
from util import load_hdr_image, save_ldr_image

def test_tonemap():
    hdr = load_hdr_image("datasets/aug_dataset/hdr/100.hdr")
    print(hdr.min(), hdr.max())
    tmo_reinhard = reinhard(hdr)
    save_ldr_image(tmo_reinhard, "test_outputs/tmo_reinhard.jpg")
    tmo_drago = drago(hdr)
    save_ldr_image(tmo_drago, "test_outputs/tmo_drago.jpg")


def test_mu_tonemap():
    directory = "../../test_images/143.hdr"
    hdr = load_hdr_image(directory)

    img = hdr[0][0]
    hdr_t = mu_tonemap(img)

    res = [10315, 10333, 10294]

    for i in range(len(hdr_t)):
        assert int(hdr_t[i] * 10000) == res[i]


def test_drago():
    directory = "../../test_images/143.hdr"
    hdr = load_hdr_image(directory)

    img = hdr[0][0]
    ldr = drago(img)

    res = [9892, 10000, 9760]

    for i in range(len(ldr)):
        assert int(ldr[i] * 10000) == res[i]

def test_reinhard():
    directory = "../../test_images/143.hdr"
    hdr = load_hdr_image(directory)

    img = hdr[0][0]
    ldr = reinhard(img)

    res = [9892, 10000, 9760]

    for i in range(len(ldr)):
        assert int(ldr[i] * 10000) == res[i]