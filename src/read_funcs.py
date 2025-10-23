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


def ls(cur_path: str, cin: list[str]) -> None:
    """
    Выводит содержимое каталога
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - токены команды
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)                 #Переход в рабочую директорию

    #Форматирование токенов
    if len(cin) == 0:     #Если токенов нет - флаг пустой, директория текущая
        flag = ''
        path = os.getcwd()
    elif len(cin) == 1:   #Если токен 1 - это либо флаг, либо директория
        if cin[0][0] == '-':
            flag = cin[0]
            path = os.getcwd()
        else:
            flag = ''
            path = cin[0]
    elif len(cin) == 2:   #Если токенов 2 - это флаг и директория(или нет)
        if cin[0][0] != '-':
            print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды ls")
            return
        else:
            flag = cin[0]
            path = cin[1]
    else:                 #Если токенов больше 2 - ошибка избытка аргументов
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды ls")
        return

    path = os.path.normpath(path.strip())    #Нормализация пути
    path = path.replace('\\', "/")+"/"

    try:                  #Попытка вывода информации по файлам
        if flag == "-l":                    #Если флаг - выводим подробно
            for file in os.listdir(path):
                stats = os.stat(os.path.join(path, file))
                size = stats.st_size
                change_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(stats.st_mtime))
                permission = permissions(stats.st_mode)
                if permission[0] == 'd':
                    print(f"{permission}  {size:>12}  {change_time}  \033[01;38;05;63;48;05;46m{file}\033[0m")
                else:
                    print(f"{permission}  {size:>12}  {change_time}  \033[01;38;05;46m{file}\033[0m")

        elif flag == "":                    #Если нет флага - выводим только названия
            for file in os.listdir(path):
                if stat.S_ISDIR(os.stat(os.path.join(path, file)).st_mode):
                    print(f"\033[01;38;05;63;48;05;46m{file}\033[0m")
                else:
                    print(f"\033[01;38;05;46m{file}\033[0m")

        else:                               #Если неизвестный флаг - ошибка
            print(f'\033[01;38;05;196mОшибка:\033[0m флаг "{flag}" вам в руки, а для этой функции существует только флаг "-l".')

    except OSError:                         #Остальные ошибки
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
    except FileNotFoundError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
    except PermissionError:
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")


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
        return os.getcwd()
    path = path.strip().replace('\\', '/')
#-------------------------
#-------------------------
#azazazazazazazazazazazaza
#-------------------------
#-------------------------
    if '~' in path:
        # print('azaza', os.path.normpath(os.path.expanduser(path)), [path])
        home_path = os.path.normpath(os.path.expanduser(path[path.rfind('~'):]))
        path = home_path
    else:
        new_path = os.path.normpath(path)
        path = new_path

    path = path.strip()
    path += "/"
    # print(path)
    try:
        os.chdir(path)
    except OSError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
    except FileNotFoundError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
    except PermissionError:
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
    return os.getcwd()


def cat(cur_path: str, cin: list[str]) -> None:
    """
    Выводит содержимое указанного файла
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - путь к целевому файлу
    :return: Функция ничего не возвращает
    """

    os.chdir(cur_path)

    #Форматирование токенов
    if len(cin) == 1:
        path = cin[0]
    else:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды cd")
        return
    path = path.strip().replace('\\', '/')

    #Попытка чтения файла
    try:
        with open(path, 'rb') as f:
            for i in f.readlines():
                o = str(i)[2:-1]
                if o[-4:] == "\\r\\n":
                    o = o[:-4]
                print(o)
    except OSError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
    except FileNotFoundError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
    except PermissionError:
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
