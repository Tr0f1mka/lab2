import unittest
from unittest.mock import patch
from src.format_funcs import mv


class TestMv(unittest.TestCase):

    @patch("os.chdir")
    @patch("shutil.move")
    @patch("src.tools.logger.info")
    @patch("src.tools.logger.error")
    @patch("sys.stdout")
    def test_mv(self, mock_cout, mock_error, mock_info, mock_move, mock_chdir):
        mv(cur_path="home", paths=["source", "target"], flags="")
        mock_move.assert_called_once()
        self.assertEqual(mock_info.call_count, 2)
        self.assertEqual(mock_error.call_count, 0)

    # Тестов ошибок здесь нет, так как их обрабатывает декоратор create_log

unittest.main()
