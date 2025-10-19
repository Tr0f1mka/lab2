"""
-----------------------
--Функции ls, cd, cat--
-----------------------
"""


"""-----Библиотеки-----"""

import os       # noqa: E402
import stat     # noqa: E402
import time     # noqa: E402


"""------Функции-------"""

def permissions(mode: int) -> str:
    """
    Преобразовывает численное значение права доступа в вид Linux
    :param mode: Целое число - право доступа
    :return: Строка - право доступа как в Linux
    """
    perms = 'd' if stat.S_ISDIR(mode) else '-'
    perms += 'r' if mode & stat.S_IRUSR else '-'
    perms += 'w' if mode & stat.S_IWUSR else '-'
    perms += 'x' if mode & stat.S_IXUSR else '-'
    perms += 'r' if mode & stat.S_IRGRP else '-'
    perms += 'w' if mode & stat.S_IWGRP else '-'
    perms += 'x' if mode & stat.S_IXGRP else '-'
    perms += 'r' if mode & stat.S_IROTH else '-'
    perms += 'w' if mode & stat.S_IWOTH else '-'
    perms += 'x' if mode & stat.S_IXOTH else '-'
    return perms


def ls(flag: str, path: str) -> None:
    """
    Выводит содержимое каталога
    :param flag: Строка - флаг функции
    :param path: Строка - путь к директории
    :return: Данная функция ничего не возвращает
    """

    path = path.replace(os.sep, "/")+"/"
    if flag == "-l":
        try:
            for file in os.listdir(path):
                stats = os.stat(os.path.join(path, file))
                size = stats.st_size
                change_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(stats.st_mtime))
                permission = permissions(stats.st_mode)
                print(f"{permission}  {size:>8}  {change_time}  {file}")

        except OSError:
            print("Указанного пути не существует")
        except FileNotFoundError:
            print("Указанного пути не существует")
        except PermissionError:
            print("У тебя здесь нет власти(недостаточно прав)")

    elif flag == "":
        try:
            for file in os.listdir(path):
                print(file)

        except OSError:
            print("Указанного пути не существует")
        except FileNotFoundError:
            print("Указанного пути не существует")
        except PermissionError:
            print("У тебя здесь нет власти(недостаточно прав)")

    else:
        print(f'Флаг "{flag}" вам в руки, а для этой функции существует только флаг "-l".')


def cd(path: str) -> str:
    """
    Переход в другую директорию
    :param path: Строка - путь к целевой директории
    :return: Функция ничего не возвращает
    """

    path = path.replace(os.sep, "/")+"/"
    try:
        os.chdir(path)
        return path
    except OSError:
        print()
        print("Указанного пути не существует")
    except FileNotFoundError:
        print()
        print("Указанного пути не существует")
    except PermissionError:
        print()
        print("У тебя здесь нет власти(недостаточно прав)")
    return "123.txt"
