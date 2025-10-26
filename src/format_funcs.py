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

logging.config.dictConfig(LOGGING_CONFIG)
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

    if flags:
        for i in flags:
            if i == '-r':
                flag = i
            else:
                print(f'\033[01;38;05;196mОшибка:\033[0m флаг "{i}" вам в руки, а для этой функции существует только флаг "-r".')
                loger.error(f"Unknown flag: {i}")
                return
    else:
        flag = ''

    if len(paths) == 2:
        source = paths[0]
        target = paths[1]
    elif len(paths) > 2:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды cp")
        loger.error("Too many arguments")
        return
    else:
        print("\033[01;38;05;196mОшибка:\033[0m недостаточно аргументов для команды cp")
        loger.error("Too little arguments")
        return

    if flag == "":
        try:
            # print(normalisation_path(os.getcwd(), source), normalisation_path(os.getcwd(), target))
            shutil.copy2(normalisation_path(os.getcwd(), source), normalisation_path(os.getcwd(), target))
            loger.info("Result: Succes")
        except FileNotFoundError:
            print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
            loger.error("File not found")
        except PermissionError:
            print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
            loger.error("Not enough permissions")
        except OSError:
            print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
            loger.error("Error of OS")
    else:
        try:
            # print(normalisation_path(os.getcwd(), source), normalisation_path(os.getcwd(), target))
            if source.split(os.sep)[-1] != target.split(os.sep)[-1]:
                target = os.path.join(target, source.split(os.sep)[-1])
            shutil.copytree(normalisation_path(os.getcwd(), source), normalisation_path(os.getcwd(), target))
            loger.info("Result: Succes")
        except FileNotFoundError:
            print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
            loger.error("File not found")
        except PermissionError:
            print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
            loger.error("Not enough permissions")
        except OSError:
            print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
            loger.error("Error of OS")


def mv(cur_path: str, cin: list[str]) -> None:
    """
    Перемещает файл в назначение
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - токены команды
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if len(cin) < 2:
        print("\033[01;38;05;196mОшибка:\033[0m недостаточно аргументов для команды mv")
        loger.error("Too little arguments")
        return
    elif len(cin) == 2:
        source = normalisation_path(os.getcwd(), cin[0])
        target = normalisation_path(os.getcwd(), cin[1])
    else:
        print("\033[01;38;05;196mОшибка:\033[0m слишком много аргументов для команды mv")
        loger.error("Too many arguments")
        return

    try:
        shutil.move(source, target)
        loger.info("Result: Succes")
    except FileNotFoundError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("File not found")
    except PermissionError:
        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
        loger.error("Not enough permissions")
    except OSError:
        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
        loger.error("Error of OS")


def rm(cur_path: str, paths: list[str], flags: list[str]) -> None:
    """
    Удаляет указанный объект
    :param cur_path: Строка - рабочая директория
    :param cin: Список строк - токены команды
    :return: Данная функция ничего не возвращает
    """

    os.chdir(cur_path)

    if flags:
        for i in flags:
            if i == '-r':
                flag = '-r'
            else:
                print(f'\033[01;38;05;196mОшибка:\033[0m флаг "{i}" вам в руки, а для этой функции существует только флаг "-r".')
                loger.error(f"Unknown flag: {i}")
    else:
        flag = ''

    if paths:
        for j in range(len(paths)):
            paths[j] = normalisation_path(os.getcwd(), paths[j])
    else:
        print("\033[01;38;05;196mОшибка:\033[0m у функции rm нет цели, но есть путь(должен быть)")
        loger.error("Too little arguments")
        return

    if flag == "":
        for path in paths:
            if (path[-2] == ':\\') or (path == '/'):
                print("\033[01;38;05;196mОшибка:\033[0m нельзя удалять корневой каталог")
                loger.error("Attempt to delete the root directory")
                continue
            if os.getcwd() in path:
                print(f"Вы уверены, что хотите удалить файл {path}? [y/n]")
                ans = input("\033[01;38;05;222m").strip()
                print("\033[0m")
                loger.info(ans)
                if ans == 'y':
                    try:
                        os.remove(path)
                        loger.info("Result: Succes")
                    except FileNotFoundError:
                        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                        loger.error("File not found")
                    except PermissionError:
                        print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
                        loger.error("Not enough permissions")
                    except OSError:
                        print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                        loger.error("Error of OS")
                else:
                    continue
            else:
                print("\033[01;38;05;196mОшибка:\033[0m нельзя удалять родительский каталог")
                loger.error("Attempt to delete the parent directory")

    else:
        for path in paths:
            print(f"Вы уверены, что хотите удалить папку {path}? [y/n]")
            ans = input("\033[01;38;05;222m").strip()
            print("\033[0m", end='')
            loger.info(ans)
            if ans == 'y':
                try:
                    shutil.rmtree(path)
                    loger.info("Result: Succes")
                except FileNotFoundError:
                    print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                    loger.error("File not found")
                except PermissionError:
                    print("\033[01;38;05;196mОшибка:\033[0m у тебя здесь нет власти(недостаточно прав)")
                    loger.error("Not enough permissions")
                except OSError:
                    print("\033[01;38;05;196mОшибка:\033[0m указанного пути не существует")
                    loger.error("Error of OS")
            else:
                continue
