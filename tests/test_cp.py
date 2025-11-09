import unittest
from unittest.mock import patch
from src.format_funcs import cp


class TestCp(unittest.TestCase):

    @patch("os.chdir")
    @patch("os.path.isdir")
    @patch("os.listdir")
    @patch("shutil.copytree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cp_with_succes_without_flag_with_empty_dir(self, mock_cout, mock_error, mock_info, mock_copytree, mock_listdir, mock_isdir, mock_chdir):
        mock_isdir.return_value = True
        mock_listdir.return_value = []
        cp(cur_path="home", paths=["source", "target"], flags="")
        mock_copytree.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("os.path.isdir")
    @patch("os.listdir")
    @patch("shutil.copytree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cp_with_succes_without_flag_with_full_dir(self, mock_cout, mock_error, mock_info, mock_copytree, mock_listdir, mock_isdir, mock_chdir):
        mock_isdir.return_value = True
        mock_listdir.return_value = ["file1"]
        cp(cur_path="home", paths=["source", "target"], flags="")
        self.assertEqual(mock_info.call_count, 1)
        mock_error.assert_called_once_with("[RESULT] <cp> -r flag is missing")


    @patch("os.chdir")
    @patch("os.path.isdir")
    @patch("shutil.copy2")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cp_with_succes_without_flag_with_file(self, mock_cout, mock_error, mock_info, mock_copy, mock_isdir, mock_chdir):
        mock_isdir.return_value = False
        cp(cur_path="home", paths=["source", "target"], flags="")
        mock_copy.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("shutil.copytree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_cp_with_succes_with_flag(self, mock_cout, mock_error, mock_info, mock_copytree, mock_chdir):
        cp(cur_path="home", paths=["source", "target"], flags="r")
        mock_copytree.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log

unittest.main()
