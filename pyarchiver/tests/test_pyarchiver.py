from unittest import TestCase


import pyarchiver


class TestPyarchiver(TestCase):
    def test_1(self):
        file_to_archive="/tmp/pyarchiver.txt"
        path_of_archive="/tmp"
        archive_file="pyarchiver"
        method='lzma'
        s = pyarchiver.pyarchiver(file_to_archive,path_of_archive,archive_file,method)
        self.assertTrue(s)

    def test_2(self):
        file_to_archive="/tmp/pyarchiver_asdasdasdasd.txt"
        path_of_archive="/tmp"
        archive_file="pyarchiver"
        method='lzma'
        s = pyarchiver.pyarchiver(file_to_archive,path_of_archive,archive_file,method)
        self.assertTrue(s)
