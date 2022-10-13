# Blackboard Submission Number: d609f27b-2245-4fa1-840d-9941a478a396
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     11/27/2018


# PROBLEM:
# Problem 1 : Text book, problem 6, chapter 15, page 708
# Converting decimal numbers to binary numbers and be done recursively. Write a function that takes a
# positive int argument and returns the corresponding binary number as an int composed of only ones and
# zeros. For example, convert(5) returns the int: 101
# The insight for this problem comes from the fact that the right most digit of a decimal n is easy
# to calculate. It is the remainder when dividing by the base 2: n%2. To get the next right most digit,
# you can take the resulting quotient, that is n2 = n/2, and find its remainder, n2%2, which is the next
# digit. Unfortunately, that generates the digits from right to left and we want them from left to right. We
# could easily do that non-recursively using string concatenation or string reversal, but in this exercise
# you are to use recursion to recursively calculate the digits. Effectively, you are letting recursion reverse
# the ordering: think in terms of calculating the rightmost digit as described previously, but then let
# recursion reverse the digits.


# GIVEN:
# 5 converted to binary should be 101.
# n%2 will give the right digit
# recursion of the function finding the remainder of int(n//2) till n = 0 will give the rest of the digits
# multiplying each recursion by 10 will put the digits in the proper place
# A positive integer is a whole number greater than 0


# ANALYSIS:
#    Input: a positive whole number
#    Output: the binary function number for the whole number
#
#    Input: a positive float number or anything but an integer
#    Output: False
#
#    Input: any number <= 0
#    Output: False


# METHOD/ALGORITHM:
# Import Unit Test
# Define the Function
# Check to see if Integer greater than 0
# Else Return False
# Test Function


# TEST CASES:
#    Input: 5
#    Output: 101
#
#    Input: 7
#    Output: 111
#
#    Input: 11
#    Output: 1011
#
#    Input: 3
#    Output: 10001
#
#    Input: 23
#    Output: 10111
#
#    Input: 32
#    Output: 100000
#
#    Input: 0
#    Output: False
#
#    Input: 5.5
#    Output: False


# PROGRAM:
import unittest  # Import Unit Test


def convert_int_to_bin(integer):  # Define the Function
    """Function converts a positive integer to binary and the binary number is returned.
       If anything but a positive integer is inputted into the function False is returned."""
    if integer > 0 and type(integer) == int:  # Check to see if Integer greater than 0
        return integer % 2 + 10*convert_int_to_bin(int(integer // 2))  # If conditions met return binary function
    else:
        return False  # Else Return False


class TestUM(unittest.TestCase):  # Test Function
    def setUp(self):
        pass

    def test_number_0(self):
        self.assertEqual(convert_int_to_bin(5), 101)

    def test_number_1(self):
        self.assertEqual(convert_int_to_bin(7), 111)

    def test_number_2(self):
        self.assertEqual(convert_int_to_bin(11), 1011)

    def test_number_3(self):
        self.assertEqual(convert_int_to_bin(17), 10001)

    def test_number_4(self):
        self.assertEqual(convert_int_to_bin(23), 10111)

    def test_number_5(self):
        self.assertEqual(convert_int_to_bin(32), 100000)

    def test_number_6(self):
        self.assertEqual(convert_int_to_bin(0), False)

    def test_number_7(self):
        self.assertEqual(convert_int_to_bin(5.5), False)


if __name__ == '__main__':
    unittest.main()

input()
