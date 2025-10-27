import unittest
from unittest.mock import patch
from src.check_input import input_check, normalisation_path


class TestCheckInput(unittest.TestCase):

    def test_input_check(self):
        self.assertEqual(input_check('cd -r "azaza 1"'), [['cd', 'azaza 1'],['-r']])
        self.assertEqual(input_check("rm qwerty rt 'All in' -rrrrrrr"), [['rm', 'qwerty', 'rt', "All in"], ['-r']])
        self.assertEqual(input_check('cat \'yt  rter\' "tytr t"'), [['cat', "yt  rter", 'tytr t'], []])

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    def test_normalisation_path(self, mock_abs, mock_home, mock_chdir):
        mock_abs.return_value = '/c:/folder1/file1.txt'
        self.assertEqual(normalisation_path('folder1', 'file1.txt'), '/c:/folder1/file1.txt')

        mock_home.return_value = '/home/user1/Docs A'
        mock_abs.return_value = '/c:/home/user1/Docs A'
        self.assertEqual(normalisation_path('folder1', 'target/~/user1/Docs A'), '/c:/home/user1/Docs A')

        mock_home.return_value = '/home/user1/Docs A'
        mock_abs.return_value = '/c:/home/user1/Docs B'
        self.assertEqual(normalisation_path('folder1', 'target/~/user1/Docs A/..//Docs B'), '/c:/home/user1/Docs B')

unittest.main()
