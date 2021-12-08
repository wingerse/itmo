from tmo import reinhard, drago
from util import load_hdr_image, save_ldr_image

hdr = load_hdr_image("gen_linear.hdr")
tmo_reinhard = reinhard(hdr)
save_ldr_image(tmo_reinhard, "test_output/tmo_reinhard.jpg")
tmo_drago = drago(hdr)
save_ldr_image(tmo_drago, "test_output/tmo_drago.jpg")