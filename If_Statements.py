# If Statements

# We can define conditional statements, known as if-statements.
# A block of code is executed if certain conditions are met.

x = 3
print(x)
if x > 10:
    print("x is bigger than 10 or equal")
else:
    print("x smaller than 10")

# If you set x to be larger than 10, it will execute the second code block.
# We use indentation (4 spaces) to define the blocks.

# Sample Game:

age = 15

print("Guess my age, you have 1 chance!")
guess = int(input("Guess: "))

if guess != age:
    print("Wrong!")
else:
    print("Correct")

# Operators

# = to sets something equal to another
# == checks if two things are equal

# !=	not equal
# ==	equals
# >	greater than
# <	smaller than
# >=    greater than or equal ot
# <=    less than or equal to

a = 12
b = 33

if a > 10:
    if b > 20:
        print("Good")

# We can combine conditions using the and keyword. (not && but and)

if guess > 10 and guess < 20:
    print("In range")
else:
    print("Out of range")

# We can also use the or keyword

a = 25
b = 36

if a > 10 or b < 20:
    print("In range")
else:
    print("Out of range")

