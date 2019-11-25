# Inheritance

# - Classes can inherit functionality of other classes.
# - If an object is created using a class that inherits from a superclass, the object will contain the methods of both the class and the superclass.
# - The same holds true for variables of both the superclass and the class that inherits from the super class.

# Python supports inheritance from multiple classes, unlike other popular programming

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Programmer User:

class User:
    name = ""
    
    def __init__(self, name):
        self.name = name
    
    def printName(self):
        print("Name  = " + self.name)
    
brian = User("brian")
brian.printName()

# This creates one instance called brian which outputs its given name.

# Programmer Class:

class Programmer(User):

    def __init__(self, name):
        self.name = name

    def doPython(self):
        print("Programming Python")

# User is given in the parameters.
# This means all functionality of the class User is accessible in the Programmer class.

diana = Programmer("Diana")
diana.printName()
diana.doPython()

# Brian is an instance of User and can only access the method printName.
# Diana is an instance of Programmer, a class with inheritance from User, and can access both the methods in Programmer and User.
