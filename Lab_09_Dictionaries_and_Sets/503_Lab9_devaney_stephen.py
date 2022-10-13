# Blackboard Submission Number: 83177280-4903-43c0-84b1-d92b8a459be2
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     11/13/2018


# PROBLEM:
# Problem 1 (Problem 22, text book, chapter 9, page 479)
# Write a function that takes as an argument an unordered list of integers and return dictionary of the
# three integers with the highest count and their counts. That is, key is integer; value is its count. In case
# of a tie, either value can be returned.
# Problem 2
# Write a function that takes a dictionary and an integer as arguments and return all keys of the dictionary
# whose values equal to the integer.

# GIVEN:
# P1.) Set new integers in the list as keys of the dictionary while setting value to one
#     If keys is already in dictionary increase value you to maintain the count
# P2.) The integer needs to equal the value not the key
#     The keys need to be returned
#     Use for loop to iterate through dict
#     Use items method to get both keys and values


# ANALYSIS:
#    Input_P1: list of integers
#    Output_P1: dict of 3 integers with highest count and their count
#
#    Input_P1: improper types in parameters
#    Output_P1: -1
#
#    Input_P1: a dict and a integers
#    Output_P1: returns all keys whose values equal the integer
#
#    Input_P2: improper types in parameters
#    Output_P2: -1


# METHOD/ALGORITHM:
# P1.) Define highest count function with a integer list as a parameter
#      Check to see if parameters types are correct
#      Create empty counting dictionary
#      iterate through list
#      Check to see if parameters types are correct
#      create empty list to be sorted
#      If integer is in dict add one else add to dict and set count to 1
#      add values and keys to list as a tuple
#      sort list in reverse order
#      create new dictionary
#      iterate through sliced list adding keys and values to new dictionary
#      return new dictionary
# P2.) Define find_integer function with an int dict and int for parameters
#      Create empty list
#      Check to see if parameters types are correct
#      Iterate through dict using .items() method
#      If integer equals value add key to list
#      Return list of keys


# TEST CASES:
#    Input_P1:[1, 9, 5, 8, 7, 5, 6, 1, 8, 5, 4, 3, 5, 2, 1]
#    Output_P1: {5: 4, 1: 3, 8: 2}
#
#    Input_P1: (9, 8, 7, 9, 6, 5, 8, 9, 4, 3, 1, 2, 7, 8, 9)
#    Output_P1: {9: 4, 8: 3, 7: 2}
#
#    Input_P1: [1, 2, 1, 4, 1, 7.7, 2, 1, 7]
#    Output_P1: -1
#
#    Input_P1: "1,2,1,4,1,7,2,1,7"
#    Output_P1: -1
#
#    Input_P2: {"a":1, "b":9, "c":5, "d":8, "e":7, "f":5, "g":6, "h":1, "i":8, "j":5, "k":4, "l":3, "m":5, "n":2, "o":1}, 5
#    Output_P2: ['c', 'f', 'j', 'm']
#
#    Input_P2: {"a":9, "b":8, "c":7, "d":9, "e":6, "f":5, "g":8, "h":9, "i":4, "j":3, "k":1, "l":2, "m":7, "n":8, "o":9}, 9
#    Output_P2: ['a', 'd', 'h', 'o']
#
#    Input_P2: {"a":1, "b":9, "c":5, "d":8, "e":7, "f":5}, "a"
#    Output_P2: -1
#
#    Input_P2: [1, 2, 1, 4, 1, 7.7, 2, 1, 7], 7
#    Output_P2: -1
#


# PROGRAM:
import unittest


def highest_count(int_list):  # Define highest count function with a integers list as a parameter
    """This function takes a list of integers finds the top three integers that shows up the most in the list and returns a
       dictionary. The integers are the keys and the count are the values.
       If parameter int_list is not an list of only integers -1 is returned instead."""
    if not (type(int_list) == list or type(int_list) == tuple):  # Check to see if parameters types are correct
        return -1
    int_dict_count = {}  # Create empty counting dictionary
    for i in int_list:  # iterate through list
        if not (type(i) == int):  # Check to see if parameters types are correct
            return-1
        if i in int_dict_count:  # If integer is in dict add one else add to dict and set count to 1
            int_dict_count[i] += 1
        else:
            int_dict_count[i] = 1
    sort_list = []  # create empty list to be sorted
    for k, v in int_dict_count.items():  # add values and keys to list as a tuple
        sort_list.append((v, k))
    sort_list.sort(reverse=True)  # sort list in reverse order
    new_dict = {}  # create new dictionary
    for tup in sort_list[:3]:  # iterate through sliced list adding keys and values to new dictionary
        new_dict[tup[1]] = tup[0]
    return new_dict  # return new dictionary


def find_integer(int_dict, in_int):  # Define find_integer function with a int dict and a int for parameters
    """This function takes a dictionary and an integer, searches through the values of the dictionary.
       Then a list of keys is return where the values match the integer.
       If the input type for int_dict parameter is not a dictionary then -1 is returned.
       If the input type for in_int parameter is not a integer then -1 is returned."""
    if not(type(int_dict) == dict):  # Check to see if parameters types are correct
        return -1
    if not (type(in_int) == int):
        return -1
    keys = []  # Create empty list
    for key, value in int_dict.items():  # Iterate through dict using .items() method
        if in_int == value:  # If integer equals value add key to list
            keys.append(key)
    return keys  # Return list of keys


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_0(self):
        self.assertEqual(highest_count([1, 9, 5, 8, 7, 5, 6, 1, 8, 5, 4, 3, 5, 2, 1]), {5: 4, 1: 3, 8: 2})

    def test_number_1(self):
        self.assertEqual(highest_count((9, 8, 7, 9, 6, 5, 8, 9, 4, 3, 1, 2, 7, 8, 9)), {9: 4, 8: 3, 7: 2})

    def test_number_2(self):
        self.assertEqual(highest_count([1, 2, 1, 4, 1, 7.7, 2, 1, 7]), -1)

    def test_number_3(self):
        self.assertEqual(highest_count("1,2,1,4,1,7,2,1,7"), -1)

    def test_number_4(self):
        self.assertEqual(find_integer({"a": 1, "b": 9, "c": 5, "d": 8, "e": 7, "f": 5, "g": 6, "h": 1, "i": 8, "j": 5,
                                       "k": 4, "l": 3, "m": 5, "n": 2, "o": 1}, 5), ['c', 'f', 'j', 'm'])

    def test_number_5(self):
        self.assertEqual(find_integer({"a": 9, "b": 8, "c": 7, "d": 9, "e": 6, "f": 5, "g": 8, "h": 9, "i": 4, "j": 3,
                                       "k": 1, "l": 2, "m": 7, "n": 8, "o": 9}, 9), ['a', 'd', 'h', 'o'])

    def test_number_6(self):
        self.assertEqual(find_integer({"a": 1, "b": 9, "c": 5, "d": 8, "e": 7, "f": 5}, "a"), -1)

    def test_number_7(self):
        self.assertEqual(find_integer([1, 2, 1, 4, 1, 7.7, 2, 1, 7], 7), -1)


if __name__ == '__main__':
    unittest.main()

input()
