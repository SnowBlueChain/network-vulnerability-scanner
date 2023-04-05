"""Check the system of the target host.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

from scapy.all import *


def icmp_trace(ip: str) -> None:
    """Send an ICMP packet to the target host and check the ttl.

    Args:
        ip (str): The target host.
    """
    p = sr1(IP(dst=ip) / ICMP() / Raw(load="Hello World"), timeout=1, verbose=0)
    if not p:
        print("\nHost is down")
        exit()

    print("\nHost is up")
    which_system(ttl=p.ttl)


def which_system(ttl: str) -> None:
    """Determine the system of the target host.

    Args:
        ttl (str): The ttl of the ICMP packet.
    """
    if ttl <= 64:
        print(f"Linux/Unix -> ttl={ttl}\n")
    elif ttl <= 128:
        print(f"Windows -> ttl={ttl}\n")
    else:
        print("Unknown sytem\n")
