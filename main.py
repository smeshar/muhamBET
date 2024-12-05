import colorama
from colorama import Fore, just_fix_windows_console
import functions
import connection
import time

def main():
    just_fix_windows_console()
    functions.logo()
    version = "0.1.0"
    name = ""
    id = 0
    balance = 0



    print(f""" Версия игры: {version}\n---""")
    #
    # last_version = conn.get_version()
    # if version != last_version:
    #     print("Ваша версия игры устарела")
    #     print(f"Последняя версия игры: {last_version}")
    #     print("Пожалуйста скачайте последний релиз игры по ссылке https://github.com/smeshar/gasprom4/releases/")
    #     a = input()
    #     return
    print(
        f""" Чтобы играть вам нужно {Fore.LIGHTRED_EX}зарегистрироваться{Fore.RESET}/{Fore.LIGHTGREEN_EX}войти{Fore.RESET} в аккаунт
{Fore.LIGHTRED_EX} Зарегистрироваться{Fore.RESET} 1
{Fore.LIGHTGREEN_EX} Войти в существующий аккаунт{Fore.RESET} 2""")

    inp = int(input())
    if inp == 1:
        print(f'''---
{Fore.LIGHTGREEN_EX} Введите ваш никнейм (может содержать буквы, цифры и специальные символы, максимальная длина 20, аккаунты с непристойными никнеймами будут удалены){Fore.RESET}''')
        nick = input()
        print(f' {Fore.LIGHTBLUE_EX}Введите пароль (может содержать буквы, цифры и специальные символы, максимальная длина 20){Fore.RESET}')
        psw = input()
        print(f' {Fore.LIGHTYELLOW_EX}Успешная регистрация!{Fore.RESET}')
        time.sleep(0.5)

    elif inp == 2:
        print('---')
        print(
            f' {Fore.LIGHTGREEN_EX}Введите ваш никнейм{Fore.RESET}')
        nick = input()
        print(f' {Fore.LIGHTBLUE_EX}Введите пароль{Fore.RESET}')
        psw = input()
        time.sleep(1)

try:
    main()
except Exception as e:
    print(f"Вы получили ошибку: {e}")
    inp = input()
