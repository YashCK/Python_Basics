# Python Classes

# Everything in Python is an object.
# Every object can contain methods and variables (with unique values). O
# Objects can be created from classes.

# ------------------------------------------------------------------------------

# Example : 

class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + ' walks.')

duck = Animal('Duck')
duck.walk()

# ------------------------------------------------------------------------------

# Explanation

# We create one object called ‘duck’ from the class Animal.
# The class has a method (walk) that can be called on each object.
# We also have a method called init(), this is a method that is always called when a new object is created.
# The self keyword is required for every method.
# We set the variables with the class (self.name = ..).

# ------------------------------------------------------------------------------

# A program can consist of many classes and objects.
# Class with two objects:

class Animal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(self.name + ' walks.')

duck = Animal('Duck')
duck.walk()

rhino = Animal('African Rhino')
rhino.walk()
