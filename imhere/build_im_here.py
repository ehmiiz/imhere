import PyInstaller.__main__
import os

icons_dir = "icons"
disabled_icon = os.path.join(icons_dir, "disabled_icon.ico")
enabled_icon = os.path.join(icons_dir, "enabled_icon.ico")

PyInstaller.__main__.run([
    'im_here.py',
    '--onefile',
    '--noconsole',
    '--add-data=' + f'{disabled_icon};icons',
    '--add-data=' + f'{enabled_icon};icons',
    '--name=imhere',
    '--icon=' + disabled_icon  # Set the default icon for the exe
])
