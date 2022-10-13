# Blackboard Submission Number: cc289516-df2c-4f5b-be9e-6024f373f04c
# Blackboard Submission Number: 44e25310-fb5b-42ed-81cd-60cbd9496f3c
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     11/20/2018


# PROBLEM:
# Problem 1 : File copy – Text book: Programming project 2, chapter 14, page 685
# All operating systems have commands that will create a copy of a file. In this exercise, you are to
# create a program that will make an exact copy of a file. Provide the following capabilities:
# - Copy only files that end with a “.txt” extension. Generate an appropriate error if something else is
# specified.
# - Using the os module, check whether the source file exists.
# - Using the os module, check whether the destination file exists. If so, ask the user if he or she wants to
# overwrite it.
# - If no paths are specified, assume that the file is in the current folder (directory). Otherwise, use the os
# module to separate the path from the file name. If a path is specified for the destination file, check
# whether the path exists – otherwise, generate an error.


# GIVEN:
# OS module
# File must end with .txt extension
# Source file and path must exist for copy to be successful
# Destination path must exist for copy to be successful
# If destination file already exist old file will be overwritten unless user is prompted and user changes their mind
# current directory is where the program is located
# path must be split from file name to be able to check it if os.path.split() is use a tuple will be created containing both
# can make an exact copy of a text file by reading each line and printing line to new file (carriage returns must be stripped)


# ANALYSIS:
#    Input: 2 proper file paths, and name. The source exist and either the destination exist or user answer they want to overwrite the file
#    Output: Newly copy file and print Copy is successful
#
#    Input: a improper file path or name. Or the source exist. or the destination does exist and the user answered they don't want to over write the file
#    Output: print Copy Failed with the proper generated errors


# METHOD/ALGORITHM:
# Define check for .txt function
#     check if file name ends with .txt
#     return True if it does
#     else raise error and return false
# Define check source file function
#     check if file exist
#     return True if it does
#     else raise error and return false
# Define check destination file function
#     Check to see if file already exists
#     If file already exist ask user if they want to overwrite the file
#     If answer is no return False
#     If answer is yes return True
#     Return True if file does not exists
# Define check path function
#     Split file name from file path
#     check to see if file path is included in file list
#     if file path does not exist in the list set file path to current directory
#     check to see if file path exist on the drive
#     if it does return True
#     else raise error and return false
# Define Main function
#     Get users input for source file
#     use functions to check source file
#     Get users input for destination file
#     use functions to check destination file
#     If all conditions are met continue with program
#     Open source file for reading
#     Open destination file for writing
#     read individual lines
#     strip carriage return
#     copy each line to new file
#     else return "Copy has failed"


# TEST CASES:
#    Input: results.txt
#    Input: results2.txt
#    Output: Copy is successful
#
#    Input: C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\devaney_poker_possibilities.txt
#    Input: devaney_poker_possibilities.txt
#    Output: Copy is successful
#
#    Input: 503_lab9_devaney_stephen.py
#    Output: Error file 503_Lab9_devaney_stephen.py does not end with .txt.
#    Output: Copy has failed
#
#    Input: C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\devaney_poker_possibilitiess.txt
#    Output: Error file, C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\devaney_poker_possibilitiess.txt does not exist.
#    Output: Copy has failed
#
#    Input:C:\\Users\steph\.PyCharmEdu2018.2\config\scratchess\devaney_poker_possibilities.txt
#    Output: File location C:\\Users\steph\.PyCharmEdu2018.2\config\scratchess does not exist
#    Output: Copy has failed
#
#    Input: results.txt
#    Input: C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\results.txt
#    Output: Copy is successful
#
#    Input: results.txt
#    Input: C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\results.txt
#    Output:File already exist would you like to overwrite C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\results.txt Y/N:
#    Input: N
#    Output: Copy has failed
#
#    Input: results.txt
#    Input: C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\results.txt
#    Output:File already exist would you like to overwrite C:\\Users\steph\.PyCharmEdu2018.2\config\scratches\results.txt Y/N:
#    Input: Y
#    Output: Copy has Successful
#
#    Input: results.txt
#    Input: C:\\Users\steph\.PyCharmEdu2018.2\config\scratchess\results.txt
#    Output: File location C:\\Users\steph\.PyCharmEdu2018.2\config\scratchess does not exist
#    Output: Copy has failed
#
#    Input: results.txt
#    Input: 503_lab9_devaney_stephen.py
#    Output: Error file 503_Lab9_devaney_stephen.py does not end with .txt.
#    Output: Copy has failed


