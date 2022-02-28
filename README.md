# Inverse Tone Mapping
Transform LDR (Low Dynamic Range) images to HDR (High Dynamic Range) images using machine learning which improves image 
contrast and reconstructs areas lost due to underexposure or overexposure.  
The machine learning algorithm is a modified version of [FHDR](https://github.com/mukulkhanna/FHDR)

LDR images are images captured with a typical camera. Since their dynamic range is limited, they are unable to capture 
all brightness values in a scene without overexposure or underexposure. 

Example of an HDR image compared to its LDR counterparts: 

| HDR Image | Overexposure | Underexposure |
|:--:|:--:|:--:|
|<img src="./docs/hdr.jpg" width=350></img>|<img src="./docs/overexposure.jpg" width=350></img>|<img src="./docs/underexposure.jpg" width=350></img>|

# GUI

![](./docs/gui1.png)

Example output: 

![](./docs/gui2.png)

## Setup
- Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
- `conda env create -f environment.yml` 
- `conda activate fyp`
- `pip install dearpygui==1.2.3`
- `python src/scripts/main.py`

## Dataset
Download the dataset from [this](https://drive.google.com/file/d/1EwVvrWESQlXJ87E6JvTwFG_7arEoBZMz/view?usp=sharing) link.

# Scripts
Check out the scripts at `src/scripts/` for doing training, testing, image augmentation, and running TMO and ITMO.

# Test images
You can test with images in `test_images/demo` or `datasets/testing_data_ours/ldr`. You can also try with images captured
from your own camera.  
