"""
------------------------
---Функции cp, mv, rm---
------------------------
"""



"""-----Библиотеки------"""

import os        # noqa: E402
# import shutil    # noqa: E402



"""-------Функции-------"""

def cp(cur_path: str, cin: list[str]) -> None:
    """
    Копирует файл из одной директории в другую
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - токены команды
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)
    # if len(cin) == 2:
    #     source = cin[0]
    #     target = cin[1]
