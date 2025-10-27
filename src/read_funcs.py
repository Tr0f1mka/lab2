"""
-----------------------
--Функции ls, cd, cat--
-----------------------
"""


"""-----Библиотеки-----"""

import os                                          # noqa: E402
import stat                                        # noqa: E402
import time                                        # noqa: E402
import logging                                     # noqa: E402
from src.config import LOGGING_CONFIG              # noqa: E402
from src.check_input import normalisation_path     # noqa: E402



"""-------Логер--------"""

logging.config.dictConfig(LOGGING_CONFIG)
loger = logging.getLogger(__name__)



"""------Функции-------"""

def permissions(mode: int) -> str:
    """
    Преобразовывает численное значение права доступа в вид Linux
    :param mode: Целое число - право доступа
    :return: Строка - право доступа как в Linux
    """
    perms = 'd' if stat.S_ISDIR(mode) else '-'          # Разрешение на директорию
    perms += 'r' if mode & stat.S_IRUSR else '-'        # Разрешение на чтение владельцем
    perms += 'w' if mode & stat.S_IWUSR else '-'        # Разрешение на запись владельцем
    perms += 'x' if mode & stat.S_IXUSR else '-'        # Разрешение на исполнение владельцем
    perms += 'r' if mode & stat.S_IRGRP else '-'        # Разрешение на чтение группой
    perms += 'w' if mode & stat.S_IWGRP else '-'        # Разрешение на запись группой
    perms += 'x' if mode & stat.S_IXGRP else '-'        # Разрешение на исполнение группой
    perms += 'r' if mode & stat.S_IROTH else '-'        # Разрешение на чтение другими поьзователями
    perms += 'w' if mode & stat.S_IWOTH else '-'        # Разрешение на запись другими поьзователями
    perms += 'x' if mode & stat.S_IXOTH else '-'        # Разрешение на исполнение другими поьзователями
    return perms


def ls(cur_path: str, paths: list[str], flags: list[str]) -> None:
    """
    Выводит содержимое каталога
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Список строк - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)                 #Переход в рабочую директорию

    if flags:
        for i in flags:
            if i == '-l':
                flag = i
            else:
                print(f'\033[01;38;05;196mОшибка:\033[0m флаг "{i}" вам в руки, а для этой функции существует только флаг "-l".')
                loger.error(f"Result: Unknown flag {i}")
                return
    else:
        flag = ""

    if paths:
        for j in range(len(paths)):
            paths[j] = normalisation_path(os.getcwd(), paths[j])
            # print(paths[j])
    else:
        paths = [os.getcwd()]
        # print('bibas')

    # print(paths)
    # print(flags)

    try:                  #Попытка вывода информации по файлам
        if flag == "-l":                    #Если флаг - выводим подробно
            for path in paths:
                print(path)
                for file in os.listdir(path):
                    stats = os.stat(os.path.join(path, file))
                    size = stats.st_size
                    change_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(stats.st_mtime))
                    permission = permissions(stats.st_mode)
                    if permission[0] == 'd':
                        print(f"   {permission}  {size:>12}  {change_time}  \033[01;38;05;63;48;05;46m{file}\033[0m")
                    else:
                        print(f"   {permission}  {size:>12}  {change_time}  \033[01;38;05;46m{file}\033[0m")
                    # print(stats, type(stats))

        else:                    #Если нет флага - выводим только названия
            for path in paths:
                print(path)
                for file in os.listdir(path):
                    if stat.S_ISDIR(os.stat(os.path.join(path, file)).st_mode):
                        print(f"   \033[01;38;05;63;48;05;46m{file}\033[0m")
                    else:
                        print(f"   \033[01;38;05;46m{file}\033[0m")
        loger.info("Result: Succes")

    except FileNotFoundError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: File not found")
    except PermissionError:
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Result: Not enough permissions")
    except OSError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: Error of OS")


def cd(cur_path: str, cin: list[str]) -> str:
    """
    Переход в другую директорию
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - путь к целевой директории
    :return: Функция возвращает целевой или текущий адрес
    """

    os.chdir(cur_path)

    #Форматирование токенов
    if len(cin) == 1:
        path = cin[0]
    else:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды cd")
        loger.error("Result: Too many arguments")
        return os.getcwd()

    path = normalisation_path(os.getcwd(), path)
    # print([path])

    try:
        os.chdir(path)
        loger.info("Result: Succes")
    except FileNotFoundError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: File not found")
    except PermissionError:
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Result: Not enough permissions")
    except OSError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: Error of OS")
    return os.getcwd()


def cat(cur_path: str, cin: list[str]) -> None:
    """
    Выводит содержимое указанного файла
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - путь к целевому файлу
    :return: Функция ничего не возвращает
    """

    os.chdir(cur_path)

    if cin:
        for i in range(len(cin)):
            cin[i] = normalisation_path(os.getcwd(), cin[i])
    else:
        print("\033[01;38;05;196mОшибка:\033[0m у функции cat нет цели, но есть путь(должен быть)")
        loger.error("Result: Argument not found")
        return

    #Попытка чтения файла
    try:
        for path in cin:
            print(path)
            with open(path, 'rb') as f:
                for line in f.readlines():
                    o = str(line)[2:-1]
                    if o[-4:] == "\\r\\n":
                        o = o[:-4]
                    print(f"\033[01;48;05;64m   \033[0m{o}")
        loger.info("Result: Succes")
    except FileNotFoundError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: File not found")
    except PermissionError:
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Result: Not enough permissions")
    except OSError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: Error of OS")
