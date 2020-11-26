import random
import numpy as np
import re
import os

regex_N_test = r"N.*test.*\.npy"
regex_P_test = r"P.*test.*\.npy"
regex_N_train = r"N.*train.*\.npy"
regex_P_train = r"P.*train.*\.npy"

dir_files = os.listdir() # Getting all the file names of the current folder

flag_N_test = 0
flag_N_train = 0
flag_P_test = 0
flag_P_train = 0
index_tracker = {} # The dictionary will track the indexes of each file
#print(type(index_tracker))

low = 0 # To store the lower index of the next feature array
cols = 0 # To store total number of columns in all the files

Y_N_test = []   # To store all the N_test arrays
Y_N_train = []  # To store all the N_train arrays
Y_P_test = []   # To store all the P_test arrays
Y_P_train = []  # To store all the P_train arrays

#---------------------1st level Concatenation---------------------#
for f in dir_files:
    if re.search(regex_N_test, f):
        X = np.load(f, allow_pickle=True) # Loading the .npy file to a np.ndarray
        if flag_N_test == 0:  # If it's the first file, then just store it to the variable Y_N_test
            Y_N_test = X
            # Changing the value of "flag_N_test", so that it doesn't enter this block again
            flag_N_test += 1
        else: # Append the newly loaded np.ndarray to Y_N_test
            Y_N_test = np.append(Y_N_test, X, axis=1) # This line concatenates X to Y_N_test and stores it to Y_N_test
    
    elif re.search(regex_N_train, f):
        # Loading the .npy file to a np.ndarray
        X = np.load(f, allow_pickle=True)
        cols += X.shape[1]  # Adding the number of columns of X
        f = f[f.find('_', 9, -4)+1:-4]
        if flag_N_train == 0:  # If it's the first file, then just store it to the variable Y_N_train
            Y_N_train = X
            index_tracker[f] = (0, X.shape[1]-1)
            low = X.shape[1]
            # Changing the value of "flag_N_train", so that it doesn't enter this block again
            flag_N_train += 1
        else:  # Append the newly loaded np.ndarray to Y_N_train
            # This line concatenates X to Y_N_train and stores it to Y_N_train
            Y_N_train = np.append(Y_N_train, X, axis=1)
            # Keeping track of the indexes of the appended arrays
            index_tracker[f] = (low, low + X.shape[1]-1)
            low = low + X.shape[1]
    elif re.search(regex_P_test, f):
        # Loading the .npy file to a np.ndarray
        X = np.load(f, allow_pickle=True)
        cols += X.shape[1]  # Adding the number of columns of X
        if flag_P_test == 0:  # If it's the first file, then just store it to the variable Y_P_test
            Y_P_test = X
            # Changing the value of "flag_P_test", so that it doesn't enter this block again
            flag_P_test += 1
        else:  # Append the newly loaded np.ndarray to Y_P_test
            # This line concatenates X to Y_P_test and stores it to Y_P_test
            Y_P_test = np.append(Y_P_test, X, axis=1)
            # Keeping track of the indexes of the appended arrays
            
    elif re.search(regex_P_train, f):
        # Loading the .npy file to a np.ndarray
        X = np.load(f, allow_pickle=True)
        cols += X.shape[1]  # Adding the number of columns of X
        f = f[f.find('_', 9, -4)+1:-4]
        if flag_P_train == 0:  # If it's the first file, then just store it to the variable Y_P_train
            Y_P_train = X
            index_tracker[f] = (0, X.shape[1]-1)
            low = X.shape[1]
            # Changing the value of "flag_P_train", so that it doesn't enter this block again
            flag_P_train += 1
        else:  # Append the newly loaded np.ndarray to Y_P_train
            # This line concatenates X to Y_P_train and stores it to Y_P_train
            Y_P_train = np.append(Y_P_train, X, axis=1)
            # Keeping track of the indexes of the appended arrays
            index_tracker[f] = (low, low + X.shape[1]-1)
            low = low + X.shape[1]

if not os.path.isdir("Assignment-2"):
    os.mkdir("Assignment-2")

np.save("Assignment-2/All_N_test.npy", Y_N_test)
np.save("Assignment-2/All_N_train.npy", Y_N_train)
np.save("Assignment-2/All_P_test.npy", Y_P_test)
np.save("Assignment-2/All_P_train.npy", Y_P_train)
np.save("Index_tracker.npy", index_tracker)
new = np.load("Index_tracker.npy", allow_pickle=True).item() # Loading the saved dictionary as a dictionary

# To check the shape of the Y files
print("After the 1st level Concatenation...")
#print(new == index_tracker) # To see if the saved and loaded dictionary are the same(True)
print(index_tracker)
print(Y_N_test.shape)
print(Y_N_train.shape)
print(Y_P_test.shape)
print(Y_P_train.shape)
# To check if all the columns are concatenated or not
#print("Y_N_test: ", Y_N_test.shape[1], "X: ", cols)

#---------------------2nd level Concatenation---------------------#
X_train = np.copy(Y_P_train) # Copying the N_train array to the X_train array
X_train = np.append(X_train, Y_N_train, axis=0) # Now concating the P_train array to the ALll_train array row-wise
#print("Added row no. : ", Y_N_train.shape[0] + Y_P_train.shape[0], "Appended array row no. : ", X_train.shape[0])

X_test = Y_P_test.copy() # Copying the N_test array to the X_train array
X_test = np.append(X_test, Y_N_test, axis=0) # Now concating the P_test array to the ALll_train array row-wise
#print("Added row no. : ", Y_N_test.shape[0] + Y_P_test.shape[0], "Appended array row no. : ", X_test.shape[0])

np.save("Assignment-2/X_test.npy", X_test) # Saving the final concatenated file for testing features as .npy file
np.save("Assignment-2/X_train.npy", X_train) # Saving the final concatenated file for training features as .npy file

# To check the shape of the X files
print("After the 2nd level concatenation...")
print("X_test: ", X_test.shape)
print("X_train: ", X_train.shape)
#--------------------------------------------------------------#
### Creating the label files, y

# Getting the No. of rows of  test cases
P_test_rows = Y_P_test.shape[0] # positive row numbers
N_test_rows = Y_N_test.shape[0] # negative row numbers

# Getting the No. of rows of  test cases
P_train_rows = Y_P_train.shape[0] # positive row numbers
N_train_rows = Y_N_train.shape[0] # negative row numbers

# Giving label as zero(0) for all the rows of y
y_test = np.zeros([(P_test_rows+N_test_rows), 1]) # for test
y_train = np.zeros([(P_train_rows+N_train_rows), 1]) # for train

# Changing the values to 1 for the positive cases of y
y_test[:P_test_rows, :] = 1 # for test
y_train[:P_train_rows, :] = 1 # for train

# Saving the label files// Not needed for this assignment
#np.save("Assignment-2/y_test.npy", y_test) # for test
#np.save("Assignment-2/y_train.npy", y_train) # for train

# To check the shape of the y files
print("After making the y files...")
print("y_test: ", y_test.shape)
print("y_train: ", y_train.shape)
#--------------------------------------------------------------#
# To check no. of ones
#print(np.count_nonzero(y_for_test))
#print(np.count_nonzero(y_for_train))

"""
- These classifiers have to be applied on the datasets
    XGBoost, SVC linear and SVC with RBF kernel, Linear Regression, AdaBoost, Random Forest
- Eval. Metric
    Accuracy, MCC, Sensitivity, Specificity
- Validation dataset : 20% of training dataset
"""
