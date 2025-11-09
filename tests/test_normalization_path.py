import unittest
from unittest.mock import patch
from src.tools import normalization_path
import os
from os.path import expanduser
import io


class TestNormalizationPath(unittest.TestCase):

    def test_normalization_path(self):

        self.assertEqual(normalization_path("C:/folder1/fil1.txt"), f"C:{os.sep}folder1{os.sep}fil1.txt")

    def test_normalization_path_with_home_path(self):

        self.assertEqual(normalization_path("~\\dir1\\dir2/dir3/dir4"), f"{expanduser("~")}{os.sep}dir1{os.sep}dir2{os.sep}dir3{os.sep}dir4")

    def test_normalization_path_with_repeat_slashes(self):

        self.assertEqual(normalization_path("C:\\\\/folder1//file1"), f"C:{os.sep}folder1{os.sep}file1")

    @patch("platform.system")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_normalization_path_with_root_dir(self, mock_cout, mock_sys):
        mock_sys.return_value = "Windows"

        self.assertEqual(normalization_path("C:"), "C:\\")

unittest.main()
