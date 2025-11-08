"""-----Библиотеки------"""

import os
import shutil
from src.tools import Color, check_flags, check_paths, create_log, user_input, logger
from src.my_exception import LessRMFlagError



"""
------------------------
---Функции cp, mv, rm---
------------------------
"""



"""-------Функции-------"""


@create_log
def cp(cur_path: str, paths: list[str], flags: str) -> None:
    """
    Копирует файл из одной директории в другую
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Строка - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, "r")
    paths = check_paths(paths, 2)
    source = paths[0]
    target = paths[1]
    if source.split(os.sep)[-1] != target.split(os.sep)[-1]:
        target = os.path.join(target, source.split(os.sep)[-1])


    if flags == "":
        if os.path.isdir(source):
            if not(os.listdir(source)):
                shutil.copytree(source, target)
            else:
                print(f'{Color.ERROR}Ошибка:{Color.RESET} для копирования директории с содержимым нужен флаг "-r"')
        else:
            shutil.copy2(source, target)
    else:
        shutil.copytree(source, target)


@create_log
def mv(cur_path: str, paths: list[str], flags: str) -> None:
    """
    Перемещает файл в назначение
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Строка - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, "")
    paths = check_paths(paths, 2)
    source = paths[0]
    target = paths[1]

    shutil.move(source, target)


@create_log
def rm(cur_path: str, paths: list[str], flags: str) -> None:
    """
    Перемещает файл в назначение
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Строка - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, "r")
    paths = check_paths(paths, -1)

    if flags == "":
        for path in paths:
            print(f"Вы уверены, что хотите удалить файл {path}? [y/n]")     #запрос подтверждения
            ans = user_input()
            if ans == "y":
                if os.path.isdir(path):
                    if not(os.listdir(path)):
                        shutil.rmtree(path)
                    else:
                        print(f"{Color.ERROR}Ошибка:{Color.RESET} для удаления директории с содержимым нужен флаг \"-r\"")
                        raise LessRMFlagError
                else:
                    os.remove(path)
            else:
                logger.info("[RESULT] <rm> Cancel delete")
    
    else:
        for path in paths:
            if (path[-2:] == ':\\') or (path == '/'):         #защита от удаления корня
                print(f"{Color.ERROR}Ошибка:{Color.RESET} нельзя удалять корневой каталог")
                continue
            if path not in os.getcwd():              #если путь не является началом текущей рабочей директории, пытаемся удалить
                print(f"Вы уверены, что хотите удалить папку {path}? [y/n]")     #запрос подтверждения удаления
                ans = user_input()
                if ans == 'y':
                    shutil.rmtree(path)
                else:
                    logger.info("[RESULT] <rm> Cancel delete")
            else:
                print(f"{Color.ERROR}Ошибка:{Color.RESET} нельзя отворачиваться от семьи(нельзя удалять родительский каталог)")
                logger.error("[RESULT] <rm> Attempt to delete the parent directory")