import include_parent_path
from tmo.util import logmean
from util import load_hdr_image

def test_logmean():
    directory = "../../test_images/143.hdr"
    hdr = load_hdr_image(directory)
    one_pixel_1 = hdr[0][0]
    one_pixel_2 = hdr[0][1]

    result_1 = int(logmean(one_pixel_1) * 10000)
    result_2 = int(logmean(one_pixel_2) * 10000)

    assert result_1 == 16142
    assert result_2 == 14311
