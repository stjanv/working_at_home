from zipfile import ZipFile
from os import mkdir
import string
import itertools

directory = "ExtractArchive/searches"
try:
    mkdir(directory)
except FileExistsError:
    pass

