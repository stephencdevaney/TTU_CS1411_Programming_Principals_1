# Blackboard Submission Number: 15ea6d67-38e5-4324-b7d7-6cc6059a7d03
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     10/02/2018


# PROBLEM:
# Write a program that prompts the user to input a password and checks if the password is valid. If the
# password is valid, print a confirmation statement and end the program. If it is not, print a statement the
# the password is not valid and ask the user to re-enter the password until valid one found.


# GIVEN:
# The password must be at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, one upper case letter, and one number.


# ANALYSIS
# Input:  Password between six and 20 characters that contains at least one lowercase character, one uppercase character,
#        and one digit.
# Output: vaild password statement and end program statement
#
# Input:  Password between that is not between 6 and 20 characters
# Output: invaild password statement and reinput for password
#
# Input:  Password between that is between 6 and 20 characters and does not have at least one lower case character, one
#        uppercase character, and one digit
# Output: invaild password statement and reinput for password


# METHOD/ALGORITHM:
# Introduce the program
# Create basic setup for program
# Input user's chosen password
# Check password's length
# Create setup for check of other conditions
# check to see if password has a lowercase character
# check to see if password has a uppercase character
# check to see if password has a digit
# if all conditions are met print valid password message
# if all conditions are not met reset loop and print invalid password message
# verify natural exit of the loop


# TEST CASES:
# Input:   Bad94
# Output:  Your password is invalid. Try Again.
#
# Input:   BADPASSWORD89
# Output:  Your password is invalid. Try Again.
#
# Input:   Badpassword
# Output:  Your password is invalid. Try Again.
#
# Input:   badpassword45
# Output:  Your password is invalid. Try Again.
#
# Input:   /!_/!_
# Output:  Your password is invalid. Try Again.
#
# Input:   Thi5_Pa55phra5e_I5_Way_T00_L0ng
# Output:  Your password is invalid. Try Again.
#
# Input:   AG00dPa55w0rd
# Output:  Your password is valid.
#         Have a nice day!
#
# Input:   7hi5_Gr3a7_Pa55w0rd!
# Output:  Your password is valid.
#         Have a nice day!


# #PROGRAM:
# Introduce the program
print("Please create a password that is between 6 and 20 characters. The password must also have at least")
print("one uppercase character, one lowercase character, and one digit.")
print()

# Basic setup for the program
password_length = False
password_lowercase = False
password_uppercase = False
password_digit = False
while not(password_length and password_lowercase and password_uppercase and password_digit):

    # Input user's chosen password
    user_password = input("Please input a valid password: ")

    # Check password's length
    if 6 <= len(user_password) <= 20:
        password_length = True

    # Setup for check of other conditions
    for i in range(0, len(user_password)):
        user_character = user_password[i]

        # check to see if password has a lowercase character
        if user_character.islower():
            password_lowercase = True

        # check to see if password has a uppercase character
        if user_character.isupper():
            password_uppercase = True

        # check to see if password has a digit
        if user_character.isdigit():
            password_digit = True

    # if all conditions are met print valid password message
    if password_length and password_lowercase and password_uppercase and password_digit:
        print("Your password is valid.")

    # if all conditions are not met reset loop and print invalid password message
    else:
        password_length = False
        password_lowercase = False
        password_uppercase = False
        password_digit = False
        print("Your password is invalid. Try Again.")

# verify natural exit of the loop
print("Have a nice day!")
input()
