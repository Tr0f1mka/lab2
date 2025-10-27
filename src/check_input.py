"""
--------------------------
--Функция проверки ввода--
--------------------------
"""

"""------Библиотеки-------"""

import src.patterns as patterns  # noqa: E402
import os                        # noqa: E402



"""--------Функции--------"""

def input_check(cin_str: str) -> list[list[str]]:
    """
    Проверяет пользовательский ввод и выводит ошибку
    :param cin: Строка - пользовательский ввод
    :return: Список из 2 списков строк - списка флагов и списка прочего
    """

    # cin = list(patterns.TOKEN_RE.finditer(cin_str))
    # print(cin[-1].groupdict())
    # print()
    cin: list[list[str]] = [[], []]
    for i in patterns.TOKEN_RE.finditer(cin_str):
        if i.group("KAWYCHKI") or i.group("SKAWYCHKI"):
            cin[0].append(i.group(0)[1:-1])
            # cin.append(i)
        elif i.group("SPACE"):
            continue
        elif i.group("FLAG"):
            cin[1].append(i.group(0))
            # print(type(i.group(0)))
            # cin.append(i)
        else:
            cin[0].append(i.group(0))
            # cin.append(i)
    cin[1] = list(set(cin[1]))

    for j in range(len(cin[1])):
        flag = list(set(list(cin[1][j])))
        str_flag = '-'
        for o in flag:
            str_flag += o if o != '-' else ''
        cin[1][j] = str_flag

    cin[1] = list(set(cin[1]))

    return cin

def normalisation_path(cur_path: str, bad_path: str) -> str:
    """
    Нормализует путь, убирая .. и ~
    :param cur_path: Строка - рабочая директория
    :param bad_path: Строка - путь
    :return: Строка - нормальный путь
    """

    os.chdir(cur_path)
    bad_path = bad_path.replace('\\', '/').strip()
    if '~' in bad_path:
        home_path = os.path.normpath(os.path.expanduser(bad_path[bad_path.rfind('~'):]))
        bad_path = home_path
    else:
        new_path = os.path.normpath(bad_path)
        bad_path = new_path

    bad_path= bad_path.strip()
    bad_path += "/" if bad_path[-1] == ':' else ''

    # print(os.path.abspath(bad_path))
    return os.path.abspath(bad_path)


# print(input_check("cd -lllll 'azaza"))
