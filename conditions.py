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

# 1. Check if the number is divisible by 5 or not with solution

number = 10

if number % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")


# 2. Check if the number is positive, negative or zero

number = 0

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")
# 3. Check if the number is even or odd


number = 10

if number % 2 == 0:
    print("Even")

else:
    print("Odd")


age = 18
if age >= 18:

    if (age >= 18) and (age <= 30):
        print("You are eligible for the job")

    else:
        print("You are not eligible for the job")
else:
    print("You are not eligible for the job")


# Example 1: Checking Age for a Discount (Using and)


age = int(input("Enter your age: "))

if age >= 18 and age <= 25:
    print("You are eligible for a student discount.")
else:
    print("You are not eligible for a student discount.")


# Checking Login Credentials (Using or)
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" or password == "admin123":
    print("Access granted!")
else:
    print("Access denied!")


#  Traffic Light Decision (Using elif, and, or)
signal = input("Enter traffic light color (red/yellow/green): ").lower()
speed = int(input("Enter your speed: "))

if signal == "red" or speed > 80:
    print("Stop! Either the signal is red or you are overspeeding.")
elif signal == "yellow" and speed < 40:
    print("Proceed with caution.")
elif signal == "green":
    print("You can go.")
else:
    print("Invalid input.")


# University Admission Eligibility
marks = int(input("Enter your percentage: "))
extracurricular = input("Do you have extracurricular achievements? (yes/no): ").lower()

if marks >= 90 and extracurricular == "yes":
    print("You are eligible for a full scholarship.")
elif marks >= 75 and marks < 90:
    print("You are eligible for admission but without a scholarship.")
elif marks < 75 or extracurricular == "no":
    print("You need to improve your grades for admission.")
else:
    print("Invalid input.")


# Example 1: Bank Account System (Using and / or)
# This example simulates a basic bank account system where a user can perform various actions based on the account balance, account type, and verification.

account_balance = float(input("Enter your account balance: $"))
account_type = input("Enter your account type (savings/current): ").lower()
is_verified = input("Are you verified with the bank? (yes/no): ").lower()

if is_verified == "no":
    print("You must be verified to perform transactions.")
elif account_balance >= 1000 and account_type == "savings":
    print("You can withdraw up to $500 without any fee.")
elif account_balance < 1000 and account_type == "savings":
    print("You are allowed to withdraw only up to $100 without any fee.")
elif account_balance >= 500 and account_type == "current" and is_verified == "yes":
    print("You can withdraw any amount but with a small processing fee.")
elif account_balance < 500 and (account_type == "current" or account_type == "savings"):
    print("Your balance is insufficient for a transaction.")
else:
    print("Invalid input, please check your details and try again.")
