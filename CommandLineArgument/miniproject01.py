'''Problem Statement:
 You are given three strings as command line arguments, separated by space. 
 Each string contains numbers separated by hyphens ('-'). 
 - The first string contains the numbers you like.
 - The second string contains the numbers you dislike.
 - The third string contains the numbers given to you.

 Your initial happiness is 0.
 For each number in the third string:
  - If the number is present in your like list (string 1), add 1 to happiness.
  - If the number is present in your dislike list (string 2), subtract 1 from happiness.
   - If the number is not present in either, happiness remains unchanged.
 Output your final happiness'''

import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <like_string> <dislike_string> <given_string>")
        return

    like_str, dislike_str, given_str = sys.argv[1], sys.argv[2], sys.argv[3]
    like_set = set(like_str.split('-'))
    dislike_set = set(dislike_str.split('-'))

    given_numbers = given_str.split('-')
    
    happiness = 0

    for num in given_numbers:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1


    print(happiness)

