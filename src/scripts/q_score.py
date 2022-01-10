"""
usage: q_score.py {directory}

Script to calculate Q-Score
"""
import include_parent_path
import matlab.engine
import os
import sys

# Get the directory from command prompt
directory = sys.argv[1]
# Connecting Python to MATLAB
eng = matlab.engine.connect_matlab()

# Changing working directory
os.chdir('src/hdrvdp')
eng.cd(os.getcwd())

# List of folders for comparison
folders = ['gt_hdr', 'hdr', 'ldr']

# Getting the images from the directory specified
images = os.listdir(os.path.join(directory, 'hdr'))

total = 0
# Calculating the average Q-score
for image in images:
    total += (eng.calculate_q_score(os.path.join(directory, folders[0], image), os.path.join(directory, folders[1], image)))
average = total / len(images)

print(average)
