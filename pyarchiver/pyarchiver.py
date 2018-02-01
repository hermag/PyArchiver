# -*- coding: utf-8 -*-
"""PyArchiver core."""
import os


class pyarchiver:
	""".Basic pyarchiver class."""
	def __init__(self,file_to_archive,archivation_path,archive_filename,archiving_method):
		self.file_to_archive = file_to_archive
		self.archivation_path = archivation_path
		self.archive_filename = archive_filename
		self.archiving_method = archiving_method
		self.archiving_methods= ['bz2','gzip','lzma']


	def get_archivation_methods(self):
		""".Returns the all available methods for\
		 archiving the file with this tool"""
		return self.archiving_methods


	def check_if_path_exists(self):
		""".If file/folder exist return True, else False."""
		try:
			if os.path.exists(self.file_to_archive):
				return True
			else:
				return False
		except OSError:
			print("Check if you have permissions to %s"%self.file_to_archive)
			return False
		return False


	def create_path(self):
		""".Checks if folder exists and creates if not."""
		if os.path.exists(self.archivation_path):
			return True
		else:
			try:
				os.makedirs(self.archivation_path)
				return True
			except OSError:
				print("Check if you have permissions to %s"%self.archivation_path)
				return False
		return False


	def pyarchiver(self):
		""".The main function doing the archivation."""
		if self.check_if_path_exists():
			return True
		else:
			return False
		return False
