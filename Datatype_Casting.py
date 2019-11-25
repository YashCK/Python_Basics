# Datatype Casting

# - Python determines the datatype automatically, to illustrate:

x = 3           # x is of type integer 
y = "text"      # y is of type string.

# - Functions accept a certain datatype.

print(2)
print("2")
print(3.4)
print(True)

# In this example below we want to print two numbers, an integer and a floating point number:

x = 3
y = 2.15315315313532

print("We have defined two numbers.")

print("x = " + str(x))
print("x = " , x)
print("y = " + str(y))
print("y = " , y)

# - We cast the int x and the float y to a string using the str() function.

# If we have text that we want to store as number, we will have to cast again:

a = "135.31421"
b = "133.1112223"
c = float(a) + float(b)
print(c)
print(a + b)

# - We cast two variables with the datatype string to the datatype float.

# Conversions Functions

# To convert between datatypes you can use:

# Function                             Purpose

# int(x)	            Converts x to an integer
# long(x)	 Converts x to a long integer (No longer available)
# float(x)	      Converts x to a floating point number
# str(x)	            Converts x to an string.
# hex(x)	   Converts x integer to a hexadecimal string
# chr(x)	     Converts x integer to a character
# ord(x)	    Converts character x to an integer

# The one main disadvantage of binary numbers is that the binary string equivalent of a large decimal base-10 number can be quite long.
# When working with computers, it is common to find binary numbers consisting of 8, 16 and even 32 digits.
# This makes it difficult to work with, without producing errors especially when working with lots of 16 or 32-bit binary numbers.

# One common way of overcoming this problem is to arrange the binary numbers into groups or sets of four bits (4-bits).
# These groups of 4-bits uses another type of numbering system also commonly used in computer and digital systems called Hexadecimal Numbers.
