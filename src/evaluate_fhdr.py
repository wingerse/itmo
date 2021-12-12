from itmo.fhdr.test import test

psnr, ssim = test("itmo/fhdr/checkpoints/FHDR-iter-2.ckpt", "../datasets/training_data_test", "test_output/fhdr")
print(f"PSNR: {psnr} dB")
print(f"SSIM: {ssim}")