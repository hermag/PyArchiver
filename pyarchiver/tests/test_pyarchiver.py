from unittest import TestCase


from pyarchiver import pyarchiver


class TestPyarchiver(TestCase):
    def test_1(self):
        file_to_archive="/tmp/pyarchiver.txt"
        path_of_archive="/tmp"
        archive_file="pyarchiver"
        method='lzma'
        s = pyarchiver(file_to_archive,path_of_archive,archive_file,method)
        self.assertTrue(s.pyarchiver())

    def test_gzip_in_pyarchiver(self):
        file_to_archive="/tmp/pyarchiver_asdasdasdasd.txt"
        path_of_archive="/tmp"
        archive_file="pyarchiver"
        method='gzip'
        s = pyarchiver(file_to_archive,path_of_archive,archive_file,method)
        self.assertTrue(method in s.get_archivation_methods())


    def test_bz2_in_pyarchiver(self):
        file_to_archive="/tmp/pyarchiver_asdasdasdasd.txt"
        path_of_archive="/tmp"
        archive_file="pyarchiver"
        method='bz2'
        s = pyarchiver(file_to_archive,path_of_archive,archive_file,method)
        self.assertTrue(method in s.get_archivation_methods())


    def test_lzma_in_pyarchiver(self):
        file_to_archive="/tmp/pyarchiver_asdasdasdasd.txt"
        path_of_archive="/tmp"
        archive_file="pyarchiver"
        method='lzma'
        s = pyarchiver(file_to_archive,path_of_archive,archive_file,method)
        self.assertTrue(method in s.get_archivation_methods())
