import socket
from platform import system

from scapy.all import *

from utils.ascii_art import ART, NAME
from utils.user import admin_check, user_system_check


def get_ip() -> str:
    try:
        ip = input("Enter IPv4: ")
        socket.inet_aton(ip)
    except socket.error:
        print("Invalid IPv4")
        exit()

    return ip


def icmp_trace(ip: str) -> None:
    p = sr1(IP(dst=ip)/ICMP()/Raw(load="Hello World"), timeout=1, verbose=0)
    if not p:
        print("\nHost is down")
        exit()

    print("\nHost is up")
    which_system(ttl=p.ttl)


def which_system(ttl: str) -> None:
    if ttl <= 64:
        print(f"Linux/Unix -> ttl={ttl}\n")
    elif ttl <= 128:
        print(f"Windows -> ttl={ttl}\n")
    else:
        print("Unknown sytem\n")


def scan_ports(ip: str) -> bool:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    established = False

    print("PORT\t  STATE")

    for port in range(1, 65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.settimeout(0.5)
                client_socket.connect((ip, port))
                print(f"{port}/tcp".ljust(9), "open")
                established = True
            except:
                pass

    return established


if __name__ == "__main__":
    user_system = system()
    user_system_check(user_system)
    admin_check(user_system)

    print(ART[random.randint(0, len(ART) - 1)])
    print(NAME)

    ip = get_ip()
    icmp_trace(ip)
    established = scan_ports(ip)

    if not established:
        print(f"{ip} is not listening on any port")
