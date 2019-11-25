# Method_Overloading

# - Several ways to call a method (method overloading)
# - You can define a method in such a way that there are multiple ways to call it.

# - Given a single method or function, we can specify the number of parameters ourself.
# - Depending on the function definition, it can be called with zero, one, two or more parameters.

# This is known as method overloading. Not all programming languages support method overloading.

# --------------------------------------------------------------------------------------------------

# Two Functions With The Same Name - Not supported

# First product method. 
# Takes two argument and print their 
# product 
def product(a, b): 
    p = a * b 
    print(p) 
      
# Second product method 
# Takes three argument and print their 
# product 
def product(a, b, c): 
    p = a * b*c 
    print(p) 
  
# Uncommenting the below line shows an error     
# product(4, 5) 
  
# This line will call the second product method 
product(4, 5, 5) 

# --------------------------------------------------------------------------------------------------

# One Function With Optional Parameters - Supported

# We create a class with one method sayHello().
# The first parameter of this method is set to None, this gives us the option to call it with or without a parameter.

# An object is created based on the class, and we call its method using zero and one parameter.

class Human:

    def sayHello(self, name = None):
    
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
        

# Create instance
obj = Human()
    
# Call the method
obj.sayHello()
    
# Call the method with a parameter
obj.sayHello('Guido')

# - We created a method that can be called with fewer arguments than it is defined to allow.
# - We are not limited to two variables, a method could have more variables which are optional.
