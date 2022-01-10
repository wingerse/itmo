"""
usage: run_itmo.py [-h] [--itmo {linear,fhdr}] [--tmo {reinhard,drago}] ldr_path hdr_path

Run an ITMO

positional arguments:
  ldr_path              Path of LDR image
  hdr_path              Path of output HDR image

optional arguments:
  -h, --help            show this help message and exit
  --itmo {linear,fhdr}  What itmo to use (default: fhdr)
  --tmo {reinhard,drago}
                        What tmo to use (default: reinhard)
"""
import include_parent_path
import argparse
from util import load_ldr_image, save_hdr_image, save_ldr_image
from itmo import fhdr, linear
from tmo import drago, reinhard

p = argparse.ArgumentParser(description="Run an ITMO", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("--itmo", help="What itmo to use", choices=["linear", "fhdr"], default="fhdr")
p.add_argument("--tmo", help="What tmo to use", choices=["reinhard", "drago"], default="reinhard")
p.add_argument("ldr_path", help="Path of LDR image")
p.add_argument("hdr_path", help="Path of output HDR image")

args = p.parse_args()


# selecting the itmo
if args.itmo == "linear":
  itmo_func = linear
else:
  itmo_func = fhdr


# selecting tmo
if args.tmo == "reinhard":
  tmo_func = reinhard
else:
  tmo_func = drago

ldr = load_ldr_image(args.ldr_path)
hdr = itmo_func(ldr)
hdr_tmo = tmo_func(hdr)
save_hdr_image(hdr, args.hdr_path)
save_ldr_image(hdr_tmo, args.hdr_path.replace(".hdr", ".jpg"))