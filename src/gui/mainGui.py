import sys
sys.path.append('../')

import dearpygui.dearpygui as dpg

def add_and_load_image(image_path, parent=None):
    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id)
    else:
        return dpg.add_image(texture_id, parent=parent)
    
def uploadImage(sender, app_data, user_data):
    width, height, channels, data = dpg.load_image(app_data['file_path_name'])

    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    with dpg.window(label="Image"):
        dpg.add_image(texture_id)
    

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.file_dialog(directory_selector=False, show=False, callback=uploadImage, id="file_dialog_id"):
    dpg.add_file_extension(".jpg")
    dpg.add_file_extension(".png")

with dpg.window(label="LDR to HDR Converter"):
    dpg.add_button(label="Upload Image", callback=lambda: dpg.show_item("file_dialog_id"))

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()