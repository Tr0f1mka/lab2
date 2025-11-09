import unittest
from unittest.mock import patch
from src.read_funcs import ls


class TestLs(unittest.TestCase):

    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("os.listdir")
    @patch("os.stat")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_ls_with_succes_without_paths_without_flags(self, mock_cout, mock_error, mock_info, mock_stat, mock_listdir, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home"
        mock_listdir.return_value = ["test1"]
        mock_stat.return_value.st_mode = 0

        ls(cur_path="home", paths=[], flags="")

        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)
        self.assertEqual(mock_stat.call_count, 1)
        mock_listdir.assert_called_once_with("home")


    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("os.listdir")
    @patch("os.stat")
    @patch("time.strftime")
    @patch("src.read_funcs.permissions")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_ls_with_succes_without_paths_with_flags(self, mock_cout, mock_error, mock_info, mock_perms, mock_time, mock_size, mock_listdir, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home"
        mock_listdir.return_value = ["test1"]
        mock_size.return_value.st_size = 1

        ls(cur_path="home", paths=[], flags="l")
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)
        self.assertEqual(mock_perms.call_count, 1)
        mock_listdir.assert_called_once_with("home")


    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("os.listdir")
    @patch("os.stat")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_ls_with_succes_with_paths_without_flags(self, mock_cout, mock_error, mock_info, mock_stat, mock_listdir, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home"
        mock_listdir.return_value = ["test1"]
        mock_stat.return_value.st_mode = 0

        ls(cur_path="home", paths=["dir1"], flags="")

        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)
        self.assertEqual(mock_stat.call_count, 1)
        mock_listdir.assert_called_once_with("dir1")


    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("os.listdir")
    @patch("os.stat")
    @patch("time.strftime")
    @patch("src.read_funcs.permissions")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_ls_with_succes_with_paths_with_flags(self, mock_cout, mock_error, mock_info, mock_perms, mock_time, mock_size, mock_listdir, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home"
        mock_listdir.return_value = ["test1"]
        mock_size.return_value.st_size = 1

        ls(cur_path="home", paths=["dir1"], flags="l")
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)
        self.assertEqual(mock_perms.call_count, 1)
        mock_listdir.assert_called_once_with("dir1")


    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log

unittest.main()
