# While loops are used to execute a block of code repeatedly as long as a specified condition is true. The condition is evaluated before each iteration of the loop. If the condition is true, the code inside the loop is executed. If the condition is false, the loop terminates and the program continues with the next statement after the loop.


# Example of a while loop

i = 1
while i <= 5:
    print(i)

listOfStudents = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Example of a while loop with a list
i = 0
while i < len(listOfStudents):
    newStudent = listOfStudents[i] + "@gmail.com"
    print(newStudent)
    i = i + 1

# The break statement is used to exit the loop prematurely, bypassing the normal loop condition. It is used to terminate the loop when a certain condition is met.

# Example of a while loop with a break statement
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i = i + 1


# The continue statement is used to skip the current iteration of the loop and continue with the next iteration. It is used to skip the rest of the code inside the loop for the current iteration.

# Example of a while loop with a continue statement
i = 1
while i <= 5:
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1


# The pass statement is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute. It is a null operation, and nothing happens when it is executed.

# Example of a while loop with a pass statement
i = 1
while i <= 5:
    pass
    print(i)
    i = i + 1


# While loop with dictionary
studentGrades = {"Alice": 85, "Bob": 90, "Charlie": 75, "David": 80, "Eve": 95}
i = 0

while i < len(studentGrades):
    student = list(studentGrades.keys())[i]
    grade = studentGrades[student]

    if grade >= 90:
        print(student + " has an A grade.")
    elif grade >= 80:
        print(student + " has a B grade.")
    elif grade >= 70:
        print(student + " has a C grade.")
    else:
        print(student + " has a failing grade.")
    i = i + 1
