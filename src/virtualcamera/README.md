Code from [HDRCNN](https://github.com/gabrieleilertsen/hdrcnn/tree/master/training_code/virtualcamera)  

# Compilation
Install opencv and compile as follows:

    g++ -Wall -O3 virtualcamera.cpp `pkg-config --cflags --libs opencv4` -o virtualcamera

# Run

    ./virtualcamera -input_path <hdr_images_path> -output_path <training_pairs_path> -imsize 256 256 3 -subimages 2