Problem 1 : File copy – Text book: Programming project 2, chapter 14, page 685
All operating systems have commands that will create a copy of a file. In this exercise, you are to
create a program that will make an exact copy of a file. Provide the following capabilities:
- Copy only files that end with a “.txt” extension. Generate an appropriate error if something else is
specified.
- Using the os module, check whether the source file exists.
- Using the os module, check whether the destination file exists. If so, ask the user if he or she wants to
overwrite it.
- If no paths are specified, assume that the file is in the current folder (directory). Otherwise, use the os
module to separate the path from the file name. If a path is specified for the destination file, check
whether the path exists – otherwise, generate an error.