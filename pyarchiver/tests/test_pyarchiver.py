import os
import subprocess
from unittest import TestCase

from pyarchiver import pyarchiver


class TestPyarchiver(TestCase):

    def test_lzma(self):
        with open("/tmp/foo_lzma.txt", "wb") as out:
            out.write(os.urandom(1280000))
        out.close()
        file_to_archive = "/tmp/foo_lzma.txt"
        path_of_archive = "/tmp/archive_folder"
        method = 'lzma'
        test_object = pyarchiver(file_to_archive, path_of_archive, method)
        self.assertTrue(test_object.pyarchiver())

    def test_bzip2(self):
        with open("/tmp/foo_bzip2.txt", "wb") as out:
            out.write(os.urandom(1280000))
        out.close()
        file_to_archive = "/tmp/foo_bzip2.txt"
        path_of_archive = "/tmp/archive_folder"
        method = 'bzip2'
        test_object = pyarchiver(file_to_archive, path_of_archive, method)
        self.assertTrue(test_object.pyarchiver())

    def test_gzip(self):
        with open("/tmp/foo_gzip.txt", "wb") as out:
            out.write(os.urandom(1280000))
        out.close()
        file_to_archive = "/tmp/foo_gzip.txt"
        path_of_archive = "/tmp/archive_folder"
        method = 'gzip'
        test_object = pyarchiver(file_to_archive, path_of_archive, method)
        self.assertTrue(test_object.pyarchiver())
