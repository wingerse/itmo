import include_parent_path
from tmo.util import logmean
import numpy as np

def test_logmean():
    one_pixel = np.array([[[1.0, 1.3, 2.0]]])
    two_pixel = np.array([[[1.0, 1.3, 2.0], [1.0, 2.0, 2.5]]])
    three_pixel = np.array([[[1.0, 1.3, 2.0], [2.0, 2.1, 2.5],[1.0, 2.0, 2.5]]])

    result_1 = int(logmean(one_pixel) * 10000)
    result_2 = int(logmean(two_pixel) * 10000)
    result_3 = int(logmean(three_pixel) * 10000)

    assert result_1 == 13750
    assert result_2 == 15334
    assert result_3 == 17267
