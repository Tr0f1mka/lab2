import unittest
from unittest.mock import patch
import math
import io
from src.tools import create_log
import src.my_exceptions as my_exceptions

"""
------------------------------------------------
---Функции, необходимые для тестов декоратора---
------------------------------------------------
"""


# функция для теста декоратора, которая что-то возвращает(в самой программе это функция cd)
# содерхит те же аргументы, что и декорируемые функции
@create_log
def test_func_with_return(cur_path: str, paths: list[str], flags: str) -> int:
    res = int(math.pow(2, 8))
    return res

# функция для теста декоратора, которая ничего не возвращает(в самой программе это любая функция кроме cd)
# содерхит те же аргументы, что и декорируемые функции
@create_log
def test_func_without_return(cur_path: str, paths: list[str], flags: str) -> None:
    ...


class TestCreateLog(unittest.TestCase):

    func = "test_func_with_return"

    """
    Тесты, когда всё хорошо
    """

    @patch("src.tools.logger")
    def test_create_log_with_succes_with_return(self, mock_logger):

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")

        self.assertEqual(result, 256)

    @patch("src.tools.logger")
    def test_create_log_with_succes_without_return(self, mock_logger):

        result = test_func_without_return(cur_path="/folder1", paths=[], flags="")

        self.assertEqual(result, None)


    """
    Дальше идут тесты ошибок на базе функции, имеющей вывод
    (для функций без вывода механика аналогична)
    """

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_file_not_found_error(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = FileNotFoundError

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(" файл не найден\n")

        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_file_exists_error(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = FileExistsError

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(" файл уже существует в этой директории\n")

        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("pygame.mixer")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_file_permission_error(self, mock_cout, mock_mixer, mock_pow, mock_logger):

        mock_pow.side_effect = PermissionError

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(" у тебя здесь нет власти(недостаточно прав)\n")

        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_undefined_flag_error(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = my_exceptions.UndefinedFlagError("f")

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(" неизвестный флаг \"f\"\n")

        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_too_few_paths_error_mode_1(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = my_exceptions.TooFewPathsError("1")

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(f" недостаточно путей для функции {self.func}\n")
        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_too_few_paths_error_mode_0(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = my_exceptions.TooFewPathsError("0")

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(f" у функции {self.func} нет цели, но есть путь(по крайней мере должен быть)\n")
        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_too_many_paths_error(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = my_exceptions.TooManyPathsError

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(f" слишком много путей для функции {self.func}\n")
        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_not_a_directory_error(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = NotADirectoryError

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(f" применение {self.func} не к директории невозможно или требует флагов\n")
        self.assertEqual(result, "/folder1")
        self.assertTrue(check)

    @patch("src.tools.logger")
    @patch("math.pow")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_log_with_less_rm_flag_error(self, mock_cout, mock_pow, mock_logger):

        mock_pow.side_effect = my_exceptions.LessRFlagError

        result = test_func_with_return(cur_path="/folder1", paths=[], flags="")
        check = (mock_cout.getvalue()).endswith(" для манипуляций с непустой директории нужен флаг \"-r\"\n")
        self.assertEqual(result, "/folder1")
        self.assertTrue(check)


unittest.main()
