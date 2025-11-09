import unittest
from src.tools import check_flags
from src.my_exceptions import UndefinedFlagError


class TestCheckFlags(unittest.TestCase):

    def test_check_flags_with_succes(self):

        self.assertEqual(check_flags("asdf", "qweasdf"), None)
        self.assertEqual(check_flags("", "q"), None)
        self.assertEqual(check_flags("as", "qweasdf"), None)

    def test_check_flags_with_undefined_flag_error(self):

        with self.assertRaises(UndefinedFlagError):
            check_flags("q", "l")

        with self.assertRaises(UndefinedFlagError):
            check_flags("qwerty", "ytrwq")

        with self.assertRaises(UndefinedFlagError):
            check_flags("q", "")

unittest.main()
