# 1. Write a program to count the number of upper and lower case letters in a string.
def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for c in s:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

count_upper_lower("The Quick Brown Fox")  # Output: Uppercase letters: 3, Lowercase letters: 13

# 2. Write a program that will check whether a given String is Palindrome or not.
def is_palindrome(s):
    s = s.lower()  
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

is_palindrome("madam")  # Output: Palindrome

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be > 2. If input is "wipro", then output should be "wiwiwiwiwi".
def n_copies_first_two(s):
    n = len(s)
    first_two = s[:2]
    print(first_two * n)

n_copies_first_two("wipro")  # Output: wiwiwiwiwi

# 4. Given a string, if the first or last character is 'x', return the string without those 'x' character(s), else return the string unchanged. If the input is "xHix", then output is "Hi".
def remove_first_last_x(s):
    if len(s) > 0 and s[0] == 'x':
        s = s[1:]
    if len(s) > 0 and s[-1] == 'x':
        s = s[:-1]
    print(s)

remove_first_last_x("xHix")  # Output: Hi

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.

def repeat_last_n(s, n):
    last_n = s[-n:]
    print(last_n * n)

repeat_last_n("wipro", 3)  # Output: propropro
