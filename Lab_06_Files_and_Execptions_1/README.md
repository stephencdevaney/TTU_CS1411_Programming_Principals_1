Create a function that will take a file name as an argument and another filename to write the program
output to. This function should attempt (use try except) to open the file associated with that file
name. Error will be caught if the file does not exist. The program will read each line of that file and try
to compute the expression (assume that each line is one mathematic expression, you can use python
function eval(...) for this purpose). Unsupported operators should be caught. It should then
write the result of that operation to an output file (which is the second argument of this function). Upon
unsupported operation, “bad expression” will be written to output file instead and the program still
continues until it reaches end of file. The program should inform user about successful file creation if
no error occurs. Below is an example of the program session:
Example of progress session:
Please enter your input file: math_exp.txt
Please enter your output file: result.txt
Output file is successfully created. The output is written to
result.txt
Content of math_exp.txt and result.txt
Line number math_exp.txt result