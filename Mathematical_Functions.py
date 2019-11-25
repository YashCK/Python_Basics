# Mathematical Functions adn Operations

# Operation	       Result
# x + y	          sum of x and y.
# x * y	    multiplication of x and y.
# x - y	      difference of x and y.
# x / y	       division of x by y.

# x % y	         remainder of x/y
# x ** y	x to the power of y
# abs(x)	absolute value of x
# sqrt(x)	square root of x

x = int(input("Enter an int: "))
y = int(input("Enter an int: "))

import math

print(x + y)
print(x * y)
print(x/y)
print(x - y)
print(x % y)
print(x ** y)
print(abs(x))
print(math.sqrt(y))

# Function	              Return

# abs(x)          Returns the absolute value of x.

x = -35
x = abs(x)
print(x)

# exp(x)         Returns the exponential of x (e^x)

x = 4
print(math.exp(x))

# log(x)	     The natural logarithm of x

x = 42
print(math.log(x))

# log10(x)           The base-10 logarithm of x

x = 100
print(math.log10(x))

# pow(x,y)	        The result of x**y

x = 5
print(math.pow(x, 3))

# sqrt(x)	      The square root of x

x = 81
print(math.sqrt(x))
