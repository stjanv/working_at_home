from pprint import pprint
import os

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
# # searching_file_log.close()

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


def write_file(toWrite):
    pass


def add_file_to_list(this_file):
    takes_Words_in_lines = []
    takes_lines = this_file.readlines()
    for word in takes_lines:
        takes_Words_in_lines.append(word.split('\t'))

    return takes_Words_in_lines

def create_log_file_with_searches(file_log): #file_log это массив строк в прочтенном файле
    log_file_searches={}
    searches=[]
    # count1=0
    # count2=0
    for record_index in range(len(file_log)):
        # count1+=1
        if file_log[record_index][5] in log_file_searches:
            log_file_searches[file_log[record_index][5]]+=1
        else:
            log_file_searches[file_log[record_index][5]]=1
    for key,arg in log_file_searches.items():
        if arg == 1:
            # count2+=1
            searches.append(key)

    return searches


def count_searches(file_log,searches):
    for jter in file_log:
        for jjter in searches:
            if jjter == jter[5]:




if __name__ == '__main__':
    dirsPathesList = chech_dirs_tree(MyPath)
    pprint(dirsPathesList)
    print(lines)
    filesNamesAdnTheirPathesInDirs = chech_My_dir_for_files(dirsPathesList)
    pprint(filesNamesAdnTheirPathesInDirs)
    print(lines)
    file_name_and_path = take_file_name_and_path(filesNamesAdnTheirPathesInDirs, 0)
    pprint(file_name_and_path)
    print(lines)
    f = read_file(file_name_and_path)
    takes_Words_in_lines = add_file_to_list(f)
    file_close(f)
    #printing(takes_Words_in_lines)
    log_file_searches=create_log_file_with_searches(takes_Words_in_lines)
    searches=log_file_searches

    print(lines)
