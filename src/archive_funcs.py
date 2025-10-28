"""
---------------------------
----Функции для архивов----
---------------------------
"""



"""-------Библиотека-------"""

import os                                          # noqa: E402
import zipfile                                     # noqa: E402
import tarfile                                     # noqa: E402
import logging                                     # noqa: E402
from src.config import LOGGING_CONFIG              # noqa: E402
from src.check_input import normalisation_path     # noqa: E402



"""---------Логер---------"""

logging.config.dictConfig(LOGGING_CONFIG)       #настройка логера
loger = logging.getLogger(__name__)



"""--------Функции--------"""

def zip(cur_path: str, paths: list[str]) -> None:
    """
    Создаёт zip-архив
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if len(paths) == 2:                     #проверка, что дано только 2 пути: источник и назначение
        source = normalisation_path(os.getcwd(), paths[0])
        target = normalisation_path(os.getcwd(), paths[1])
    elif len(paths) > 2:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды zip")
        loger.error("Result: Too many arguments")
        return
    else:
        print("\033[01;38;05;196mОшибка:\033[0m недостаточно аргументов для команды zip")
        loger.error("Result: Too little arguments")
        return

    try:                                   #попытка архивнуть директорию
        if os.path.exists(source):
            if os.path.isdir(source):
                with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, dirs, files in os.walk(source):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, start=source)
                            zipf.write(file_path, arcname)
                loger.info("Result: Succes")
            else:                              #ошибка, если не директория
                print("\033[01;38;05;196mОшибка:\033[0m нельзя архивировать файлы")
                loger.error("Result: Try create archive from file")
        else:                               #ошибка, если нет этого
            print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
            loger.error("Result: File not found")
    except PermissionError:                #ошибка, если нет прав
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Result: Not enough permissions")
    except OSError:                        #прочие ошибки ОС
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: Error of OS")


def unzip(cur_path: str, paths: list[str]) -> None:
    """
    Разархивирует zip-архив
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if len(paths) == 1:                  #проверка, что дан только 1 путь: источник
        source = normalisation_path(os.getcwd(), paths[0])
    elif len(paths) > 1:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды unzip")
        loger.error("Result: Too many arguments")
        return
    else:
        print("\033[01;38;05;196mОшибка:\033[0m у функции unzip нет цели, но есть путь(должен быть)")
        loger.error("Result: Too little arguments")
        return

    try:                                 #попытка разархивнуть директорию
        with zipfile.ZipFile(source, 'r') as zipf:
            zipf.extractall(os.getcwd())
        loger.info("Result: Succes")
    except FileNotFoundError:            #ошибка, если нет архива
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: File not found")
    except PermissionError:              #ошибка, если нет прав
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Result: Not enough permissions")
    except OSError:                      #прочие ошибки ОС
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: Error of OS")


def tar(cur_path: str, paths: list[str]) -> None:
    """
    Создаёт tar-архив
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if len(paths) == 2:                     #проверка, что дано только 2 пути: источник и назначение
        source = normalisation_path(os.getcwd(), paths[0])
        target = normalisation_path(os.getcwd(), paths[1])
    elif len(paths) > 2:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды tar")
        loger.error("Result: Too many arguments")
        return
    else:
        print("\033[01;38;05;196mОшибка:\033[0m недостаточно аргументов для команды tar")
        loger.error("Result: Too little arguments")
        return

    try:                                    #попытка архивнуть директорию
        if os.path.exists(source):
            if os.path.isdir(source):
                with tarfile.open(target, 'w:gz') as tarf:
                    tarf.add(source, arcname=os.path.basename(source))
                loger.info("Result: Succes")
            else:                               #ошибка, если не директория
                print("\033[01;38;05;196mОшибка:\033[0m нельзя архивировать файлы")
                loger.error("Result: Try create archive from file")
        else:                               #ошибка, если нет этого
            print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
            loger.error("Result: File not found")
    except PermissionError:                 #ошибка, если нет прав
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Result: Not enough permissions")
    except OSError:                         #прочие ошибки ОС
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: Error of OS")


def untar(cur_path: str, paths: list[str]) -> None:
    """
    Разархивирует tar-архив
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if len(paths) == 1:                  #проверка, что дан только 1 путь: источник
        source = normalisation_path(os.getcwd(), paths[0])
    elif len(paths) > 1:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды untar")
        loger.error("Result: Too many arguments")
        return
    else:
        print("\033[01;38;05;196mОшибка:\033[0m у функции untar нет цели, но есть путь(должен быть)")
        loger.error("Result: Too little arguments")
        return

    try:                                 #попытка разархивнуть директорию
        with tarfile.open(source, 'r:gz') as tarf:
            tarf.extractall()
        loger.info("Result: Succes")
    except FileNotFoundError:            #ошибка, если нет архива
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: File not found")
    except PermissionError:              #ошибка, если нет прав
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Result: Not enough permissions")
    except OSError:                      #прочие ошибки ОС
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Result: Error of OS")
