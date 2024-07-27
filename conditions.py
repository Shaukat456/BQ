# restrictions when using if else statement

# 1. Indentation is important
# 2. Use of colon

# Syntax:
# if condition:
#     # block of code
# else:
#     # block of code


# give a number and check if it is even or odd
num = 10

if num < 2:
    print("Number is less than 2")

else:
    print("Number is greater than 2")


# elif exercise to check the number is positive, negative or zero
num = 0
if num > 0:
    print("Positive")

elif num < 0:
    print("Negative")

else:
    print("Zero")


# Nested if else example
# check the number is positive, negative or zero and even or odd
num = 10

if num >= 0:
    if num == 2:
        print("Number is 2")
    else:
        if num % 2 == 0:
            print("Positive and Even")
        else:
            print("Positive and Odd")


else:
    if num % 2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")


# excercises to get a good understanding of if else statement

# 1. Check if the number is divisible by 5 or not
# 2. Check if the number is positive, negative or zero
# 3. Check if the number is even or odd
# 4. Check if the number is positive and even
# 5. Check if the number is positive and odd
# 6. Check if the number is negative and even
# 7. Check if the number is negative and odd
# 8. Check if the number is divisible by 5 or not


age = 18


if age >= 18:
    if (age >= 18) and (age <= 30):
        print("You are eligible for the job")

    else:
        print("You are not eligible for the job")
else:
    print("You are not eligible for the job")
