

# --------------------> module <--------------------

# module: module is a file containing a set of codea or set of function  which can include to an application
#         it is a file containg a single variable,a function or a big code base

#                import user defined module

import mymodule_ex1 

print(mymodule_ex1.generate_fullname("arpit","mishra"))

# import function from a module ()

from mymodule_ex1 import generate_fullname,sum_two_num,person,gravity

print(generate_fullname("arpit","mishra"))
print(sum_two_num(1,9))
mass=100
weight=mass*gravity
print(weight)
print(person["first_name"])

# import function from a module and renaming

from mymodule_ex1 import generate_fullname as fullname,sum_two_num as total,person as p,gravity as g

print(fullname("arpit","mishra"))
print(total(1,9))
mass=100
weight=mass*g
print(weight)
print(p["first_name"])

#             import built in module

# os module

import os
# make dir

#os.mkdir("unusepython")  # it already maded once

# change current directory

#print(os.chdir("path"))

# getting current working directory

print(os.getcwd())

# removing directory

#os.rmdir('C:\Users\bapun\OneDrive\Desktop\python\unusepython\dowhile.py') # in bapun \b and \a is unicode so ith throw error

# list directory

print(os.listdir())

import os
folders=os.listdir("data")
print("\n")
print(folders)
print("\n")
print(os.getcwd())#its told that at which directory the file and folder are placed: getcwd() or This function returns the current working directory.
for folder in folders:
    print(folder)
    print("\n")
    print(os.listdir(f"data/{folder}"))

# shuting down of pc
import os 
#os.system("shutdown /s /t 10") # (/time how_much_second_you_want_to_off_pc)

#os.chdir(path): This function changes the current working directory to the specified path.
#os.listdir(path): This function returns a list of all files and directories in the specified path.
#os.getcwd(): This function returns the current working directory.
#os.system(command): This function executes a system command and returns the exit status.
#os.mkdir(path): This function creates a new directory at the specified path.
#os.remove(path): This function deletes a file at the specified path.
#os.environ: This is a dictionary containing environment variables.
#os.path.exists(path): This function checks if a file or directory exists at the specified path.
#os.path.isfile(path): This function checks if the specified path is a file.
#os.path.isdir(path): This function checks if the specified path is a directory.
#os.path.join(path, *paths): This function joins one or more path components intelligently.
#os.path.abspath(path): This function returns an absolute path.
#os.path.basename(path): This function returns the base name in a pathname.
#os.path.dirname(path): This function returns the directory name of a pathname.
#os.path.getatime(path): This function returns the last access time of a file.
#os.path.getmtime(path): This function returns the last modification time of a file.
#os.path.getctime(path): This function returns the creation time of a file.
#os.path.getsize(path): This function returns the size of a file.
#os.path.isabs(path): This function checks if the specified path is absolute.
#os.path.realpath(path): This function returns the canonical path of a file.
#These are some of the most commonly used functions in the os module. They provide a way to interact with the operating system, such as
# working with files, directories, and environment variables, as well as executing system commands and spawning new processes.

#For example, os.getcwd() can be used to get the current working directory, os.chdir(path) can be used to change the current working 
#directory, os.listdir(path) can be used to list all files and directories in a directory, os.system(command) can be used to execute a
# system command, os.mkdir(path) can be used to create a new directory, os.remove(path) can be used to delete a file, os.environ can be
# used to access environment variables, os.path.exists(path) can be used to check if a file or directory exists, os.path.isfile(path)
# can be used to check if a path is a file, os.path.isdir(path) can be used to check if a path is a directory, os.path.join(path, *paths) 
#can be used to join path components, os.path.abspath(path) can be used to get an absolute path, os.path.basename(path) can be used to 
#get the base name of a path, os.path.dirname(path) can be used to get the directory name of a path, os.path.getatime(path) can be used
# to get the last access time of a file, os.path.getmtime(path) can be used to get the last modification time of a file, os.path.
#getctime(path) can be used to get the creation time of a file, os.path.getsize(path) can be used to get the size of a file, os.path.
#isabs(path) can be used to check if a path is absolute, and os.path.realpath(path) can be used to get the canonical path of a file.

import os
if( not os.path.exists("data")):
    os.mkdir("data")
    for i in  range(0,4):
       os.mkdir(f"data/day{i+1}")
else:
      print("directory is exist")
# sys module :it provide function and variable that used to manipulate different part of python run time environment

#import sys as s
#print(s.argv[0],argv[1],argv[2]) this line would print out :filename argument1 and argument2
#print("welcome {}. enjoy {} challenge".format(s.argv[1],s.argv[2]))










# statistic module

from statistics import *

ages=[20,21,22,23,24,25,26,27,28,23]
print(mean(ages))# Return the sample arithmetic mean of data.
print(median(ages))# Return the median (middle value) of numeric data.
print(mode(ages))# Return the most common data point from discrete or nominal data.
print(stdev(ages))# Return the square root of the sample variance.

# math module

import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

# string module

from string import *

print(ascii_letters)# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(digits)       # 0123456789
print(punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# random module : it provide the random between 0 to 0.9999....

from random import *

print(random())
print(randint(5,20))




