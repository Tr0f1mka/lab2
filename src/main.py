"""
------------------------
------главный файл------
------------------------
"""



"""-------библиотека-------"""

import os                                # noqa: E402
import src.check_input as check_input    # noqa: E402
import src.read_funcs as read_funcs      # noqa: E402



"""--------функции---------"""

def start() -> None:
    """
    Функция для вывода приветственного сообщения
    :return: Данная функция ничего не возвращает
    """

    print()
    print("TR0F1MKASOFT [Version 0.0.0.1]")
    print("Корпорация TR0F1MKASOFT (TR0F1MKASOFT Corporation). Все права защищены")
    print()

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    start()

    working = True
    while (working):
        cin_str = input("Ввод: ")
        cin = check_input.input_check(cin_str)

        if cin[0] != "-1":
            if cin[0] == "exit":
                working = False
            elif cin[0] == "ls":
                print()
                if len(cin) == 1:
                    read_funcs.ls("", os.getcwd())
                elif len(cin) == 2:
                    if cin[1][0] != '-':
                        read_funcs.ls("", cin[1])
                    else:
                        read_funcs.ls(cin[1], os.getcwd())
                elif len(cin) == 3:
                    read_funcs.ls(cin[1], cin[2])
                else:
                    print('Слишком много аргументов для функции "ls"')
            elif cin[0] == "cd":
                if len(cin) != 2:
                    print('Для функции "cd" нужен 1 аргумент(путь к целевой директории)')
                else:
                    try:
                        os.chdir(read_funcs.cd(cin[1]))
                    except(TypeError):
                        continue


        print()

    print("Завершение работы")



if __name__ == "__main__":
    main()
