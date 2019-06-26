from pprint import pprint
import os

from zipfile import ZipFile
from os import mkdir
import string
import itertools

line = '-----------------------------'

# def generator(chars):
#     #attempts = 0
#     for password_length in range(1, 9):
#         for password in itertools.product(chars, repeat=password_length):
#             #attempts += 1
#             password = ''.join(password)
#             archive.setpassword(password.encode())
#             try:
#                 archive.extractall(directory)
#             except:
#                 yield "[False]:" + password
#             else:
#                 yield line + "\n[True]: " + password
#                 return
#
#
# directory = "ExtractArchive"
# try:
#     mkdir(directory)
# except FileExistsError:
#     pass
#
# print(line)
# chars = string.ascii_lowercase
# with ZipFile(input("Archive: ")) as archive:
#     print(line)
#     for password in generator(chars):
#         print(password)
# print(line)


MyPath = '.\ExtractArchive\lesson6'

lines = '=================================================================================================='
takes_Words_in_lines = []
takes_Words_in_lines2 = []


def printing(takes_Words_in_lines):
    for lines in takes_Words_in_lines:
        print(lines)


def chech_dirs_tree(MyPath):
    dirsPathesList = []
    for dirpath, dirnames, files in os.walk(MyPath):
        if os.listdir(dirpath) != []:
            dirsPathesList.append((dirpath, files))
    return dirsPathesList


def read_file(i, j):
    f = open(i[0] + '\\' + j, 'r', encoding='utf-8')
    return f


def add_file_to_list(this_file):
    takes_lines = this_file.readlines()
    for word in takes_lines:
        takes_Words_in_lines.append(word.split('\t'))

    return takes_Words_in_lines


def create_files(llist: list):
    set_of_id = set()
    set_of_sityes = set()
    for i in llist:
        set_of_sityes.add(i[3])
    for sity in set_of_sityes:
        searches_dict = {}
        searches_dict.clear()
        for item in llist:
            if item[3] == sity:
                if item[5] not in searches_dict:
                    if item[4] not in set_of_id:
                        set_of_id.add(item[4])
                        searches_dict[item[5]] = 1
                    else:
                        continue
                else:
                    if item[4] not in set_of_id:
                        set_of_id.add(item[4])
                        searches_dict[item[5]] += 1
                    else:
                        continue

        if os.listdir(path='.\ExtractArchive\searches') == []:
            new_file = open('.\ExtractArchive\searches' + '\\' + sity + '.tsv', 'w', encoding='utf-8')
            for key in searches_dict.keys():
                new_file.write(key + '\t' + str(searches_dict[key]) + '\n')
            new_file.close()
        else:
            new_file = open('.\ExtractArchive\searches' + '\\' + sity + '.tsv', 'w', encoding='utf-8')
            for key in searches_dict.keys():
                new_file.write(key + '\t' + str(searches_dict[key]) + '\n')
            new_file.close()


if __name__ == '__main__':
    # os.chdir('C:/Users/2K_Mefis_Try/PycharmProjects/home_work')
    dirsPathesList = chech_dirs_tree(MyPath)
    pprint(dirsPathesList)
    print(lines)
    for i in dirsPathesList:
        for j in i[1]:
            f = read_file(i, j)
            takes_Words_in_lines2 = add_file_to_list(f)
            f.close()
    printing(takes_Words_in_lines2)
    print(len(takes_Words_in_lines2))
    print(create_files(takes_Words_in_lines2))
