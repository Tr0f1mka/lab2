"""
------------------------
--Шаблоны для парсинга--
------------------------
"""



"""-----Библиотеки------"""
import re  # noqa: E402



"""-------Шаблоны-------"""

COMMANDS = r"((ls)|(cd)|(cat)|(cp)|(mv)|(rm)|)(?=\s+)"
FLAGS = r"-[a-z]*(?=\s+)"
PATH_PATT_WITH_DOUBLE_KAWYCHKI = r"\"[^\"]*\""
PATH_PATT_WITH_SINGLE_KAWYCHKI = r"'[^\']*'"


PATTERN = rf"""\s*(
  {COMMANDS}                           |
  {PATH_PATT_WITH_DOUBLE_KAWYCHKI}     |
  {PATH_PATT_WITH_SINGLE_KAWYCHKI}     |
  {FLAGS}                              |
  \S+
)
"""

TOKEN_RE = re.compile(PATTERN, re.VERBOSE)
