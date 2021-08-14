import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["PyQt5"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PIPE Installer",
    version="1.0.0",
    description="Pipe Generator Beta Teste Version",
    options={"build_exe": build_exe_options},
    executables=[Executable("info.py", base=base)]
)