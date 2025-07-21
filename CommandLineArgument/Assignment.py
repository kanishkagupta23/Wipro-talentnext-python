''' Command Line Arguments Assignment
   python assignments.py sum2 <num1> <num2>'''


import sys

def sum_two_numbers(args):
    """
    Accepts two numbers as command line arguments and displays their sum.
    Usage: python assignments.py sum2 <num1> <num2>
    """
    if len(args) != 2:
        print("Usage: python assignments.py sum2 <num1> <num2>")
        return
    num1 = int(args[0])
    num2 = int(args[1])
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
    
def print_welcome_message(args):
    """
    Accepts a welcome message and displays file name along with the message.
    Usage: python assignments.py welcome <message>
    """
    if len(args) != 1:
        print("Usage: python assignments.py welcome <message>")
        return
    print(f"File Name: {sys.argv[0]}")
    print(f"Welcome Message: {args[0]}")

def is_prime(n):
    """
    Utility function to check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True



def sum_prime_numbers(args):
    """
    Accepts 10 numbers and calculates the sum of primes among them.
    Usage: python assignments.py prime10 <num1> <num2> ... <num10>
    """
    if len(args) != 10:
        print("Usage: python assignments.py prime10 <num1> <num2> ... <num10>")
        return
    numbers = [int(arg) for arg in args]
    prime_sum = sum(num for num in numbers if is_prime(num))
    print(f"Sum of prime numbers: {prime_sum}")

