"""
usage: main.py

Starts the application.
"""

import include_parent_path
import dearpygui.dearpygui as dpg
from gui.constants import *
from gui.image_callbacks import *
from gui.theme import *
import numpy as np

class Images:
    """
    Object to hold images and necessary info to be passed around in UI functions
    """
    def __init__(self):
        self.tmo = REINHARD
        self.itmo = FHDR
        self.ldr = None
        self.generated = None
        self.generated_ldr = None

if __name__ == '__main__':
    np.seterr(all='raise')
    
    images = Images()
    tmo_items = [REINHARD, DRAGO]
    itmo_items = [FHDR, LINEAR]
    
    dpg.create_context()
    dpg.create_viewport(title="LDR to HDR Converter", width=1530, height= 800, x_pos=0, y_pos=0)
    dpg.setup_dearpygui()
    
    # load fonts
    with dpg.font_registry():
        default_font = dpg.add_font("src/gui/fonts/Roboto-Bold.ttf", 18)
        title = dpg.add_font("src/gui/fonts/Roboto-Bold.ttf", 48)
        h1 = dpg.add_font("src/gui/fonts/Roboto-Bold.ttf", 36)
        h2 = dpg.add_font("src/gui/fonts/Roboto-Bold.ttf", 28)
        normal_text = dpg.add_font("src/gui/fonts/Roboto-Light.ttf", 24)
        subtitle = dpg.add_font("src/gui/fonts/Roboto-LightItalic.ttf", 18)
    
    # main UI window
    with dpg.window(label="LDR to HDR Converter", tag="main") as main_window:
        
        with dpg.group(horizontal=True):
            title_text = dpg.add_text("LDR to HDR Converter")
            dpg.add_spacer(width=50)
            credit = dpg.add_text("By Ahmed Aiman, Ngu Bing Xian, Yaaseen Edoo & Vanessa Tan\n"
                                  "Group FIT3161/62_MA_14\n"
                                  "Monash University")
            
        dpg.add_spacer(height=20)
        dpg.add_separator()
        dpg.add_spacer(height=10)
        
        instructions = dpg.add_text("Welcome to our LDR to HDR Image Converter!\n"
                                    "Start by choosing a tone mapping operator. Don't worry, you can change this at any time.\n"
                                    "Then, select an LDR image file. Only one file can be selected but you may reselect as many times as needed.\n" 
                                    "Choose one of the inverse tone mapping techniques. This can also be changed at any time.\n"                                    
                                    "Once you are ready, simply click the 'Generate' button.\n"
                                    "You can then save the generated image by clicking the 'Save Image' button and the image will be saved in both .hdr and .png formats.")
        
        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_spacer(height=20)
        
        with dpg.group(horizontal=True):
            
            with dpg.group():
                tmo_title = dpg.add_text("Tone Mapping Operator")
                tmo_info = dpg.add_text("HDR images have to be tone mapped to be displayed on most monitors.\n"
                                        "Select a technique from below to choose how the generated image\n"
                                        "should be displayed.")
                dpg.add_spacer(height=10)
                tmo_listbox = dpg.add_listbox(items=tmo_items, num_items=2, width=LISTBOX_WIDTH, callback=change_tmo_display, user_data=(images))
                
            dpg.add_spacer(width=50)
                
            with dpg.group(indent=SECOND_COLUMN_INDENT):
                itmo_title = dpg.add_text("Inverse Tone Mapping Operator")
                itmo_info = dpg.add_text("See how our FHDR model compares to a linear technique!\n"
                                         "Select a technique from below to choose a method of conversion\n"
                                         "for the generated image.")
                dpg.add_spacer(height=10)
                itmo_listbox = dpg.add_listbox(items=itmo_items, num_items=2, width=LISTBOX_WIDTH, callback=change_itmo, user_data=(GENERATED_CONTAINER, images))
                    
        dpg.add_spacer(height=30)
        
        with dpg.group(horizontal=True):
            
            with dpg.group(tag=LDR_CONTAINER):
                ldr_title = dpg.add_text("Original LDR Image")
                dpg.add_button(label="Select LDR Image", width=SELECT_BUTTON_WIDTH, height=BUTTON_HEIGHT, callback=lambda: dpg.show_item(SELECT_LDR_DIALOG))
                dpg.add_spacer(height=10)
                    
            dpg.add_spacer(width=50)
            
            with dpg.group(indent=SECOND_COLUMN_INDENT, tag=GENERATED_CONTAINER): 
        
                generated_title = dpg.add_text("Generated Image")
                
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Generate", tag=GENERATE_BUTTON, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, enabled=False, callback=generate, user_data=(GENERATED_CONTAINER, images))   
                    dpg.add_button(label="Save Image", tag=SAVE_BUTTON, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, enabled=False, callback=lambda: dpg.show_item("save_file_dialog"))
                    
                    with dpg.group(show=False, tag=PROGRESS_GROUP):
                        loading = dpg.add_text("Loading...")
                        dpg.add_progress_bar(width=PROGRESS_WIDTH, height=PROGRESS_HEIGHT, tag=PROGRESS_BAR)
                
                dpg.add_spacer(height=10)
                
    # file dialog for selecting an LDR image file
    with dpg.file_dialog(directory_selector=False, width=FILE_DIALOG_WIDTH, height=FILE_DIALOG_HEIGHT, show=False, callback=select_ldr, id=SELECT_LDR_DIALOG, user_data=(LDR_CONTAINER, images)):
        dpg.add_file_extension("{.png,.jpg,.jpeg}")
        
    # file dialog for saving generated images in both ldr and hdr formats
    with dpg.file_dialog(directory_selector=False, width=FILE_DIALOG_WIDTH, height=FILE_DIALOG_HEIGHT, show=False, callback=save_image, id=SAVE_FILE_DIALOG, user_data=(images)):
        dpg.add_file_extension("{.png,.hdr}")
        
    # error modal
    with dpg.window(modal=True, show=False, id=ERROR_MODAL, height=ERROR_HEIGHT, pos=(550, 250), on_close=lambda: dpg.configure_item(PROGRESS_GROUP, show=False), no_resize=True) as error_display:
        error_title = dpg.add_text("An error occured :(")
        dpg.add_spacer(height=10)
        dpg.add_text("", tag=ERROR_MESSAGE)
    
    # save modal
    with dpg.window(modal=True, show=False, id=SAVE_MODAL, pos=(550, 250), no_resize=True) as save_display:
        save_message = dpg.add_text("Saved successfully!")

    # set fonts
    dpg.bind_font(default_font)
    dpg.bind_item_font(title_text, title)
    dpg.bind_item_font(credit, subtitle)
    dpg.bind_item_font(instructions, normal_text)
    dpg.bind_item_font(tmo_title, h2)
    dpg.bind_item_font(tmo_info, normal_text)
    dpg.bind_item_font(tmo_listbox, h2)
    dpg.bind_item_font(itmo_title, h2)
    dpg.bind_item_font(itmo_info, normal_text)
    dpg.bind_item_font(itmo_listbox, h2)
    dpg.bind_item_font(ldr_title, h1)
    dpg.bind_item_font(generated_title, h1)
    dpg.bind_item_font(loading, subtitle)
    dpg.bind_item_font(error_title, h1)
    dpg.bind_item_font(save_message, h1)

    # set the theme
    dpg.bind_theme(global_theme)
    dpg.bind_item_theme(error_display, modal_theme)
    dpg.bind_item_theme(save_display, modal_theme)
    
    # start display
    dpg.show_viewport()
    dpg.set_primary_window("main", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
