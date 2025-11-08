"""-------Библиотеки-------"""

import os
from src.tools import user_input, parser
import src.read_funcs as read_funcs
import src.format_funcs as format_funcs
import src.archive_funcs as archive_funcs
from src.patterns import Color

"""
------------------------
------Главный файл------
------------------------
"""


"""----Словарь функций-----"""

funcs = {"ls"    : read_funcs.ls,
         "cd"    : read_funcs.cd,
         "cat"   : read_funcs.cat,
         "cp"    : format_funcs.cp,
         "mv"    : format_funcs.mv,
         "rm"    : format_funcs.rm,
         "unzip" : archive_funcs.unpack_archive,
         "untar" : archive_funcs.unpack_archive
        }

# path+flag - ls, cp, rm, cd, cat, mv, unzip, untar
# path+mode - zip, tar



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

    print(f'{Color.INPUT}help{Color.RESET} - выводит справку по функциям')
    print(f'{Color.INPUT}exit{Color.RESET} - завершает программу')
    print(f'{Color.INPUT}ls [-l] [<path>]{Color.RESET} - выводит содержимое директории')
    print(f'{Color.INPUT}cd <path>{Color.RESET} - переходит в указанную директорию')
    print(f'{Color.INPUT}cat <path>{Color.RESET} - выводит содержимое указанного файла')
    print(f'{Color.INPUT}cp [-r] <path> <dir>{Color.RESET} - копирует файл(директорию) в dir')
    print(f'{Color.INPUT}mv <path> <dir>{Color.RESET} - перемещает файл(директорию) в dir')
    print(f'{Color.INPUT}rm [-r] <path> [<path> ...]{Color.RESET} - удаляет указанные файлы(директории)')
    print(f'{Color.INPUT}zip <path> <archive.zip>{Color.RESET} - создаёт zip-архив из директории с указанным именем')
    print(f'{Color.INPUT}unzip <path>{Color.RESET} - разархивирует указанный zip-архив в рабочую директорию')
    print(f'{Color.INPUT}tar <path> <archive.zip>{Color.RESET} - создаёт tar.gz-архив из директории с указанным именем')
    print(f'{Color.INPUT}untar <path>{Color.RESET} - разархивирует указанный tar.gz-архив в рабочую директорию')

    # loger.info("Result: Succes")


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    start()

    while ((cin_str := user_input()) != "exit"):

        if cin_str == "help":
            help()
        elif cin_str == "":
            continue
        else:                              #если не справка - парсим ввод и ищем команду
            # print(2)
            paths, flag = parser(cin_str)
            try:
                command = paths.pop(0)
                # result = funcs[command](cur_path=os.getcwd(), paths=paths, flags=flag)
                if command == 'zip' or command == 'tar':
                    archive_funcs.make_archive(os.getcwd(), paths, command if command == 'zip' else 'gztar', flag)
                else:
                    result = funcs[command](cur_path=os.getcwd(), paths=paths, flags=flag)
                    if result: 
                        os.chdir(result)
            except KeyError:
                print(f"Unknown command: {command}")
            except IndexError:
                print(f"Unknow1n command: {flag}")
        print()

    print(f"{Color.RESET}Завершение работы")
    # loger.info("Result: Completion of work")


if __name__ == "__main__":
    main()
