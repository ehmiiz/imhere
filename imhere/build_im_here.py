import os
import PyInstaller.__main__

# Get the full path to the icons directory
icons_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))

print(icons_dir)

# Run PyInstaller
PyInstaller.__main__.run([
    'im_here.py',
    '--onefile',
    '--noconsole',
    f'--icon={icons_dir}',  # Use the icon file path
    '--name=imhere'
])
