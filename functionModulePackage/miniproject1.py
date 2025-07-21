''' Problem Statement:
 Write a Python function that accepts a hyphen-separated sequence of colors as input 
 and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
 Constraint: All the colors will be completely in either lower case or upper case.'''

def sort_colors(color_sequence):
    """
    Accepts a hyphen-separated string of colors and returns 
    a hyphen-separated string with colors sorted alphabetically.
    
    Parameters:
        color_sequence (str): Hyphen-separated colors (all upper or all lower case)
    
    Returns:
        str: Hyphen-separated, alphabetically sorted colors
    """
    # Split the input string into a list by hyphens
    colors = color_sequence.split('-')
    
    # Sort the list alphabetically
    colors.sort()
    
    # Join the sorted list back into a hyphen-separated string
    sorted_sequence = '-'.join(colors)
    
    return sorted_sequence

# Sample usage:
input1 = "green-red-yellow-black-white"
print(sort_colors(input1))   # Output: black-green-red-white-yellow

input2 = "PINK-BLUE-TAN-PURPLE"
print(sort_colors(input2))   # Output: BLUE-PINK-PURPLE-TAN
