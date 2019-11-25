# Encapsulation

# It is possible to restrict access to methods and variables.
# This can prevent the data from being modified by accident and is known as encapsulation.

# -----------------------------------------------------------------------------------------

# Private Methods

# Let's create a class Car which has two methods:  drive() and updateSoftware(
# When a car object is created, it will call the private methods __updateSoftware().  
# This function cannot be called on the object directly, only from within the class.

class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
# redcar.__updateSoftware() is not accesible.

# - Encapsulation prevents from accessing accidentally, but not intentionally.
# - The private attributes and methods are not really hidden, they’re renamed adding _Car” in the beginning of their name.
# - The method can actually be called using redcar._Car__updateSoftware()

# redcar._Car__updateSoftware()

print("-----------------------------------------------------------------------------------------")

# Private Variables

# - Variables can also be private which can be useful as well.
# A private variable can only be changed within a class method and not outside of the class.
# Objects can hold crucial data for your application and you do not want that data to be changeable from anywhere in the code.

class Car:

    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    
    def drive(self):
        print('driving: maxspeed ', self.__maxspeed)

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()

print("-----------------------------------------------------------------------------------------")

# To change the value of a private variable, a setter method is used.
# This is simply a method that sets the value of a private variable.

class Car2:

    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    
    def drive(self):
        print('driving. maxspeed ', self.__maxspeed)

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

redcar = Car2()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()

# -----------------------------------------------------------------------------------------

# Encapsulation gives you more control of your code.
# It allows a class to change its implementation without affecting other parts of the code.

# Types of Encapsulation                                    Description

# public methods                                      Acessible from anywhere
# private methods                                  Acesssible only in the class
# protected methods         Cannot be acessed other than in the class and subclassesn (single underscore)
# public variables                                    Acessible from anywhere
# private variables       Accesible only in their own class or by a method defined. starts with two underscores
# protected variables       Cannot be acessed other than in the class and subclassesn (single underscore)
