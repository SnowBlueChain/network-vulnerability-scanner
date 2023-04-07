"""Fuzzing module.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import readline
import requests


def request_response(url: str) -> None:
    """Send a request to a URL.

    Args:
        url (str): URL to send the request.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] Found directory: {url}")
    except requests.exceptions.ConnectionError:
        pass


def dir_fuzzer(ip: str, http: bool = False, https: bool = False) -> None:
    """Fuzz directories.

    Args:
        ip (str): IP address to fuzz.
        http (bool, optional): Use HTTP protocol. Defaults to False.
        https (bool, optional): Use HTTPS protocol. Defaults to False.
    """
    print("\nDIRECTORY DISCOVERY")
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    dictionary = input("  Enter a path to a wordlist: ")

    with open(dictionary, "r") as wordlist:
        print("\033[1;31m" + "\n[*] Fuzzing directories..." + "\033[0m")

        for word in wordlist:
            word = word.strip()
            if http:
                url = f"http://{ip}/{word}"
                request_response(url)
            if https:
                url = f"https://{ip}/{word}"
                request_response(url)
