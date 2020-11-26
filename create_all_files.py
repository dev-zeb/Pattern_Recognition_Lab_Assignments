import pandas as pd
import numpy as np
import os
import re

# Following code block is to create the special files
print("Creating Special Files...")
dir_files = os.listdir("./")
regex = r".+Gpick_.{0,6}\.txt"
# Regex explanation
# Starting with atleast one character, then 'Gpick_',
# Then any chararcter occuring upto 6 characters, ending with '.txt'
for files in dir_files:
    result = re.search(regex, files)
    if result != None:
        #print(files)
        old_file = open(files)
        file_special = files[:-4]+"_special.txt"
        #print(file_special)
        new_file = open(file_special, 'w')  # Creates the file
        line = old_file.readline()
        while line:
            if line[0] == '>':
                line = line.strip('\n') + '|1|training\n'
            new_file.write(line)
            line = old_file.readline()
        old_file.close()
        new_file.close()
print("Special Files Created")

# Following code block is to execute the feature commands
print("Executing The Feature Commands...")
cmd_file = open("1.Commands.txt")
cmd = cmd_file.readline() # Extracting the commands from the "1.Command.txt" file
cmd_line = "" # But the command has to be modified and concatenated with the directory changing command
count = 0
while cmd:
    if cmd[0] != '#':
        cmd_line = "cd D:\\A1\\iLearn-master &" + cmd[cmd.index(':')+1:].strip('\n')  # The command to be run
        #print(cmd_line)
        os.system(cmd_line) # Running the command line code to create the .csv file
        #count += 1
    cmd = cmd_file.readline()
#print(count)
print("Feature Commands Executed")

# Following block is to create the .npy files
print("Creating The .npy Files...")
regex = r".*\.csv"
dir_files = os.listdir('./')
count = 0
for files in dir_files:
    result = re.search(regex, files)
    if result != None:
        ds = pd.read_csv(files, header=None)
        # Removing the first column & converting to np-array
        X = ds.to_numpy()[:, 1:]
        # To check that 1st column is removed or not, uncomment the following 2 lines
        #print(ds.shape)
        #print(X.shape)
        # Saving the data of X into .npy file
        npy = files[:-4]+".npy"
        print(npy)
        np.save(npy, X)
        #X = np.load(npy, allow_pickle=True)  # Loading the saved file
        '''
        if X.shape[1] == 0:
            print(files, "with 0 columns", X.shape)
            count += 1
        '''
        count += 1
print(count)
print("All .npy Files Created")
"""
file_list = os.listdir('adnantest')
#os.mkdir('XYZ')

for files in file_list:
    file_info = files.split('.')
    print(file_info[0])
    dataset = pd.read_csv(f"adnantest/{files}",header=None)
    X = dataset.to_numpy()[:,:]
    np.save(f"XYZ/{file_info[0]}.npy", X)
"""
# If we need to delete all the .npy files, uncomment the following block
'''
regex = r".*\.npy"
dir_files = os.listdir('./')
count = 0
cmd = ""
for files in dir_files:
    result = re.search(regex, files)
    if result != None:
        print(files+" is Deleted")
        cmd = "del " + files
        os.system(cmd)
        count += 1
print(count)
'''

"""
# Kmer
1: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --kmer 1 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_kmr1.csv
2: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --kmer 2 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_kmr2.csv
3: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --kmer 3 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_kmr3.csv
4: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --kmer 4 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_kmr4.csv
1: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --kmer 1 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_kmr1.csv
2: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --kmer 2 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_kmr2.csv
3: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --kmer 3 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_kmr3.csv
4: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --kmer 4 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_kmr4.csv
1: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --kmer 1 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_kmr1.csv
2: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --kmer 2 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_kmr2.csv
3: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --kmer 3 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_kmr3.csv
4: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --kmer 4 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_kmr4.csv
1: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --kmer 1 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_kmr1.csv
2: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --kmer 2 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_kmr2.csv
3: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --kmer 3 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_kmr3.csv
4: python descnucleotide/Kmer.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --kmer 4 --normalize --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_kmr4.csv
# ENAC
5:  python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --slwindow 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_ENAC5.csv
10: python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --slwindow 10 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_ENAC10.csv
5:  python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --slwindow 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_ENAC5.csv
10: python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --slwindow 10 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_ENAC10.csv
5:  python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --slwindow 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_ENAC5.csv
10: python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --slwindow 10 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_ENAC10.csv
5:  python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --slwindow 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_ENAC5.csv
10: python descnucleotide/ENAC.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --slwindow 10 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_ENAC10.csv
# Binary
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --method binary --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_binary.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --method binary --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_binary.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --method binary --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_binary.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --method binary --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_binary.csv
# CKSNAP
1: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --gap 1 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_CKSNAP1.csv
3: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --gap 3 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_CKSNAP3.csv
5: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --gap 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_CKSNAP5.csv
7: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --gap 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_CKSNAP7.csv
1: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --gap 1 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_CKSNAP1.csv
3: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --gap 3 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_CKSNAP3.csv
5: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --gap 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_CKSNAP5.csv
7: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --gap 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_CKSNAP7.csv
1: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --gap 1 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_CKSNAP1.csv
3: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --gap 3 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_CKSNAP3.csv
5: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --gap 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_CKSNAP5.csv
7: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --gap 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_CKSNAP7.csv
1: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --gap 1 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_CKSNAP1.csv
3: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --gap 3 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_CKSNAP3.csv
5: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --gap 5 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_CKSNAP5.csv
7: python descnucleotide/CKSNAP.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --gap 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_CKSNAP7.csv
# ANF
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --method ANF --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_ANF.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --method ANF --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_ANF.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --method ANF --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_ANF.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --method ANF --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_ANF.csv
# EIIP
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --method EIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_EIIP.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --method EIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_EIIP.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --method EIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_EIIP.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --method EIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_EIIP.csv
# PseEIIP
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --method PseEIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_PseEIIP.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --method PseEIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_PseEIIP.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --method PseEIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_PseEIIP.csv
1: python iLearn-nucleotide-basic.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --method PseEIIP --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_PseEIIP.csv
# DAC
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --method DAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_DAC.csv
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --method DAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_DAC.csv
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --method DAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_DAC.csv
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --method DAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_DAC.csv
# TAC
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_train_special.txt --method TAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_train_TAC.csv
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\NGpick_test_special.txt --method TAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\NGpick_test_TAC.csv
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_train_special.txt --method TAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_train_TAC.csv
1: python iLearn-nucleotide-acc.py --file D:\\A1\\Dataset\\Datasets_2\\PGpick_test_special.txt --method TAC --type DNA --lag 7 --format csv --out D:\\A1\\Dataset\\Datasets_2\\Assignment_1\\PGpick_test_TAC.csv

"""
