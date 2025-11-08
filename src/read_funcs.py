"""-----Библиотеки-----"""

import os                                          
import stat                                        
import time             
from src.tools import check_flags, check_paths, create_log
from src.patterns import Color



"""
-----------------------
--Функции ls, cd, cat--
-----------------------
"""



"""------Функции-------"""

def permissions(mode: int) -> str:
    """
    Преобразовывает численное значение права доступа в вид Linux
    :param mode: Целое число - право доступа
    :return: Строка - право доступа как в Linux
    """

    perms = 'd' if stat.S_ISDIR(mode) else '-'          # разрешение на директорию
    perms += 'r' if mode & stat.S_IRUSR else '-'        # разрешение на чтение владельцем
    perms += 'w' if mode & stat.S_IWUSR else '-'        # разрешение на запись владельцем
    perms += 'x' if mode & stat.S_IXUSR else '-'        # разрешение на исполнение владельцем
    perms += 'r' if mode & stat.S_IRGRP else '-'        # разрешение на чтение группой
    perms += 'w' if mode & stat.S_IWGRP else '-'        # разрешение на запись группой
    perms += 'x' if mode & stat.S_IXGRP else '-'        # разрешение на исполнение группой
    perms += 'r' if mode & stat.S_IROTH else '-'        # разрешение на чтение другими поьзователями
    perms += 'w' if mode & stat.S_IWOTH else '-'        # разрешение на запись другими поьзователями
    perms += 'x' if mode & stat.S_IXOTH else '-'        # разрешение на исполнение другими поьзователями
    return perms


@create_log
def ls(cur_path: str, paths: list[str], flags: str) -> None:
    """
    Выводит содержимое каталога
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Строка - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, "l")
    paths = check_paths(paths, 0)
    paths = paths if paths else [os.getcwd()]

    if flags == "":
        for path in paths:
            print(path)
            for file in os.listdir(path):
                if stat.S_ISDIR(os.stat(os.path.join(path, file)).st_mode):
                    print(f"   {Color.DIR}{file}{Color.RESET}")
                else:
                    print(f"   {Color.FILE}{file}{Color.RESET}")
    else:
        for path in paths:
            print(path)
            for file in os.listdir(path):
                stats = os.stat(os.path.join(path, file))
                size = stats.st_size
                change_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(stats.st_mtime))
                permission = permissions(stats.st_mode)
                #директории - синие символы на зелёном фоне
                if permission[0] == 'd':
                    print(f"   {permission}  {size:>12}  {change_time}  \033[01;38;05;63;48;05;46m{file}{Color.RESET}")
                #файлы - зелёные символы без фона
                else:
                    print(f"   {permission}  {size:>12}  {change_time}  {Color.FILE}{file}{Color.RESET}")
                # print(stats, type(stats))


@create_log
def cd(cur_path: str, paths: list[str], flags: str) -> None:
    """
    Переход в другую директорию
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Строка - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, "")
    paths = check_paths(paths, 1)

    os.chdir(paths[0])

    return paths[0]


@create_log
def cat(cur_path: str, paths: list[str], flags: str) -> None:
    """
    Выводит содержимое указанного файла
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Строка - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, "")
    paths = check_paths(paths, -1)

    for path in paths:
        print(path)
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                print(f"{Color.PAGE}   {Color.RESET}{line}", end="")