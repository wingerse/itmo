from itmo.fhdr.test import test

if __name__ == "__main__":
    psnr, ssim = test("itmo/fhdr/checkpoints/epoch_200.ckpt", "../datasets/fhdr dataset/256", "test_output/fhdr")
    print(f"PSNR: {psnr} dB")
    print(f"SSIM: {ssim}")