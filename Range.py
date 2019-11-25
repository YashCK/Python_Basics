# Range

# The range() function returns of generates a sequence of numbers, starting from the lower bound to the upper bound.

# - Lower_bound: The starting value of the list.

# - Upper_bound: The max value of the list, excluding this number.

# - Step_bound: The step size, the difference between each number in the list.

# The lower_bound and step_size parameters are optional.
# By default the lower bound is set to zero, the incremental step is set to one.
# The parameters must be of the type integers, but may be negative.

print(list(range(5)))
print(list(range(0,5)))
print(list(range(1,6)))
print(list(range(6,1,-1)))
print(list(range(0,-10, -2)))
