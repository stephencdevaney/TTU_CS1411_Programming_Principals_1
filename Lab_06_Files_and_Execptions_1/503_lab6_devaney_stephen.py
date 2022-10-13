# Blackboard Submission Number: 4d32b127-9872-494e-9e29-3bf16607a41c
# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     10/16/2018


# PROBLEM:
# Create a function that will take a file name as an argument and another filename to write the program output to.
# This function should attempt (use try except) to open the file associated with that file name. Error will be caught
# if the file does not exist. The program will read each line of that file and try to compute the expression
# (assume that each line is one mathematical expression, you can use python function eval(...) for this purpose).
# Unsupported operators should be caught. It should then write the result of that operation to an output file
# (which is the second argument of this function). Upon unsupported operation, “bad expression” will be written to
# output file instead and the program still continues until it reaches end of file. The program should inform user
# about successful file creation if no error occurs


# GIVEN:
# A FileNotFoundError is raised when a file is open to be read and it does not exist
# A OSError may be raised if the file that is being open contains special characters
# A NameError is raised if a variable is given which is not in the programs namespace
# A SyntaxError could be raised if using too many or wrong operators
# A TypeError could be raised if using certain operators with different types
# A ZeroDivisionError could be raised if divided by zero
# A ValueError could be raised if user tires to convert a string of letters to a float


# ANALYSIS:
# File Name
#    Input: bad file name
#    Output: File Not Found
#    Input: proper file name
#    Output: Output file is successfully created. The output is written to (file_name)
#
# Results
#    Input: Unsupported Operation
#    Output: "Bad Expression" to file_name
#    Input: Proper Math Expression
#    Output: Result to file


# METHOD/ALGORITHM:
# Define function
#     Iterate through each line in the file
#     Evaluate each line on the page use try/except to print error statement while keeping iteration going
#     Print success statement
#     Close files to ensure output is properly saved to file
# Main Program
#     Get user's file names
#     Use users input in function


# TEST CASES:
# File Name Test Cases
#    Input: input file name: math_ex.txt
#    Output: "File Not Found"
#    Input: input file name: lab6_math_exp.txt, output file name: results.txt
#    Output: Output file is successfully created. The output is written to results.txt
#
# Results Test Cases
#    Input:1+2+3*4
#    Output: 15
#    Input:3*4
#    Output: 12
#    Input:123>321
#    Output: False
#    Input:4-10/xx
#    Output: "Bad Expression"
#    Input:999/0
#    Output: "Bad Expression"
#    Input:5***10
#    Output: "Bad Expression"
#    Input:555+"555"
#    Output: "Bad Expression"
#    Input:float('abc')
#    Output: "Bad Expression"


# PROGRAM:
# Define function
def file_math(input_math_expression_file, output_result_file):

    # Use try/except to get file names and prevent errors
    try:
        in_file = open(input_math_expression_file, "r")
        out_file = open(output_result_file, 'w')
    except FileNotFoundError:
        print('File Not Found')
        return -1
    except OSError:
        print('File Not Found')
        return -1

    # Iterate through each line in the file
    for line_str in in_file:

        # Evaluate each line on the page use try/except to print error statement while keeping iteration going
        line = line_str
        try:
            result = eval(line)
            print(result, file=out_file)
        except NameError:
            print('Bad Expression', file=out_file)
        except SyntaxError:
            print('Bad Expression', file=out_file)
        except TypeError:
            print('Bad Expression', file=out_file)
        except ZeroDivisionError:
            print('Bad Expression', file=out_file)
        except ValueError:
            print('Bad Expression', file=out_file)
    # Print success statement
    print('Output file is successfully created. The output is written to', output_result_file)
    # Close files to ensure output is properly saved to file
    in_file.close()
    out_file.close()
    return 0


# Main Program
restart = -1
while restart == -1:

    # Get user's file names
    user_infile = input("Please enter your input file: ")
    user_outfile = input("Please enter your output file: ")

    # Use users input in function
    restart = file_math(user_infile, user_outfile)
input()
