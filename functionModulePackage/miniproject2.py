''' Problem Statement:
 Create a Python module with the following functions:
 1. ispalindrome(name): Returns True if the input name is a palindrome, else False.
 2. count_the_vowels(name): Returns the count of vowels in the input name.
3. frequency_of_letters(name): Returns a dictionary with the frequency of each letter in the name.
 Note: Input name will be entirely in lower or upper case.'''

def ispalindrome(name):
    """
    Checks if the given name is a palindrome.
    
    Args:
        name (str): The input name (all lowercase or all uppercase).
    Returns:
        bool: True if palindrome, False otherwise.
    """
    return name == name[::-1]

def count_the_vowels(name):
    """
    Counts the number of vowels in the given name.
    
    Args:
        name (str): The input name (all lowercase or all uppercase).
    Returns:
        int: Number of vowels.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for letter in name if letter in vowels)

def frequency_of_letters(name):
    """
    Counts the frequency of each letter in the given name.
    
    Args:
        name (str): The input name (all lowercase or all uppercase).
    Returns:
        dict: Dictionary with letters as keys and their counts as values.
    """
    freq = {}
    for letter in name:
        freq[letter] = freq.get(letter, 0) + 1
    return freq
