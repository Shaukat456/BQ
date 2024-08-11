# Reading from and writing to files, Handling text and CSV files, Try-except blocks for error handling, Handling common file-related exceptions, File manipulation exercises, Debugging and preventing errors


# Reading from and writing to files
# Python provides built-in functions for reading from and writing to files. These functions allow you to interact with files on your computer, such as reading data from a text file or writing data to a new file. In this section, we will cover the basics of file operations in Python.

# Reading from a file
# To read data from a file, you can use the built-in open() function in Python. The open() function takes two arguments: the file name and the mode in which you want to open the file. The mode specifies whether you want to read, write, or append data to the file.

# The most common modes for reading files are 'r' (read) and 'rb' (read in binary mode). When you open a file in read mode, you can read the contents of the file using the read() method.

# Here is an example of reading data from a text file named 'example.txt':

# Open the file in read mode
file = open("./something.txt", "r")

# Read the contents of the file

content = file.read()

# Print the contents of the file
print(content)

# Close the file
file.close()

# In this example, we open the file 'example.txt' in read mode ('r') and read the contents of the file using the read() method. We then print the contents of the file and close the file using the close() method.


# Writing to a file
# To write data to a file, you can use the built-in open() function in Python. When you open a file in write mode ('w'), you can write data to the file using the write() method.

# Here is an example of writing data to a new text file named 'output.txt':

# Open the file in write mode
file = open("output.txt", "w")

# Write data to the file

file.write("Hello, World!")

# Close the file
file.close()


# In this example, we open the file 'output.txt' in write mode ('w') and write the string 'Hello, World!' to the file using the write() method. We then close the file using the close() method.

# Note: When you open a file in write mode ('w'), the contents of the file are overwritten. If you want to append data to an existing file, you can open the file in append mode ('a').


# Handling text and CSV files
# In addition to reading and writing text files, Python also provides support for reading and writing CSV (Comma-Separated Values) files. CSV files are commonly used to store tabular data, such as spreadsheets or databases.


# Reading from a CSV file
# To read data from a CSV file, you can use the built-in csv module in Python. The csv module provides functions for reading and writing CSV files, such as the reader() function for reading data from a CSV file.


# Here is an example of reading data from a CSV file named 'data.csv':

import csv

# Open the CSV file in read mode
with open("data.csv", "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Read the contents of the file
    for row in reader:
        print(row)

# In this example, we open the CSV file 'data.csv' in read mode and create a CSV reader object using the csv.reader() function. We then iterate over the rows in the CSV file and print each row.


# Writing to a CSV file
# To write data to a CSV file, you can use the csv.writer() function in Python. The csv.writer() function allows you to write data to a CSV file row by row.


# Here is an example of writing data to a new CSV file named 'output.csv':

import csv

# Data to write to the CSV file
data = [["Alice", 25], ["Bob", 30], ["Charlie", 35]]


# Open the CSV file in write mode
with open("output.csv", "w", newline="") as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write data to the file
    writer.writerows(data)


# In this example, we define a list of lists called data, where each inner list represents a row of data to write to the CSV file. We then open the CSV file 'output.csv' in write mode and create a CSV writer object using the csv.writer() function. We write the data to the CSV file using the writer.writerows() method.


# Try-except blocks for error handling
# In Python, you can use try-except blocks to handle exceptions and errors that may occur during the execution of your code. Try-except blocks allow you to catch and handle exceptions gracefully, preventing your program from crashing.


# Here is an example of using a try-except block to handle a ZeroDivisionError:

try:
    result = 10 / 0
except ZeroDivisionError:

    print("Error: Division by zero")


# In this example, we use a try-except block to catch a ZeroDivisionError that occurs when dividing by zero. If a ZeroDivisionError occurs, the code inside the except block is executed, and the error message "Error: Division by zero" is printed.


# Handling common file-related exceptions
# When working with files in Python, you may encounter common file-related exceptions that can be handled using try-except blocks. Some common file-related exceptions include FileNotFoundError, PermissionError, and IOError.


# Here is an example of handling a FileNotFoundError when opening a non-existent file:

try:
    file = open("./helo.txt", "r")
except FileNotFoundError:
    print("Error: File not found")


# In this example, we use a try-except block to catch a FileNotFoundError that occurs when trying to open a non-existent file. If a FileNotFoundError occurs, the code inside the except block is executed, and the error message "Error: File not found" is printed.


# File manipulation exercises
# Now that you have learned the basics of file operations in Python, you can try the following exercises to practice reading from and writing to files:


# Exercise 1: Write a Python program that reads data from a text file named 'input.txt' and writes the data to a new text file named 'output.txt'.


# Exercise 2: Write a Python program that reads data from a CSV file named 'input.csv' and writes the data to a new CSV file named 'output.csv'.

# Debugging and preventing errors

# When working with files in Python, it is important to handle errors and exceptions that may occur during file operations. Here are some tips for debugging and preventing errors when working with files:
