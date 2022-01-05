import include_parent_path
from itmo.fhdr.train import train
import sys

sys.stdout.reconfigure(line_buffering=True)

if __name__ == "__main__":
    train("src/itmo/fhdr/checkpoints", "datasets/training_data_ours", iteration_count=1, batch_size=8)