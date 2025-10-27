"""
------------------------
------Главный файл------
------------------------
"""



"""-------Библиотека-------"""

import os                                  # noqa: E402
import logging                             # noqa: E402
from src.config import LOGGING_CONFIG      # noqa: E402
import src.check_input as check_input      # noqa: E402
import src.read_funcs as read_funcs        # noqa: E402
import src.format_funcs as format_funcs    # noqa: E402
import src.archive_funcs as archive_funcs  # noqa: E402



"""---------Логер----------"""

logging.config.dictConfig(LOGGING_CONFIG)
loger = logging.getLogger(__name__)



"""--------Функции---------"""

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

    print('\033[01;38;05;222mhelp\033[0m - выводит справку по функциям')
    print('\033[01;38;05;222mexit\033[0m - завершает программу')
    print('\033[01;38;05;222mls [-l] [<path>]\033[0m - выводит содержимое директории')
    print('\033[01;38;05;222mcd <path>\033[0m - переходит в указанную директорию')
    print('\033[01;38;05;222mcat <path>\033[0m - выводит содержимое указанного файла')
    print('\033[01;38;05;222mcp [-r] <path> <dir>\033[0m - копирует файл(директорию) в dir')
    print('\033[01;38;05;222mmv <path> <dir>\033[0m - перемещает файл(директорию) в dir')
    print('\033[01;38;05;222mrm [-r] <path> [<path> ...]\033[0m - удаляет указанные файлы(директории)')
    print('\033[01;38;05;222mzip <path> <archive.zip>\033[0m - создаёт zip-архив из директории с указанным именем')
    print('\033[01;38;05;222munzip <path>\033[0m - разархивирует указанный zip-архив в рабочую директорию')
    print('\033[01;38;05;222mtar <path> <archive.zip>\033[0m - создаёт tar.gz-архив из директории с указанным именем')
    print('\033[01;38;05;222muntar <path>\033[0m - разархивирует указанный tar.gz-архив в рабочую директорию')

    loger.info("Result: Succes")


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    start()

    working = True
    while (working):
        cin_str = input(f"\033[01;38;05;46m{os.getlogin()}\033[0m:\033[01;38;05;63m{os.getcwd()}\033[0m$ \033[01;38;05;222m")
        print('\033[0m', end = '')
        loger.info(cin_str)
        cin_str = cin_str.strip()
        if cin_str == "exit":
            working = False
        elif cin_str == "help":
            help()
        else:
            cin = check_input.input_check(cin_str)
            if cin[0]:
                flags = cin[1]
                paths = cin[0][1:]

                match cin[0][0]:
                    case 'ls':
                        read_funcs.ls(os.getcwd(), paths, flags)

                    case 'cd':
                        if flags:
                            print('\033[01;38;05;196mОшибка:\033[0m для этой функции не существует флагов.')
                            loger.error("Result: There are no flags for function cd")
                        else:
                            os.chdir(read_funcs.cd(os.getcwd(), paths))
                    case 'cat':
                        if flags:
                            print('\033[01;38;05;196mОшибка:\033[0m для этой функции не существует флагов.')
                            loger.error("Result: There are no flags for function cat")
                        else:
                            read_funcs.cat(os.getcwd(), paths)

                    case 'cp':
                        format_funcs.cp(os.getcwd(), paths, flags)

                    case 'mv':
                        if flags:
                            print('\033[01;38;05;196mОшибка:\033[0m для этой функции не существует флагов.')
                            loger.error("Result: There are no flags for function mv")
                        else:
                            format_funcs.mv(os.getcwd(), paths)

                    case 'rm':
                        format_funcs.rm(os.getcwd(), paths, flags)

                    case 'zip':
                        if flags:
                            print('\033[01;38;05;196mОшибка:\033[0m для этой функции не существует флагов.')
                            loger.error("Result: There are no flags for function zip")
                        else:
                            archive_funcs.zip(os.getcwd(), paths)

                    case 'unzip':
                        if flags:
                            print('\033[01;38;05;196mОшибка:\033[0m для этой функции не существует флагов.')
                            loger.error("Result: There are no flags for function unzip")
                        else:
                            archive_funcs.unzip(os.getcwd(), paths)

                    case 'tar':
                        if flags:
                            print('\033[01;38;05;196mОшибка:\033[0m для этой функции не существует флагов.')
                            loger.error("Result: There are no flags for function tar")
                        else:
                            archive_funcs.tar(os.getcwd(), paths)

                    case 'untar':
                        if flags:
                            print('\033[01;38;05;196mОшибка:\033[0m для этой функции не существует флагов.')
                            loger.error("Result: There are no flags for function untar")
                        else:
                            archive_funcs.untar(os.getcwd(), paths)

                    case _:
                        print(f'\033[01;38;05;196mОшибка:\033[0m неопознанная команда {cin[0][0]}. Чтобы вывести список команд, введите "help".')
                        loger.error(f"Result: Unknoun command: {cin[0][0]}")
            else:
                continue

        print()

    print("Завершение работы")
    loger.info("Result: Completion of work")


if __name__ == "__main__":
    main()
