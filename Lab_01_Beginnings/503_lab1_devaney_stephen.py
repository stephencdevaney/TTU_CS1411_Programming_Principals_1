# NAME:     Stephen Curtis Devaney
# COURSE:   1411-503
# DATE:     09/04/2018

# PROBLEM:
#   Given a telephone book with 1 to N lines on a page, and each pages has exactly
#   1 to C Columns. Output  which page, column, and line number that X is on.

# GIVEN:
#   All entries start with 1
#   C: number of columns on a page
#   N: number of lines on a page
#   X: entry user is looking for

# ANALYSIS
#   Input #1:    number of columns on each page
#   Input #2:    number of lines on each page
#   Output #1:   page number entry is on
#   Output #2:   column number entry is on
#   Output #3:   line number entry is on

# METHOD/ALGORITHM:
#   introduce program
#   input user_c from user (column number)
#   input user_n from user (line number)
#   input user_x from user (entry number)
#   find page_number by adding one to the quotient of the entry number divided by ( the number of lines multiplied by the number of columns)
#   find column_number by adding one to quotient of the remainder of the entry number divided by (the number of lines multiplied by the number of columms) all divided by the number of lines
#   find line_number by finding the remainder of (the entry number minus one) dividied by (the number of columns multiplied by the number of lines)
#   print the output for the user by stating ('Your entry is located on page:', page_number, 'in column:', column_number, 'on line:', line_number)

# TEST CASES:
#   test case 1:
#   input: 1 columns, 1 line, entry number 1
#   output: The name and phone number you are looking for is located on page: 1 in column: 1 on line: 1

#   test case 2:
#   input: 2 columns, 10 line, entry number 12
#   output: The name and phone number you are looking for is located on page: 1 in column: 2 on line: 2

#   test case 3:
#   input: 2 columns, 10 line, entry number 25
#   output: The name and phone number you are looking for is located on page: 2 in column: 1 on line: 5

#   test case 4:
#   input: 3 columns, 5 line, entry number 55
#   output: The name and phone number you are looking for is located on page: 4 in column: 2 on line: 5

#   test case 5:
#   input: 2 columns, 10 line, entry number 81
#   output: The name and phone number you are looking for is located on page: 5 in column: 1 on line: 1


# PROGRAM:
#   introduce the program:
print('Take a telephone book and input the number of lines and columns on each')
print('page. Then input the entry number of the name and phone number you are')
print('looking for in this telephone book. Afterwards this program will give')
print('your the page number, column number, and line number of the name and')
print('phone number you are looking for.')
print('')

#   input user_c from user:
user_c = int(input('Please enter the number of columns per page (from 1 to n): '))
print('')

#   input user_n from user:
user_n = int(input('Please enter the number of lines per page (from 1 to n): '))
print('')

#   input user_x from user:
user_x = int(input('Please enter the entry number of the name and phone number that your are looking for (from 1 to n): '))
print('')

#   find page_number by adding on to the quotient of entry number divided by (number of lines multiplied by the number of columns) 
page_number = 1+(user_x-1) // (user_c * user_n)
# page_number = 1+(user_x-1) // user_n

#   find column_number by adding one to quotient of the remainder of the (entry number minus one) divided by (the number of columns multiplied by the number of lines) all divided by the number of lines
column_number = 1+(user_x-1) % (user_c * user_n) // user_n
# column_number = 1+(user_x-1) % user_n // (user_n // user_c)

#   find line_number by finding the remainder of (the entry number minus one) dividied by (the number of columns multiplied by the number of lines)
line_number = 1+(user_x-1) % user_n
# line_number = (user_x-1)%(user_n//user_c)+1

#   print the output for the user ('Your entry is located on page:', page_number, 'in column:', column_number, 'on line:', line_number)
print('The name and phone number you are looking for is located on page:', page_number, 'in column:', column_number, 'on line:', line_number)

input()

# algorithms after code in comments relate to lines being total on page instead of rows on page
