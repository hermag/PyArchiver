# -*- coding: utf-8 -*-
"""PyArchiver core."""
import os


def check_if_path_exists(full_path_to_file_or_folder):
    """If file/folder exist return True, else False."""
    the_path = full_path_to_file_or_folder
    try:
        if os.path.exists(the_path):
            return True
        else:
            return False
	except OSError:
		print("Check if you have permissions to %s"%the_path)
        return False


def create_path(the_path):
	"""Checks if folder exists and creates if not."""
	if os.path.exists(the_path):
		return True
	else:
		try:
			os.makedirs(the_path)
			return True
		except OSError:
			print("Check if you have permissions to %s"%the_path)
			return False


def pyarchiver(file_to_archive,
			   archivation_path,
			   archive_filename,
			   archiving_method):
	"""The main function doing the archivation."""
	if check_if_path_exists(file_to_archive):
		return True
	else:
		return False