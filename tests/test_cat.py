import unittest
from unittest.mock import patch
from src.read_funcs import cat


class TestCat(unittest.TestCase):

    @patch("os.chdir")
    @patch("builtins.open")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cat_with_1_path(self, mock_cout, mock_error, mock_info, mock_open, mock_chdir):
        cat(cur_path="home", paths=["file1"], flags="")
        mock_open.assert_called_once_with("file1", "r", encoding="utf-8")
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("builtins.open")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cat_with_more_path(self, mock_cout, mock_error, mock_info, mock_open, mock_chdir):
        cat(cur_path="home", paths=["file1", "file2"], flags="")
        self.assertEqual(mock_open.call_count, 2)
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("builtins.open")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cat_without_path(self, mock_cout, mock_error, mock_info, mock_open, mock_chdir):
        cat(cur_path="home", paths=[], flags="")
        self.assertEqual(mock_open.call_count, 0)
        self.assertEqual(mock_info.call_count, 1)
        self.assertEqual(mock_error.call_count, 1)



    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log

unittest.main()
