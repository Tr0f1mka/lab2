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
    
    check_flags(flags, '')
    paths = check_paths(paths, -2)

    source = paths[0]
    target = paths[1]
    
    shutil.make_archive(target, mode, source)


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

    check_flags(flags, "")

    paths = check_paths(paths, 1)

    shutil.unpack_archive(paths[0])



# def zip(cur_path: str, paths: list[str]) -> None:
    # """
    # Создаёт zip-архив
    # :param cur_path: Строка - рабочая директория
    # :param paths: Список строк - пути
    # :return: Данная функция ничего не возвращает
    # """

#     os.chdir(cur_path)

#     if len(paths) == 2:                     #проверка, что дано только 2 пути: источник и назначение
#         source = normalization_path(os.getcwd(), paths[0])
#         target = normalization_path(os.getcwd(), paths[1])
#     elif len(paths) == 1:
#         source = normalization_path(paths[0])
#         target = normalization_path(paths[0])
#     elif len(paths) > 2:
#         print("{Color.ERROR}Ошибка:{Color.RESET} слишком много аргументов для команды zip")
#         # loger.error("Result: Too many arguments")
#         return
#     else:
#         print("{Color.ERROR}Ошибка:{Color.RESET} у функции zip нет цели, но есть путь(должен быть)")
#         # loger.error("Result: Too little arguments")
#         return
#     print(source, target)
#     try:                                   #попытка архивнуть директорию
#         if os.path.exists(source):
#             # if os.path.isdir(source):
#             with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zipf:
#                 for root, dirs, files in os.walk(source):
#                     for file in files:
#                         file_path = os.path.join(root, file)
#                         arcname = os.path.relpath(file_path, start=source)
#                         zipf.write(file_path, arcname)
#                 # loger.info("Result: Succes")
#             # else:                           #ошибка, если не директория
#             #     with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zipf:
#             #         zipf.write(source)
#             #     # shutil.rmtree(path_dir_arch)
#             #     loger.info("Result: Succes")
#         else:                               #ошибка, если нет этого
#             print("{Color.ERROR}Ошибка:{Color.RESET} указанного пути не существует")
#             # loger.error("Result: File not found")
#     except PermissionError:                #ошибка, если нет прав
#         print("{Color.ERROR}Ошибка:{Color.RESET} у тебя здесь нет власти(недостаточно прав)")
#         # loger.error("Result: Not enough permissions")
#     except OSError:                        #прочие ошибки ОС
#         print("{Color.ERROR}Ошибка:{Color.RESET} указанного пути не существует")
#         # loger.error("Result: Error of OS")


# def unzip(cur_path: str, paths: list[str]) -> None:
#     """
#     Разархивирует zip-архив
#     :param cur_path: Строка - рабочая директория
#     :param paths: Список строк - пути
#     :return: Данная функция ничего не возвращает
#     """

#     os.chdir(cur_path)

#     if len(paths) == 1:                  #проверка, что дан только 1 путь: источник
#         source = normalization_path(paths[0])
#     elif len(paths) > 1:
#         print("{Color.ERROR}Ошибка:{Color.RESET} слишком много аргументов для команды unzip")
#         # loger.error("Result: Too many arguments")
#         return
#     else:
#         print("{Color.ERROR}Ошибка:{Color.RESET} у функции unzip нет цели, но есть путь(должен быть)")
#         # loger.error("Result: Too little arguments")
#         return
#     print(source, os.getcwd())
#     try:                                 #попытка разархивнуть директорию
#         shutil.unpack_archive(source)
#         # loger.info("Result: Succes")
#     except FileNotFoundError:            #ошибка, если нет архива
#         print("{Color.ERROR}Ошибка:{Color.RESET} указанного пути не существует")
#         # loger.error("Result: File not found")
#     except PermissionError:              #ошибка, если нет прав
#         print("{Color.ERROR}Ошибка:{Color.RESET} у тебя здесь нет власти(недостаточно прав)")
#         # loger.error("Result: Not enough permissions")
#     except OSError:                      #прочие ошибки ОС
#         print("{Color.ERROR}Ошибка:{Color.RESET} указанного пути не существует")
#         # loger.error("Result: Error of OS")


