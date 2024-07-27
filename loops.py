# when do we use while loop
# Reading a file until the end is reached.
# Waiting for a user input or an external event.


# Example of a while loop
i = 1
while i <= 5:
    print(i)
    i = i + 2


# We use a for loop when we want to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. Iterating through a sequence is called traversal. for loops are preferred when the number of iterations is known or finite.

# Example use cases for a for loop:

# Iterating over elements of a list, tuple, etc.
# Running a loop a specific number of times using range().
# Iterating over keys or values of a dictionary.

listOfStudents = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Example of a for loop
for student in listOfStudents:
    newStudent = student + "@gmail.com"
    print(newStudent)

# The range() function is used to generate a sequence of numbers. It can take up to three arguments: start, stop, and step. The range() function generates numbers starting from the start value up to, but not including, the stop value, incrementing by the step value.


# Example of using the range() function
for i in range(1, 6):
    print(i)


# The break statement is used to exit the loop prematurely, bypassing the normal loop condition. It is used to terminate the loop when a certain condition is met.


# Example of a for loop with a break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# The continue statement is used to skip the current iteration of the loop and continue with the next iteration. It is used to skip the rest of the code inside the loop for the current iteration.


# Example of a for loop with a continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# The pass statement is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute. It is a null operation, and nothing happens when it is executed.


# Example of a for loop with a pass statement
for i in range(1, 6):

    print(i)


# The else statement is used in conjunction with loops to execute a block of code when the loop condition is false or when the loop completes successfully without encountering a break statement.

# Example of a for loop with an else statement

for i in range(1, 6):
    print(i)

else:
    print("Loop completed successfully")


# exercies to get a good understanding of loops

# 1. Print numbers from 1 to 10 using a for loop

# 2. Print even numbers from 1 to 10 using a for loop

# 3. Print odd numbers from 1 to 10 using a for loop


# 4. Print numbers from 1 to 10 using a while loop
