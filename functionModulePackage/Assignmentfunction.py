# 1. Write a function to return the sum of all numbers in a list.
#    Sample List: [8, 2, 3, 0, 7]
#    Expected Output: 20
def sum_of_list(numbers):
    return sum(numbers)

# 2. Write a function to return the reverse of a string.
#    Sample String: "1234abcd"
#    Expected Output: "dcba4321"
def reverse_string(s):
    return s[::-1]

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 4. Write a function that accepts a string and prints the number of upper case and lower case letters in it.
def count_case_letters(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    print(f"Upper case letters: {upper}")
    print(f"Lower case letters: {lower}")

# 5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
#    Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    Expected result: [2, 4, 6, 8]
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True