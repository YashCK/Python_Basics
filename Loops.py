# Loops

# Code can be repeated using a loop.
# Lines of code can be repeated n times, where n is manually configurable.
# Code will be repeated until a condition is met.

# Python has 3 types of loops: for loops, while loops and nested loops.

# -------------------------------------------------------------------------------------------------------------------------------------------

# For Loop

items = [ "Abby","Brenda","Cindy","Diddy" ]

for item in items:
    print(item)

# With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(6):
    print(x)

# It is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter:

for x in range(2, 30, 3):
    print(x)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# -------------------------------------------------------

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# For loops cannot be empty, but if you have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
    pass

# Break statements can be used to exit out of a loop

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print('Current Letter :' + letter)

# -------------------------------------------------------------------------------------------------------------------------------------------

# While Loops

correctNumber = 5
guess = 0

while guess != correctNumber:
    guess = int(input("Guess the number: "))
    
    if guess != correctNumber:
        print('False guess')

print('You guessed the correct number')

# Break statements can be used to exit a loop

var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var - 1 # No -- or ++
   if var == 5:
      break

print ("Good bye!")

# Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1

# The continue statement can stop the current interation and continue with the next

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else statement can a block of code when the condition is no longer true

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# -------------------------------------------------------------------------------------------------------------------------------------------


# Nested Loops

# We can combine for loops using nesting. If we want to iterate over an (x,y) field we could use:

for x in range(1,10):
    for y in range(1,10):
        print("(" + str(x) + "," + str(y) + ")")

# -------------------------------------------------------------------------------------------------------------------------------------------
