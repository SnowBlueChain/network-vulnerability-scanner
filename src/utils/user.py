"""Check the user system.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import ctypes
import os
from platform import system

user_system = system()


def user_system_check() -> None:
    """Check the user system and exit if it is not supported."""

    if user_system != "Linux" and user_system != "Windows":
        print("Your OS is not supported yet")
        exit()


def admin_check() -> None:
    """Check if the user is root or not and exit if not."""

    if (user_system == "Linux" and not os.getuid() == 0) or (
        user_system == "Windows" and not ctypes.windll.shell32.IsUserAnAdmin()
    ):
        print("Error: permission denied, run as root")
        exit()
