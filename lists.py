# explain lists in python

# Lists are a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names.


# Accessing Elements in a List
# Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

# The index of the first element in a list is 0, not 1. This is true in many programming languages, and the reason is that the index is an offset from the beginning of the list. The index of the second element is 1, the index of the third element is 2, and so forth. Negative indices refer to items at the end of the list; -1 refers to the last item, -2 refers to the second-to-last item, and so forth.

# The following example shows how to access the first and second items in a list of bicycles:


bicycles = ["trek", "redline", "specialized"]

print(bicycles[0])

# print(bicycles[0].title())


# The output of this code is the first item in the list, 'trek', followed by the title() method, which capitalizes the first letter of the first item in the list. The output is as follows:

# trek
# Trek


# Index Positions Start at 0, Not 1

# Python considers the first item in a list to be at position 0, not position 1. This is true of most programming languages, and the reason is that list indexes are offsets from the first position in the list. Here’s how you can access each element in a list:


bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles[0])

print(bicycles[1])


# Using Individual Values from a List

# You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list. Let’s try pulling the first bicycle from the list and composing a message using that value:


bicycles = ["trek", "cannondale", "redline", "specialized"]

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)


# The output of this code is a simple message that includes the first item in the list, 'trek', with the first letter capitalized. The output is as follows:


# My first bicycle was a Trek.


# more examples of lists

# You can define a list by putting the items inside square brackets, separated by commas. For example, here’s how you can define a list of the first three even numbers:


even_numbers = [2, 4, 6]

print(even_numbers)


# The output of this code is a list of the first three even numbers. The output is as follows:


# [2, 4, 6]


# use loops with lists

# You can use a for loop to work with each individual item in a list. For example, here’s how you can print each item in a list of even numbers:


even_numbers = [2, 4, 6, "SHAUKAT", True]

even_numbers[1] = 5


for number in even_numbers:

    print(number)


lisst = [["shaukat, ahmed"], [1, 3, 5]]


for name in lisst:
    print(name)


# The output of this code is each item in the list of even numbers printed on a separate line. The output is as follows:


# use nested lists with examples


# A list can contain any mix of Python data types, including other lists. For example, here’s how you can define a list of lists:


bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]


vehicles = [bicycles, cars]

print(vehicles)


# The output of this code is a list of lists. The output is as follows:


# [['trek', 'cannondale', 'redline', 'specialized'], ['audi', 'bmw', 'subaru', 'toyota']]


# You can access an individual item in a list of lists by giving two sets of square brackets. For example, here’s how you can access the first item in the list of bicycles:


bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]

vehicles = [bicycles, cars]

print(vehicles[0][0])


# use loops with nested lists

# You can use a for loop to work with each individual item in a list of lists. For example, here’s how you can print each item in a list of lists:


bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]

vehicles = [bicycles, cars]

for vehicle in vehicles:

    print(vehicle)


# The output of this code is each list in the list of lists printed on a separate line. The output is as follows:


# ['trek', 'cannondale', 'redline', 'specialized']
# ['audi', 'bmw', 'subaru', 'toyota']


# You can use a for loop to work with each individual item in a list of lists. For example, here’s how you can print each item in a list of lists:


bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]

vehicles = [bicycles, cars]

for vehicle in vehicles:

    for item in vehicle:

        print(item)


# use if else with for loops with lists

# You can use an if statement to work with specific items in a list. For example, here’s how you can print each item in a list of lists, but print a message if the item is 'bmw':

bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]

vehicles = [bicycles, cars]


for vehicle in vehicles:

    for item in vehicle:

        if item == "bmw":

            print(f"I love {item.upper()} cars!")

        else:

            print(item)


# use arithmetic operators and logical operator with lists in for loop

# You can use arithmetic operators and logical operators to work with items in a list. For example, here’s how you can print each item in a list of lists, but print a message if the item is 'bmw' and another message if the item is 'subaru':

bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]


vehicles = [bicycles, cars]


for vehicle in vehicles:

    for item in vehicle:

        if item == "bmw":

            print(f"I love {item.upper()} cars!")

        elif item == "subaru":

            print(f"I love {item.upper()} cars, but I also like {item.upper()} cars.")

        else:

            print(item)


# Modifying Elements in a List

# The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have. For example, let’s say we have a list of motorcycles, and the first item in the list is 'honda'. Here’s how you can change this value:


motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles)


motorcycles[0] = "ducati"

print(motorcycles)


# COMMON LISTS METHODS  IN PYTHON

# Python includes a number of built-in methods that you can use on lists. Here are a few of the most common ones:

# append(): Add an item to the end of the list.
# insert(): Add an item at any position in the list.
# del: Remove an item from any position in the list.
# pop(): Remove an item from the end of the list.
# remove(): Remove an item by value.
# sort(): Sort a list.
# reverse(): Reverse the order of a list.


# Adding Elements to a List

# You can add elements to the end of a list, or you can insert them at a specific position. For example, let’s say we have a list of motorcycles, and we want to add a new motorcycle to the end of the list. Here’s how you can add the new motorcycle 'ducati' to the end of the list:


motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles)


motorcycles.append("ducati")


print(motorcycles)


# using list with while loop

# You can use a while loop to work with a list. For example, here’s how you can remove items from a list until it’s empty:


motorcycles = ["honda", "yamaha", "suzuki", "honda"]

print(motorcycles)

motorcycles.remove("honda")


# The output of this code is each item in the list of motorcycles printed on a separate line, starting with the last item in the list. The output is as follows:


# use list in real world examples

# Lists are used in many real-world applications. For example, you can use a list to store the names of all the people in your family, the make and model of all the cars in a parking lot, or the names of all the countries in the world. You can use a list to store any number of items, and you can access and modify these items in many different ways. Lists are a powerful tool in Python, and they’re used in many different types of programs.


# use list with functions

# You can use a list as an argument in a function. For example, here’s how you can pass a list of motorcycles to a function that prints each item in the list:


# def print_motorcycles(motorcycles):

#     for motorcycle in motorcycles:

#         print(motorcycle)
