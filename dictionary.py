# explain dictionary in python

# A dictionary in Python is a collection of key-value pairs. Each key is associated with a value, and you can use the key to access the corresponding value. Dictionaries are unordered, changeable, and indexed. They are used to store data in a structured way and are commonly used for mapping one value to another.

# syntax of a dictionary in python

# A dictionary in Python is defined using curly braces {} and key-value pairs separated by a colon :. The general syntax for a dictionary is as follows:


# dictionary = {key1: value1, key2: value2, key3: value3}

# In this syntax, key1, key2, and key3 are the keys, and value1, value2, and value3 are the corresponding values. Each key-value pair is separated by a comma ,.


# example of a dictionary in python

# Here's an example of a dictionary in Python that stores information about a person:


person = {"name": "John", "age": 30, "city": "New York"}


# In this dictionary, the keys are "name", "age", and "city", and the corresponding values are "John", 30, and "New York".


# Accessing Elements in a Dictionary

# You can access the values in a dictionary by using the keys. To access a value, you can use the key inside square brackets [] or the get() method. Here are some examples:


# Accessing a value using square brackets

name = person["name"]

print(name)


# Accessing a value using the get() method

age = person.get("age")

print(age)  # Output: 30


# If the key is not present in the dictionary, using square brackets to access the value will raise a KeyError, while the get() method will return None. You can also specify a default value to be returned if the key is not found using the get() method:


# Accessing a value with a default value

city = person.get("city", "Unknown")


print(city)  # Output: New York


# Modifying Elements in a Dictionary


# You can modify the values in a dictionary by using the key to access the value you want to change and then assigning a new value to that key. Here's an example:


# use loop with dictionary
for key in person:
    print(key, person[key])


# Modifying a value in a dictionary

person["age"] = 35

print(person)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}


# Adding Elements to a Dictionary

# You can add new key-value pairs to a dictionary by using a new key and assigning a value to it. Here's an example:


# Adding a new key-value pair to a dictionary
