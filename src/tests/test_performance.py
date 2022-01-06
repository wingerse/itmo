import include_parent_path
from itmo import linear, fhdr
from tmo import drago
from tmo.reinhard import reinhard
from util import load_hdr_image, save_hdr_image, save_ldr_image, load_ldr_image
import numpy as np
import pytest
import os
from quality import evaluation_metric
import time
from timeit import default_timer


def running_function1():
    ldr = load_ldr_image("test_images/ldr_test.png")

    hdr = fhdr(ldr, f"src/itmo/fhdr/checkpoints/ours.ckpt")
    save_hdr_image(hdr, "test_outputs/fhdr.hdr")

    hdr_t = reinhard(hdr)
    save_ldr_image(hdr_t, "test_outputs/fhdr.png")
    assert os.path.isfile("test_outputs/fhdr.hdr") == True
    assert os.path.isfile("test_outputs/fhdr.png") == True

    gt_hdr = load_hdr_image("test_images/hdr_test.hdr")
    ground_truth_tmo = reinhard(gt_hdr)
    # print(evaluationMetric.PSNR(hdr_t,ground_truth_tmo))
    # print(evaluationMetric.PSNR(ldr, ground_truth_tmo))
    assert evaluation_metric.psnr(hdr_t, ground_truth_tmo) > evaluation_metric.psnr(ldr, ground_truth_tmo)
    assert evaluation_metric.ssim(hdr_t, ground_truth_tmo) > evaluation_metric.ssim(ldr, ground_truth_tmo)


# print(test_itmo())
def test_benchmark(benchmark):
    benchmark(running_function1)


def running_function2(filename):
    ldr = load_ldr_image("test_images/" + filename)
    hdr = fhdr(ldr, f"src/itmo/fhdr/checkpoints/ours.ckpt")
    save_ldr_image(drago(hdr), "test_outputs/" + filename)


def test_time_for_four_runs():
    t = default_timer()
    running_function2("ldr_test.png")
    t = default_timer() - t
    print(t)
    t = default_timer()
    running_function2("ldr_test2.jpg")
    t = default_timer() - t
    print(t)
    t = default_timer()
    running_function2("ldr_test2.jpg")
    t = default_timer() - t
    print(t)
    t = default_timer()
    running_function2("ldr_test3.jpg")
    t = default_timer() - t
    print(t)