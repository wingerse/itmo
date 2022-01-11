"""
usage: theme.py

Contains the theme and styling for UI items.
"""

import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 50, 50, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 18, category=dpg.mvThemeCat_Core)    
        
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 187, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (222, 162, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (222, 141, 0), category=dpg.mvThemeCat_Core)
        
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (140, 140, 140), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (37, 37, 38), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (37, 37, 38), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (37, 37, 38), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)

    with dpg.theme_component(dpg.mvListbox):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (255, 187, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (37, 37, 38), category=dpg.mvThemeCat_Core)
          
          
with dpg.theme() as modal_theme:
    
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (37, 37, 38), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 40, 40, category=dpg.mvThemeCat_Core)
    