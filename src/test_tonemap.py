from tmo.reinhard import reinhard
from util import load_image, save_ldr_image
import cv2

hdr = load_image("../images/Oxford_Church.hdr")
ldr = reinhard(hdr, 0.18)
save_ldr_image(ldr, "tmo.jpg")

aspect_ratio = ldr.shape[0] / ldr.shape[1]
ldr = cv2.resize(ldr, (600, int(600 * aspect_ratio)), interpolation=cv2.INTER_CUBIC)
cv2.imshow("ldr", cv2.cvtColor(ldr, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)