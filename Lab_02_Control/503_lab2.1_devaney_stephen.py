# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     09/11/2018

# PROBLEM:
#        Write a program that prompts for an integer and prints the integer, but if something other than an
#        integer is input, the program keeps asking for an integer.

# GIVEN:
#        an integer is a whole number
#        a float is not an integer
#        a letter is not an integer
#        a fraction that does not equal a whole number is not an integer

# ANALYSIS:
#        Input: A integer
#        Output: Prints the integer
#        Input: A float
#        Output: "Error: try again. Input an integer: "
#        Input: A Letter
#        Output: "Error: try again. Input an integer: "


# METHOD/ALGORITHM:
#        User input number
#        Limit user input to be integer
#        Print the integer

# TEST CASES:
#        Test Case 1
#        Input: 4a
#        Output: Error: TRY AGAIN. Input an Integer:

#        Test Case 2
#        Input: 2.5
#        Output: Error: TRY AGAIN. Input an Integer:

#        Test Case 3
#        Input: abc
#        Output: Error: TRY AGAIN. Input an Integer:

#        Test Case 4
#        Input: 5/2
#        Output: Error: TRY AGAIN. Input an Integer:

#        Test Case 5
#        Input: 123
#        Output: The Integer is 123

#        Test Case 6
#        Input: -123
#        Output: The Integer is -123


# PROGRAM:
# Basic program setup
print('Enter a number to find out if it is an integer:')
#    User inputs a number:
num = input('Input an integer: ')

#    Limit user input to be integer
while not(num.lstrip('-').isdigit()):
    num = input('Error: TRY AGAIN. Input an Integer: ')

#    Print the integer
print('The Integer is', num)
input()
