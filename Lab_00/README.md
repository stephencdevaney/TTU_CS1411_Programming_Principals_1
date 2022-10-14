Lab 0: getting started with Python
What’s this lab about?



In Lab 0, our goal is to introduce you to a few things:

•  Logging in to lab computers with your CS account.
•  Getting started with the Python computer language.
•  Using Python shell to execute commands.
•  Using Python's IDLE editor to write and save python programs.

Are you using a lab machine?
If you are using a lab machine, Python Interpreter is already installed and ready to try. You may 
need to access the remote lab (http://www.depts.ttu.edu/coe/dean/engineeringitservices/remote-lab- 
preparing.php).

What to run Python on the Internet?
You can do so here:

•  https://www.tutorialspoint.com/execute_python3_online.php
•  https://www.python.org/shell/
Or your own machines? Install Python!
Unlike most UNIX systems and services, Windows does not require Python natively and thus does not 
pre-install a version of Python. You need to download Python 3.7.0 from here and install it on your 
own machines (be sure to check install the path so that your system has the path to the python 
folders).

Trying out Python at python shell







•  Open IDLE, which should be in your start menu under the newly created Python program 
group.

•  Now, let’s get Python to say "Hello World" by entering:
print (“Hello world”)

•  Let’s try a few more commands:
print(“Here are the ten numbers from 1 to 10”) for i in Range(10):
print(i)

Don't worry too much about knowing the exact rules for making programs yet: the idea is that we can 
experiment with Python by typing in commands.


Running a program from a file







We can't directly save what's on the interpreter window. What we'd like is to make a prepared file, 
save that as a document and run python over that.

•  In an Editor, write a simple program to print out numbers from 1 to 10, save it as test.py and 
run
python over that.
