# Detect the os and clear the terminal
#####
#Follow me on Github: https://github.com/TheRealMitch
#####

import subprocess
import os

def clear():
    """
    To clear the working terminal window.
    """
    if os.name == "posix": # detect if the operating is linux/macos
        subprocess.call("clear", shell=True)
    else:
        subprocess.call("cls", shell=True)

