from colorama import Fore
import random


def logo():
    print(f"""---{Fore.RED}
  __  __       _                     ____  ______ _______ 
 |  \/  |     | |                   |  _ \|  ____|__   __|
 | \  / |_   _| |__   __ _ _ __ ___ | |_) | |__     | |   
 | |\/| | | | | '_ \ / _` | '_ ` _ \|  _ <|  __|    | |   
 | |  | | |_| | | | | (_| | | | | | | |_) | |____   | |   
 |_|  |_|\__,_|_| |_|\__,_|_| |_| |_|____/|______|  |_|{Fore.RESET}   
---""")


def get_team():
    l = []
    with open("singular.txt", "r", encoding='utf-8') as f:
        l = f.read().splitlines()

    ans = random.choice(l)
    return ans
