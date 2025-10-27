import unittest
from unittest.mock import patch, MagicMock, mock_open
import stat
import io
import src.read_funcs as read_funcs


class TestReadFuncs(unittest.TestCase):

    @patch('os.chdir')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch('src.read_funcs.normalisation_path')
    @patch('os.getcwd')
    @patch('os.listdir')
    @patch('os.stat')
    @patch('src.read_funcs.permissions')
    @patch('stat.S_ISDIR')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ls(self, mock_cout, mock_dir, mock_perms, mock_stat, mock_listdir, mock_getcwd, mock_norm, mock_info, mock_error, mock_chdir):
        #Тест ls без флага
        mock_norm.return_value = '/c:/folder1/dir1'
        mock_listdir.return_value = ['file1.txt', 'dir a']
        mock_dir.side_effect = [False, True]

        read_funcs.ls('folder1', ['dir1'], [])
        self.assertEqual(mock_cout.getvalue(), '/c:/folder1/dir1\n   \x1b[01;38;05;46mfile1.txt\x1b[0m\n   \x1b[01;38;05;63;48;05;46mdir a\x1b[0m\n')

    @patch('os.chdir')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch('src.read_funcs.normalisation_path')
    @patch('os.getcwd')
    @patch('os.listdir')
    @patch('os.stat')
    @patch('src.read_funcs.permissions')
    @patch('stat.S_ISDIR')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ls_flag(self, mock_cout, mock_dir, mock_perms, mock_stat, mock_listdir, mock_getcwd, mock_norm, mock_info, mock_error, mock_chdir):
        #Тест ls с флагом
        mock_norm.return_value = '/c:/folder1/dir1'
        mock_listdir.return_value = ['file1.txt', 'dir a']

        def mock_stat_side_effect(path):
            mock_stat_result = MagicMock()
            if 'dir' in path:
                mock_stat_result.st_mode = stat.S_IFDIR  # Директория
                mock_stat_result.st_size = 4096
            else:
                mock_stat_result.st_mode = stat.S_IFREG  # Обычный файл
                mock_stat_result.st_size = 1024
            mock_stat_result.st_mtime = 1701426600
            return mock_stat_result

        mock_stat.side_effect = mock_stat_side_effect
        mock_perms.side_effect = ['-rwxrwxrwx', 'dr-xr-xr-x']

        read_funcs.ls('folder1', ['dir1'], ['-l'])
        self.assertEqual(mock_cout.getvalue(), '/c:/folder1/dir1\n   -rwxrwxrwx          4096  2023-12-01 13:30  \x1b[01;38;05;46mfile1.txt\x1b[0m\n   dr-xr-xr-x          4096  2023-12-01 13:30  \x1b[01;38;05;63;48;05;46mdir a\x1b[0m\n')

    @patch('os.chdir')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch('src.read_funcs.normalisation_path')
    @patch('os.getcwd')
    @patch('os.listdir')
    @patch('os.stat')
    @patch('src.read_funcs.permissions')
    @patch('stat.S_ISDIR')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ls_err(self, mock_cout, mock_dir, mock_perms, mock_stat, mock_listdir, mock_getcwd, mock_norm, mock_info, mock_error, mock_chdir):
        #Тест ls с ошибкой
        mock_norm.return_value = '/c:/folder1/dir1'
        mock_listdir.side_effect = FileNotFoundError

        read_funcs.ls('folder1', ['dir1'], [])
        # self.assertIn(mock_cout.getvalue(), '')
        self.assertEqual(mock_cout.getvalue(), '/c:/folder1/dir1\n\x1b[01;38;05;196mОшибка:\x1b[0m указанного пути не существует\n')


    @patch('os.chdir')
    @patch('os.getcwd')
    @patch('src.read_funcs.normalisation_path')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cd(self, mock_cout, mock_info, mock_error, mock_norm, mock_get, mock_chdir):
        #Тест cd
        mock_norm.return_value = '/c:/folder1/dir a/dir b'

        read_funcs.cd('folder1', ['dir a/dir b'])
        self.assertEqual(mock_cout.getvalue(), '')

    @patch('os.chdir')
    @patch('os.getcwd')
    @patch('src.read_funcs.normalisation_path')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cd_err(self, mock_cout, mock_info, mock_error, mock_norm, mock_get, mock_chdir):
        #Тест cd с ошибкой избытка аргументов
        # mock_norm.return_value = '/c:/folder1/dir a/dir b'

        read_funcs.cd('folder1', ['dir a/dir b', 'dir2'])
        self.assertEqual(mock_cout.getvalue(), '\x1b[01;38;05;196mОшибка:\x1b[0m слишком много аргументов для команды cd\n')


    @patch('os.chdir')
    @patch('src.read_funcs.normalisation_path')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch("builtins.open", new_callable=mock_open, read_data=b"line1\nline2\n")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cat(self, mock_cout, mock_file, mock_info, mock_err, mock_norm, mock_chdir):
        #Тест cat
        mock_norm.return_value = 'c:/folder1/file1.txt'

        read_funcs.cat('folder1', ['file1.txt'])
        self.assertEqual(mock_cout.getvalue(), 'c:/folder1/file1.txt\n\x1b[01;48;05;64m   \x1b[0mline1\\n\n\x1b[01;48;05;64m   \x1b[0mline2\\n\n')
        mock_file.assert_called_once_with("c:/folder1/file1.txt", 'rb')

    @patch('os.chdir')
    @patch('src.read_funcs.normalisation_path')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch("builtins.open", new_callable=mock_open, read_data=b"line1\nline2\n")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cat_2(self, mock_cout, mock_file, mock_info, mock_err, mock_norm, mock_chdir):
        #Тест cat с двумя параметрами
        mock_norm.side_effect = ['c:/folder1/file1.txt', 'c:/folder1/file2.txt']

        read_funcs.cat('folder1', ['file1.txt', 'file2.txt'])
        self.assertEqual(mock_cout.getvalue(), 'c:/folder1/file1.txt\n\x1b[01;48;05;64m   \x1b[0mline1\\n\n\x1b[01;48;05;64m   \x1b[0mline2\\n\nc:/folder1/file2.txt\n\x1b[01;48;05;64m   \x1b[0mline1\\n\n\x1b[01;48;05;64m   \x1b[0mline2\\n\n')

    @patch('os.chdir')
    @patch('src.read_funcs.normalisation_path')
    @patch('src.read_funcs.loger.error')
    @patch('src.read_funcs.loger.info')
    @patch("builtins.open", new_callable=mock_open, read_data=b"line1\nline2\n")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cat_err(self, mock_cout, mock_file, mock_info, mock_err, mock_norm, mock_chdir):
        #Тест cat с ошибкой прав доступа
        mock_norm.return_value = 'c:/folder1/file1.txt'
        mock_file.side_effect = PermissionError

        read_funcs.cat('folder1', ['file1.txt'])
        self.assertEqual(mock_cout.getvalue(), 'c:/folder1/file1.txt\n\x1b[01;38;05;196mОшибка:\x1b[0m у тебя здесь нет власти(недостаточно прав)\n')
        mock_file.assert_called_once_with("c:/folder1/file1.txt", 'rb')

unittest.main()
