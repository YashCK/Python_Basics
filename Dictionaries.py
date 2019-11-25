# Dictionaries

# - A dictionary can be thought of as an unordered set of keys: value pairs.
# - A pair of braces creates an empty dictionary: {}.
# - Each element can maps to a certain value.
# - An integer or string can be used for the index.
# - Dictonaries do not have an order.

# Dictionary Example

words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"

print("words : ", words)

print(words["Hello"]) # Output is Bonjour
print(words["No"]) # Output is Non

# - We are by no means limited to single word defintions in the value part.

dict = {}
dict['Ford'] = "Car"
dict['Python'] = "The Python Programming Language"
dict[2] = "This sentence is stored here."

print("dict : ", dict)

print(dict['Ford'])
print(dict['Python'])
print(dict[2])

# Manipulating the Dictionary

# - We can manipulate the data stored in a dictionairy after declaration :

print("words : ", words)         # print key-pairs.
del words["Yes"]                 # delete a key-pair.
print("words : ", words)         # print key-pairs.
words["Yes"] = "Oui!"            # add new key-pair.
print("words : ", words)         # print key-pairs.
