# Functions

# - A function is reusable code that can be called anywhere in your program.
# - Functions improve readability of your code as well.
# - Functions can be reused or modified which also improve testability and extensibility.

# Define

def function(parameters):
    instructions
    return value

# Example

def f(x):
    return(x*x)
    
print(f(3))

# Parameters

# - We can pass in multiple variables to a function which it then can perform operations upon

def f(x,y):
    print('You passed in values x : ' + str(x) + ' and y : ' + str(y))
    print('x * y = ' + str(x*y))

f(3,2)

def method(a):
    print(a + a)

method([1,2,4])
