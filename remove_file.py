## files with common search terms can be removed in multiple directories
import os
import sys

def remove_files(inpath, file_name):
    for list_dir in os.listdir(inpath):
        if os.path.isdir(inpath + '/' + list_dir):       
            for list_files in os.listdir(inpath + '/' + list_dir):
                if file_name in list_files:
                    #for DMP_input in os.listdir(list_dir + '/'+list_files):
                    if os.path.isfile(inpath + '/' + list_dir + '/'+list_files):
                        print (inpath + '/' + list_dir + '/'+list_files)
                        os.remove(inpath + '/' + list_dir + '/'+list_files)

if __name__== "__main__":
    remove_files(sys.argv[1], sys.argv[2])

# python remove_file.py D:/Skyline/NTMs/NTMs_In_silico_Peptides/ _Unique_Peptides.txt

