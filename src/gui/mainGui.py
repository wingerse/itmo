import dearpygui.dearpygui as dpg
from constants import *
from image_callbacks import *
from theme import *

class Images:
    def __init__(self):
        self.ldr = None
        self.hdr = None
        self.ldr_flag = False
        self.hdr_flag = False

if __name__ == '__main__':
    
    images = Images()
    
    dpg.create_context()
    dpg.create_viewport(title="LDR to HDR Converter", width=1500, height= 750, x_pos=0, y_pos=0)
    dpg.setup_dearpygui()

    with dpg.window(label="LDR to HDR Converter", tag="main") as main_window:
        
        with dpg.group(horizontal=True):
            title_text = dpg.add_text("LDR to HDR Converter")
            dpg.add_spacer(width=50)
            credit = dpg.add_text("By Ahmed Aiman, Ngu Bing Xian, Yaaseen Edoo & Vanessa Tan\n"
                                  "Group FIT3161_MA_14\n"
                                  "Monash University")
            
        dpg.add_spacer(height=20)
        dpg.add_separator()
        dpg.add_spacer(height=10)
        instructions = dpg.add_text("Welcome to our LDR to HDR Image Converter!\n"
                                    "Start by uploading an LDR image and a reference HDR image. But do make sure that they are of the same scene!\n" 
                                    "Once you are ready, simply click the 'Generate' button to start the conversion.\n"
                                    "You can then save the generated image by clicking the 'Save Image' button and the image will be saved in both .hdr and .png formats.")
        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_spacer(height=10)
        
        with dpg.group(horizontal=True):
            
            with dpg.group():
                
                with dpg.group() as ldr_container:
                    ldr_title = dpg.add_text("Original LDR Image")
                    dpg.add_button(label="Upload LDR Image", width=150, height=BUTTON_HEIGHT, callback=lambda: dpg.show_item(UPLOAD_LDR_DIALOG))
                    
                dpg.add_spacer(height=20)
                
                with dpg.group() as hdr_container:
                    hdr_title = dpg.add_text("HDR Reference Image")
                    dpg.add_button(label="Upload HDR Image", width=150, height=BUTTON_HEIGHT, callback=lambda: dpg.show_item(UPLOAD_HDR_DIALOG))
                                
            dpg.add_spacer(width=50)
            
            with dpg.group(indent=600) as generated_container:
                generated_title = dpg.add_text("Generated Image")
                
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Generate", tag=GENERATE_BUTTON, width=100, height=BUTTON_HEIGHT, enabled=False, callback=convert_image, user_data=(generated_container, images))   
                    dpg.add_button(label="Save Image", tag=SAVE_BUTTON, width=100, height=BUTTON_HEIGHT, enabled=False, callback=lambda: dpg.show_item("save_file_dialog"))

                with dpg.group(show=False, tag=PROGRESS_GROUP):
                    dpg.add_spacer(height=10)
                    loading = dpg.add_text("Loading...")
                    dpg.add_spacer(height=5)
                    dpg.add_progress_bar(tag=PROGRESS_BAR)
                
                
    # file dialog for uploading LDR image
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_ldr, id=UPLOAD_LDR_DIALOG, user_data=(ldr_container, images)):
        dpg.add_file_extension("{.png,.jpg}")
        
    # file dialog for uploading HDR reference image
    with dpg.file_dialog(directory_selector=False, show=False, callback=upload_hdr, id=UPLOAD_HDR_DIALOG, user_data=(hdr_container, images)):
        dpg.add_file_extension(".hdr")
        
    # file dialog for saving generated images in both ldr and hdr formats
    with dpg.file_dialog(directory_selector=False, show=False, callback=save_image, id=SAVE_FILE_DIALOG):
        dpg.add_file_extension("{.png,.jpg,.hdr}")
        
    # error modal
    with dpg.window(label="Error", modal=True, show=False, id=ERROR_MODAL, pos=(600, 300)) as error_display:
        dpg.add_text("There was a problem generating the image :(")

    # set fonts
    dpg.bind_font(default_font)
    dpg.bind_item_font(title_text, title)
    dpg.bind_item_font(credit, subtitle)
    dpg.bind_item_font(instructions, normal_text)
    dpg.bind_item_font(ldr_title, h1)
    dpg.bind_item_font(hdr_title, h1)
    dpg.bind_item_font(generated_title, h1)
    dpg.bind_item_font(loading, normal_text)
    
    # set the theme
    dpg.bind_theme(global_theme)
    dpg.bind_item_theme(error_display, error_theme)
    
    # dpg.show_style_editor()

    # start display
    dpg.show_viewport()
    dpg.set_primary_window("main", True)
    # dpg.start_dearpygui()
    while dpg.is_dearpygui_running():
        if images.ldr_flag and images.hdr_flag:
            dpg.configure_item(GENERATE_BUTTON, enabled=True)
            images.ldr_flag = False
            images.hdr_flag = False
        dpg.render_dearpygui_frame()
    dpg.destroy_context()
