from pprint import pprint
import os

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


MyPath = '.\ExtractArchive\lesson6'

lines = '=================================================================================================='


def printing(takes_Words_in_lines):
    for lines in takes_Words_in_lines:
        print(lines)
    return


def chech_My_dir_for_files(dirsPathesList):
    filesNamesAdnTheirPathesInDirs = []
    for i in range(len(dirsPathesList)):
        for f in os.listdir(path=dirsPathesList[i]):
            if f.endswith('.txt'):
                filesNamesAdnTheirPathesInDirs.append((f, dirsPathesList[i]))

    return filesNamesAdnTheirPathesInDirs


def chech_dirs_tree(MyPath):
    dirsPathesList = []
    for dirpath, dirnames, files in os.walk(MyPath):
        if os.listdir(dirpath) != []:
            dirsPathesList.append(dirpath)
    return dirsPathesList


def take_file_name_and_path(filesNamesAdnTheirPathesInDirs, FileNumber):
    take_file_name_and_path = filesNamesAdnTheirPathesInDirs[FileNumber]
    return take_file_name_and_path


def read_file(file_name_and_path):
    f = open(file_name_and_path[1] + '\\' + file_name_and_path[0], 'r', encoding='utf-8')
    return f


def file_close(file):
    return file.close()


# def write_file(toWrite):
#     pass


def add_file_to_list(this_file):
    takes_Words_in_lines = []
    takes_lines = this_file.readlines()
    for word in takes_lines:
        takes_Words_in_lines.append(word.split('\t'))

    return takes_Words_in_lines
#
# def create_log_file_with_sities(file_log): #file_log это массив строк в прочтенном файле
#     log_file_searches={}
#     searches=[]
#     # count1=0
#     # count2=0
#     for record_index in range(len(file_log)):
#         # count1+=1
#         if file_log[record_index][5] in log_file_searches:
#             log_file_searches[file_log[record_index][3]]+=1
#         else:
#             log_file_searches[file_log[record_index][3]]=1
#     for key,arg in log_file_searches.items():
#         if arg == 1:
#             # count2+=1
#             searches.append(key)
#
#     return searches


def create_log_file_with_id(file_log):
    n=0
    spisok_search={}
    spisok_id={}
    spisok_id_id=[]
    for i in file_log:
        if i[4] in spisok_id:
            spisok_id[i[4]]+=1
        else:
            spisok_id[i[4]]=1

    for ii in spisok_id:
        if spisok_id[ii]==1:
            spisok_id_id.append(ii)

    for j in file_log:
        if j[5] in spisok_search:
            if j[4] in spisok_id_id:
                spisok_search[j[5]]+=1
        elif j[4] in spisok_id_id :
            spisok_search[j[5]]=1

    for jj in file_log:
        if jj[4] in spisok_id_id:
            if jj[5] in spisok_search:
                new_file = open('.\ExtractArchive\searches' + '\\' + jj[3] + '.tsv', 'a+', encoding='utf-8')
                if jj[5] not in new_file.readlines():
                    new_file.write(jj[5]+'\t'+str(spisok_search[jj[5]])+'\n')
                    file_close(new_file)

    return spisok_search

# def create_file(sities):
#     for ff in sities:
#         for f in os.listdir(path='.\ExtractArchive\searches'):
#             if f!=(ff+'.tsv'):
#                 new_file=open('.\ExtractArchive\searches'+'\\'+ff+'.tsv','w',encoding='utf-8')
#                 file_close(new_file)
#             else:
#                 continue
#     return



if __name__ == '__main__':
    dirsPathesList = chech_dirs_tree(MyPath)
    pprint(dirsPathesList)
    print(lines)
    filesNamesAdnTheirPathesInDirs = chech_My_dir_for_files(dirsPathesList)
    pprint(filesNamesAdnTheirPathesInDirs)
    print(lines)
    for i in range(len(filesNamesAdnTheirPathesInDirs)):
        file_name_and_path = take_file_name_and_path(filesNamesAdnTheirPathesInDirs, i)
        pprint(file_name_and_path)
        print(lines)
        f = read_file(file_name_and_path)
        takes_Words_in_lines = add_file_to_list(f)
        file_close(f)
        #printing(takes_Words_in_lines)
        create_log_file_with_id(takes_Words_in_lines)



    # log_file_searches=create_log_file_with_sities(takes_Words_in_lines)
    # searches=log_file_searches
    # #pprint(searches)
    # create_file(searches)
    # print(lines)
    # pprint(create_log_file_with_id(takes_Words_in_lines))
    # print(lines)