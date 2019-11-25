# Read File

# - The file that needs to be read has to be in the same directory as your program, if it is not you need to specify a path.

# Define a filename.
filename = "Range.py"

# Open the file as f.
# The function readlines() reads the file.

with open(filename) as f:
    content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.

for line in content:
    print(line),

# The first part of the code will read the file content.
# Every line read will be stored in the variable content.
# The for loop will iterate over every line in the variable contents.

print("----------------------------------------------------------------------------------------------------------")

# If you do not want to read the newline characters ‘\n’, you can change the statement f.readlines() to this:

with open(filename) as f:
    content = f.read().splitlines()

for line in content:
    print(line),

print("----------------------------------------------------------------------------------------------------------")

# It is important to test if the file we want to open exists.
# We will test first if the file exists, if it does it will read the file otherwise return an error:

import os.path

# Define a filename.
filename = "String_Slices.py"

if not os.path.isfile(filename):
    print('File does not exist.')
else:
    
# Open the file as f.
# The function readlines() reads the file.
    with open(filename) as f:
        content = f.read().splitlines()
# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
    for line in content:
        print(line)

print("----------------------------------------------------------------------------------------------------------")

# Sample Example

# Python program to explain os.path.isfile() method  
    
# importing os module  

#       import os 
  
# Path 
#       path = '/home/User/Desktop/file.txt'
  
# Check whether the  
# specified path is  
# an existing file

#       isFile = os.path.isfile(path) 
#       print(isFile) 
  
  
# Path

#       path = '/home/User/Desktop/'
  
# Check whether the  
# specified path is  
# an existing file

#       isFile = os.path.isfile(path) 
#       print(isFile) 
