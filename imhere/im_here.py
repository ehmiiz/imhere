import time
import threading
import os
from pyautogui import move
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item
"""
    `im_here` is a python program that will create a tray
    application that enables you to keep your computer
    active while not actually being there.
"""
global icon_enabled
icon_enabled = False

def im_here():
    # Main program, simple mouse wiggle to simulate that the user is infact
    # here.
    
    while icon_enabled:
        # Wiggle the mouse!
        move(0, 1)
        move(0, -1)
        # sleep 1 second, check condition, sleep one more, 30 times
        # this allows for a more dynamic user experience instead of just
        # sleeping 30 seconds.
        for i in range(30):
            if icon_enabled == False:
                break
            time.sleep(1)
            

def enable_app():
    # Starts a thread with the im_here function running
    global icon_enabled, tray_icon, im_here_thread
    icon_enabled = True
    im_here_thread = threading.Thread(target=im_here)
    print("App was enabled.")
    update_tray_icon()

    # Start the im_here thread
    im_here_thread.start()

def disable_app():
    # If the thread is running, it's being stopped. Updats the icon.
    global icon_enabled
    icon_enabled = False
    print("App was disabled.")
    if im_here_thread.is_alive():
        im_here_thread.join()
    update_tray_icon()

def exit_app(icon):
    # Exits the application
    icon.stop()

def update_tray_icon():
    global tray_icon, icon_enabled
    # Get the absolute path to the icon images
    

    # Update the tray icon image based on the application status
    if icon_enabled:
        tray_icon.icon = Image.open(enabled_icon_path_absolute)
    else:
        tray_icon.icon = Image.open(disabled_icon_path_absolute)

def create_tray_icon():
    # Creates the tray application that calls the internal functions
    
    # Global functions being used for initial icon setting and dynamic icon setting
    global tray_icon, disabled_icon_path_absolute, enabled_icon_path_absolute

    # Define the filenames of the icons and it's relative folder name
    enabled_icon_filename = "enabled_icon.ico"
    disabled_icon_filename = "disabled_icon.ico"
    icons_dir = "icons"

    # Construct the absolute paths to the icons
    enabled_icon_path_absolute = os.path.abspath(os.path.join(icons_dir, enabled_icon_filename))
    disabled_icon_path_absolute = os.path.abspath(os.path.join(icons_dir, disabled_icon_filename))

    # Instantiate an image object
    icon_image = Image.open(disabled_icon_path_absolute)

    # Create the tray icon
    tray_icon = icon("im_here", icon_image, menu=menu(
        item("Enable", enable_app),
        item("Disable", disable_app),
        item("Exit", exit_app),
    ))

    # Run the tray icon application
    tray_icon.run()

# Call the application
create_tray_icon()