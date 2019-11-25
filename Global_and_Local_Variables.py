# Global and Local Variables

# There are two types of variables: global variables and local variables.
#       - A global variable can be reached anywhere in the code, a local only in the scope.
#           - Variables can only reach the area in which they are defined, which is called scope.
#           - Think of it as the area of code where variables can be used.

# Local Variables

# - The Local Variables are x and y
def sum(x,y):
    sum = x + y
    return sum

print(sum(8,6))

# - print(x) will not work as it is outside it's scope

# Global Variables

# - A global variable can be used anywhere in the code.
# - In the example below we define a global variable z

z = 10

def afunction():
    global z
    print(z)

afunction()
print(z)

# A global variable can modified inside a function and change for the entire program :

z = 112

def afunction():
    global z
    z = 9

afunction()
print(z)

# We can get thte contents of a function by returning a variable

def highFive():
    return 5

def f(x,y):
    z = highFive() # we get the variable contents from highFive()
    return x+y+z # returns x+y+z. z is reachable becaue it is defined above

result = f(3,2)
print(result)
