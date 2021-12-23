import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    default_font = dpg.add_font("fonts/Roboto-Bold.ttf", 18)
    title_font = dpg.add_font("fonts/Roboto-Bold.ttf", 48)
    h1 = dpg.add_font("fonts/Roboto-Bold.ttf", 36)
    normal_text = dpg.add_font("fonts/Roboto-Light.ttf", 24)

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 50, 50, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 18, category=dpg.mvThemeCat_Core)    
        
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 187, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(222, 162, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (222, 141, 0), category=dpg.mvThemeCat_Core)
        
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (140, 140, 140), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (40, 36, 36), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(40, 36, 36), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (40, 36, 36), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
        

        
    
