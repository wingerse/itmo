"""
usage: image_callbacks.py

Contains functions concerning the user interface.
"""

import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg
import cv2
import numpy as np
from .constants import *
from util import *
from tmo import reinhard, drago
from itmo import fhdr, linear

""" HELPER FUNCTIONS """

def display_error(error, message):
    """
    Helper function to display error modal with custom message.
    
    :param error: The error caught
    :param message: String to be displayed in the error modal
    """
    dpg.configure_item(ERROR_MESSAGE, default_value=message)
    dpg.configure_item(ERROR_MODAL, show=True)
    print("Error:", error)
    
    
def display_image(image, window, registry_tag, image_tag):
    """
    Helper function to display image.
    
    :param image: Numpy array that represents image to be displayed
    :param window: Container that the image will be displayed in
    :param registry_tag: Alias for texture registry that should contain the new texture
    :param image_tag: Alias for the image that should be displayed 
    """
    height = image.shape[0]
    width = image.shape[1]
        
    # resize image if necessary
    image, height, width = scale_image(image, height, width)
        
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
    Helper function to tone map HDR images to LDR for display.
    
    :param image: Numpy array of image to be tone mapped
    :param tmo_technique: The technique chosen for tone mapping (Reinhard or Drago)
    :return: A tone mapped image (in numpy array format) if successful, else raise exception
    """
    # raise exception if any floating point exceptions instead of warning
    np.seterr(all='raise')
    
    try:
        if tmo_technique == REINHARD:
            image = reinhard(image)
        else:
            image = drago(image)
    except Exception as e:
        display_error(e, "There was a problem displaying the image.")
        raise Exception(e)
    
    return image


def inverse_tone_map(image, itmo_technique):
    """
    Helper function to inversely tone map LDR images to HDR.
    
    :param image: Numpy array of image to be tone mapped
    :param tmo_technique: The technique chosen for inverse tone mapping (FHDR or Linear)
    :return: An inversely tone mapped image (in numpy array format) if successful, else raise exception
    """
    try:
        if itmo_technique == FHDR:
            image = fhdr(image)
        else:
            image = linear(image)
    except Exception as e:
        display_error(e, "There was a problem converting the image.")
        raise Exception(e)
    
    return image


def convert_image(window, images):
    """
    Helper function for converting an LDR image to HDR.
    
    :param window: Container that the image will be displayed in
    :param images: Object that holds the images and necessary information
    """        
    # disable save image button temporarily while converting
    dpg.configure_item(SAVE_BUTTON, enabled=False)
    
    # show progress bar to generate image
    dpg.configure_item(PROGRESS_GROUP, show=True)
    dpg.set_value(PROGRESS_BAR, 0.3)
    
    # inverse tone mapping to convert the LDR image to HDR
    try:
        images.generated = inverse_tone_map(images.ldr, images.itmo)
    except Exception as e:
        raise Exception(e)
        
    dpg.set_value(PROGRESS_BAR, 0.7)
    
    # tone mapping for HDR display
    try:
        images.generated_ldr = tone_map(images.generated, images.tmo)
    except Exception as e:
        raise Exception(e)

    # update progress bar and hide it
    dpg.set_value(PROGRESS_BAR, 1.0)
    dpg.configure_item(PROGRESS_GROUP, show=False)
        
    # display image and enable save button
    display_image(images.generated_ldr, window, GENERATED_REGISTRY, GENERATED_IMAGE)
    dpg.configure_item(SAVE_BUTTON, enabled=True)


""" LISTBOX CALLBACKS """


def change_tmo_display(sender, app_data, user_data):
    """
    Callback when tone mapping operator used to display HDR images is changed (Reinhard or Drago).
    """
    tmo_technique = app_data
    images = user_data
    
    # show progress bar to generate image
    dpg.configure_item(PROGRESS_GROUP, show=True)
    dpg.set_value(PROGRESS_BAR, 0.3)
    
    # update display tmo technique in Images object
    if images.tmo != tmo_technique:
        images.tmo = tmo_technique
        
        # redisplay image if it already exists
        if dpg.does_alias_exist(GENERATED_IMAGE):
            try:
                tone_mapped_image = tone_map(images.generated, tmo_technique)
            except:
                return
            
            dpg.set_value(PROGRESS_BAR, 0.7)
            
            display_image(tone_mapped_image, GENERATED_CONTAINER, GENERATED_REGISTRY, GENERATED_IMAGE)
            images.generated_ldr = tone_mapped_image
            
    # update progress bar and hide it
    dpg.set_value(PROGRESS_BAR, 1.0)
    dpg.configure_item(PROGRESS_GROUP, show=False)
    

def change_itmo(sender, app_data, user_data):
    """
    Callback for selecting an itmo technique (FHDR or Linear).
    """
    itmo_technique = app_data
    window = user_data[0]
    images = user_data[1]
    
    # update itmo in Images object
    if images.itmo != itmo_technique:
        images.itmo = itmo_technique
        
        # redisplay image if it already exists
        if dpg.does_alias_exist(GENERATED_IMAGE):
            try:
                convert_image(window, images)
            except:
                dpg.delete_item(GENERATED_IMAGE)
                dpg.delete_item(GENERATED_REGISTRY)
 

""" BUTTON CALLBACKS """
    
    
def select_ldr(sender, app_data, user_data):
    """
    Callback for opening and loading an LDR image file.
    """
    file_name = app_data['file_name']
    image_path = app_data['file_path_name']
    window = user_data[0]
    images = user_data[1]
    
    # load and store LDR image
    try:
        images.ldr = load_ldr_image(image_path)
    except Exception as e:
        display_error(e, "The following image file could not be found:\n'{}'\nRemember to include file extensions!".format(file_name))
        return
    images.ldr_flag = True
    
    # remove generated image
    if dpg.does_alias_exist(GENERATED_IMAGE):
        dpg.delete_item(GENERATED_IMAGE)
        dpg.delete_item(GENERATED_REGISTRY)
        images.generated = None
        images.generated_ldr = None
        dpg.configure_item(SAVE_BUTTON, enabled=False)

    
    # display and enable generate button
    display_image(images.ldr, window, LDR_REGISTRY, ORIGINAL_LDR_IMAGE)
    dpg.configure_item(GENERATE_BUTTON, enabled=True)
    
    
def generate(sender, app_data, user_data):
    """
    Callback for when the 'Generate' button is clicked.
    """          
    window = user_data[0]
    images = user_data[1]
    
    try:
        convert_image(window, images)
    except:
        return
    
    
def save_image(sender, app_data, user_data):
    """
    Callback for saving the generated image.
    """
    images = user_data

    # prepare file path names for both HDR and LDR
    file_path_name = app_data['file_path_name']
    hdr_name = file_path_name + ".hdr"
    ldr_name = file_path_name + ".png"
        
    # save both HDR and LDR images
    try:
        save_hdr_image(images.generated, hdr_name)
        save_ldr_image(images.generated_ldr, ldr_name)
    except Exception as e:
        display_error(e, "There was a problem saving the images.")
        return
    
    # show save modal
    dpg.configure_item(SAVE_MODAL, show=True)