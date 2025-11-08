"""------Библиотеки-------"""

from src.patterns import TOKEN_RE, Color  
import os                        
from logging import config, getLogger
from functools import wraps
from src.config import LOGGING_CONFIG
from src.my_exception import CountArgumentsError, UndefinedFlagError, TooFewPathsError, TooManyPathsError, LessRMFlagError

"""
--------------------------
--Функция проверки ввода--
--------------------------
"""



"""--------Логгер---------"""

config.dictConfig(LOGGING_CONFIG)
logger = getLogger(__name__)



"""--------Функции--------"""

def user_input() -> str:
    result = input(f"{Color.FILE}{os.getlogin()}{Color.CUR_DIR}{os.getcwd()}{Color.RESET}$ {Color.INPUT}").strip()
    print(Color.RESET)
    logger.info(f"[INPUT] {result}")
    return result


def parser(cin_str: str) -> list[list[str], str]:
    """
    Проверяет пользовательский ввод и выводит ошибку
    :param cin: Строка - пользовательский ввод
    :return: Список из 2 элемнтов - список путей и строка флага
    """

    cin: list[list[str], str] = [[], []]                         #Выходной список из 2 списков: 1)с командой и путями; 2) с флагами
    for i in TOKEN_RE.finditer(cin_str):
        if i.group("KAWYCHKI") or i.group("SKAWYCHKI"):          #Если путь с кавычками - обрезаем их и кладём к путям
            cin[0].append(i.group(0)[1:-1])
        elif i.group("SPACE"):                                   #Пробел - скип
            continue
        elif i.group("FLAG"):                                    #Флаг - к остальным флагам
            cin[1].append(i.group(0))
        else:                                                    #Остаток - к путям
            cin[0].append(i.group(0))

    full_flag = ""                                               #Сборка всех флагов в один с уникальными буквами
    for flag in cin[1]:
        for sym in flag[1:]:
            full_flag += sym if sym not in full_flag else ""

    cin[1] = full_flag

    return cin


def normalization_path(bad_path: str) -> str:
    """
    Нормализует путь, убирая .. и ~
    :param bad_path: Строка - путь
    :return: Строка - абсолютный путь
    """

    bad_path = bad_path.replace('\\', '/').strip()      #меняем разделители на нормальные
    while ('//' in bad_path): 
        bad_path = bad_path.replace('//', '/')
    
    bad_path = os.path.normpath(os.path.expanduser(bad_path))
    bad_path = bad_path.strip()                          #удаляем пробелы по краям
 
    bad_path += "\\" if ((bad_path[-1] == ':') and (os.sep == "\\")) else ''     #если пользователь на винде, но ввёл название корня без разделителя, добавляем /
    
    return bad_path

def create_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(args, kwargs)
        logger.info(f"[CALL] {func.__name__}{args, kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"[RESULT] <{func.__name__}> Succes")
            return result
        except FileNotFoundError:
            logger.error(f"[RESULT] <{func.__name__}> File not found")
        except PermissionError:
            logger.error(f"[RESULT] <{func.__name__}> Not enough permissions")
        except CountArgumentsError:
            logger.error(f"[RESULT] <{func.__name__}> Not enough argumments")
        except UndefinedFlagError as e:
            logger.error(f"[RESULT] <{func.__name__}> Undefined flag \"{e}\"")
        except TooFewPathsError as e:
            logger.error(f"[RESULT] <{func.__name__}> Too few paths")
            if e == '1':
                print("Мало путей")
            else:
                print("0 путей")
        except TooManyPathsError:
            logger.error(f"[RESULT] <{func.__name__}> Too many paths")
        except NotADirectoryError:
            logger.error(f"[RESULT] <{func.__name__}> Not a directory")
        except LessRMFlagError:
            logger.error(f"[RESULT] <{func.__name__}> -r flag is missing")
        return kwargs["cur_path"]
    return wrapper

def check_flags(input_flag: str, control_flag: str) -> None:
    """
    Проверяет флаги, вызывая исключение при некорректном флаге
    :param input_flag: Строка - введённый флаг
    :param control_flag: Строка - контрольный флаг
    :return: Данная функция ничего не возвращает
    """

    for i in input_flag:
        if i not in control_flag:
            raise UndefinedFlagError(i)
        
def check_paths(input_paths: list[str], cnt: int) -> list[str]:
    """
    Проверяет количество путей и нормализует их
    :param input_paths: Список строк - введённые пути
    :param cnt: Целое число - количество путей, которое может обработать команда(особые значения: 0 - от 0 до бесконечности, -1 - от 1 до бесконечности, -2 - 1-2)
    :return: Данная функция возвращает список нормализованных путей
    """

    len_paths = len(input_paths)

    if cnt == -2:              # 1-2 путей
        if len_paths == 2:
            input_paths[0] = normalization_path(input_paths[0])
            input_paths[1] = normalization_path(input_paths[1])
        elif len_paths == 1:
            input_paths[0] = normalization_path(input_paths[0])
            input_paths.append(input_paths[0])
        elif len_paths == 0:
            raise TooFewPathsError(0)
        else:
            raise TooManyPathsError
    elif cnt == -1:            # от 1 до бесконечности путей
        if input_paths:
            for i in range(len_paths):
                input_paths[i] = normalization_path(input_paths[i])
        else:
            raise TooFewPathsError(0)
    elif cnt == 0:           # от 0 до бесконечности путей
        for i in range(len_paths):
            input_paths[i] = normalization_path(input_paths[i])
    else:
        if len_paths == cnt:
            for i in range(len_paths):
                input_paths[i] = normalization_path(input_paths[i])
        elif len_paths > cnt:
            raise TooManyPathsError
        else:
            raise TooFewPathsError(0) if len_paths == 0 else TooFewPathsError(1)
    return input_paths