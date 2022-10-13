# Blackboard Submission Number: 7ea20333-6378-4f9e-a6ff-b235b5ae2d19
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     10/23/2018


# PROBLEM:
# Write a program that prompts for the height of the Pascal’s triangle and then generates the triangle.
# Hint: Use a list for each row, and use a list of row lists to hold the whole triangle.


# GIVEN:
# The rows of Pascal’s triangle are conventionally enumerated starting with row 0, and the numbers in
# each row are usually staggered relative to the numbers in the adjacent rows. A simple construction of
# the triangle proceeds in the following manner. On row 0, write only the number 1. Then, to construct
# the elements of following rows, add the number directly above and to the left with the number directly
# above and to the right to find the new value. If either the number to the right or the left s not present,
# substitute a zero in its place. For example, the first number in the first row is 0+1=1, whereas the
# numbers 1 and 3 in the third row are added to produce the number 4 in the fourth row. Here are the first
# five rows of Pascal’s triangle:
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1


# ANALYSIS:
#    Input:  an integer less than one
#    Output: Error: integer is not a positive integer greater than 0. Please try again.
#
#    Input:  anything that is not an integer
#    Output: Error: item is not a positive integer greater than 0. Please try again.
#
#    Input:  an positive integer
#    Output: Pascal's Triangle to the row height of input


# METHOD/ALGORITHM:
# while loop setup
# get users input and set to column_length
# find row length
# create first row
# use first row as basis for future rows
# modify current row
# find left value
# find right value
# add values together to make current row
# add current row to rows
# Print space for 0 else print integer in rows
# Use try / except to make program robust
# create a would you like to continue statement for the loop


# TEST CASES:
#    Input: abc
#    Output: Error: abc is not a positive integer greater than 0. Please try again.
#
#    Input: -23
#    Output: Error: -23 is not a positive integer greater than 0. Please try again.
#
#    Input: 0
#    Output: Error: 0 is not a positive integer greater than 0. Please try again.
#
#    Input: 1
#    Output: 1
#
#    Input: 6
#    Output: Your triangle:
#                 1
#                1 1
#               1 2 1
#              1 3 3 1
#             1 4 6 4 1
#            1 5 10 10 5 1
#
#    Input: 10
#    Output: Your triangle:
#                 1
#                1 1
#               1 2 1
#              1 3 3 1
#             1 4 6 4 1
#            1 5 10 10 5 1
#           1 6 15 20 15 6 1
#          1 7 21 35 35 21 7 1
#         1 8 28 56 70 56 28 8 1
#        1 9 36 84 126 126 84 36 9 1


# PROGRAM:
# while loop setup
done = False
while not done:
    # get users input and set to column_length
    tri_height = input("Please enter the height of the triangle: ")
    try:
        column_length = int(tri_height)

        # find row length
        row_length = 2*(column_length-1)+1
        rows = []

        # create first row
        row = [0 for i in range(row_length)]
        index = column_length-1
        row[index] = 1
        rows.append(row)

        # use first row as basis for future rows
        for i in range(column_length-1):
            cur_row = [0 for t in range(row_length)]
            prev_row = rows[i]

            # modify current row
            for c in range(row_length):

                # find left value
                if c <= 0:
                    left_value = 0
                else:
                    left_value = prev_row[c-1]

                # find right value
                if c >= row_length-1:
                    right_value = 0
                else:
                    right_value = prev_row[c+1]

                # add values together
                cur_row[c] = left_value+right_value

            # add current row to rows
            rows.append(cur_row)
        max_len = len(str(max(rows[-1])))

        # Print space for 0 else print integer in rows
        print("Your triangle: ")
        for r in rows:
            for c in r:
                if c == 0:
                    print(' ' * max_len, end="")
                else:
                    constant = str(c)
#                    print(constant, end ='')
                    space = (max_len - len(constant))
                    left = space // 2
                    if space % 2 == 0:
                        right = space // 2
                    else:
                        right = (space // 2) + (space % 2)
                    print(' ' * left + constant + ' ' * right, end="")
            print()

    # Use try / except to make program robust
    except ValueError:
        print("Error:", tri_height, "is not a positive integer greater than 0. Please try again.")
        continue
    except IndexError:
        print("Error:", tri_height, "is not a positive integer greater than 0. Please try again")
        continue

# create a would you like to continue statement for the loop
    done = input("Would you like to continue please answer with y or n: ")
    while not (done == "Y" or done == "y" or done == "n" or done == "N" or done == "quit" or done == "exit"):
        done = input("Error: Would you like to continue please answer with y or n: ")
    if done == "Y" or done == "y":
        done = False
    elif done == "N" or done == "n" or done == "quit" or done == "exit":
        done = True
print("You have quit have a nice day!")
