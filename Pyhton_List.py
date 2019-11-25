# Python List

# Lists is a sequence and a basic data structure.
# A list may contain strings (text) and numbers.
# A list is similar to an array in other programming languages, but has additional functionality.
    # Arrays can also only have data of one type, whereas a list can have entries of various object types.
    # Arrays are also more efficient for some numerical computation.
    # There is a difference in direct access Vs sequential access.
        # Arrays allow both direct and sequential access
        # Lists allow only sequential access.
        # And this is because the way that these data structures are stored in memory.
        
# We define lists with brackets []. To access the data, brackets are used as well.

# Define

l = [ "Drake", 457, 32.5, True ]

print(l)     # prints all elements
print(l[0])  # print first element
print(l[1])  # prints second element
print(l[2])  # print third element
print(l[3])  # prints fourth element

# Add / Remove Elements

print(l)                # prints all elements
l.append("Victoria")   # add element.
print(l)                # print all elements
l.remove(457)       # remove element.
l.remove(32.5)      # remove element.
print(l)

# Sort Elements


l = [ "Drake", "Derp", "Derek", "Dominique" ]

# Ascensing Order

print(l)     # prints all elements
l.sort()    # sorts the list in alphabetical order
print(l)     # prints all elements

# Descending Order

l = [ "Drake", "Derp", "Derek", "Dominique" ]

print(l)     # prints all elements
l.sort()    # sorts the list in alphabetical order
l.reverse() # reverse order.
print(l)     # prints all elements
