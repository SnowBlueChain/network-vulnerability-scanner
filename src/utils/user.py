import ctypes
import os


def user_system_check(user_system: str) -> None:
    if user_system != "Linux" and user_system != "Windows":
        print("Your OS is not supported yet")
        exit()


def admin_check(user_system: str) -> None:
    if (user_system == "Linux" and not os.getuid() == 0) or (
        user_system == "Windows" and not ctypes.windll.shell32.IsUserAnAdmin()
    ):
        print("Error: permission denied, run as root")
        exit()
