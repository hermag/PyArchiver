import os
import subprocess
from unittest import TestCase

from pyarchiver import pyarchiver


class TestPyarchiver(TestCase):

    def test_bz2_in_pyarchiver(self):
        """.Checks if bz2 method is in the list of available archiving methods."""
        file_to_archive = "/tmp/pyarchiver_asdasdasdasd.txt"
        path_of_archive = "/tmp"
        archive_file = "pyarchiver"
        method = 'bz2'
        test_object = pyarchiver(file_to_archive, path_of_archive, archive_file, method)
        self.assertTrue(method in test_object.get_archivation_methods())

    def test_gzip_in_pyarchiver(self):
        """.Checks if gzip method is in the list of available archiving methods."""
        file_to_archive = "/tmp/pyarchiver_asdasdasdasd.txt"
        path_of_archive = "/tmp"
        archive_file = "pyarchiver"
        method = 'gzip'
        test_object = pyarchiver(file_to_archive, path_of_archive, archive_file, method)
        self.assertTrue(method in test_object.get_archivation_methods())

    def test_lzma_in_pyarchiver(self):
        """.Checks if lzma method is in the list of available archiving methods."""
        file_to_archive = "/tmp/pyarchiver_asdasdasdasd.txt"
        path_of_archive = "/tmp"
        archive_file = "pyarchiver"
        method = 'lzma'
        test_object = pyarchiver(file_to_archive, path_of_archive, archive_file, method)
        self.assertTrue(method in test_object.get_archivation_methods())

    def test_lzma(self):
        with open("/tmp/foo_lzma.txt", "wb") as out:
            out.write(os.urandom(1280000))
        out.close()
        file_to_archive = "/tmp/foo_lzma.txt"
        path_of_archive = "/tmp/archive_folder"
        archive_file = "foo_test.txt"
        method = 'lzma'
        test_object = pyarchiver(file_to_archive, path_of_archive, archive_file, method)
        self.assertTrue(test_object.pyarchiver())

    def test_bzip2(self):
        with open("/tmp/foo_bzip2.txt", "wb") as out:
            out.write(os.urandom(1280000))
        out.close()
        file_to_archive = "/tmp/foo_bzip2.txt"
        path_of_archive = "/tmp/archive_folder"
        archive_file = "foo_test.txt"
        method = 'bz2'
        test_object = pyarchiver(file_to_archive, path_of_archive, archive_file, method)
        self.assertTrue(test_object.pyarchiver())

    def test_gzip(self):
        with open("/tmp/foo_gzip.txt", "wb") as out:
            out.write(os.urandom(1280000))
        out.close()
        file_to_archive = "/tmp/foo_gzip.txt"
        path_of_archive = "/tmp/archive_folder"
        archive_file = "foo_test.txt"
        method = 'gzip'
        test_object = pyarchiver(file_to_archive, path_of_archive, archive_file, method)
        self.assertTrue(test_object.pyarchiver())
