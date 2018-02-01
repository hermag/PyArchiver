from unittest import TestCase


import pyarchiver


class TestPyarchiver(TestCase):
    def test_is_string(self):
        file_to_archive="/tmp/pyarchiver.txt"
        path_of_archive="/tmp"
        archive_file="pyarchiver"
        method='lzma'
        s = pyarchiver.pyarchiver(file_to_archive,)
        self.assertTrue(isinstance(s, basestring))
