"""-----Библиотеки------"""

import os
import shutil
from src.tools import Color, check_flags, check_paths, create_log, user_input, logger
from src.my_exceptions import LessRFlagError
from pygame import mixer       #type: ignore



"""
------------------------
---Функции cp, mv, rm---
------------------------
"""



"""--Загрузка музыки---"""

mixer.init()
music1 = mixer.Sound(os.path.abspath("src/music/rm_parent_dir_error.ogg"))



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

    check_flags(flags, "r")                                      # Проверки флагов и путей
    paths = check_paths(paths, 2)
    source = paths[0]
    target = paths[1]
    if source.split(os.sep)[-1] != target.split(os.sep)[-1]:     # Доработка целевого пути(если в конце не указано название источника)
        target = os.path.join(target, source.split(os.sep)[-1])


    if flags == "":                                              # Копирование:
        if os.path.isdir(source):
            if not(os.listdir(source)):                          # пустой папки
                shutil.copytree(source, target)
            else:
                raise LessRFlagError
        else:                                                    # файла
            shutil.copy2(source, target)
    else:                                                        # непустой директории
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

    check_flags(flags, "")                                       # Проверки флагов и путей
    paths = check_paths(paths, 2)
    source = paths[0]
    target = paths[1]

    shutil.move(source, target)                                  # Перемещение источника в назначение


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

    check_flags(flags, "r")                                      # Проверки флагов и путей
    paths = check_paths(paths, -1)

    if flags == "":                                              # Удаление:
        for path in paths:

            print(f"Вы уверены, что хотите удалить файл {path}? [y/n]")
            ans = user_input()

            if ans == "y":
                if os.path.isdir(path):
                    if not(os.listdir(path)):                    # пустой директории
                        shutil.rmtree(path)
                    else:
                        raise LessRFlagError
                else:                                            # файла
                    os.remove(path)
            else:
                logger.info("[RESULT] <rm> Cancel delete")

    else:
        for path in paths:
            if (path[-2:] == ':\\') or (path == '/'):         #защита от удаления корня
                print(f"{Color.ERROR}Ошибка:{Color.RESET} нельзя удалять корневой каталог")
                logger.error("[RESULT] <rm> cancel remove root directory")
                continue

            if not (os.getcwd()).startswith(os.path.abspath(path)):              # Если путь не является началом текущей рабочей директории, пытаемся удалить

                print(f"Вы уверены, что хотите удалить папку {path}? [y/n]")
                ans = user_input()

                if ans == 'y':
                    shutil.rmtree(path)                          # непустой директории
                else:
                    logger.info("[RESULT] <rm> Cancel delete")
            else:                                                # Удаление родительской директории - ошибка
                mixer.stop()
                music1.play()
                print(f"{Color.ERROR}Ошибка:{Color.RESET} нельзя отворачиваться от семьи(нельзя удалять родительский каталог)")
                logger.error("[RESULT] <rm> Attempt to delete the parent directory")
