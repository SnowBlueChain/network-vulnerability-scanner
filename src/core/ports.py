import socket


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
