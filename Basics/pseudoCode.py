# PseudoCode

# Writing pseudocode in Python involves creating a high-level description of the program's logic without worrying about the exact syntax. Here are some tips for writing pseudocode, along with an example:

# Tips for Writing Pseudocode
# Use Plain Language: Describe each step of the algorithm in simple, natural language.
# Avoid Specific Syntax: Don't use the exact syntax of any programming language.
# Be Consistent: Maintain a consistent format throughout the pseudocode.
# Indentation: Use indentation to show the structure of the logic (e.g., loops, conditions).
# Describe Logic Clearly: Make sure each step is clear and unambiguous.


# Example:   Pseudocode for Checking if a Number is Even or Odd
#  START
#   INPUT number
#   IF number is divisible by 2
#     PRINT "The number is even"
#   ELSE
#     PRINT "The number is odd"
# END


# Translating Pseudocode to Python Code
# Once you have written the pseudocode, you can translate it into Python code. Here is the Python code for the above pseudocode:

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# This Python code follows the logic described in the pseudocode, but it uses the actual syntax of the Python programming language.


# Example: Pseudocode for Finding the Maximum of Three Numbers
# START
#   INPUT num1, num2, num3
#   IF num1 is greater than num2 AND num1 is greater than num3
#     max = num1
#   ELSE IF num2 is greater than num1 AND num2 is greater than num3
#     max = num2
#   ELSE
#     max = num3
#   PRINT max
# END


# Start of the program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the maximum number
if num1 > num2 and num1 > num3:
    max_num = num1
elif num2 > num1 and num2 > num3:
    max_num = num2
else:
    max_num = num3

# Print the maximum number
print("The maximum number is:", max_num)
# # End of the program
