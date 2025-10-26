"""
------------------------
--Шаблоны для парсинга--
------------------------
"""



"""-----Библиотеки------"""
import re  # noqa: E402



"""-------Шаблоны-------"""

COMMANDS = r"(?P<COMMANDS>((ls)|(cd)|(cat)|(cp)|(mv)|(rm))(?=\s+))"
FLAGS_PATT = r"(?P<FLAG>-[a-z]+)"
PATH_PATT_WITH_DOUBLE_KAWYCHKI = r"(?P<KAWYCHKI>\"[^\"]*\")"
PATH_PATT_WITH_SINGLE_KAWYCHKI = r"(?P<SKAWYCHKI>'[^\']*\')"
ETC_PATT = r"(?P<ETC>\S+)"
SPACE_PATT = r"(?P<SPACE>\s+)"


PATTERN = rf"""(
  {COMMANDS}                           |
  {PATH_PATT_WITH_DOUBLE_KAWYCHKI}     |
  {PATH_PATT_WITH_SINGLE_KAWYCHKI}     |
  {FLAGS_PATT}                              |
  {ETC_PATT}                           |
  {SPACE_PATT}
)
"""

TOKEN_RE = re.compile(PATTERN, re.VERBOSE)

# print(re.fullmatch(FLAGS_PATT, '-l'))
