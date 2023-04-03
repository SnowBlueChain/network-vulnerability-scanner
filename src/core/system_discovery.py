from scapy.all import *


def icmp_trace(ip: str) -> None:
    p = sr1(IP(dst=ip) / ICMP() / Raw(load="Hello World"), timeout=1, verbose=0)
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
