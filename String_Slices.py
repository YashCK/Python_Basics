# String Index

# Python indexes the characters of a string, every index is associated with a unique character.
# For instance, the characters in the string ‘python’ have indices:

# The 0th index is used for the first character of a string. Try the following:

s = "Hello Python"
print(s)      # prints whole string
print(s[0])   # prints "H"
print(s[1]) # prints "e"

# String Slicing

# Given a string s, the syntax for a slice is: s[ startIndex : pastIndex ]

print(s[0:8])

# The startIndex is the start index of the string. pastIndex is one past the end of the slice.

# If you omit the first index, the slice will start from the beginning. If you omit the last index, the slice will go to the end of the string. For instance:

print(s[:2]) # prints "He"
print(s[2:4]) # prints "ll"
print(s[6:])  # prints "Python"
