import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg
from theme import global_theme, default_font, title_font, h1, normal_text
from util import load_ldr_image, load_hdr_image, save_ldr_image, save_hdr_image
from tmo import reinhard
from itmo import fhdr

BUTTON_HEIGHT = 40
UPLOAD_LDR_DIALOG = "upload_ldr_dialog"
UPLOAD_HDR_DIALOG = "upload_hdr_dialog"
SAVE_FILE_DIALOG = "save_file_dialog"
SAVE_BUTTON = "save_button"
ORIGINAL_LDR_ALIAS = "original_ldr"
REFERENCE_HDR_ALIAS = "hdr_reference"
GENERATED_ALIAS = "generated"
LDR_REGISTRY = "ldr_registry"
HDR_REGISTRY = "hdr_registry"
GENERATED_REGISTRY = "generated_registry"

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
    
    # print("sender: ", sender)
    # print("app_data: ", app_data)
    # print("user_data: ", user_data)
    
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
    
    # print("sender: ", sender)
    # print("app_data: ", app_data)
    # print("user_data: ", user_data)
    
    window = user_data[0]
    images = user_data[1]
    
    generated, psnr, ssim = fhdr(
    images.ldr, 
    images.hdr,
    ".././itmo/fhdr/checkpoints/FHDR-iter-2.ckpt")

    # print(generated.min(), generated.max())
    # print(f"PSNR={psnr}, SSIM={ssim}")
    generated_ldr = reinhard(generated)
    
    # height, width, number of channels in generated hdr image
    height = generated_ldr.shape[0]
    width = generated_ldr.shape[1]
    
    if dpg.does_alias_exist(GENERATED_ALIAS):
        dpg.delete_item(GENERATED_ALIAS)
        dpg.delete_item(GENERATED_REGISTRY)
        dpg.delete_item(SAVE_FILE_DIALOG)
        dpg.delete_item(SAVE_BUTTON)
    
    with dpg.texture_registry(tag=GENERATED_REGISTRY):
        texture_id = dpg.add_raw_texture(width, height, generated_ldr, format=dpg.mvFormat_Float_rgb)
        
    dpg.add_image(texture_id, parent=window, tag=GENERATED_ALIAS)
    with dpg.file_dialog(directory_selector=False, show=False, callback=save_image, id=SAVE_FILE_DIALOG, user_data=(generated, generated_ldr)):
        dpg.add_file_extension("{.png,.jpg,.hdr}")
    dpg.add_button(label="Save Image", parent=window, width=100, height=BUTTON_HEIGHT, tag=SAVE_BUTTON, callback=lambda: dpg.show_item("save_file_dialog"))
    
def upload_ldr(sender, app_data, user_data):
    """Callback for uploading image"""
    
    # print("sender: ", sender)
    # print("app_data: ", app_data)
    # print("user_data: ", user_data)
    
    image_path = app_data['file_path_name']
    images = user_data[1]
    images.ldr = load_ldr_image(image_path)
    images.ldr_flag = True
    window = user_data[0]
    
    # add_and_load_image(image_path, parent=window)
    
    width, height, channels, data = dpg.load_image(image_path)
    
    if dpg.does_alias_exist(ORIGINAL_LDR_ALIAS):
        dpg.delete_item(ORIGINAL_LDR_ALIAS)
        dpg.delete_item(LDR_REGISTRY)
        # dpg.remove_alias(ORIGINAL_LDR_ALIAS)

    with dpg.texture_registry(tag=LDR_REGISTRY):
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, parent=window, tag=ORIGINAL_LDR_ALIAS)
    
   
def upload_hdr(sender, app_data, user_data):
    """Callback for uploading hdr reference image"""
    
    # print("sender: ", sender)
    # print("app_data: ", app_data)
    # print("user_data: ", user_data)
    
    image_path = app_data['file_path_name']
    images = user_data[1]
    images.hdr = load_hdr_image(image_path)
    images.hdr_flag = True
    window = user_data[0]
    
    # convert hdr to ldr for better display
    reference_hdr = reinhard(images.hdr)
    
    # get height and width of reference hdr image
    height = reference_hdr.shape[0]
    width = reference_hdr.shape[1]
    
    if dpg.does_alias_exist(REFERENCE_HDR_ALIAS):
        dpg.delete_item(REFERENCE_HDR_ALIAS)
        dpg.delete_item(HDR_REGISTRY)
        # dpg.remove_alias(REFERENCE_HDR_ALIAS)
    
    with dpg.texture_registry(tag=HDR_REGISTRY):
        texture_id = dpg.add_raw_texture(width, height, reference_hdr, format=dpg.mvFormat_Float_rgb)
       
    dpg.add_image(texture_id, parent=window, tag=REFERENCE_HDR_ALIAS)    

