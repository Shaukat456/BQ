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


# Exercise 2: Concatenate Strings
# Task:
# Write a function called concatenate_strings that takes two strings as arguments and returns them concatenated together with a space in between.


def concatenate_strings(str1, str2):
    return str1 + " " + str2


result = concatenate_strings("Hello", "World")
print(result)


# Task:
# Write a function called list_length that takes a list as an argument and returns the length of the list.


def list_length(anyList):
    return len(anyList)


result = list_length([1, 2, 3, 4, 5])
print(result)


#  Check Substring
# Write a function called contains_substring that takes two strings as arguments and returns True if the second string is found within the first string, otherwise returns False.


def contains_substring(main_str, sub_str):
    return sub_str in main_str


# Test the function
result = contains_substring("Hello, world!", "world")
print(result)  # Output: True


# Reverse String
# Write a function called reverse_string that takes a string as an argument and returns the string reversed.

# sequence[start:stop:step]

s = "hello"

# Extract "ell" (from index 1 to index 4)
print(s[1:4])  # Output: "ell"

# Extract "hello" (from start to end)
print(s[:])  # Output: "hello"

# Extract "hel" (from start to index 3)
print(s[:3])  # Output: "hel"

# Extract "lo" (from index 3 to end)
print(s[3:])  # Output: "lo"

# Reverse the string
print(s[::-1])  # Output: "olleh"


def is_palindrome(s):
    # Reverse the string using slicing
    reversed_s = s[::-1]

    # Check if the original string is equal to the reversed string
    return s == reversed_s


# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


def reverse_string(s):

    return s[::-1]


# Test the function
reversed_str = reverse_string("Python")
print(reversed_str)


#  Find Key in Dictionary

# Write a function called find_key that takes a dictionary and a key as arguments and returns True if the key is found in the dictionary, otherwise returns False.


def find_key(d, key):
    return key in d


# Test the function
sample_dict = {"name": "Alice", "age": 25, "city": "New York"}
result = find_key(sample_dict, "age")
print(result)


# Count words in a string


def count_words(s):
    words = s.split()
    return len(words)


# Test the function
word_count = count_words("The quick brown fox jumps over the lazy dog")
print(word_count)


#  Join List into String

# Write a function called join_list that takes a list of strings as an argument and returns a single string with all the list elements joined by a comma and a space.


def join_list(lst):
    return ", ".join(lst)


# Test the function
joined_str = join_list(["apple", "banana", "cherry"])
print(joined_str)


# extract the unique words from a string
def unique_words(s):
    words = s.lower().split()
    return list(set(words))


# Test the function
unique = unique_words("This is a test. This test is only a test.")
print(unique)  # Output: ['this', 'is', 'a', 'test.', 'only']


# count Characters
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Test the function
char_freq = count_characters("hello world")
print(char_freq)


# Remove duplicates from a list


def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# Test the function
unique_list = remove_duplicates(["apple", "banana", "apple", "cherry", "banana"])
print(unique_list)
