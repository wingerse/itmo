import matlab.engine
import os

eng = matlab.engine.connect_matlab()

folders = ['gt_hdr', 'hdr', 'ldr']

# Replace with your root directory
rootdir = r'C:\Users\ngu\Documents\MATLAB\hdrvdp-3.0.6\testing'

file_path = []
counter = 0

for subdir, dirs, files in os.walk(rootdir):
    if counter == 0:
        file_path = dirs
    counter += 1

no_of_images = []
for i in range(len(file_path)):
    path = os.path.join(rootdir, file_path[i])
    print(path)
    count = 0
    for subdir, dirs, files in os.walk(path):
        count = len(files)
    no_of_images.append(count)
print(no_of_images)

images = []
average = []

for i in range(len(no_of_images)):
    q_score = []
    path = os.path.join(rootdir, file_path[i])
    total = 0
    for j in range(no_of_images[i]):
        total += (eng.calculate_q_score(os.path.join(path, folders[0], str(j) + '.hdr'), os.path.join(path, folders[1], str(j) + '.hdr')))
    avg = total / no_of_images[i]

    average.append((path, avg))

print(average)


