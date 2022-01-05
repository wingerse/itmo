import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg
from constants import *
from util import *
from tmo import reinhard
from itmo import fhdr

import cv2
import numpy as np

def save_image(sender, app_data, user_data):
    """Callback for saving image"""
    
    # get generated images from user data
    generated_hdr = user_data[0]
    generated_ldr = user_data[1]
    
    # prepare file path names for both ldr and hdr
    file_path_name = app_data['file_path_name']
    hdr_name = file_path_name + ".hdr"
    ldr_name = file_path_name + ".png"
    
    # save both hdr and ldr images
    save_hdr_image(generated_hdr, hdr_name)
    save_ldr_image(generated_ldr, ldr_name)
    
def convert_image(sender, app_data, user_data):
    """ Applying FHDR to convert HDR image to LDR image """
    
    # delete texture registry and image if currently exists (to be replaced with new ones)
    # and disable save image button temporarily while converting
    if dpg.does_alias_exist(GENERATED_ALIAS):
        dpg.delete_item(GENERATED_ALIAS)
        dpg.delete_item(GENERATED_REGISTRY)
        dpg.delete_item(EVALUATION)
        dpg.delete_item(PSNR_RESULTS)
        dpg.delete_item(SSIM_RESULTS)
        dpg.configure_item(SAVE_BUTTON, enabled=False)
    
    # show progress bar to generate image
    dpg.configure_item(PROGRESS_GROUP, show=True)
    dpg.set_value(PROGRESS_BAR, 0.0)
    
    # get container and uploaded images from user data
    window = user_data[0]
    images = user_data[1]
    
    # update progress bar
    dpg.set_value(PROGRESS_BAR, 0.25)
    
    # inverse tone mapping to convert the LDR image to HDR
    try:
        generated, psnr, ssim = fhdr(
        images.ldr, 
        images.hdr,
        ".././itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")
    except Exception as e:
        dpg.configure_item(ERROR_MODAL, show=True)
        print("Error:", e)
        return
    
    # update progress bar
    dpg.set_value(PROGRESS_BAR, 0.5)
    
    # tone map the generated hdr image to ldr for display and convert colour to rgba
    try:
        generated_ldr = cv2.cvtColor(reinhard(generated), cv2.COLOR_RGB2RGBA)
    except Exception as e:
        dpg.configure_item(ERROR_MODAL, show=True)
        print("Error:", e)
        return
    
    # update progress bar
    dpg.set_value(PROGRESS_BAR, 0.75)
    
    # get height and width of generated hdr image
    height = generated_ldr.shape[0]
    width = generated_ldr.shape[1]
    
    # resize image if it is too big
    if height > MAX_IMAGE_HEIGHT or width > MAX_IMAGE_WIDTH:
        generated_ldr, height, width = downsize_image(generated_ldr, height, width)
    
    # create new texture registry and add texture of tone mapped image
    with dpg.texture_registry(tag=GENERATED_REGISTRY):
        texture_id = dpg.add_raw_texture(width, height, generated_ldr, format=dpg.mvFormat_Float_rgba)
        
    # TODO: try adding to same registry without deleting, maybe use tag.#################################################################
        
    # update progress bar and hide it
    dpg.set_value(PROGRESS_BAR, 1.0)
    dpg.configure_item(PROGRESS_GROUP, show=False)
    
    # add image, and enable save button
    dpg.add_image(texture_id, parent=window, tag=GENERATED_ALIAS)
    dpg.add_text("Test Evaluation Metric", parent=window, tag=EVALUATION)
    dpg.add_text("PSNR = {}".format(psnr), parent=window, tag=PSNR_RESULTS)
    dpg.add_text("SSIM = {}".format(ssim), parent=window, tag=SSIM_RESULTS)
    dpg.configure_item(SAVE_FILE_DIALOG, user_data=(generated, generated_ldr))
    dpg.configure_item(SAVE_BUTTON, enabled=True)

def upload_ldr(sender, app_data, user_data):
    """Callback for uploading image"""
    
    # get information needed from app_data and user_data
    file_name = app_data['file_name']
    image_path = app_data['file_path_name']
    images = user_data[1]
    window = user_data[0]
    
    # store uploaded ldr image
    try:
        images.ldr = load_ldr_image(image_path)
    except Exception as e:
        dpg.configure_item(ERROR_MODAL, show=True)
        dpg.configure_item(ERROR_MESSAGE, default_value="Image with file name '{}' could not be found.\nRemember to include file extensions!".format(file_name))
        print("Error:", e)
        return
    images.ldr_flag = True
    
    # convert colour to rgba
    ldr_image = cv2.cvtColor(images.ldr.astype(np.float32), cv2.COLOR_RGB2RGBA)
    
    # get height and width of ldr image
    height = ldr_image.shape[0]
    width = ldr_image.shape[1]
    
    # resize image if it is too big
    if height > MAX_IMAGE_HEIGHT or width > MAX_IMAGE_WIDTH:
        ldr_image, height, width = downsize_image(ldr_image, height, width)
    
    # delete texture registry and image if currently exists (to be replaced with new ones)    
    if dpg.does_alias_exist(ORIGINAL_LDR_ALIAS):
        dpg.delete_item(ORIGINAL_LDR_ALIAS)
        dpg.delete_item(LDR_REGISTRY)

    # create new texture registry and add texture of tone mapped image
    with dpg.texture_registry(tag=LDR_REGISTRY):
        texture_id = dpg.add_raw_texture(width, height, ldr_image, format=dpg.mvFormat_Float_rgba)

    # display image
    dpg.add_image(texture_id, parent=window, tag=ORIGINAL_LDR_ALIAS)
    
   
def upload_hdr(sender, app_data, user_data):
    """Callback for uploading hdr reference image"""
    
    # get information needed from app_data and user_data
    file_name = app_data['file_name']
    image_path = app_data['file_path_name']
    images = user_data[1]
    window = user_data[0]
    
    # store uploaded reference hdr image
    try:
        images.hdr = load_hdr_image(image_path)
    except Exception as e:
        dpg.configure_item(ERROR_MODAL, show=True)
        dpg.configure_item(ERROR_MESSAGE, default_value="Image with file name '{}' could not be found. \nRemember to include file extensions!".format(file_name))
        print("Error:", e)
        return
    images.hdr_flag = True
    
    # tonemap hdr to ldr for display and convert colour to rgba
    reference_hdr = cv2.cvtColor(reinhard(images.hdr), cv2.COLOR_RGB2RGBA)
    
    # get height and width of reference hdr image
    height = reference_hdr.shape[0]
    width = reference_hdr.shape[1]
    
    # resize image if it is too big
    if height > MAX_IMAGE_HEIGHT or width > MAX_IMAGE_WIDTH:
        reference_hdr, height, width = downsize_image(reference_hdr, height, width)
    
    # delete texture registry and image if currently exists (to be replaced with new ones)  
    if dpg.does_alias_exist(REFERENCE_HDR_ALIAS):
        dpg.delete_item(REFERENCE_HDR_ALIAS)
        dpg.delete_item(HDR_REGISTRY)
    
    # create new texture registry and add texture of tone mapped image
    with dpg.texture_registry(tag=HDR_REGISTRY):
        texture_id = dpg.add_raw_texture(width, height, reference_hdr, format=dpg.mvFormat_Float_rgba)
       
    # display image
    dpg.add_image(texture_id, parent=window, tag=REFERENCE_HDR_ALIAS)