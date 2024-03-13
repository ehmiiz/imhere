import PyInstaller.__main__
import os

icons_dir = "icons"
disabled_icon = os.path.abspath(os.path.join(icons_dir, "disabled_icon.ico"))
enabled_icon = os.path.abspath(os.path.join(icons_dir, "enabled_icon.ico"))
icons_dir_abs_path = os.path.abspath(icons_dir)

PyInstaller.__main__.run([
    'im_here.py',
    '--onefile',
    '--noconsole',
    f'--icon={disabled_icon}',
    f'--icon={enabled_icon}',
    '--name=imhere'
])