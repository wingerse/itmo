"""
usage: run_fhdr_script.py [-h] ldr_path hdr_path

Run FHDR

positional arguments:
  ldr_path    Path of LDR image
  hdr_path    Path of output HDR image

optional arguments:
  -h, --help  show this help message and exit
"""
import include_parent_path
from run_fhdr import run_fhdr
import argparse

p = argparse.ArgumentParser(description="Run FHDR", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("ldr_path", help="Path of LDR image")
p.add_argument("hdr_path", help="Path of output HDR image")

args = p.parse_args()

run_fhdr(args.ldr_path, args.hdr_path)