if __name__ == '__main__':
    
    images = Images()
    
    dpg.create_context()
    dpg.create_viewport(title="LDR to HDR Converter", width=1500, height= 750, x_pos=0, y_pos=0)
    dpg.setup_dearpygui()

    with dpg.window(label="LDR to HDR Converter", tag="main") as main_window:
        
        title = dpg.add_text("LDR to HDR Converter")
        dpg.add_spacer(height=20)
        dpg.add_separator()
        dpg.add_spacer(height=10)
        instructions = dpg.add_text(("Welcome to our LDR to HDR Image Converter!\n"
                                    "Start by uploading an LDR image and a reference HDR image. But do make sure\n" 
                                    "that they are of the same scene. Then simply click the 'Generate' button."))
        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_spacer(height=10)
        
        with dpg.group(horizontal=True):
            
            with dpg.group():
                
                with dpg.group() as ldr_container:
                    ldr_title = dpg.add_text("Original LDR Image")
                    dpg.add_button(label="Upload LDR Image", callback=lambda: dpg.show_item(UPLOAD_LDR_DIALOG), width=150, height=BUTTON_HEIGHT)
                    
                dpg.add_spacer(height=20)
                
                with dpg.group() as hdr_container:
                    hdr_title = dpg.add_text("HDR Reference Image")
                    dpg.add_button(label="Upload HDR Image", callback=lambda: dpg.show_item(UPLOAD_HDR_DIALOG), width=150, height=BUTTON_HEIGHT)
                                
            dpg.add_spacer(width=50)
            
            with dpg.group(indent=600) as generated_container:
                generated_title = dpg.add_text("Generated Image")
                dpg.add_button(label="Generate", tag="generate_button", width=100, height=BUTTON_HEIGHT, enabled=False)   
            
    # file dialog for uploading LDR image
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_ldr, id=UPLOAD_LDR_DIALOG, user_data=(ldr_container, images)):
        dpg.add_file_extension("{.png,.jpg}")
        
    # file dialog for uploading HDR reference image
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_hdr, id=UPLOAD_HDR_DIALOG, user_data=(hdr_container, images)):
        dpg.add_file_extension(".hdr")

    # set fonts
    dpg.bind_font(default_font)
    dpg.bind_item_font(title, title_font)
    dpg.bind_item_font(instructions, normal_text)
    dpg.bind_item_font(ldr_title, h1)
    dpg.bind_item_font(hdr_title, h1)
    dpg.bind_item_font(generated_title, h1)
    
    # set the theme
    dpg.bind_theme(global_theme)
    
    # dpg.show_style_editor()

    dpg.show_viewport()
    dpg.set_primary_window("main", True)
    # dpg.start_dearpygui()
    while dpg.is_dearpygui_running():
        if images.ldr_flag and images.hdr_flag:
            dpg.configure_item("generate_button", enabled=True, callback=convert_image, user_data=(generated_container, images))
            images.ldr_flag = False
            images.hdr_flag = False
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


# import dearpygui.dearpygui as dpg

# dpg.create_context()

# with dpg.window(label="Delete Files", modal=True, show=False, id="modal_id", no_title_bar=True):
#     dpg.add_text("All those beautiful files will be deleted.\nThis operation cannot be undone!")
#     dpg.add_separator()
#     dpg.add_checkbox(label="Don't ask me next time")
#     with dpg.group(horizontal=True):
#         dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))
#         dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))

# with dpg.window(label="Tutorial"):
#     dpg.add_button(label="Open Dialog", callback=lambda: dpg.configure_item("modal_id", show=True))

# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()
