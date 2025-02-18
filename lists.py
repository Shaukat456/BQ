# A list is an ordered, mutable (changeable) collection of elements in Python. It is created using square brackets []. Lists can contain different data types, such as numbers, strings, and even other lists. Lists support indexing, slicing, and various operations like adding, removing, and updating elements.


my_list = [1, 2, 3, "apple", "banana"]
print(my_list)  # Output: [1, 2, 3, 'apple', 'banana']


# 📌 Key Features of Lists
# ✅ Ordered – Elements maintain their position.
# ✅ Mutable – Values can be changed after creation.
# ✅ Can contain different data types – Integers, strings, etc.
# ✅ Supports indexing and slicing – Like tuples.


#  Shopping List (Dynamic Data)
# A shopping list is modifiable, so a list is the best choice.
shopping_list = ["Milk", "Eggs", "Bread", "Butter"]
shopping_list.append("Cheese")  # Adding an item
shopping_list.remove("Eggs")  # Removing an item
print(shopping_list)


#  Why use a list?
# The list changes when we add or remove items.


# To-Do List
# A to-do list keeps track of tasks that change over time.


# tasks = ["Complete project", "Go to gym", "Read book"]
# tasks.append("Call mom")  # Adding a new task
# tasks.pop(1)  # Removing 'Go to gym'
# print(tasks)


# Student Marks in a Class
# A teacher stores students' marks in a list because they need to be updated.

marks = [85, 90, 78, 92, 88]
marks[2] = 80  # Updating a student's marks
print(marks)


# Social Media Notifications
# A social media app stores notifications in a list, adding new ones at the end.

notifications = ["New friend request", "Message from Alice", "New comment on your post"]
notifications.append("Someone liked your post")
print(notifications)


#  Queue of Customers in a Bank
# A bank uses a list to track customers in a queue.

queue = ["Customer1", "Customer2", "Customer3"]
queue.pop(0)  # First customer is served
print(queue)


#  Inventory Management in a Store
# A store tracks stock in a list and updates it when items are sold or restocked.


inventory = ["Laptop", "Mouse", "Keyboard"]
inventory.append("Monitor")  # New item added
inventory.remove("Mouse")  # Item sold out
print(inventory)


# Feature	List	Tuple
# Mutable?	✅ Yes (Can be modified)	❌ No (Cannot be modified)
# Faster?	❌ No (More memory)	✅ Yes (Less memory)
# Use Case	Changing data (tasks, notifications)	Fixed data (coordinates, RGB values)


# Using a for Loop with Lists
# Example 1: Print Each Item in a List (Basic Example)

fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(fruit)


# tasks = ["Wake up", "Exercise", "Study", "Work"]

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")


# Filtering Even Numbers from a List
numbers = [10, 15, 20, 25, 30, 35, 40]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)


# Sorting a List (Bubble Sort Algorithm)
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# Conclusion
# Use for loops when you know how many times you need to iterate.
# Use while loops when you don't know the exact number of iterations (e.g., processing user input).
# Nested loops are useful for 2D lists (tables, matrices, grids, etc.).
