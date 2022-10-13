# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     09/18/2018

# PROBLEM:
#    Write a program that asks user input two positive integers and prints out its greatest common divisor.

# GIVEN:
#    Input integers from two users
#    Divisors have a remainder of zero

# ANALYSIS
#    Input: two postive integers
#    Output: list of divisors and greatest common divisor

#    Input: any negative integers
#    Output: "Error: try again. Please input an integer greater than 0: "

# METHOD/ALGORITHM:
#    Basic Program Setup
#    Input users first integer:
#    Input users first integer:
#    Find and print all divisors for first input
#    Find and print all divisors for second input
#    Find the Greatest Common Divisor and print it
#    Create a would you like to continue statement for the loop

# TEST CASES:
#        Test Case 1:
#        Input: -1
#        Output: "Error: TRY AGAIN. Please input your first integer that is greater than 0:"

#        Test Case 2:
#        Input: abc
#        Output: "Error: TRY AGAIN. Please input your first integer that is greater than 0:"


#        Test Case 3:
#        Input: 54
#        Input: 5.5
#        Output: "Error: TRY AGAIN. Please input your second integer that is greater than 0:"


#        Test Case 4:
#        Input: 54
#        Input: 24
#        Output: The divisors for 54 are: 1, 2, 3, 6, 9, 18, 27, 54
#        Output: The divisors for 24 are: 1, 2, 3, 4, 6, 8, 12, 24
#        Output: The greatest common divisor is: 6
#        Output: Would you like to continue (y/n):
#        Input: y
#        Output: Please input your first integer that is greater than 0:

#        Test Case 5:
#        Input: 125
#        Input: 50
#        Output: The divisors for 125 are: 1, 5, 25, 125
#        Output: The divisors for 50 are: 1, 2, 5, 10, 25, 50
#        Output: The greatest common divisor is: 25
#        Output: Would you like to continue (y/n):
#        Input: a
#        Output: "Error: TRY AGAIN. Would you like to continue (y/n):"
#        Input: 1
#        Output: "Error: TRY AGAIN. Would you like to continue (y/n):"
#        Input: N
#        Output: Program Ends

# PROGRAM:
# Basic Program Setup
print("Input two positive integers to find all of the divisors of both integers,")
print("as well as the greatest common divisor between both integers.")
print()
print('At anytime if you wish to quit please type "exit".')
print()
print()
done = False
while not done:

    # Input users first integer:
    user_int_a = input("Please input your first 1st that is greater than 0 and less than 10,000,000: ")
    while not(user_int_a.isdigit()) or int(user_int_a) < 1 or int(user_int_a) > 10000000:
        if user_int_a == "quit" or user_int_a == "exit":
            done = True
            break
        else:
            user_int_a = input("Error: TRY AGAIN. Please input your 1st integer that is greater than 0 and less than 10,000,000: ")
    if done:
        break
    user_int_a = int(user_int_a)

# Input users second integer:
    user_int_b = input("Please input your 2nd integer that is greater than 0 and less than 10,000,000: ")
    while not(user_int_b.isdigit()) or int(user_int_b) < 1 or int(user_int_b) > 10000000:
        if user_int_b == "quit" or user_int_b == "exit":
            done = True
            break
        else:
            user_int_b = input("Error: TRY AGAIN. Please input your 2nd integer that is greater than 0 and less than 10,000,000: ")
    if done:
        break
    user_int_b = int(user_int_b)

# Find and print all divisors for first input
    print()
    print("The divisors for", user_int_a, "are: ", end="")
    for i in range(1, user_int_a+1):
        if user_int_a % i == 0:
            print(i, end=" " if i == user_int_a else ", ")
    print()
    print()

# Find and print all divisors for second input
    print("The divisors for", user_int_b, "are: ", end="")
    for i in range(1, user_int_b+1):
        if user_int_b % i == 0:
            print(i, end=" " if i == user_int_b else ", ")
    print()
    print()

# Find the Greatest Common Divisor and print it
    gcd = 1
    for i in range(2, user_int_a+1):
        if user_int_a % i == 0 and user_int_b % i == 0:
            if gcd < i:
                gcd = i
    print("The greatest common divisor is:", gcd)
    print()

# create a would you like to continue statement for the loop
    done = input("Would you like to continue please answer with y or n: ")
    while not (done == "Y" or done == "y" or done == "n" or done == "N" or done == "quit" or done == "exit"):
        done = input("Error: Would you like to continue please answer with y or n: ")
    if done == "Y" or done == "y":
        done = False
    elif done == "N" or done == "n" or done == "quit" or done == "exit":
        done = True
print("You have quit have a nice day!")
input()
