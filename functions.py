# explain why we need to use the function in programming


# Functions are a way to organize code into reusable blocks. They allow you to define a set of instructions that can be called multiple times with different inputs. This helps to reduce code duplication, improve readability, and make the code easier to maintain.


# Functions also help in modularizing code, making it easier to understand and debug. They allow you to break down complex problems into smaller, more manageable parts, which can be tested and debugged independently.


# syntax of a function in python

# def function_name(parameters):

#     # block of codeW

#     return value


# what is the meaning of return in a function

# The return statement is used to exit a function and return a value to the caller. It can be used to pass data back from the function to the calling code. The return statement can also be used to terminate the execution of a function prematurely.


# example of a function in python

# def add(a, b):
#     return a + b


# result = add(10, 20)

# print(result)


# what is the meaning of parameters in a function

# Parameters are variables that are used to pass values to a function. They are defined in the function definition and are used to specify the inputs that the function expects. Parameters allow you to pass data to a function and customize its behavior based on the inputs provided.


# what is the meaning of arguments in a function


# Arguments are the actual values that are passed to a function when it is called. They are the values that are assigned to the parameters defined in the function definition. Arguments are used to provide input data to the function and determine its behavior based on the specific values passed.


# example of a function with multiple parameters


def multiply(a, b):
    return a * b


result = multiply(5, 10)


print(result)


# example of a function with default parameters


def greet(name="World"):
    return f"Hello, {name}!"


message = greet("Alice")


print(message)


message = greet()


print(message)


# example of a function with keyword arguments


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


message = greet("Alice", greeting="Hi")


print(message)


message = greet("Bob")


print(message)


# example of a function with variable number of arguments


def add(*args):
    total = 0
    for num in args:
        total += num
    return total


result = add(1, 2, 3, 4, 5)


print(result)


# example of a function with variable number of keyword arguments


def greet(**kwargs):
    if "name" in kwargs and "greeting" in kwargs:
        return f"{kwargs['greeting']}, {kwargs['name']}!"
    else:
        return "Hello, World!"


message = greet(name="Alice", greeting="Hi")


print(message)


message = greet(name="Bob")


print(message)


# example of a function with a docstring


def greet(name):
    """
    This function greets the user by name.
    """
    return f"Hello, {name}!"


message = greet("Alice")


print(message)


# give an example of a function that takes a list as an argument and returns the sum of all the elements in the list


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


result = sum_list([1, 2, 3, 4, 5])


print(result)


# give an example of a function that takes a string as an argument and returns the number of vowels in the string


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


result = count_vowels("Hello, World!")


print(result)


# give an example of a function that takes a list of numbers as an argument and returns the average of the numbers


def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


result = average([1, 2, 3, 4, 5])


print(result)


# give an example of a function that takes a list of strings as an argument and returns the longest string in the list


def longest_string(strings):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest


result = longest_string(["apple", "banana", "cherry", "date"])


print(result)
