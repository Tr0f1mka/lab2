import unittest
from unittest.mock import patch

from src.archive_funcs import unpack_archive


class TestMakeArchive(unittest.TestCase):

    @patch("os.chdir")
    @patch("shutil.unpack_archive")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_unpack_zip_archive(self, mock_cout, mock_error, mock_info, mock_unpack_archive, mock_chdir):

        unpack_archive(cur_path="home", paths=["dir1.zip"], flags="")
        mock_unpack_archive.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)


    @patch("os.chdir")
    @patch("shutil.unpack_archive")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_unpack_tar_archive(self, mock_cout, mock_error, mock_info, mock_unpack_archive, mock_chdir):

        unpack_archive(cur_path="home", paths=["dir1.tar.gz"], flags="")
        mock_unpack_archive.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)

    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log

unittest.main()
