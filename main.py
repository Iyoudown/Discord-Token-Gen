import random, string, requests, time
from colorama import Fore
import os

def generate_token():
    starts = ["MTE0NDQ1", "MTEx", "MTIwOTQ2O", "MTE0NDky", "MTIxMTQ", "MTIxMjc"]
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
    secret = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    secret2 = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return f"{random.choice(starts)}{secret2}.{secret}.{token}"

def main():
    valid_count = 0
    inv_count = 0
    os.system("cls")
    os.system(f'Title Nexus "Token Gen" │ Valid: {valid_count} │ Invalid: {inv_count}')
    print(Fore.LIGHTMAGENTA_EX + '''
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    ''')
    while True:
        token = generate_token()
        response = requests.get("https://discord.com/api/v10/users/@me", headers={'Authorization': token})
        if response.status_code == 200:
            print(f"{Fore.RESET}{Fore.LIGHTBLUE_EX}token={Fore.LIGHTBLACK_EX}{token} {Fore.LIGHTBLUE_EX}-> {Fore.LIGHTGREEN_EX}Valid")
            valid_count += 1
            os.system(f'Title Nexus "Token Gen" │ Valid: {valid_count} │ Invalid: {inv_count}')
            with open("tokens.txt", 'a', encoding="utf-8") as File:
                File.write(f"{token}\n")
        else:
            print(f"{Fore.RESET}{Fore.LIGHTBLUE_EX}token={Fore.LIGHTBLACK_EX}{token} {Fore.LIGHTBLUE_EX}-> {Fore.LIGHTRED_EX}Invalid")
            inv_count += 1
            os.system(f'Title Nexus "Token Gen" │ Valid: {valid_count} │ Invalid: {inv_count}')
main()