# Python Objects and Classes

# 1. Statements:
#   - In the early days of computing, programmers wrote only commands.

# 2. Functions:
#   - Reusable group of statements, helped to structure that code and it improved readability.

# 3. Classes:
#    - Classes are used to create objects which have functions and variables.
#       - Strings are examples of objects:
#       - A string book has the functions book.replace() and book.lowercase().
#       - This style is often called object oriented programming.

# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Each class instance can have attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by its class) for modifying its state.

# ---------------------------------------------------------------------------------------------

# Class Example

# - We can create virtual objects in Python.
# - A virtual object can contain variables and methods.
# - A program may have many different types and are created from a class.
# - Example:

class User:
    name = ""
    
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        print("Hello, my name is " + self.name)

# create virtual objects
james = User("James")
david = User("David")
eric = User("Eric")

# call methods owned by virtual objects
james.sayHello()
david.sayHello()

# Run this program.
# In this code we have 3 virtual objects: james, david and eric.
# Each object is instance of the User class.

# The variables owned by the class is in this case “name”. These variables are sometimes called class attributes.
# We can create methods in classes which update the internal variables of the object.

# ---------------------------------------------------------------------------------------------

# Explanation

# The self variable represents the instance of the object itself.
# Most object-oriented languages pass this as a hidden parameter to the methods defined on an object; Python does not.
# You have to declare it explicitly.
# When you create an instance of the class and call its methods, it will be passed automatically.

# A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class.
# Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts.
# Constructors can also verify that there are enough resources for the object and perform any other start-up task you can think of.

# The name of a constructor is always the same, __init__().
# The constructor can accept arguments when necessary to create the object.
# Every class must have a constructor.


#       a = A()               # We do not pass any argument to the __init__ method
#       a.method_a('Sailor!') # We only pass a single argument

# The __init__ method is similar to a constructor in Python.
# When you call A() Python creates an object for you, and passes it as the first parameter to the __init__ method.
# Any additional parameters (e.g., A(24, 'Hello')) will also get passed as arguments--in this case causing an exception to be raised, since the constructor isn't expecting them.

# ---------------------------------------------------------------------------------------------

# Class Variables

# We define a class CoffeeMachine.
#    - The virtual objects hold the amount of beans and water.
# Both are defined as ints.
# We can define methods that add or remove beans as well as water.

class CoffeeMachine:

    name = ""
    beans = 0
    water = 0

    def __init__(self, name, beans, water):
        self.name = name
        self.beans = beans
        self.water = water
        
    def addBean(self):
        self.beans = self.beans + 1
    
    def removeBean(self):
        self.beans = self.beans - 1

    def addWater(self):
        self.water = self.water + 1
    
    def removeWater(self):
        self.water = self.water - 1

  #  def currentState(self):
    #    print("Name  = " + self.name)
     #   print("Beans = " + str(self.beans))
      #  print("Water = " + str(self.water))

    def currentState(self):
        print("Name  = ", self.name)
        print("Beans = ", self.beans)
        print("Water = ", self.water)
    
machine1 = CoffeeMachine("Python Bean", 83, 20)
machine1.currentState()
machine1.addBean()
machine1.currentState()

# ---------------------------------------------------------------------------------------------
