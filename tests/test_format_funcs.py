import unittest
from unittest.mock import patch
import io
import src.format_funcs as format_funcs

class TestFormat(unittest.TestCase):

    @patch('os.chdir')
    @patch('src.format_funcs.loger.error')
    @patch('src.format_funcs.loger.info')
    @patch('shutil.copy2')
    @patch('shutil.copytree')
    @patch('src.format_funcs.normalisation_path')
    def test_cp(self, mock_norm, mock_cpd, mock_cp, mock_info, mock_error, mock_chdir):
        #Тест cp
        mock_norm.side_effect = ['/c:/folder1/file1.txt', '/c:/folder1/src']

        format_funcs.cp('folder1', ['file1.txt', 'src'], [])
        mock_cp.assert_called_once_with('/c:/folder1/file1.txt', '/c:/folder1/src')
        mock_info.assert_called_once_with('Result: Succes')
        self.assertEqual(mock_cpd.call_count, 0)

    @patch('os.chdir')
    @patch('src.format_funcs.loger.error')
    @patch('src.format_funcs.loger.info')
    @patch('shutil.copy2')
    @patch('shutil.copytree')
    @patch('src.format_funcs.normalisation_path')
    def test_cp_dir(self, mock_norm, mock_cpd, mock_cp, mock_info, mock_error, mock_chdir):
        #Тест cp для директории
        mock_norm.side_effect = ['/c:/folder1/files', '/c:/folder1/src/files']

        format_funcs.cp('folder1', ['files', 'src'], ['-r'])
        mock_cpd.assert_called_once_with('/c:/folder1/files', '/c:/folder1/src/files')
        mock_info.assert_called_once_with('Result: Succes')
        self.assertEqual(mock_cp.call_count, 0)

    @patch('os.chdir')
    @patch('src.format_funcs.loger.error')
    @patch('src.format_funcs.loger.info')
    @patch('shutil.copy2')
    @patch('shutil.copytree')
    @patch('src.format_funcs.normalisation_path')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cp_err(self, mock_cout, mock_norm, mock_cpd, mock_cp, mock_info, mock_error, mock_chdir):
        #Тест cp с ошибкой ОС
        mock_cp.side_effect = OSError

        format_funcs.cp('folder1', ['file1.txt', 'src'], [])
        self.assertEqual(mock_cout.getvalue(), '\x1b[01;38;05;196mОшибка:\x1b[0m указанного пути не существует\n')

    @patch('os.chdir')
    @patch('src.format_funcs.loger.error')
    @patch('src.format_funcs.loger.info')
    @patch('src.format_funcs.normalisation_path')
    @patch('shutil.move')
    # @patch('sys.stdout', new_callable=io.StringIO)
    def test_mv(self, mock_mv, mock_norm, mock_info, mock_err, mock_chdir):
        #Тест mv
        mock_norm.side_effect = ['/c:/folder1/kazik.py', '/c:/folder1/dep']

        format_funcs.mv('folder1', ['kazik.py', 'dep'])
        mock_mv.assert_called_once_with('/c:/folder1/kazik.py', '/c:/folder1/dep')
        mock_info.assert_called_once_with('Result: Succes')

    @patch('os.chdir')
    @patch('src.format_funcs.loger.error')
    @patch('src.format_funcs.loger.info')
    @patch('src.format_funcs.normalisation_path')
    @patch('shutil.move')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mv_err(self, mock_cout, mock_mv, mock_norm, mock_info, mock_err, mock_chdir):
        #Тест mv с ошибкой отсутствия файла
        mock_norm.side_effect = ['/c:/folder1/kazik.py', '/c:/folder1/dep']
        mock_mv.side_effect = FileNotFoundError

        format_funcs.mv('folder1', ['kazik.py', 'dep'])
        self.assertEqual(mock_cout.getvalue(), '\x1b[01;38;05;196mОшибка:\x1b[0m указанного пути не существует\n')
        mock_mv.assert_called_once_with('/c:/folder1/kazik.py', '/c:/folder1/dep')
        mock_err.assert_called_once_with('Result: File not found')

    @patch('os.chdir')
    @patch('src.format_funcs.loger.error')
    @patch('src.format_funcs.loger.info')
    @patch('src.format_funcs.normalisation_path')
    @patch('os.getcwd')
    @patch('os.remove')
    @patch('os.rmtree')
    @patch('builtins.input')
    def test_rm(self, mock_input, mock_rmd, mock_rm, mock_get, mock_norm, movk_info, mock_err, mock_chdir):
        #Тест rm
        mock_input.return_value = 'y'
        mock_norm.side_effect = ['/folder1/']

        format_funcs.rm('folder1', ['windows.docx', 'lab2.py'], [])


unittest.main()
