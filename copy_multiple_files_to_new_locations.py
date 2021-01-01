import os
from itertools import islice
import argparse

##files_list = 'NTMs_Available.txt'
##files_path = 'D:/Skyline/NTMs/ALL_Mycobcaterium_Species/Mycobacterium'
##location = 'D:/Skyline/NTMs/Final_NTMs/FASTA/'


parser = argparse.ArgumentParser(description='Copy multiple files to the location of interest.', add_help=True)

parser.add_argument('files_list', metavar='-F', type=str, nargs='+', help='A .txt (text) file with a list of all the files to be copied')

parser.add_argument('file_location', metavar='-FL', type=str, nargs='+', help='Location of files from which the files have to be copied')

parser.add_argument('copy_location', metavar='-CL', type=str, nargs='+', help='Location to which all the files have to be copied')

args = parser.parse_args()

def copy_multiple_files(files_list, files_path, location):
    with open(files_list) as infile:
        files = [i.split('\t')[1] for i in islice(infile, 1, None)]
    ##    files_final = '\n'.join(fastas for fastas in os.listdir(files_path) for f in files if f == fastas)
        files_final = [fastas for fastas in os.listdir(files_path) for f in files if f == fastas]
        for fl in files_final:
            infile_path = files_path + '/' + fl
            cmd = 'cp ' + infile_path + ' ' + location
            os.system(cmd)

copy_files = copy_multiple_files(args.files_list[0], args.file_location[0], args.copy_location[0])

## Usage ##
##python copy_multiple_files_to_new_locations.py NTMs_Available.txt D:\Skyline\NTMs\ALL_Mycobcaterium_Species D:\Skyline\NTMs\Final_NTMs\FASTA\
