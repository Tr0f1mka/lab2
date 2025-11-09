import unittest
from src.tools import parser

tests = {
    "ls -l file1.py    -a dir2"                 : [["ls", "file1.py", "dir2"], ['la']],
    "cat    'New   folder1' \"New folder2\""    : [["cat", "New   folder1", "New folder2"], [""]],
    "zip folder1 dir1 file1 file2    -awawa"    : [["zip", "folder1", "dir1", "file1", "file2"], ["aw"]],
    "-l"                                        : [[], ["l"]],
    ""                                          : [[], [""]]
}

class TestParser(unittest.TestCase):

    def test_parser(self):

        for i in tests.keys():
            self.assertEqual(parser(i), tests[i])

unittest.main()
