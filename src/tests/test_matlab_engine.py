import include_parent_path
import matlab.engine

def test_matlab_engine():
    assert len(matlab.engine.find_matlab()) > 0

    eng = matlab.engine.connect_matlab()
    assert callable(eng.calculate_q_score) is True

def test_q_score():
    eng = matlab.engine.connect_matlab()
    img1 = '../../test_images/139.hdr'
    assert eng.calculate_q_score(img1, img1) == 10

    img2 = '../../test_images/hdr_test.hdr'
    img3 = '../../test_images/gt_hdr.hdr'
    assert (0 <= eng.calculate_q_score(img2, img3) <= 10) is True
