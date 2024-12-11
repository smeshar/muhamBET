import colorama
from colorama import Fore, just_fix_windows_console
import functions
import connection
import time
import os

def main():
    just_fix_windows_console()
    functions.logo()
    version = "0.1.0"
    name = ""
    id = 0
    balance = 0
    conn = connection.Conn()

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
        nick = input(f'---\n{Fore.LIGHTGREEN_EX} Введите ваш никнейм (аккаунт должен быть зарегистрирован в Gasprom Game){Fore.RESET}\n')
        psw = input(f'{Fore.LIGHTBLUE_EX} Введите пароль{Fore.RESET}\n')
        key = input(f'{Fore.LIGHTYELLOW_EX} Введите ваш ключ к игре{Fore.RESET}\n')

        register_data = conn.register(nick, psw, key)
        id = int(register_data[0])
        name = register_data[1]
        balance = float(register_data[2])

        print(f'{Fore.LIGHTYELLOW_EX} Успешная регистрация!{Fore.RESET}')
        time.sleep(0.5)

    elif inp == 2:
        nick = input(f'---\n{Fore.LIGHTGREEN_EX} Введите ваш никнейм{Fore.RESET}\n')
        psw = input(f'{Fore.LIGHTBLUE_EX} Введите пароль{Fore.RESET}\n')

        login_data = conn.login(nick, psw)
        id = int(login_data[0])
        name = login_data[1]
        balance = float(login_data[3])

        print(f'{Fore.LIGHTYELLOW_EX} Успешная авторизация!{Fore.RESET}')
        time.sleep(1)

    while True:
        # EVERYDAY NEWS
        print(f"--- \n"
              f" Коэффициент на команду {functions.get_team()}: {Fore.LIGHTRED_EX}{123123}{Fore.RESET} \n"
              f" Коэффициент на команду {functions.get_team()}: {Fore.LIGHTBLUE_EX}{634564356}{Fore.RESET} \n"
              f"---\n"
              f" Ваш баланс: {Fore.GREEN}{balance}{Fore.RESET}\n"
              f" Осталось времени до закрытия ставок: {Fore.YELLOW}{2345325234}{Fore.RESET} с\n"
              f"---\n"
              f" Текущие ставки:")

        # for transactions in all[4]: print(transactions)
        #
        print(f"""---\n{Fore.CYAN} Топ игроков:{Fore.RESET}""")
        # for top_players in all[5]: print(top_players)

        print(f"---\n"
              f" {Fore.LIGHTGREEN_EX}Сделать ставку 1{Fore.RESET}\n"
              f" {Fore.LIGHTYELLOW_EX}Обновить ставки 2{Fore.RESET}\n"
              f"---")

        try:
            query = int(input())
        except:
            print("Неверный ввод")
            time.sleep(1)
            clear = lambda: os.system('cls')
            clear()
            continue

        # MAKE BET
        if query == 1:
            continue

        # RELOAD
        if query == 2:
            clear = lambda: os.system('cls')
            clear()
            continue

        time.sleep(1)
        clear = lambda: os.system('cls')
        clear()


try:
    main()
except Exception as e:
    print(f"Вы получили ошибку: {e}")
    inp = input()
