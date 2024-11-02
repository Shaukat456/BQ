# 1


def greet(name):
    return f"Hello, {name}!"


def main():
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        message = greet(name)
        print(message)


main()


# 2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))


# 3
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prime(5))
print(is_prime(10))


# 4
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))
print(count_vowels("Python Programming"))


# 5
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(find_max([1, 3, 2, 8, 5]))


# 6
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


print(sum_digits(1234))


# 7
def string_length(s):
    return len(s)


print(string_length("Hello"))
print(string_length("This is a test string."))


# 8
def reverse_string(s):
    return s[::-1]


print(reverse_string("Hello"))
print(reverse_string("Python Programming"))


# 9
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_or_odd(4))
print(check_even_or_odd(7))


# 10
def check_positive_or_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


print(check_positive_or_negative(10))
print(check_positive_or_negative(-5))
print(check_positive_or_negative(0))
