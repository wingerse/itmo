from itmo.fhdr.train import train

train("itmo/fhdr/checkpoints/latest.ckpt", "../datasets/training_data", iteration_count=2, batch_size=6)