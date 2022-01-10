"""
Script to train the model using our dataset.  
"""
import include_parent_path
from itmo.fhdr.train import train
import sys
import argparse

if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)

    p = argparse.ArgumentParser(description="Train FHDR model", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--dataset_path", default="datasets/training_data_ours", help="Path of training dataset")
    p.add_argument("--batch_size", type=int, default=8, help="Batch size")

    args = p.parse_args()

    train("src/itmo/fhdr/checkpoints", args.dataset_path, batch_size=args.batch_size)