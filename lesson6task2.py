from zipfile import ZipFile
from os import mkdir
import string
import itertools

directory = "ExtractArchive/searches"
try:
    mkdir(directory)
except FileExistsError:
    pass

#
# def read_logs(log_file):
#     takes_Words_in_lines = []
#     takes_lines = log_file.readlines()
#     # pprint(takes_lines)
#     for word in takes_lines:
#         takes_Words_in_lines.append(word.split('\t'))
#
#     return takes_Words_in_lines
#
#
# def printing(takes_Words_in_lines):
#     for lines in takes_Words_in_lines:
#         print(lines)
#     return
#
#
# def searches(takes_Words_in_lines):
#     count = 0
#     searches_result = []
#     for lines in takes_Words_in_lines:
#         for word in lines:
#             if word == 'Texas':
#                 searches_result.append(lines)
#                 # print(lines)
#                 count += 1
#     return searches_result
#
# def take_a_log(searches_sity_list):
#     log_file_found=[]
#     for record_index in range(len(searches_sity_list)):
#         count = 0
#         for i in range(len(searches_sity_list)):
#             if record_index != i:
#                 if searches_sity_list[record_index][4] == searches_sity_list[i][4]:
#                     count += 1
#             else:
#                 continue
#         # print(count)
#         if count == 0:
#             if searches_sity_list[record_index][2] == 'F':
#                 log_file_found.append(searches_sity_list[record_index])
#     return log_file_found
#
# file_log = open('ExtractArchive/lesson6/file_17.txt', 'r', encoding='utf-8')
# takes_Words_in_lines = read_logs(file_log)
# # printing(takes_Words_in_lines)
# # printing(searches(takes_Words_in_lines))
# searches_sity_list = searches(takes_Words_in_lines)
# printing(take_a_log(searches_sity_list))
# take_a_log_for_write=take_a_log(searches_sity_list)
#
# searching_file_log=open('ExtractArchive/searches/Texas.tsv', 'w',encoding='utf-8')
# searching_file_log.writelines(take_a_log_for_write[0][3]+'\t '+str(len(take_a_log_for_write)))
# searching_file_log.close()
# # searching_file_log=open('ExtractArchive/searches/Texas.tsv', 'r',encoding='utf-8')
# # print(searching_file_log.readline())
# # searching_file_log.close(
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
