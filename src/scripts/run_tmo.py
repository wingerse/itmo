"""
usage: run_tmo.py [-h] [--tmo {reinhard,drago}] hdr_path ldr_path

Run a TMO

positional arguments:
  hdr_path              Path of HDR image
  ldr_path              Path of output LDR image

optional arguments:
  -h, --help            show this help message and exit
  --tmo {reinhard,drago}
                        What tmo to use (default: reinhard)
"""
import include_parent_path
import argparse
from util import load_hdr_image, save_ldr_image
from tmo import drago, reinhard

p = argparse.ArgumentParser(description="Run a TMO", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("--tmo", help="What tmo to use", choices=["reinhard", "drago"], default="reinhard")
p.add_argument("hdr_path", help="Path of HDR image")
p.add_argument("ldr_path", help="Path of output LDR image")

args = p.parse_args()

#selection the tmo operator to be used by user
if args.tmo == "reinhard":
  tmo_func = reinhard
else:
  tmo_func = drago

hdr = load_hdr_image(args.hdr_path)
ldr = tmo_func(hdr)
save_ldr_image(ldr, args.ldr_path)