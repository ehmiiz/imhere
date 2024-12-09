# I'm here

!['demo'](im_here.gif)

Minimalistic system tray application for keeping your PC active while being AFK for Windows.

## Setup

```powershell
git clone git@github.com:ehmiiz/imhere.git
```

### Create a virtual environment from the requirements

1. cd imhere
2. python -m venv .venv

alternativly:

1. Open `imhere/` in vscode
2. ctrl + shift + p -> Python: Create Environment
3. Use existing `requirements.txt`

### Start the application

Using PowerShell:

```powershell
Start-Job {python.exe .imhere\im_here.py}
```

Using Python:

```powershell
python imhere.py
```

### Building the application

1. `python build_imhere.py`
2. Open the .exe in `imhere\dist\imhere.exe`
