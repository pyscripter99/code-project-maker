# CODE PROJECT MAKER #

## setup ##
linux:
    sudo apt install python3-tk -y
    python3 -m pip install -r requirements.txt
    chmod +x build.sh
    ./build.sh

windows:
    On python installer make sure "tcl/tk" is enabled
    python -m pip install -r requirments.txt
    ./build.bat

add the executable to path

## running ##
Ddd a keyboard shortcut for the command code_maker or run code_maker in the terminal.
Press 1 to toggle use template, and enter to make the project.

## note ##
Make sure to add config.json where the executable is stored