"""
------------------------
--Шаблоны для парсинга--
------------------------
"""



"""-----Библиотеки------"""
import re  # noqa: E402



"""-------Шаблоны-------"""

COMMANDS = r"(?P<COMMANDS>((ls)|(cd)|(cat)|(cp)|(mv)|(rm)|(zip)|(unzip)|(tar)|(untar))(?=\s+))"   #шаблон команд
FLAGS_PATT = r"(?P<FLAG>-[a-zA-Zа-яА-Я]+)"                                                        #шаблон флагов
PATH_PATT_WITH_DOUBLE_KAWYCHKI = r"(?P<KAWYCHKI>\"[^\"]*\")"                                      #шаблон пути в "
PATH_PATT_WITH_SINGLE_KAWYCHKI = r"(?P<SKAWYCHKI>'[^\']*\')"                                      #шаблон пути в '
ETC_PATT = r"(?P<ETC>\S+)"                                                                        #шаблон путей без кавычек
SPACE_PATT = r"(?P<SPACE>\s+)"                                                                    #шаблон пробелов

#общий шаблон
PATTERN = rf"""(
  {COMMANDS}                           |
  {PATH_PATT_WITH_DOUBLE_KAWYCHKI}     |
  {PATH_PATT_WITH_SINGLE_KAWYCHKI}     |
  {FLAGS_PATT}                         |
  {ETC_PATT}                           |
  {SPACE_PATT}
)
"""

TOKEN_RE = re.compile(PATTERN, re.VERBOSE)
