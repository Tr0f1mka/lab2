"""
--------------------------
--Функция проверки ввода--
--------------------------
"""

"""------Библиотеки-------"""

import src.patterns as patterns  # noqa: E402



"""--------Функции--------"""

def input_check(cin_str: str) -> list[str]:
    """
    Проверяет пользовательский ввод и выводит ошибку
    :param cin: Строка - пользовательский ввод
    :return: Список токенов пользовательской строки
    """

    cin = [m.group(1) for m in patterns.TOKEN_RE.finditer(cin_str)]
    return cin
