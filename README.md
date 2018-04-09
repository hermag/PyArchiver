# PyArchiver
Implements archiving the files from given location, with given period in a given location.

#### Install using pip
```
pip install git+https://github.com/hermag/PyArchiver
```
#### Update of the installed package
```
pip install git+https://github.com/hermag/PyArchiver  --upgrade
```
#### Usage
```
from pyarchiver import pyarchiver
Full_Path_of_File_to_Archive = "/tmp/file_to_archive.csv"
Full_Path_of_Archive_Storage = "/tmp/archive/"
Archivation_Method = 'lzma' ###Options 'bzip2', 'gzip'
archiver = pyarchiver(Full_Path_of_File_to_Archive,Full_Path_of_Archive_Storage,Archivation_Method)
output = archiver.pyarchiver()
print(output)
True
```

