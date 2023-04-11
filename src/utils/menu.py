"""Menu module.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

from core.fuzzing import dir_fuzzer
from core.ports import open_ports


def dir_fuzzer_menu(ip: str) -> None:
    """Directory fuzzer menu.

    Args:
        ip (str): Host IP.
    """
    if 80 and 443 in open_ports:
        print("\nHTTP (80) and HTTPS (443) are open")
        dir_fuzzer(ip, http=True, https=True)
    elif 80 in open_ports:
        print("\nHTTP (80) is open")
        dir_fuzzer(ip, http=True)
    elif 443 in open_ports:
        print("\nHTTPS (443) is open")
        dir_fuzzer(ip, https=True)
    else:
        print("\n\033[0;31m" + "Error: HTTP and HTTPS are closed" + "\033[0m")


def menu(ip: str) -> None:
    """Netscanner menu.

    Args:
        ip (str): Host IP.
    """
    exit_app = False

    while not exit_app:
        print("\n\033[1;31m" + "Options:" + "\033[0m")
        # print("  Port scan -> p")
        print("  Fuzz directories -> f")
        print("  Quit -> q\n")

        option = input("\033[0;31m" + " -> ").lower()
        print("\033[0m", end="")

        if option == "f":
            dir_fuzzer_menu(ip)
        elif option == "q":
            exit_app = True
        else:
            print("\n\033[0;31m" + "Error: Invalid option" + "\033[0m")
