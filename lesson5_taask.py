from zipfile import ZipFile
from os import mkdir
import string
import itertools

line = '-----------------------------'

def generator(chars):
    #attempts = 0
    for password_length in range(1, 9):
        for password in itertools.product(chars, repeat=password_length):
            #attempts += 1
            password = ''.join(password)
            archive.setpassword(password.encode())
            try:
                archive.extractall(directory)
            except:
                yield "[False]:" + password
            else:
                yield line + "\n[True]: " + password
                return


directory = "ExtractArchive"
try:
    mkdir(directory)
except FileExistsError:
    pass

print(line)
chars = string.ascii_lowercase + string.digits
with ZipFile(input("Archive: ")) as archive:
    print(line)
    for password in generator(chars):
        print(password)
print(line)
