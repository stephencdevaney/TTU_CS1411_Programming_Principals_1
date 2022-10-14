Problem 1 – Pascal’s Triangle:
Pascal’s triangle is a geometric arrangement of sums that have interesting mathematical properties 
– most famously, the binomial coefficients.

The rows of Pascal’s triangle are conventionally enumerated starting with row 0, and the numbers in 
each row are usually staggered relative to the numbers in the adjacent rows. A simple construction 
of the triangle proceeds in the following manner. On row 0, write only the number 1. Then, to 
construct the elements of following rows, add the number directly above and to the left with the 
number directly above and to the right to find the new value. If either the number to the right or 
the left s not present, substitute a zero in its place. For example, the first number in the first 
row is 0+1=1, whereas the numbers 1 and 3 in the third row are added to produce the number 4 in the 
fourth row. Here are the first six rows of Pascal’s triangle:
Write a program that prompts for the height of the Pascal’s triangle and then generates the 
triangle in the same styles as previous example.
Hint: Use a list for each row, and use a list of row lists to hold the whole triangle.
Example of program session:
Please enter the height of the triangle: 6
Your triangle:
Would you like to continue (yes, no): yes
