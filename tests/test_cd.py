import unittest
from unittest.mock import patch
from src.read_funcs import cd


class TestCd(unittest.TestCase):

    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    def test_cd_with_succes(self, mock_error, mock_info, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home/test"
        result = cd(cur_path="home", paths=["test"], flags="")

        self.assertEqual(result, "home/test")


    @patch("os.chdir")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cd_with_error(self, mock_cout, mock_error, mock_info, mock_chdir):
        result = cd(cur_path="home", paths=[], flags="")

        self.assertEqual(result, "home")


    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log
    # В случае ошибки cd возвращает путь текущей рабочей директории, что было проверено во втором тесте

unittest.main()
