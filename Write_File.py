# Write File

# - It is possible to write a file using the .write() method with a parameter containing text data.
# - Before writing data to a file, call the open(filename,’w’) function where filename contains either the filename or the path to the filename.
# - Don’t forget to close the file as well.


# Create File For Writing

filename = "newfile.txt"

# Open the file with writing permission
myfile = open(filename, 'w')

# Write a line to the file
myfile.write('Written with Python\n') # \n writes it on a new line

# Close the file
myfile.close()

# - The ‘w’ flag makes Python truncate the file if it already exists.
# - If the file contents exists it will be replaced.


# Append to file

filename = "newfile.txt"

# The 'a' flag tells Python to keep the file contents and append (add line) at the end of the file.
myfile = open(filename, 'a')

# Add the line
myfile.write('Written with Python\n')

# Close the file
myfile.close()


# Parameters

# Flag	                  Action
#  r	        Open file for reading
#  w	Open file for writing (will truncate file)
#  b	              binary more
#  r+	   open file for reading and writing
#  a+	open file for reading and writing (appends to end)
#  w+	open file for reading and writing (truncates files)
