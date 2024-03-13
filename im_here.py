import pyautogui
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item
import time
import threading
import os

# Global variable to track application status
icon_enabled = False

def im_here():
    """
        "im_here" is a python program that will create a tray
        application that enables you to keep your computer
        active while not actually being there.
    """
    global icon_enabled
    while icon_enabled:
        # Wiggle the mouse!
        pyautogui.move(0, 1)
        pyautogui.move(0, -1)
        time.sleep(5)

def enable_app():
    global icon_enabled, tray_icon
    icon_enabled = True
    print("App was enabled.")
    update_tray_icon()

    # Start the im_here thread
    im_here_thread.start()

def disable_app():
    global icon_enabled
    icon_enabled = False
    print("App was disabled.")
    update_tray_icon()

def exit_app(icon):
    icon.stop()

def update_tray_icon():
    global tray_icon, icon_enabled
    # Get the absolute path to the icon images
    enabled_icon_path = "enabled_icon.ico"
    disabled_icon_path = "disabled_icon.ico"
    enabled_icon_path_absolute = os.path.abspath(enabled_icon_path)
    disabled_icon_path_absolute = os.path.abspath(disabled_icon_path)

    # Update the tray icon image based on the application status
    if icon_enabled:
        tray_icon.icon = Image.open(enabled_icon_path_absolute)
    else:
        tray_icon.icon = Image.open(disabled_icon_path_absolute)

# Create the thread for the im_here function
im_here_thread = threading.Thread(target=im_here)

def create_tray_icon():
    global tray_icon
    # Creates the tray application that calls the internal functions
    # Initially, set the tray icon to use the disabled icon image
    image_path = "disabled_icon.ico"
    absolute_path = os.path.abspath(image_path)
    icon_image = Image.open(absolute_path)
    
    # Create the tray icon
    tray_icon = icon("im_here", icon_image, menu=menu(
        item("Enable", enable_app),
        item("Disable", disable_app),
        item("Exit", exit_app),
    ))
    
    # Run the tray icon application
    tray_icon.run()

# Create the tray icon
create_tray_icon()