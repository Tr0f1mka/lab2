"""-------Библиотека-------"""

import os
import shutil
from src.tools import create_log, check_flags, check_paths



"""
---------------------------
----Функции для архивов----
---------------------------
"""



"""--------Функции--------"""

@create_log
def make_archive(cur_path: str, paths: list[str], mode: str, flags: str) -> None:
    """
    Создаёт архив
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param mode: Строка - тип архива(zip или tar)
    :param flag: Строка - флаг
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, '')                       # Проверка флагов и путей
    paths = check_paths(paths, -2)
    source = paths[0]
    target = paths[1]

    shutil.make_archive(target, mode, source)     # Архивация источника


@create_log
def unpack_archive(cur_path: str, paths: list[str], flags: str) -> None:
    """
    Распаковывает архив в текущую директорию
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Строка - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    check_flags(flags, "")                  # Проверка флагов и путей
    paths = check_paths(paths, 1)

    shutil.unpack_archive(paths[0])         # Разархивация
