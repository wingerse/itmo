import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg
from util import save_ldr_image, save_hdr_image
from tmo import reinhard

def add_and_load_image(image_path, parent=None):
    """Loads image into a window. Taken from: https://github.com/hoffstadt/DearPyGui/discussions/1072"""
    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id)
    else:
        return dpg.add_image(texture_id, parent=parent)
    
def upload_image(sender, app_data, user_data):
    """Callback for uploading image"""
    
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("user_data: ", user_data)
    
    image_path = app_data['file_path_name']
    window = user_data

    add_and_load_image(image_path, parent=window)

if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport(title="LDR to HDR Converter", width=1500, height= 750, x_pos=0, y_pos=0)
    dpg.setup_dearpygui()

    with dpg.window(label="LDR to HDR Converter", tag="Main") as main_window:
        dpg.add_button(label="Upload Image", callback=lambda: dpg.show_item("upload_file_dialog"))
        
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_image, id="upload_file_dialog", user_data=main_window):
        dpg.add_file_extension("{.png,.jpg}")

    dpg.show_viewport()
    dpg.set_primary_window("Main", True)
    dpg.start_dearpygui()
    dpg.destroy_context()