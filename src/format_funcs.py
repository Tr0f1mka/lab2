"""
------------------------
---Функции cp, mv, rm---
------------------------
"""



"""-----Библиотеки------"""

import os                                        # noqa: E402
import shutil                                    # noqa: E402
import logging                                   # noqa: E402
from src.config import LOGGING_CONFIG            # noqa: E402
from src.check_input import normalisation_path   # noqa: E402



"""-------Логер---------"""

logging.config.dictConfig(LOGGING_CONFIG)       #настройка логера
loger = logging.getLogger(__name__)



"""-------Функции-------"""

def cp(cur_path: str, paths: list[str], flags: list[str]) -> None:
    """
    Копирует файл из одной директории в другую
    :param cur_path: Строка - рабочая директория
    :param paths: Список строк - пути
    :param flags: Список строк - флаги
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if flags:          #проверка флагов
        for i in flags:
            if i == '-r':
                flag = i
            else:
                print(f'\033[01;38;05;196mОшибка:\033[0m флаг "{i}" вам в руки, а для этой функции существует только флаг "-r".')
                loger.error(f"Result: Unknown flag: {i}")
                return
    else:
        flag = ''

    if len(paths) == 2:    #проверка путей
        source = paths[0]
        target = paths[1]
    elif len(paths) > 2:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды cp")
        loger.error("Result: Too many arguments")
        return
    else:
        print("\033[01;38;05;196mОшибка:\033[0m недостаточно аргументов для команды cp")
        loger.error("Result: Too little arguments")
        return

    if flag == "":
        try:       #попытка копирования файла
            shutil.copy2(normalisation_path(os.getcwd(), source), normalisation_path(os.getcwd(), target))
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
    else:
        try:     #попытка копирования директории
            if source.split(os.sep)[-1] != target.split(os.sep)[-1]:
                target = os.path.join(target, source.split(os.sep)[-1])
            shutil.copytree(normalisation_path(os.getcwd(), source), normalisation_path(os.getcwd(), target))
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


def mv(cur_path: str, cin: list[str]) -> None:
    """
    Перемещает файл в назначение
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - токены команды
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if len(cin) < 2:                   #проверка путей
        print("\033[01;38;05;196mОшибка:\033[0m недостаточно аргументов для команды mv")
        loger.error("Result: Too little arguments")
        return
    elif len(cin) == 2:
        source = normalisation_path(os.getcwd(), cin[0])
        target = normalisation_path(os.getcwd(), cin[1])
    else:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды mv")
        loger.error("Result: Too many arguments")
        return

    try:                 #попытка двинуть файл/директорию(или по нему/ней, но для этого есть rm)
        shutil.move(source, target)
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


def rm(cur_path: str, paths: list[str], flags: list[str]) -> None:
    """
    Удаляет указанный объект
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - токены команды
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if flags:              #проверка флагов
        for i in flags:
            if i == '-r':
                flag = '-r'
            else:
                print(f'\033[01;38;05;196mОшибка:\033[0m флаг "{i}" вам в руки, а для этой функции существует только флаг "-r".')
                loger.error(f"Result: Unknown flag: {i}")
                return
    else:
        flag = ''

    if paths:              #проверка путей
        for j in range(len(paths)):
            paths[j] = normalisation_path(os.getcwd(), paths[j])
    else:
        print("\033[01;38;05;196mОшибка:\033[0m у функции rm нет цели, но есть путь(должен быть)")
        loger.error("Result: Too little arguments")
        return

    if flag == "":         #попытка удаления файла(-ов)
        for path in paths:
            if os.path.exists(path):
                print(f"Вы уверены, что хотите удалить файл {path}? [y/n]")     #запрос подтверждения
                ans = input("\033[01;38;05;222m").strip()
                print("\033[0m")
                loger.info(ans)
                if ans == 'y':
                    try:               #сам процесс удаления
                        os.remove(path)
                        loger.info("Result: Succes")
                    except PermissionError:
                        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
                        loger.error("Result: Not enough permissions")
                    except OSError:
                        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                        loger.error("Result: Error of OS")
                else:
                    loger.info('Result: Cancel delete object')
            else:
                print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                loger.error("Result: File not found")

    else:              #попытка удалить директорию(-и)
        for path in paths:
            if (path[-2:] == ':\\') or (path == '/'):         #защита от удаления корня
                print("\033[01;38;05;196mОшибка:\033[0m нельзя удалять корневой каталог")
                loger.error("Result: Attempt to delete the root directory")
                continue
            if path not in os.getcwd():              #если путь не является началом текущей рабочей директории, пытаемся удалить
                if (os.path.exists(path)):
                    print(f"Вы уверены, что хотите удалить папку {path}? [y/n]")     #запрос подтверждения удаления
                    ans = input("\033[01;38;05;222m").strip()
                    print("\033[0m", end='')
                    loger.info(ans)
                    if ans == 'y':
                        try:        #сам процесс удаления
                            shutil.rmtree(path)
                            loger.info("Result: Succes")
                        except PermissionError:
                            print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
                            loger.error("Result: Not enough permissions")
                        except OSError:
                            print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                            loger.error("Result: Error of OS")
                    else:
                        loger.info('Result: Cancel delete object')
                else:
                    print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                    loger.error("Result: File not found")
            else:        #попытка удаления родителя карается ошибкой, ибо нельзя отворачиваться от семьи
                print("\033[01;38;05;196mОшибка:\033[0m нельзя отворачиваться от семьи(нельзя удалять родительский каталог)")
                loger.error("Result: Attempt to delete the parent directory")
