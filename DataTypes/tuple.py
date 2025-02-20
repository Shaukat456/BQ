# What is a Tuple in Python?
# A tuple is an ordered, immutable collection in Python. It is similar to a list but cannot be modified (immutable) after creation. Tuples are created using parentheses ().


# ✅ Ordered – The elements maintain their position.
# ✅ Immutable – Cannot change values after creation.
# ✅ Can contain different data types – Numbers, strings, etc.
# ✅ Supports indexing and slicing – Like lists.


my_tuple = (1, 2, 3, "apple", "banana")
print(my_tuple)  # Output: (1, 2, 3, 'apple', 'banana')


#  Storing Database Records (Immutable Rows)
# Databases often return query results as tuples because they should remain unchanged.
student_record = (101, "Alice", "Computer Science", 3.9)
print(f"Student Name: {student_record[1]}, Major: {student_record[2]}")


#  Why use a tuple?
# Prevents accidental modification of database records


# Days of the Week
# The days of the week are fixed and do not change, making tuples perfect.


# days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(days_of_week[0])  # Output: Monday

#  Why use a tuple?
# Days never change, so immutability is useful


# Feature	Tuple	List
# Mutable?	❌ No	✅ Yes
# Faster?	✅ Yes (less memory)	❌ No (more memory)
# Loop Performance	✅ Faster	❌ Slower
# Use Case	Fixed data	Changing data


# For loop with a Tuple
fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)


# Looping with Index (enumerate)
cars = ("Tesla", "BMW", "Mercedes")

for index, car in enumerate(cars):
    print(f"Car {index + 1}: {car}")


# Finding a Specific Value
numbers = (10, 20, 30, 40, 50)

for num in numbers:
    if num == 30:
        print("Number 30 found!")
        break  # Stop the loop when found


# Using while Loop with Tuples
colors = ("red", "green", "blue")
i = 0

while i < len(colors):
    print(colors[i])
    i += 1  # Move to the next index


# Searching for an Element in a Tuple

names = ("Alice", "Bob", "Charlie", "David")
i = 0

while i < len(names):
    if names[i] == "Charlie":
        print(f"Charlie found at index {i}")
        break  # Stop searching
    i += 1


# Counting Occurrences in a Tuple
numbers = (1, 2, 3, 4, 2, 5, 2)
count = 0
target = 2  # Number to count
i = 0

while i < len(numbers):
    if numbers[i] == target:
        count += 1
    i += 1

print(f"Number {target} appears {count} times.")


# Loop	When to Use?
# for loop	When you need to iterate through all elements easily
# while loop	When you need manual index control or conditional looping


#  Question: Write a Python program that prints each element of a tuple using a for loop.
fruits = ("apple", "banana", "cherry", "orange")

for fruit in fruits:
    print(fruit)


# Question: Write a Python program to find the sum of all numbers in a tuple using a for loop.
numbers = (10, 20, 30, 40, 50)
total = 0

for num in numbers:
    total += num

print("Sum of tuple elements:", total)


# Find Maximum and Minimum Values in a Tuple
numbers = (15, 42, 8, 91, 33, 4, 72)
i = 1  # Start from index 1
max_value = numbers[0]
min_value = numbers[0]

while i < len(numbers):
    if numbers[i] > max_value:
        max_value = numbers[i]
    if numbers[i] < min_value:
        min_value = numbers[i]
    i += 1

print("Maximum value:", max_value)
print("Minimum value:", min_value)
