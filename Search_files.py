# -*- coding: utf-8 -*-
import os
from os import path
import sys
from datetime import date

today = date.today()
dt = today.strftime("%m%d%y")

def pep_number(file):
    pep_num = {}
    with open(file) as f:
        for i in f:
            pep_num[i] = 1

    total_num = len(pep_num)
    return total_num

def search_files(inpath, search_file_name, outpath):
    present = {}
    not_present = {}
    for list_dir in os.listdir(inpath):
        if os.path.isdir(inpath + '/' +list_dir):
            for files in os.listdir(inpath + '/' +list_dir):
                path = list_dir + '/' + list_dir + search_file_name
                in_path = inpath + '/' + list_dir + '/' + list_dir + search_file_name
                if os.path.exists(inpath + '/' + list_dir +'/'+ list_dir + search_file_name):
                    counts = pep_number(in_path)
                    path_count = path + '/' + str(counts)
                    if list_dir not in present:
                        present[path_count] = [list_dir]

                    else:
                        present[path_count].append(list_dir)

                else:
                    if list_dir not in not_present:
                        not_present[path] = [list_dir]
                    else:
                        not_present[path].append(list_dir)

    write1 = open(outpath + '/' + 'Directories_without_file' + '_' + dt + '.txt', 'w')
    for k, v in not_present.items():
        a = k.encode('utf-8')
        ab = str(a).replace("b'", '').replace("'", '')
        #print (len(ab.split('/')))
        cl = ''
        for l in range(len(ab.split('/'))):
            cl = cl + '\t' + ab.split('/')[l]
        write1.write(cl + '\n')
        
    write1.close()

    write2 = open(outpath + '/' + 'Directories_with_file' + '_' + dt + '.txt', 'w')
    for k, v in present.items():
        a = k.encode('utf-8')
        ab = str(a).replace("b'", '').replace("'", '')
        #print (len(ab.split('/')))
        cl = ''
        for l in range(len(ab.split('/'))):
            cl = cl + '\t' + ab.split('/')[l]
        write2.write(cl + '\n')
        
    write2.close()
                 
if __name__== "__main__":
    search_files(sys.argv[1], sys.argv[2], sys.argv[3])

##inpath = 'D:/Skyline/NTMs/NTMs_In_silico_Peptides/'
##search_file_name = '_DeepMSPeptide_Predictions.txt'
##outpath = 'D:/Skyline/NTMs/'