# PROGRAM:
import os


def check_txt(file):  # Define check for .txt function
    """Function checks with the source file ends with .txt
       If file name ends with .txt returns True
       If file name does not end with .txt, ""Error file", file, "does not end with .txt."" is printed and returns False"""
    try:
        if file.endswith(".txt"):  # check if file name ends with .txt
            check = True  # return True if it does
        else:
            raise OSError  # else raise error and return false
    except OSError:
        print("Error file", file, "does not end with .txt.")
        check = False
    return check


def check_source(source_file):  # define check source file function
    """Function checks the source file to see if it exists.
       If source file exists the function returns True
       If the source file does not exist "Error file,", source_file, "does not exist." is printed and the function returns False"""
    try:
        if os.path.isfile(source_file):  # check if file exist
            check = True  # return True if it does
        else:
            raise OSError  # else raise error and return false
    except OSError:
        print("Error file,", source_file, "does not exist.")
        check = False
    return check


def check_destination(destination_file):  # Define check destination file function
    """Function checks to see if the destination file already exist.
       If the destination file already exists the function asks the user if they would like to overwrite the file.
       If the user says no False is returned.
       If the user says yes or the file does not exist True is returned."""
    check = True  # Return True if file does not exists
    if os.path.isfile(destination_file):  # Check to see if file already exists
        print("File already exist would you like to overwrite", destination_file)
        answer = input("Y/N: ")
        # If file already exist ask user if they want to overwrite the file
        if answer == "yes" or answer == "y" or answer == "Y" or answer == "Yes" or answer == "YES":
            check = True  # If answer is no return True
        elif answer == "no" or answer == "No" or answer == "NO" or answer == "n" or answer == "N":
            check = False  # If answer is yes return False
        else:
            check_destination(destination_file)
    return check


def check_path(file):  # Define check path function
    """Function checks to see if the location for a specified file exist.
       If the path is not specified the function assumes the location is in the programs directory.
       If the path does not exist the function prints "File location", file_dir, "does not exist" and false is returned
       If the path exist True is returned"""
    file_list = os.path.split(file)  # Split file name from file path
    if file_list[0] == '':  # check to see if file path is included in file list
        file_dir = os.getcwd()  # if file path does not exist in the list set file path to current directory
    else:
        file_dir = file_list[0]
    try:
        if os.path.isdir(file_dir):  # check to see if file path exist on the drive
            check = True  # if it does return True
        else:
            raise OSError  # else raise error and return false
    except OSError:
        check = False
        print("File location", file_dir, "does not exist")
    return check


def main():  # Define Main function
    source = input("Please enter the file source to be copied: ")  # Get users input for source file
    source_check = False
    destination_check = False
    if check_txt(source) and check_path(source) and check_source(source):  # use functions to check source file
        source_check = True
        destination = input("Please enter the file destination to be copied to: ")   # Get users input for destination file
        if check_txt(destination) and check_path(destination) and check_destination(destination):  # use functions to check destination file
            destination_check = True
    if source_check and destination_check:  # If all conditions are met continue with program
        read_file = open(source, 'r')  # Open source file for reading
        write_file = open(destination, 'w')  # Open destination file for writing
#        for l in read_file:  # read individual lines
#            line = l.strip('\n')  # strip carriage return
#            print(line, file=write_file)  # copy each line to new file
        r_file_data = read_file.readlines()
        write_file.writelines(r_file_data)
        read_file.close()
        write_file.close()
        return "Copy is successful"
    else:
        return "Copy has failed"  # else return "Copy has failed"


print(main())
input()
