"""
------------------------
------главный файл------
------------------------
"""



"""-------библиотека-------"""

import os                                # noqa: E402
import src.check_input as check_input    # noqa: E402
import src.read_funcs as read_funcs      # noqa: E402
# import src.format_funcs as format_funcs  # noqa: E402



"""--------функции---------"""

def start() -> None:
    """
    Функция для вывода приветственного сообщения
    :return: Данная функция ничего не возвращает
    """

    print()
    print("TR0F1MKASOFT [Version 0.0.0.1]")
    print("Корпорация TR0F1MKASOFT (TR0F1MKASOFT Corporation). Все права защищены")
    print()

def help():
    """
    Функция для вывода справки по функциям
    :return: Данная функция ничего не возвращает
    """

    print('help - выводит справку по функциям')
    print('exit - завершает программу')


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    start()

    working = True
    while (working):
        cin_str = input(f"\033[01;38;05;46m{os.getlogin()}\033[0m:\033[01;38;05;63m{os.getcwd()}\033[0m$ ")
        cin_str = cin_str.strip()
        if cin_str == "exit":
            working = False
        elif cin_str == "help":
            help()
        else:
            cin = check_input.input_check(cin_str)
            # print(cin)
            match cin[0]:
                case 'ls':
                    read_funcs.ls(os.getcwd(), cin[1:])
                case 'cd':
                    os.chdir(read_funcs.cd(os.getcwd(), cin[1:]))
                case 'cat':
                    read_funcs.cat(os.getcwd(), cin[1:])
                case 'cp':
                    print('cp')
                case 'mv':
                    print('mv')
                case 'rm':
                    print('rm')
                case _:
                    print(f'\033[01;38;05;196mОшибка:\033[0m неопознанная команда {cin[0]}. Чтобы вывести список команд, введите "help".')


        print()

    print("Завершение работы")



if __name__ == "__main__":
    main()
