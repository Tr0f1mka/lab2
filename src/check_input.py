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

    cin: list[list[str]] = [[], []]                              #Выходной список из 2 списков: 1)с командой и путями; 2) с флагами
    for i in patterns.TOKEN_RE.finditer(cin_str):
        if i.group("KAWYCHKI") or i.group("SKAWYCHKI"):          #Если путь с кавычками - обрезаем их и кладём к путям
            cin[0].append(i.group(0)[1:-1])
        elif i.group("SPACE"):                                   #Пробел - скип
            continue
        elif i.group("FLAG"):                                    #Флаг - к остальным директориям
            cin[1].append(i.group(0))
        else:                                                    #Остаток - к путям
            cin[0].append(i.group(0))

    cin[1] = list(set(cin[1]))                                   #Убираем из флагов повторы

    for j in range(len(cin[1])):
        flag = sorted(list(set(list(cin[1][j]))), key=None, reverse=False)
        str_flag = '-'
        for o in flag:
            str_flag += o if o != '-' else ''
        cin[1][j] = str_flag

    cin[1] = list(set(cin[1]))                 #Убираем новые повторы

    return cin

def normalisation_path(cur_path: str, bad_path: str) -> str:
    """
    Нормализует путь, убирая .. и ~
    :param cur_path: Строка - рабочая директория
    :param bad_path: Строка - путь
    :return: Строка - абсолютный путь
    """

    os.chdir(cur_path)
    bad_path = bad_path.replace('\\', '/').strip()      #меняем разделители на нормальные
    if (bad_path == '~'):                               #попытка пробиться к дому
        home_path = os.path.normpath(os.path.expanduser(bad_path))
        bad_path = home_path
    elif (len(bad_path) >= 2) and (bad_path[:2] == '~/'):
        home_path = os.path.normpath(os.path.expanduser(bad_path[bad_path.rfind('~/'):]))
        bad_path = home_path
    elif (len(bad_path) >= 2) and (bad_path[-2:] == '/~'):
        home_path = os.path.normpath(os.path.expanduser(bad_path[bad_path.rfind('/~'):]))
        bad_path = home_path
    elif ('/~/' in bad_path):
        home_path = os.path.normpath(os.path.expanduser(bad_path[bad_path.rfind('/~/'):]))
        bad_path = home_path
    else:                                               #в случае неудачи просто нормализуем путь
        new_path = os.path.normpath(bad_path)
        bad_path = new_path

    bad_path= bad_path.strip()             #удаляем пробелы по краям
    bad_path += "/" if bad_path[-1] == ':' else ''     #если пользователь на винде, но ввёл название корня без разделителя, добавляем /

    return os.path.abspath(bad_path)
