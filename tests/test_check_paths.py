import unittest
from unittest.mock import patch
from src.tools import check_paths
import src.my_exceptions as my_exception


class TestCheckPaths(unittest.TestCase):


    @patch("src.tools.normalization_path")
    def test_check_paths_with_succes_with_mode_minus_2_with_2_paths(self, mock_norm):
        mock_norm.side_effect = ["/folder1", "/folder2"]

        self.assertEqual(check_paths(["/folder1", "/folder2"], -2), ["/folder1", "/folder2"])


    @patch("src.tools.normalization_path")
    def test_check_paths_with_succes_with_mode_minus_2_with_1_path(self, mock_norm):
        mock_norm.return_value = "/folder1"

        self.assertEqual(check_paths(["/folder1"], -2), ["/folder1", "/folder1"])
        mock_norm.assert_called_once()

    def test_check_paths_with_too_few_paths_error_with_mode_minus_2(self):

        with self.assertRaises(my_exception.TooFewPathsError):
            check_paths([], -2)


    def test_check_paths_with_too_many_paths_error_with_mode_minus_2(self):

        with self.assertRaises(my_exception.TooManyPathsError):
            check_paths(["/dir1", "/dir2", "/dir3"], -2)


    @patch("src.tools.normalization_path")
    def test_check_paths_with_succes_with_mode_minus_1(self, mock_norm):
        mock_norm.return_value = "/folder1"

        self.assertEqual(check_paths(["/folder1"], -1), ["/folder1"])


    def test_check_paths_with_too_few_paths_error_with_mode_minus_1(self):

        with self.assertRaises(my_exception.TooFewPathsError):
            check_paths([], -1)


    @patch("src.tools.normalization_path")
    def test_check_paths_with_succes_with_mode_0_with_1_path(self, mock_norm):
        mock_norm.return_value = "/folder1"

        self.assertEqual(check_paths(["/folder1"], 0), ["/folder1"])

        self.assertEqual(check_paths([], 0), [])

    @patch("src.tools.normalization_path")
    def test_check_paths_with_succes_with_others_mode(self, mock_norm):
        mock_norm.side_effect = ["/folder1", "/folder2"]

        self.assertEqual(check_paths(["/folder1", "/folder2"], 2), ["/folder1", "/folder2"])


    def test_check_paths_with_too_few_paths_error_with_others_mode(self):

        with self.assertRaises(my_exception.TooFewPathsError):
            check_paths(["/folder1"], 2)


    def test_check_paths_with_too_many_paths_error_with_others_mode(self):

        with self.assertRaises(my_exception.TooManyPathsError):
            check_paths(["/folder1", "/folder2", "/folder3"], 2)

unittest.main()
