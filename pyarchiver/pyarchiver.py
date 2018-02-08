# -*- coding: utf-8 -*-
"""PyArchiver core."""
import os
import subprocess


class pyarchiver:
    """.Basic pyarchiver class."""

    def __init__(self, file_to_archive, archivation_path, archived_file, archiving_method):
        self.file_to_archive = file_to_archive
        self.archivation_path = archivation_path
        self.archived_file = archived_file
        self.archiving_method = archiving_method
        self.archiving_methods = ['bz2', 'gzip', 'lzma']

    def get_archivation_methods(self):
        """.Returns the all available methods for\
         archiving the file with this tool."""
        return self.archiving_methods

    def check_if_input_file_exists(self):
        """.If file/folder exist return True, else False."""
        try:
            if os.path.exists(self.file_to_archive):
                return True
            else:
                return False
        except OSError:
            print("Check if you have permissions to %s" % self.file_to_archive)
            return False
        return False

    def check_and_make_output_location(self):
        """.Checks if folder exists and creates if not."""
        if os.path.exists(self.archivation_path):
            return True
        else:
            try:
                os.makedirs(self.archivation_path)
                print("%s created" % self.archivation_path)
                return True
            except OSError:
                print("Check if you have permissions to %s" % self.archivation_path)
                return False
        return False

    def make_bz2(self):
        """.Makes tar.bz2 archive out of the file/folder."""
        output_file_full_path = "%s/%s.bz2" % (self.archivation_path, self.archived_file)
        try:
            p = subprocess.Popen(["bzip2", self.file_to_archive], stdout=subprocess.PIPE)
            output, err = p.communicate()
            return_code = p.returncode
            if return_code != 0:
                print(err)
                return False
            else:
                p = subprocess.Popen(["mv", "%s.bz2" % self.file_to_archive, output_file_full_path])
                p.communicate()
                return True
        except subprocess.CalledProcessError as e:
            print(e.output)
            return False
        return False

    def make_gzip(self):
        "Makes gzip archive out of the file/folder."
        output_file_full_path = "%s/%s.gz" % (self.archivation_path, self.archived_file)
        try:
            p = subprocess.Popen(["/bin/gzip", self.file_to_archive], stdout=subprocess.PIPE)
            output, err = p.communicate()
            return_code = p.returncode
            if return_code != 0:
                print(err)
                return False
            else:
                p = subprocess.Popen(["mv", "%s.gz" % self.file_to_archive, output_file_full_path])
                p.communicate()
                return True
        except subprocess.CalledProcessError as e:
            print(e.output)
            return False
        return False

    def make_lzma(self):
        "Makes lzma archive out of the file/folder."
        output_file_full_path = "%s/%s.lzma" % (self.archivation_path, self.archived_file)
        try:
            p = subprocess.Popen(["/usr/bin/lzma", self.file_to_archive], stdout=subprocess.PIPE)
            output, err = p.communicate()
            return_code = p.returncode
            if return_code != 0:
                print(err)
                return False
            else:
                p = subprocess.Popen(["mv", "%s.lzma" % self.file_to_archive, output_file_full_path])
                p.communicate()
                return True
        except subprocess.CalledProcessError as e:
            print(e.output)
            return False
        return False

    def pyarchiver(self):
        """.The main function doing the archivation."""
        if self.check_and_make_output_location():
            pass
        else:
            print("Output location %s is not available" % self.archivation_path)
            return False

        if self.check_if_input_file_exists():
            pass
        else:
            print("File/Folder %s to archive is not available." % self.file_to_archive)
            return False

        if self.archiving_method == 'bz2':
            if self.make_bz2():
                return True
            else:
                return False
        elif self.archiving_method == 'gzip':
            if self.make_gzip():
                return True
            else:
                return False
        elif self.archiving_method == 'lzma':
            if self.make_lzma():
                return True
            else:
                return False
        else:
            print("Archiging method %s is invalid" % self.archiving_method)
            return False

        print("PyArchiver Failed With Unknown Reason.")
        return False
