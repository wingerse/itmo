import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg
import cv2
import numpy as np
from .constants import *
from util import *
from tmo import reinhard, drago
from itmo import fhdr

def display_error(error, message):
    """
    Helper function to display error modal with custom message
    """
    
    dpg.configure_item(ERROR_MESSAGE, default_value=message)
    dpg.configure_item(ERROR_MODAL, show=True)
    print("Error:", error)
    
    
def display_image(image, window, registry_tag, image_tag):
    """
    Helper function to add image
    """
    
    height = image.shape[0]
    width = image.shape[1]
        
    # resize image if it is too big
    if height > MAX_IMAGE_HEIGHT or width > MAX_IMAGE_WIDTH:
        image, height, width = downsize_image(image, height, width)
        
    image = cv2.cvtColor(image.astype(np.float32), cv2.COLOR_RGB2RGBA)
        
    # delete texture registry and image if currently exists (to be replaced with new ones)  
    if dpg.does_alias_exist(image_tag):
        dpg.delete_item(image_tag)
        dpg.delete_item(registry_tag)
    
    with dpg.texture_registry(tag=registry_tag):
        texture_id = dpg.add_raw_texture(width, height, image, format=dpg.mvFormat_Float_rgba)
       
    dpg.add_image(texture_id, parent=window, tag=image_tag)
    

def tone_map(image, tmo_technique):
    """
    Helper function to tone map HDR images to LDR for display
    """
    
    try:
        if tmo_technique == REINHARD:
            image =  reinhard(image)
        else:
            image = drago(image)
    except Exception as e:
        display_error(e, "There was a problem displaying the image.")
        return
    
    return image
    

def upload_ldr(sender, app_data, user_data):
    """
    Callback for uploading LDR image
    """
    
    file_name = app_data['file_name']
    image_path = app_data['file_path_name']
    window = user_data[0]
    images = user_data[1]
    
    # load and store uploaded LDR image
    try:
        images.ldr = load_ldr_image(image_path)
    except Exception as e:
        display_error(e, "Image with file name '{}' could not be found.\nRemember to include file extensions!".format(file_name))
        return
    images.ldr_flag = True
    
    # display and enable generate button
    display_image(images.ldr, window, LDR_REGISTRY, ORIGINAL_LDR_IMAGE)
    dpg.configure_item(GENERATE_BUTTON, enabled=True)
    

def save_image(sender, app_data, user_data):
    """
    Callback for saving image
    """
    
    images = user_data

    # prepare file path names for both HDR and LDR
    file_path_name = app_data['file_path_name']
    hdr_name = file_path_name + ".hdr"
    ldr_name = file_path_name + ".png"
        
    # save both HDR and LDR images
    save_hdr_image(images.generated, hdr_name)
    save_ldr_image(images.generated_ldr, ldr_name)
    
    
def convert_image(sender, app_data, user_data):
    """
    Using FHDR model to convert LDR image to HDR image
    """
    # delete current generated image if it exists
    if dpg.does_alias_exist(GENERATED_IMAGE):
        dpg.delete_item(GENERATED_IMAGE)
        dpg.delete_item(GENERATED_REGISTRY)
    
    # disable save image button temporarily while converting
    dpg.configure_item(SAVE_BUTTON, enabled=False)
    
    # show progress bar to generate image
    dpg.configure_item(PROGRESS_GROUP, show=True)
    dpg.set_value(PROGRESS_BAR, 0.0)
    
    window = user_data[0]
    images = user_data[1]
    
    dpg.set_value(PROGRESS_BAR, 0.3)
    
    # inverse tone mapping to convert the LDR image to HDR using the FHDR model
    try:
        images.generated = fhdr(images.ldr, "src/itmo/fhdr/checkpoints/ours.ckpt")
    except Exception as e:
        display_error(e, "There was a problem generating the image.")
        return
        
    dpg.set_value(PROGRESS_BAR, 0.6)
    
    images.generated_ldr = tone_map(images.generated, images.tmo)

    # update progress bar and hide it
    dpg.set_value(PROGRESS_BAR, 1.0)
    dpg.configure_item(PROGRESS_GROUP, show=False)
        
    # display image, update evaluation and enable save button
    display_image(images.generated_ldr, window, GENERATED_REGISTRY, GENERATED_IMAGE)
    dpg.configure_item(SAVE_BUTTON, enabled=True)
    
    
def change_tmo_display(sender, app_data, user_data):
    """
    Callback when tone mapping technique used to display HDR images is changed (Drago or Reinhard)
    """
        
    tmo_technique = app_data
    images = user_data
    
    # update display tmo technique in Images object
    if images.tmo != tmo_technique:
        images.tmo = tmo_technique
        
        # get information to redisplay image if it already exists
        if dpg.does_alias_exist(GENERATED_IMAGE):
            tone_mapped_image = tone_map(images.generated, tmo_technique)
            display_image(tone_mapped_image, GENERATED_CONTAINER, GENERATED_REGISTRY, GENERATED_IMAGE)
            
            images.generated_ldr = tone_mapped_image
        else:
            return
        
    else:
        return

