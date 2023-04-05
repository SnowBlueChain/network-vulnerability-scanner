"""Open host ports.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import socket

open_ports = []


def scan_ports(ip: str) -> bool:
    """Scan open ports in a host.

    Args:
        ip (str): Host IP.

    Returns:
        bool: True if there are open ports, False otherwise.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    established = False

    for port in range(1, 65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.settimeout(0.5)
                client_socket.connect((ip, port))

                if not established:
                    print("PORT\t  STATE")
                    established = True

                open_ports.append(port)
                print(f"{port}/tcp".ljust(9), "open")
            except:
                pass

    return established
