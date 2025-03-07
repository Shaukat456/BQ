# Prime Number using for loop

num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")

# Prime Number using while loop

num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False

else:
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")


def is_prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)


num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")

# Prime Number using for loop


# Factorial of a number

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}.")


#  Factorial of a number using while loop

num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is {factorial}.")


#  Factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}.")


#  Fibonacci series using for loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#  Fibonacci series using while loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1

i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1


#  Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i), end=" ")


#  Sum of natural numbers using for loop
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i


# Largest Number in a List
numbers = [10, 20, 30, 40, 50]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}.")

# Smallest Number in a List
numbers = [10, 20, 30, 40, 50]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(f"The smallest number is {smallest}.")


#  Sum of natural numbers using while loop
n = int(input("Enter a number: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"The sum of natural numbers up to {n} is {total}.")


#  Sum of natural numbers using recursion
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)


num = int(input("Enter a number: "))
result = sum_natural(num)
print(f"The sum of natural numbers up to {num} is {result}.")

#  Sum of natural numbers using formula
num = int(input("Enter a number: "))
total = num * (num + 1) // 2
print(f"The sum of natural numbers up to {num} is {total}.")


# Sorting a list using for loop (Bubble Sort Algorithm)

# Bubble sort algorithm
# Bubble Sort is a simple algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the
# list is repeated until the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

#  Bubble Sort Algorithm
# 1. Start with the first element in the list.
# 2. Compare the current element with the next element.
# 3. If the current element is greater than the next element, swap them.
# 4. Move to the next element and repeat steps 2 and 3.
# 5. Continue this process until the list is sorted.


numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


print("Sorted list:", numbers)

# step 1: [34, 25, 12, 22, 11, 64, 90]
# step 2: [25, 12, 22, 11, 34, 64, 90]
# step 3: [12, 22, 11, 25, 34, 64, 90]
# step 4: [12, 11, 22, 25, 34, 64, 90]
# step 5: [11, 12, 22, 25, 34, 64, 90]
# step 6: [11, 12, 22, 25, 34, 64, 90]
# step 7: [11, 12, 22, 25, 34, 64, 90]


#  Sorting a list using while loop (Bubble Sort Algorithm)
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

i = 0
while i < n:
    j = 0
    while j < n - i - 1:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        j += 1
    i += 1

print("Sorted list:", numbers)
