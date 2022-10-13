# Blackboard Submission #: 52db62a9-bcdd-4ea8-b566-39b9942dcc27
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     10/09/2018


# PROBLEM:
# Substring matching is the process of determining whether shorter string (the substring) is contained within a longer
# string. Substring matching plays important roles in the reconstruction of an unknown DNA string from pieces, and in
# searching for interesting substrings within a known DNA string.
#
# Python provides a find (substring, start, end) string method that returns the lowest index (integer) where the
# substring is found in the index range start <= index < end. The start and end arguments are optional, but for this
# exercise we will make them required (you will learn later how to handle optional arguments). If the substring is not
# found, -1 is returned.
#
# Without using the find string method, write a function name multi_find(some_string, sub_string, start, end) that,
# instead of returning one integer index, returns a string that contains zero or more indices separated by commas. In
# this case, the string will contain digits representing the integer indices. If the substring is not found, an empty
# string is returned.


# GIVEN:
# Python's S.find format is string.find(sub[, start[,end]])
# The quote string from pythons S.find function states that it returns the lowest index in S where substring sub
#    is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in
#    slice notation. Return -1 on failure.
# My find function will search for first substring within the main string
# My multi find function will use a loop and my find function to search for remainder of the substrings within the
#    main string
# A defined function still has to be placed in code with to be executed.


# ANALYSIS
# Input: substring within string in the length parameters
# Output: all integer indices where the substring is within the main string
#
# Input: substring within string some in the length parameters some not in the  length parameters
# Output: all integer indices where the substring is within the main string that are within the length parameters
#
# Input: substring not within string
# Output: return empty string will later prints not found statement
#
# Input: substring within string but not in the length parameters
# Output: return empty string will later prints not found statement


# METHOD/ALGORITHM:
# define find function
#    test if substring is in the string, starting from index i
#    return findings
#    if no findings return an empty string
# define multi find function
#    retrieve first index from find function
#    if first index is empty sting return and empty string
#    setup for output
#    use find function to find all substrings in the main string
#    use find function
#    add findings to output
#    return output
# Main Program
#    Receive user input
#    Use multi find function
#    if return from multi_find is an empty string print a no substring statement
#    Would you like to continue statement:


# TEST CASES:
# Input: string: "string", substring: "g", start: 0, end: 3,
# Output: No substring found
#
# Input: string: "this is a test string that tests are done on to make sure it tests it successfully",
# # # # substring: "test", start: 0, end: 1000
# Output: Found substrings at:  10, 27, 61
#
# Input: string: "this is a test string that tests are done on to make sure it tests it successfully",
# # # # substring: "test", start: 26, end: 31
# Output: Found substrings at:
#
# Input: string: "this is a test string that tests are done on to make sure it tests it successfully",
# # # # substring: "t", start: 0, end: 1000
# Output: Found substrings at:  0, 10, 13, 16, 22, 25, 27, 30, 45, 59, 61, 64, 68
#
# Input: string: "", substring: "", start: 0, end: 1000,
# Output: No substring found


# #PROGRAM:
# define find function
def find(string, substring, start, end):
    end_2 = end
    if end > len(string):
        end_2 = len(string)
    if len(substring) > len(string):
        return''
    for i in range(start, end_2):
        # test if substring is in the string, starting from index i
        found = True
        idx = 0
        for t in range(len(substring)):
            if string[i+idx] != substring[t]:
                found = False
                break
            idx = idx + 1
        if found:
            # return findings
            return i
    # if no findings return an empty string
    return ''


# define multi find function
def multi_find(string, substring, start, end):
    # retrieve first index from find function
    first_index = find(string, substring, start, end)
    # if first index is empty sting return and empty string
    if first_index == '':
        output = ''
        return output
    # setup for output
    output = str(first_index) + ', '
    # use find function to find all substrings in the main string
    start = int(first_index)+1
    while start <= end:
        # use find function
        next_index = find(string, substring, start, end)
        if next_index == '':
            break
        start = int(next_index)+1
        # add findings to output
        output += str(next_index) + ', '
    # return output
    return output.rstrip(' ,')


# Main Program
done = False
while not done:
    # Receive user input
    user_string = input("Please enter a string: ")
    user_substring = input("Please enter a substring: ")
    user_start = int(input("Please enter a starting index (integers only): "))
    user_end = int(input("Please enter a ending index integers only): "))
    # Use new multi find function
    user_found_substring = multi_find(user_string, user_substring, user_start, user_end)
    # if return from multi_find is an empty string print a no substring statement
    if user_found_substring == '':
        print("No substring found ")
    else:
        print("Found substrings at: ", user_found_substring)
    # Would you like to continue statement:
    done = input("Would you like to continue please answer with y or n: ")
    while not (done == "Y" or done == "y" or done == "n" or done == "N"):
        done = input("Error: Would you like to continue please answer with y or n: ")
    if done == "Y" or done == "y":
        done = False
    elif done == "N" or done == "n":
        done = True
print("You have quit have a wonderful day!")
