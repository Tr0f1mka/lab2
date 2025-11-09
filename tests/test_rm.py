import unittest
from unittest.mock import patch
from src.format_funcs import rm


class TestMv(unittest.TestCase):

    @patch("os.chdir")
    @patch("src.format_funcs.user_input")
    @patch("os.path.isdir")
    @patch("os.listdir")
    @patch("shutil.rmtree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_without_flag_without_cancel_with_empty_dir(self, mock_cout, mock_error, mock_info, mock_rm, mock_listdir, mock_isdir, mock_cin, mock_chdir):
        mock_cin.return_value = "y"
        mock_isdir.return_value = True
        mock_listdir.return_value = []

        rm(cur_path="home", paths=["source"], flags="")
        mock_rm.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("src.format_funcs.user_input")
    @patch("os.path.isdir")
    @patch("os.listdir")
    @patch("os.remove")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_without_flag_without_cancel_with_full_dir(self, mock_cout, mock_error, mock_info, mock_rm, mock_listdir, mock_isdir, mock_cin, mock_chdir):
        mock_cin.return_value = "y"
        mock_isdir.return_value = True
        mock_listdir.return_value = ["file1"]

        rm(cur_path="home", paths=["source"], flags="")
        self.assertEqual(mock_info.call_count, 1)
        mock_error.assert_called_once_with("[RESULT] <rm> -r flag is missing")
        # self.assertEqual(mock_error.call_count, 1)


    @patch("os.chdir")
    @patch("src.format_funcs.user_input")
    @patch("os.path.isdir")
    @patch("os.listdir")
    @patch("os.remove")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_without_flag_without_cancel_with_file(self, mock_cout, mock_error, mock_info, mock_rm, mock_listdir, mock_isdir, mock_cin, mock_chdir):
        mock_cin.return_value = "y"
        mock_isdir.return_value = False

        rm(cur_path="home", paths=["source"], flags="")
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("src.format_funcs.user_input")
    @patch("os.path.isdir")
    @patch("os.listdir")
    @patch("os.remove")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_without_flag_with_cancel(self, mock_cout, mock_error, mock_info, mock_rm, mock_listdir, mock_isdir, mock_cin, mock_chdir):
        mock_cin.return_value = "n"

        rm(cur_path="home", paths=["source"], flags="")
        self.assertEqual(mock_info.call_count, 3)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("src.format_funcs.check_paths")
    @patch("src.format_funcs.user_input")
    @patch("shutil.rmtree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_with_flag_with_root_dir(self, mock_cout, mock_error, mock_info, mock_rm, mock_cin, mock_check_path, mock_chdir):
        mock_check_path.return_value = ["C:\\"]

        rm(cur_path="home", paths=["C:\\"], flags="r")
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 1)


    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("os.path.abspath")
    @patch("src.format_funcs.user_input")
    @patch("shutil.rmtree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_with_flag_without_root_and_parent_dir_without_cancel(self, mock_cout, mock_error, mock_info, mock_rm, mock_cin, mock_abspath, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home"
        mock_abspath.return_value = "home/dir1"
        mock_cin.return_value = "y"


        rm(cur_path="home", paths=["dir1"], flags="r")
        mock_rm.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("os.path.abspath")
    @patch("src.format_funcs.user_input")
    @patch("shutil.rmtree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_with_flag_without_root_and_parent_dir_with_cancel(self, mock_cout, mock_error, mock_info, mock_rm, mock_cin, mock_abspath, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home"
        mock_abspath.return_value = "home/dir1"
        mock_cin.return_value = "n"


        rm(cur_path="home", paths=["dir1"], flags="r")
        self.assertEqual(mock_rm.call_count, 0)
        self.assertEqual(mock_info.call_count, 3)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("os.getcwd")
    @patch("os.path.abspath")
    @patch("src.format_funcs.mixer")
    @patch("shutil.rmtree")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_rm_succes_with_flag_with_parent_dir(self, mock_cout, mock_error, mock_info, mock_rm, mock_mixer, mock_abspath, mock_getcwd, mock_chdir):
        mock_getcwd.return_value = "home/user/cmd"
        mock_abspath.return_value = "home/user"

        rm(cur_path="home/user/cmd", paths=["home/user"], flags="r")
        self.assertEqual(mock_rm.call_count, 0)
        self.assertEqual(mock_info.call_count, 2)
        mock_error.assert_called_once_with("[RESULT] <rm> Attempt to delete the parent directory")

    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log

unittest.main()
