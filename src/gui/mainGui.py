import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg
from util import load_ldr_image, load_hdr_image, save_ldr_image, save_hdr_image
from tmo import reinhard
from itmo import fhdr

class Images:
    def __init__(self):
        self.ldr = None
        self.hdr = None
        self.ldr_flag = False
        self.hdr_flag = False

def add_and_load_image(image_path, parent=None):
    """Loads image into a window. Taken from: https://github.com/hoffstadt/DearPyGui/discussions/1072"""
    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id)
    else:
        return dpg.add_image(texture_id, parent=parent)
    
def save_image(sender, app_data, user_data):
    """Callback for saving image"""
    
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("user_data: ", user_data)
    
    # get generated images from user data
    generated_hdr = user_data[0]
    generated_ldr = user_data[1]
    
    # prepare file path names for both ldr and hdr
    file_path_name = app_data['file_path_name']
    hdr_name = file_path_name + ".hdr"
    ldr_name = file_path_name + ".png"
    
    save_hdr_image(generated_hdr, hdr_name)
    save_ldr_image(generated_ldr, ldr_name)
    
def convert_image(sender, app_data, user_data):
    """ Applying FHDR to convert HDR image to LDR image """
    
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("user_data: ", user_data)
    
    window = user_data[0]
    images = user_data[1]
    
    generated, psnr, ssim = fhdr(
    images.ldr, 
    images.hdr,
    ".././itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")

    print(generated.min(), generated.max())
    print(f"PSNR={psnr}, SSIM={ssim}")
    generated_ldr = reinhard(generated)
    
    # height, width, number of channels in generated hdr image
    height = generated_ldr.shape[0]
    width = generated_ldr.shape[1]
    
    with dpg.texture_registry():
        dpg.add_raw_texture(width, height, generated_ldr, format=dpg.mvFormat_Float_rgb, tag="generated_ldr")
        
    dpg.add_text("\nGENERATED\n\n", parent=window)
    dpg.add_image("generated_ldr", parent=window)
    dpg.add_file_dialog(directory_selector=False, show=False, callback=save_image, tag="save_file_dialog", user_data=(generated, generated_ldr))
    dpg.add_button(label="Save Image", parent=window, callback=lambda: dpg.show_item("save_file_dialog"))
    
def upload_ldr(sender, app_data, user_data):
    """Callback for uploading image"""
    
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("user_data: ", user_data)
    
    image_path = app_data['file_path_name']
    images = user_data[1]
    images.ldr = load_ldr_image(image_path)
    images.ldr_flag = True
    window = user_data[0]
    
    dpg.add_text("\nORIGINAL LDR\n\n", parent=window)
    add_and_load_image(image_path, parent=window)
   
def upload_hdr(sender, app_data, user_data):
    """Callback for uploading hdr reference image"""
    
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("user_data: ", user_data)
    
    image_path = app_data['file_path_name']
    images = user_data[1]
    images.hdr = load_hdr_image(image_path)
    images.hdr_flag = True
    window = user_data[0]
    
    # convert hdr to ldr for better display
    reference_hdr = reinhard(images.hdr)
    
    # height, width of reference hdr image
    height = reference_hdr.shape[0]
    width = reference_hdr.shape[1]
    
    with dpg.texture_registry():
        dpg.add_raw_texture(width, height, reference_hdr, format=dpg.mvFormat_Float_rgb, tag="reference_hdr")
     
    dpg.add_text("\nHDR REFERENCE\n\n", parent=window)   
    dpg.add_image("reference_hdr", parent=window)    

if __name__ == '__main__':
    
    images = Images()
    
    dpg.create_context()
    dpg.create_viewport(title="LDR to HDR Converter", width=1500, height= 750, x_pos=0, y_pos=0)
    dpg.setup_dearpygui()

    with dpg.window(label="LDR to HDR Converter", tag="Main") as main_window:
        dpg.add_button(label="Upload LDR Image", callback=lambda: dpg.show_item("upload_ldr_dialog"))
        dpg.add_button(label="Upload HDR Image", callback=lambda: dpg.show_item("upload_hdr_dialog"))
        # dpg.add_separator()
        # dpg.add_spacing()   
            
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_ldr, id="upload_ldr_dialog", user_data=(main_window, images)):
        dpg.add_file_extension("{.png,.jpg}")
        
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_hdr, id="upload_hdr_dialog", user_data=(main_window, images)):
        dpg.add_file_extension(".hdr")

    dpg.show_viewport()
    dpg.set_primary_window("Main", True)
    # dpg.start_dearpygui()
    while dpg.is_dearpygui_running():
        if images.ldr_flag and images.hdr_flag:
            dpg.add_button(label="Generate", callback=convert_image, parent=main_window, user_data=(main_window, images))
            images.ldr_flag = False
            images.hdr_flag = False
        dpg.render_dearpygui_frame()
    dpg.destroy_context()