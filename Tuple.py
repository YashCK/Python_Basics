# Tuple

# - The tuple data structure is used to store a group of data.
# - The elements in this group are separated by a comma. Once created, the values of a tuple cannot change.  

# - Python represents all its data as objects.
# - Some of these objects like lists and dictionaries are mutable , meaning you can change their content without changing their identity.
# - The difference between lists and strings is that lists are mutable while tuples are immutable.

# An Empty Tuple

tuple = ()

# Tuple With 1 Item

tuple = (3,)

# - Without the comma for a single item, you cannot access the element.
# - For multiple items, you do not have to put a comma at the end. Example:

personInfo = ("Bob", 32, "New York")

# - The data inside a tuple can be of one or more data types such as text and numbers.

# Data Access

# - To access the data we can simply use an index. As usual, an index is a number between brackets:

print(personInfo[0])
print(personInfo[1])
print(personInfo[2])

for elem in personInfo:
    print(type(elem))

# Tuples can be to used to assign multiple variables at once.

name,age,country,career = ('Rip',32,'Canada','CompSci')
print(name)
print(age)
print(country)
print(career)

# Append to a Tuple

# If you have an existing tuple, you can append to it with the + operator.
# You can only append a tuple to an existing tuple.

x = (3,4,5,6)
x = x + (1,2,3)
print(x)
