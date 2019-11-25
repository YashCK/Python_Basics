# Random Numbers

# - Using the random module, we can generate pseudo-random numbers.
# - The function random() generates a random number between zero and one [0, 0.1 .. 1].
# - Numbers generated with this module are not truly random but they are enough random for most purposes.

# Random number between 0 and 1:

from random import *

print(random())

from random import sample 
  
# Prints list of random items of given length 
list1 = [1, 2, 3, 4, 5]  
  
print(sample(list1, 3)) 

# Generate a random number between 1 and 100:

print(randint(1, 100))

# Store random number in a variable

x = randint(1, 100)
print(x)

# Random floating point number between 1 and 10:

print(uniform(1, 10))

# Randomly shuffling a list:

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("items : ", items)
shuffle(items)
print("shuffled items: ", items)

# Pick a random Number from a list:

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = sample(items,  1)   # Pick a random item from the list
print(x)
print(x[0])

y = sample(items, 4)    # Pick 4 random items from the list
print(y)

# Pick a random String from a list

items = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']

x = sample(items,  1)   # Pick a random item from the list
print(x[0])

y = sample(items, 4)    # Pick 4 random items from the list
print(y)
