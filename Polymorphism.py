# Polymorphism

# - Sometimes an object comes in many types or forms.
# - If we have a button, there are many different draw outputs (round button, check button, square button, button with image) but they share the same logic: onClick().
#       - We access them using the same method . This idea is called Polymorphism.
#       - Polymorphism is based on the greek words Poly (many) and morphism (forms).
#       - We will create a structure that can take or use many forms of objects.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Polymorphism with a function

# We create two classes:  Bear and Dog, both  can make a distinct sound.
# We then make two instances and call their action using the same method.

class Bear(object):
    def sound(self):
        print("Groarrr")
    
class Dog(object):
    def sound(self):
        print("Woof woof!")
    
def makeSound(animalType):
        animalType.sound()
    
bearObj = Bear()
dogObj = Dog()
    
makeSound(bearObj)
makeSound(dogObj)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Another Example

# We dont know what type of format a user will open a file in - (pdf or word)

# Imagine we could acess them like this :
#   - for document in documents:
#   -   print document.name + ': ' + document.show()

# To do so, we create an abstract class called document.
#   - This class does not have any implementation but defines the structure (in form of functions) that all forms must have.
#   - If we define the function show() then both the PdfDocument and WordDocument must have the show() function.

class Document:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'

class Word(Document):
    def show(self):
        return 'Show word contents!'

documents = [Pdf('Document1'), Pdf('Document2'), Word('Document3')]

for document in documents:
    print document.name + ': ' + document.show()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Inbuilt Polymorphic functions:

# len() being used for a string 
print(len("geeks")) 
  
# len() being used for a list 
print(len([10, 20, 30]))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
  
    def language(self): 
        print("Hindi the primary language of India.") 
  
    def type(self): 
        print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
        print("English is the primary language of USA.") 
  
    def type(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type()
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
