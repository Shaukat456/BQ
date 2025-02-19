# Dictionaries in Python
# A dictionary in Python is an unordered collection of key-value pairs. Each key must be unique, and each key is associated with a value. You can think of a dictionary like a real-world address book, where each contact's name (key) maps to their phone number (value).


# Creating a Dictionary
# A dictionary is created using curly braces {} and separating keys and values with a colon

person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)


# Accessing Dictionary Values
person = {"name": "Alice", "age": 25, "city": "New York"}

print(person["name"])  # Accessing value by key
print(person.get("age"))  # Using get() method (avoids error if key doesn't exist)


# Adding or Modifying Items
# You can add new key-value pairs or modify an existing value by using the key.

person = {"name": "Alice", "age": 25}

# Adding a new key-value pair
person["city"] = "New York"

# Modifying an existing key-value pair
person["age"] = 26

print(person)


# Removing Items
# You can remove key-value pairs from a dictionary using del, pop(), or popitem()
# Using Del
del person["age"]
print(person)

# using pop
city = person.pop("city")
print(person)
print("Removed:", city)


# iterating Through a Dictionary
# you can loop through a dictionary to access its keys, values, or both.

# Iterating Over Keys
for key in person:
    print(key)


# Iterating Over Values
for value in person.values():
    print(value)


# Iterating Over Keys and Values
for key, value in person.items():
    print(key, ":", value)


#  Checking If a Key Exists
# You can check if a key is present in a dictionary using the in keyword.
if "name" in person:
    print("Name is present.")
else:
    print("Name is not present.")


# Nested Dictionaries
# Dictionaries can also contain other dictionaries as values (creating a nested structure).
person = {
    "name": "Alice",
    "contact": {"email": "alice@example.com", "phone": "123-456-7890"},
}

# Accessing nested dictionary value
print(person["contact"]["email"])


# 8️⃣ Dictionary Methods
# keys(): Returns a list of all the keys.
# values(): Returns a list of all the values.
# items(): Returns a list of all the key-value pairs.
# clear(): Clears the dictionary.


person = {"name": "Alice", "age": 26, "city": "New York"}

print(person.keys())  # Keys
print(person.values())  # Values
print(person.items())  # Key-Value pairs

person.clear()  # Clears all items
print(person)


# Dictionary Comprehension
# Dictionary comprehension is a concise way to create dictionaries.

squares = {x: x**2 for x in range(5)}
print(squares)


# 10️⃣ Real-World Example of a Dictionary:
# Storing Student Data
# Imagine you want to store information about students (name, age, and grades).


students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 21, "grade": "A"},
}

# Accessing Bob's grade
print(students["Bob"]["grade"])  # Output: B


# Conclusion:
# Dictionaries are key-value pairs and are unordered collections.
# They are mutable (can be changed after creation) and useful for fast lookups by key.
# You can access, add, remove, and iterate over the dictionary elements in various ways.


# Using while Loop with a Dictionary
# Since dictionaries are not indexed like lists, we need to convert them into a list of items and then use a while loop.

person = {"name": "Alice", "age": 25, "city": "New York"}

# Convert dictionary items into a list
items = list(person.items())
index = 0

while index < len(items):
    key, value = items[index]
    print(f"{key}: {value}")
    index += 1


# 3️⃣ Real-World Example: Counting Word Frequency in a Sentence
# Let's say we have a sentence and want to count how many times each word appears.

# Example 5: Using for Loop for Word Frequency Count


sentence = "apple banana apple orange banana apple"
words = sentence.split()

word_count = {}

# Counting words
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


# Example 6: Using while Loop for Word Frequency Count
sentence = "apple banana apple orange banana apple"
words = sentence.split()

word_count = {}

# Counting words
index = 0
while index < len(words):
    word = words[index]
    word_count[word] = word_count.get(word, 0) + 1
    index += 1

print(word_count)

# ✅ Use for loops when directly iterating over keys, values, or key-value pairs.
# ✅ Use while loops when iterating manually, such as using an index.
# ✅ Both loops can be used for practical problems, like word frequency counting.
