import unittest
from unittest.mock import patch, MagicMock
import io
import zipfile
import src.archive_funcs as archive_funcs

class TestArchive(unittest.TestCase):

    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('os.walk')
    @patch('zipfile.ZipFile')
    @patch('os.path.exists')
    @patch('os.path.isdir')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zip(self, mock_cout, mock_isdir, mock_exists, mock_zip, mock_walk, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест zip
        mock_norm.side_effect = ['/folder1/source', '/folder1/source.zip']
        mock_zip.return_value = MagicMock()
        mock_exists.return_value = True
        mock_isdir.return_value = True

        archive_funcs.zip('folder1', ['source', 'source.zip'])
        mock_zip.assert_called_once_with('/folder1/source.zip', 'w', zipfile.ZIP_DEFLATED)
        mock_info.assert_called_once_with('Result: Succes')

    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('os.walk')
    @patch('zipfile.ZipFile')
    @patch('os.path.exists')
    @patch('os.path.isdir')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zip_err(self, mock_cout, mock_isdir, mock_exists, mock_zip, mock_walk, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест zip с ошибкой
        mock_norm.side_effect = ['/folder1/source', '/folder1/source.zip']
        mock_exists.return_value = False

        archive_funcs.zip('folder1', ['source', 'source.zip'])
        self.assertEqual(mock_zip.call_count, 0)
        mock_err.assert_called_once_with('Result: File not found')


    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('os.walk')
    @patch('zipfile.ZipFile')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_unzip(self, mock_cout, mock_zip, mock_walk, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест unzip
        mock_norm.return_value = '/folder1/source.zip'
        mock_zip.return_value = MagicMock()

        archive_funcs.unzip('folder1', ['source.zip'])
        mock_zip.assert_called_once_with('/folder1/source.zip', 'r')
        mock_info.assert_called_once_with('Result: Succes')

    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('os.walk')
    @patch('zipfile.ZipFile')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_unzip_err(self, mock_cout, mock_zip, mock_walk, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест unzip с ошибкой
        mock_norm.return_value = '/folder1/source.zip'
        mock_zip.side_effect = PermissionError

        archive_funcs.unzip('folder1', ['source.zip'])
        mock_zip.assert_called_once_with('/folder1/source.zip', 'r')
        mock_err.assert_called_once_with('Result: Not enough permissions')


    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('tarfile.open')
    @patch('os.path.isdir')
    @patch('os.path.exists')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tar(self, mock_cout, mock_exists, mock_isdir, mock_tar, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест tar
        mock_norm.side_effect = ['/folder1/source', '/folder1/source1.tar.gz']
        mock_tar.return_value.__enter__.return_value = MagicMock()
        mock_isdir.return_value = True
        mock_exists.return_value = True

        archive_funcs.tar('folder1', ['source', 'source1.tar.gz'])
        mock_tar.assert_called_once_with('/folder1/source1.tar.gz', 'w:gz')
        mock_info.assert_called_once_with('Result: Succes')


    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('tarfile.open')
    @patch('os.path.isdir')
    @patch('os.path.exists')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tar_err(self, mock_cout, mock_exists, mock_isdir, mock_tar, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест tar с ошибкой
        mock_norm.side_effect = ['/folder1/source', '/folder1/source.tar.gz']
        mock_exists.return_value = False

        archive_funcs.tar('folder1', ['source', 'source.tar.gz'])
        self.assertEqual(mock_tar.call_count, 0)
        mock_err.assert_called_once_with('Result: File not found')


    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('tarfile.open')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_untar(self, mock_cout, mock_tar, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест untar
        mock_norm.return_value = '/folder1/source.tar.gz'
        mock_tar.return_value.__enter__.return_value = MagicMock()

        archive_funcs.untar('folder1', ['source.tar.gz'])
        mock_tar.assert_called_once_with('/folder1/source.tar.gz', 'r:gz')
        mock_info.assert_called_once_with('Result: Succes')

    @patch('os.chdir')
    @patch('src.archive_funcs.normalization_path')
    @patch('src.archive_funcs.loger.info')
    @patch('src.archive_funcs.loger.error')
    @patch('tarfile.open')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_untar_err(self, mock_cout, mock_tar, mock_err, mock_info, mock_norm, mock_chdir):
        #Тест untar с ошибкой
        mock_norm.return_value = '/folder1/source.tar.gz'
        mock_tar.side_effect = PermissionError

        archive_funcs.untar('folder1', ['source.tar.gz'])
        mock_tar.assert_called_once_with('/folder1/source.tar.gz', 'r:gz')
        mock_err.assert_called_once_with('Result: Not enough permissions')

unittest.main()
