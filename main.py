import socket

try:
    ip = input("Enter IPv4: ")
    socket.inet_aton(ip)
except socket.error:
    print("Invalid IPv4")
    exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
established = False

for port in range(1, 65535):
    try:
        client_socket.connect((ip, port))
        print(f"{port}/tcp OPEN")
        established = True
    except:
        pass

if not established:
    print(f"{ip} is not listening on any port")
