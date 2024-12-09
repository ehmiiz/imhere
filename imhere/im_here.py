import time
import threading
import os
import sys
from pyautogui import move
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item

global icon_enabled
icon_enabled = False
im_here_thread = None  # Declare globally to manage the thread

def resource_path(relative_path):
    """Get the absolute path to a resource, works for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def im_here():
    # Main program, simple mouse wiggle to simulate that the user is in fact here.
    while icon_enabled:
        move(0, 1)
        move(0, -1)
        for i in range(30):  # Check every second for 30 seconds
            if not icon_enabled:
                return
            time.sleep(1)

def enable_app():
    # Starts a thread with the im_here function running
    global icon_enabled, im_here_thread
    if icon_enabled:  # Avoid duplicate threads
        return
    icon_enabled = True
    im_here_thread = threading.Thread(target=im_here, daemon=True)
    print("Enable was called.")
    im_here_thread.start()
    update_tray_icon()

def disable_app():
    # Stops the im_here thread and updates the icon
    global icon_enabled
    if not icon_enabled:  # Avoid redundant actions
        return
    icon_enabled = False
    print("Disable was called.")
    if im_here_thread and im_here_thread.is_alive():
        im_here_thread.join()
    update_tray_icon()

def exit_app(tray_icon):
    # Exits the application
    global icon_enabled
    print("Exit was called.")
    icon_enabled = False
    if im_here_thread and im_here_thread.is_alive():
        im_here_thread.join()  # Ensure the thread stops
    tray_icon.stop()

def update_tray_icon():
    global tray_icon, icon_enabled
    if icon_enabled:
        tray_icon.icon = Image.open(enabled_icon_path_absolute)
    else:
        tray_icon.icon = Image.open(disabled_icon_path_absolute)
    tray_icon.update_menu()  # Refresh the menu to show updated state

def create_tray_icon():
    # Global variables for icon paths
    global tray_icon, disabled_icon_path_absolute, enabled_icon_path_absolute

    # Load icon paths for the bundled executable
    enabled_icon_path_absolute = resource_path("icons/enabled_icon.ico")
    disabled_icon_path_absolute = resource_path("icons/disabled_icon.ico")

    # Instantiate an image object for the initial icon
    icon_image = Image.open(disabled_icon_path_absolute)

    def menu_item_checked(option):
        # This function dynamically sets the checkmark for the active item
        return option and icon_enabled

    # Create the tray icon
    tray_icon = icon(
        "im_here",
        icon_image,
        menu=menu(
            item("Enable", enable_app, checked=lambda _: icon_enabled),
            item("Disable", disable_app, checked=lambda _: not icon_enabled),
            item("Exit", exit_app),
        ),
    )

    tray_icon.run()

# Call the application
create_tray_icon()
