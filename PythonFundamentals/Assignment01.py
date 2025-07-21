# Python Fundamentals - Exercises


print("="*60)
print("TM-01 Python Fundamentals - Exercises")
print("="*60)

# Q1. Write a program to check if a given number is Positive, Negative or Zero.
print("\nQ1. Check if a number is Positive, Negative or Zero")
print("-" * 50)

def check_number_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Test Q1
test_num = float(input("Enter a number: "))
result = check_number_sign(test_num)
print(f"The number {test_num} is {result}")

# Q2. Write a program to check if a given number is odd or even.
print("\nQ2. Check if a number is Odd or Even")
print("-" * 50)

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test Q2
test_num2 = int(input("Enter an integer: "))
result = check_odd_even(test_num2)
print(f"The number {test_num2} is {result}")

# Q3. Given two non-negative values, print true if they have the same last digit
print("\nQ3. Check if two numbers have the same last digit")
print("-" * 50)

def same_last_digit(num1, num2):
    return num1 % 10 == num2 % 10

# Test Q3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = same_last_digit(num1, num2)
print(f"Numbers {num1} and {num2} have same last digit: {result}")

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
print("\nQ4. Print numbers 1 to 10 with tab spacing")
print("-" * 50)

print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end="\t")
print()  # New line after the numbers

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
print("\nQ5. Print even numbers between 23 and 57")
print("-" * 50)

print("Even numbers between 23 and 57:")
for i in range(24, 58):  # Start from 24 (first even after 23) to 57
    if i % 2 == 0:
        print(i)

# Q6. Write a program to check if a given number is prime or not.
print("\nQ6. Check if a number is Prime")
print("-" * 50)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test Q6
test_prime = int(input("Enter a number to check if it's prime: "))
if is_prime(test_prime):
    print(f"{test_prime} is a prime number")
else:
    print(f"{test_prime} is not a prime number")

# Q7. Write a program to print prime numbers between 10 and 99.
print("\nQ7. Prime numbers between 10 and 99")
print("-" * 50)

print("Prime numbers between 10 and 99:")
prime_count = 0
for i in range(10, 100):
    if is_prime(i):
        print(f"{i:2d}", end="  ")
        prime_count += 1
        if prime_count % 10 == 0:  # Print 10 numbers per line
            print()
print(f"\nTotal prime numbers found: {prime_count}")

# Q8. Write a program to print the sum of all the digits of a given number.
print("\nQ8. Sum of digits of a number")
print("-" * 50)

def sum_of_digits(num):
    num = abs(num)  # Handle negative numbers
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

# Test Q8
test_num8 = int(input("Enter a number to find sum of its digits: "))
digit_sum = sum_of_digits(test_num8)
print(f"Sum of digits of {test_num8} is: {digit_sum}")

# Q9. Write a program to reverse a given number and print.
print("\nQ9. Reverse a number")
print("-" * 50)

def reverse_number(num):
    is_negative = num < 0
    num = abs(num)
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return -reversed_num if is_negative else reversed_num

# Test Q9
test_num9 = int(input("Enter a number to reverse: "))
reversed_num = reverse_number(test_num9)
print(f"Original number: {test_num9}")
print(f"Reversed number: {reversed_num}")

# Q10. Write a program to find if the given number is palindrome or not.
print("\nQ10. Check if a number is Palindrome")
print("-" * 50)

def is_palindrome(num):
    return num == reverse_number(num)

# Test Q10
test_num10 = int(input("Enter a number to check if it's palindrome: "))
if is_palindrome(test_num10):
    print(f"{test_num10} is a palindrome")
else:
    print(f"{test_num10} is not a palindrome")

print("\n" + "="*60)
print("MINI PROJECTS")
print("="*60)
