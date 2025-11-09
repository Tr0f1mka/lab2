import unittest
from unittest.mock import patch

from src.archive_funcs import make_archive


class TestMakeArchive(unittest.TestCase):

    @patch("os.chdir")
    @patch("shutil.make_archive")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_make_archive_zip_with_1_path(self, mock_cout, mock_error, mock_info, mock_make_archive, mock_chdir):

        make_archive(cur_path="home", paths=["dir1"], mode="zip", flags="")
        mock_make_archive.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("shutil.make_archive")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_make_archive_zip_with_2_path(self, mock_cout, mock_error, mock_info, mock_make_archive, mock_chdir):

        make_archive(cur_path="home", paths=["dir1", "dir2/dir1.zip"], mode="zip", flags="")
        mock_make_archive.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("shutil.make_archive")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_make_archive_tar_with_1_path(self, mock_cout, mock_error, mock_info, mock_make_archive, mock_chdir):

        make_archive(cur_path="home", paths=["dir1"], mode="gztar", flags="")
        mock_make_archive.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("shutil.make_archive")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_make_archive_tar_with_2_path(self, mock_cout, mock_error, mock_info, mock_make_archive, mock_chdir):

        make_archive(cur_path="home", paths=["dir1", "dir2/dir1.tar.gz"], mode="gztar", flags="")
        mock_make_archive.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)

    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log

unittest.main()
