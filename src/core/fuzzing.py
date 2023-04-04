import requests


def request_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] Found directory: {url}")
    except requests.exceptions.ConnectionError:
        pass


def dir_fuzzer(ip, http=False, https=False):
    print("\nDIRECTORY DISCOVERY")
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
