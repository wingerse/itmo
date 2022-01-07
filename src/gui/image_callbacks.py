import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg
import cv2
import numpy as np
from constants import *
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
    images = user_data[1]
    window = user_data[0]
    
    # load and store uploaded LDR image
    try:
        images.ldr = load_ldr_image(image_path)
    except Exception as e:
        display_error(e, "Image with file name '{}' could not be found.\nRemember to include file extensions!".format(file_name))
        return
    images.ldr_flag = True
    
    # convert colour to rgba and display
    display_image(images.ldr, window, LDR_REGISTRY, ORIGINAL_LDR_IMAGE)
    
   
def upload_hdr(sender, app_data, user_data):
    """
    Callback for uploading HDR reference image
    """
    
    file_name = app_data['file_name']
    image_path = app_data['file_path_name']
    images = user_data[1]
    window = user_data[0]
    
    # load and store uploaded HDR reference image
    try:
        images.hdr = load_hdr_image(image_path)
    except Exception as e:
        display_error(e, "Image with file name '{}' could not be found. \nRemember to include file extensions!".format(file_name))
        return
    images.hdr_flag = True
    
    # tone map HDR image to LDR for display
    reference_hdr = tone_map(images.hdr, images.hdr_display)
    display_image(reference_hdr, window, HDR_REGISTRY, REFERENCE_HDR_IMAGE)


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
    
    # delete texture registry and image if currently exists (to be replaced with new ones),
    # hide evaluation and disable save image button temporarily while converting
    if dpg.does_alias_exist(GENERATED_IMAGE):
        dpg.delete_item(GENERATED_IMAGE)
        dpg.delete_item(GENERATED_REGISTRY)
        dpg.configure_item(EVALUATION, show=False)
        dpg.configure_item(SAVE_BUTTON, enabled=False)
    
    # show progress bar to generate image
    dpg.configure_item(PROGRESS_GROUP, show=True)
    dpg.set_value(PROGRESS_BAR, 0.0)
    
    window = user_data[0]
    images = user_data[1]
    
    dpg.set_value(PROGRESS_BAR, 0.3)
    
    # inverse tone mapping to convert the LDR image to HDR using the FHDR model
    try:
        images.generated, psnr, ssim = fhdr(
        images.ldr, 
        images.hdr,
        ".././itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")
    except Exception as e:
        display_error(e, "There was a problem generating the image.")
        return
        
    dpg.set_value(PROGRESS_BAR, 0.6)
    
    images.generated_ldr = tone_map(images.generated, images.generated_display)

    # update progress bar and hide it
    dpg.set_value(PROGRESS_BAR, 1.0)
    dpg.configure_item(PROGRESS_GROUP, show=False)
        
    # display image, update evaluation and enable save button
    display_image(images.generated_ldr, window, GENERATED_REGISTRY, GENERATED_IMAGE)
    dpg.configure_item(PSNR_RESULTS, default_value="PSNR = {0:.4f}".format(psnr))
    dpg.configure_item(SSIM_RESULTS, default_value="SSIM = {0:.4f}".format(ssim))
    dpg.configure_item(EVALUATION, show=True)
    dpg.configure_item(SAVE_BUTTON, enabled=True)
    
    
def change_tmo_display(sender, app_data, user_data):
    """
    Callback when tone mapping technique used to display HDR images is changed (Drago or Reinhard)
    """
        
    tmo_technique = app_data
    display = user_data[0]
    window = user_data[1]
    images = user_data[2]
    
    # update display tmo technique in Images object
    if display == REFERENCE_HDR_DISPLAY and images.hdr_display != tmo_technique:
        images.hdr_display = tmo_technique
        
        # get information to redisplay image if it already exists
        if dpg.does_alias_exist(REFERENCE_HDR_IMAGE):
            image = images.hdr
            registry = HDR_REGISTRY
            image_alias = REFERENCE_HDR_IMAGE
        else:
            return
        
    elif display == GENERATED_DISPLAY and images.generated_display != tmo_technique:
        images.generated_display = tmo_technique
        
        # get information to redisplay image if it already exists
        if dpg.does_alias_exist(GENERATED_IMAGE):
            image = images.generated
            registry = GENERATED_REGISTRY
            image_alias = GENERATED_IMAGE
        else:
            return
        
    else:
        return
        
    # redisplay image with new chosen tmo technique
    image = tone_map(image, tmo_technique)
    display_image(image, window, registry, image_alias)
    
    # update generated ldr in Images object
    if display == GENERATED_DISPLAY:
        images.generated_ldr = image
