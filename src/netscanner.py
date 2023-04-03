import random
import socket

from core.ports import scan_ports
from core.system_discovery import icmp_trace
from utils.ascii_art import ART, NAME
from utils.user import admin_check, user_system_check


def get_ip() -> str:
    try:
        ip = input("\033[1;33m" + "Enter IPv4: " + "\033[1;35m")
        print("\033[0m", end="")
        socket.inet_aton(ip)
    except socket.error:
        print("Invalid IPv4")
        exit()

    return ip


if __name__ == "__main__":
    user_system_check()
    admin_check()

    print(ART[random.randint(0, len(ART) - 1)])
    print(NAME)

    ip = get_ip()
    icmp_trace(ip)
    established = scan_ports(ip)

    if not established:
        print(f"{ip} is not listening on any port")