# def tar(cur_path: str, paths: list[str]) -> None:
#     """
#     Создаёт tar-архив
#     :param cur_path: Строка - рабочая директория
#     :param paths: Список строк - пути
#     :return: Данная функция ничего не возвращает
#     """

#     os.chdir(cur_path)

#     if len(paths) == 2:                     #проверка, что дано только 2 пути: источник и назначение
#         source = normalization_path(os.getcwd(), paths[0])
#         target = normalization_path(os.getcwd(), paths[1])
#     elif len(paths) == 1:
#         source = normalization_path(os.getcwd(), paths[0])
#         target = normalization_path(os.getcwd(), paths[0]) + ".tar.gz"
#     elif len(paths) > 2:
#         print("{Color.ERROR}Ошибка:{Color.RESET} слишком много аргументов для команды tar")
#         # loger.error("Result: Too many arguments")
#         return
#     else:
#         print("{Color.ERROR}Ошибка:{Color.RESET} у функции tar нет цели, но есть путь(должен быть)")
#         # loger.error("Result: Too little arguments")
#         return

#     try:                                    #попытка архивнуть директорию
#         if os.path.exists(source):
#             # if os.path.isdir(source):
#                 with tarfile.open(target, 'w:gz') as tarf:
#                     tarf.add(source, arcname=os.path.basename(source))
#                 # loger.info("Result: Succes")
#             # else:                               #ошибка, если не директория
#             #     print("{Color.ERROR}Ошибка:{Color.RESET} нельзя архивировать файлы")
#             #     loger.error("Result: Try create archive from file")
#         else:                               #ошибка, если нет этого
#             print("{Color.ERROR}Ошибка:{Color.RESET} указанного пути не существует")
#             # loger.error("Result: File not found")
#     except PermissionError:                 #ошибка, если нет прав
#         print("{Color.ERROR}Ошибка:{Color.RESET} у тебя здесь нет власти(недостаточно прав)")
#         # loger.error("Result: Not enough permissions")
#     except OSError:                         #прочие ошибки ОС
#         print("{Color.ERROR}Ошибка:{Color.RESET} указа1нного пути не существует")
#         # loger.error("Result: Error of OS")


# def untar(cur_path: str, paths: list[str]) -> None:
#     """
#     Разархивирует tar-архив
#     :param cur_path: Строка - рабочая директория
#     :param paths: Список строк - пути
#     :return: Данная функция ничего не возвращает
#     """

#     os.chdir(cur_path)

#     if len(paths) == 1:                  #проверка, что дан только 1 путь: источник
#         source = normalization_path(os.getcwd(), paths[0])
#     elif len(paths) > 1:
#         print("{Color.ERROR}Ошибка:{Color.RESET} слишком много аргументов для команды untar")
#         # loger.error("Result: Too many arguments")
#         return
#     else:
#         print("{Color.ERROR}Ошибка:{Color.RESET} у функции untar нет цели, но есть путь(должен быть)")
#         # loger.error("Result: Too little arguments")
#         return

#     try:                                 #попытка разархивнуть директорию
#         with tarfile.open(source, 'r:gz') as tarf:
#             tarf.extractall()
#         # loger.info("Result: Succes")
#     except FileNotFoundError:            #ошибка, если нет архива
#         print("{Color.ERROR}Ошибка:{Color.RESET} указанного пути не существует")
#         # loger.error("Result: File not found")
#     except PermissionError:              #ошибка, если нет прав
#         print("{Color.ERROR}Ошибка:{Color.RESET} у тебя здесь нет власти(недостаточно прав)")
#         # loger.error("Result: Not enough permissions")
#     except OSError:                      #прочие ошибки ОС
#         print("{Color.ERROR}Ошибка:{Color.RESET} указанного пути не существует")
#         # loger.error("Result: Error of OS")


# make_archive(os.getcwd(), [], 'zip')