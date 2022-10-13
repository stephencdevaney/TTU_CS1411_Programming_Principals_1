# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     09/11/2018

# PROBLEM:
# Create a program that prompts for a positive number greater than 2 (check this condition), then keeps taking the
# square root of this number until the square root is less than 2. Print the value each time the square root is taken,
# along with the number of times the operation has been completed.

# GIVEN:
#      The integer must be greater than two
#      An integer is not a letter
#      An integer is not a decimal point

# ANALYSIS
#        Input: A integer great than two
#        Output: Prints the Square Roots until Square Root is less than 2
#        Input: A float
#        Output: "Error: try again. Input an integer greater than 2: "
#        Input: A Letter
#        Output: "Error: try again. Input an integer that is greater than 2: "

# METHOD/ALGORITHM:
#        Basic Setup for program
#        User inputs a number:
#        Limit user input to be integer that is greater than 2:
#        Perform math functions and print the outcome

# TEST CASES:
#        Test Case 1:
#        Input: -5
#        Output: Error: TRY AGAIN. Input an Integer that is greater than 2:

#        Test Case 2:
#        Input: 2
#        Output: Error: TRY AGAIN. Input an Integer that is greater than 2:

#        Test Case 3:
#        Input: 5.5
#        Output: Error: TRY AGAIN. Input an Integer that is greater than 2:

#        Test Case 4:
#        Input: 20
#        Output: 1 :  4.472
#        Output: 2 :  2.115
#        Output: 3 :  1.454

#        Test Case 5:
#        Input: 999
#        Output: 1 :  31.61
#        Output: 2 :  5.622
#        Output: 3 :  2.371
#        Output: 3 :  1.54


# PROGRAM:
#    Basic Setup for program
from math import sqrt
count_num = 0
print('Enter a number to find its square root and the square root of roots received. \
Until the square root is less than 2:')

#    User inputs a number:
user_num = input('Input an Integer that is greater than 2: ')

#    Limit user input to be integer that is greater than 2:
while not(user_num.isdigit()) or int(user_num) < 3:
    user_num = input('Error: TRY AGAIN. Input an Integer that is greater than 2: ')

#        Perform math functions and print the outcome
user_num = float(user_num)
while user_num > 2:
        user_num = sqrt(user_num)
        count_num = count_num + 1
        print(count_num, ':', ' {:.4}'.format(user_num))
input()
