# Blackboard Submission Number: 19726b6d-5e84-4a6b-b58a-c2025c60d97c
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     11/06/2018


# PROBLEM:
# Problem 1 – Remove Odds or Evens (Textbook-problem 17, chapter 8, page 417)
# a) Write a function that takes a list of integers as an argument, removes even numbers from the list, and
# returns the modified list.
# b) Write a function that takes a list of integers as an argument, removes odd numbers from the list, and
# returns the modified list.
# c) Write a function that takes a list of integers and a Boolean as arguments. If the Boolean is True, the
# function removes odd numbers from the list; otherwise, evens are removed. The function returns the
# modified list.

# GIVEN:
# Unittest will allow for testing of the functions.
# dividing by 2 and giving a remainder of 0 will show the number is even
# dividing by 2 and the remainder not being 0 will show the number is odd
# a boolean value is true or false
# to make functions more robust:
#     tuples and list can be iterated through as a list
#     if a string is iterated through it will include punctuation and white space remove the allowance of string in function
#     a integer is not a float or a string remove allowance of these in the list
#     remove the allowance of non boolean values for the boolean parameter


# ANALYSIS:
#    Input: A list or tuple of integers and a True boolean expression or value
#    Output: A new list containing only the even numbers from the input list
#
#    Input: A list or tuple of integers and a False boolean expression or value
#    Output: A new list containing only the odd numbers from the input list
#
#    Input: A list of integers and a non boolean value or expression
#    Output: In proper expression
#    return: -1
#
#    Input: A list or a tuple that include non-integers and a True or False boolean value or expression
#    Output: In proper expression
#    return: -1
#
#    Input: Anything but a list or a tuple and a True or False boolean value or expression
#    Output: In proper expression
#    return: -1


# METHOD/ALGORITHM:
# import unit test to test function
# define function to remove even numbers
#     create new empty list
#     check to makes sure integer_list is a list or tuple
#     iterate through list
#     check to make sure list contains only integers
#     check if even
#     if not even add to new list
#     return -1 if error
#     return new list
# define function to remove odd numbers
#     create new empty list
#     check to makes sure integer_list is a list or tuple
#     iterate through list
#     check to make sure list contains only integers
#     if 0 is in list skip over 0
#     check if even
#     if even add to new list
#     return -1 if error
#     return new list
# define function to remove even or odd based on boolean value
#     check if boolean_value is a boolean_value
#     if boolean_value is true use remove_odd function
#     else use remove_even function
#     return -1 if error
#     return new list
# test function


# TEST CASES:
#    Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True
#    return: [2, 4, 6, 8, 10]
#
#    Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False
#    return: [1, 3, 5, 7, 9]
#
#    Input: (92, 23, 57, 66, 84, 75, 16, 33, 48, 99, 100), True
#    return: [92, 66, 84, 16, 48, 100]
#
#    Input: (92, 23, 57, 66, 84, 75, 16, 33, 48, 99, 100), False
#    return: [23, 57, 75, 33, 99]
#
#    Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1
#    Output: "Improper Input
#    return: -1
#
#    Input: [0, 1, 2, 3, 4, 5, 6.5, 7, 8, 9, 10], True
#    Output: "Improper Input
#    return: -1
#
#    Input: "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10", False
#    Output: "Improper Input
#    return: -1


# PROGRAM:
import unittest


def remove_even(integer_list):  # define function to remove even numbers
    """ Takes an list of integers and returns a new list without even numbers.
        If the list does not contain only integers -1 is returned.
        If integer_list is not a list or a tuple -1 is returned."""
    new_list = []  # create new empty list
    try:
        if not (type(integer_list) == list or type(integer_list) == tuple):  # check to makes sure integer_list is a list or tuple
            raise ValueError
        for i in integer_list:  # iterate through list
            if type(i) != int:  # check to make sure list contains only integers
                raise ValueError
            if i % 2 != 0:  # check if even
                new_list.append(i)  # if not even add to new list
        return new_list  # return new list
    except ValueError:
        return -1


def remove_odd(integer_list):  # define function to remove odd numbers
    """ Takes a list of integers and returns a new list without odd numbers.
        If the list does not contain only integers -1 is returned.
        If integer_list is not a list or a tuple -1 is returned."""
    new_list = []  # create new empty list
    try:
        if not (type(integer_list) == list or type(integer_list) == tuple):  # check to makes sure integer_list is a list or tuple
            raise ValueError
        for i in integer_list:  # iterate through list
            if type(i) != int:  # check to make sure list contains only integers
                raise ValueError
            if i == 0:  # if 0 is in list skip over 0
                pass
            elif i % 2 == 0:  # check if even
                new_list.append(i)  # if even add to new list
        return new_list  # return new list
    except ValueError:
        return -1


def even_or_odd_remove(integer_list, boolean_value):  # define function to remove even or odd based on boolean value
    """ Takes an list of integers and a value from a boolean expression.
        If the value is True remove_odd() function is used and a new list of even numbers is returned.
        If the value is False remove_even() function is used and a new list of odd numbers is returned.
        If integer_list does not contain only integers -1 is returned.
        If integer_list is not a list or a tuple -1 is returned.
        If boolean_value is not a boolean value -1 is returned."""
    if type(boolean_value) == bool:  # check if boolean_value is a boolean_value
        if boolean_value:  # if boolean_value is true use remove_odd function
            new_list = remove_odd(integer_list)
        else:  # else use remove_even function
            new_list = remove_even(integer_list)
    else:
        new_list = -1
    if new_list == -1:
        print("even_or_odd_remove function has Improper Input")
    return new_list  # return new list


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_0(self):
        self.assertEqual(even_or_odd_remove([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True), [2, 4, 6, 8, 10])

    def test_number_1(self):
        self.assertEqual(even_or_odd_remove([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False), [1, 3, 5, 7, 9])

    def test_number_2(self):
        self.assertEqual(even_or_odd_remove((92, 23, 57, 66, 84, 75, 16, 33, 48, 99, 100), True), [92, 66, 84, 16, 48, 100])

    def test_number_3(self):
        self.assertEqual(even_or_odd_remove((92, 23, 57, 66, 84, 75, 16, 33, 48, 99, 100), False), [23, 57, 75, 33, 99])

    def test_number_4(self):
        self.assertEqual(even_or_odd_remove([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), -1)

    def test_number_5(self):
        self.assertEqual(even_or_odd_remove([0, 1, 2, 3, 4, 5, 6.5, 7, 8, 9, 10], True), -1)

    def test_number_6(self):
        self.assertEqual(even_or_odd_remove("0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10", False), -1)


if __name__ == '__main__':
    unittest.main()

input()
